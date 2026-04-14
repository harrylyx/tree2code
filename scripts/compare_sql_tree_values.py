#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from bisect import bisect_left
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

NUMBER_RE = re.compile(
    r"(?<![A-Za-z0-9_])[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?(?![A-Za-z0-9_])"
)
CASE_WHEN_RE = re.compile(r"\bcase\s+when\b", re.IGNORECASE)
CASE_END_RE = re.compile(r"\b(case|end)\b", re.IGNORECASE)
TREE_ALIAS_RE = re.compile(r"\bas\s+tree_(\d+)_score\b", re.IGNORECASE)
EXP_MARGIN_RE = re.compile(r"exp\s*\(\s*-\s*\(", re.IGNORECASE)
MIN_THRESHOLD_DECIMAL = Decimal("1e-13")


@dataclass
class TreeCompareSummary:
    tree_index: int
    status: str
    total_tokens_a: int
    total_tokens_b: int
    exact_only_a_count: int
    exact_only_b_count: int
    approx_shared_count: int
    threshold_mismatch_count: int


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _skip_spaces(text: str, pos: int) -> int:
    n = len(text)
    while pos < n and text[pos].isspace():
        pos += 1
    return pos


def _find_matching_paren(text: str, open_pos: int) -> int:
    depth = 0
    i = open_pos
    n = len(text)
    in_str = False

    while i < n:
        ch = text[i]
        if ch == "'":
            if in_str and i + 1 < n and text[i + 1] == "'":
                i += 2
                continue
            in_str = not in_str
            i += 1
            continue
        if in_str:
            i += 1
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError("Unbalanced parentheses in SQL text")


def _find_case_end(text: str, case_start: int) -> int:
    depth = 0
    for match in CASE_END_RE.finditer(text, case_start):
        token = match.group(1).lower()
        if token == "case":
            depth += 1
            continue
        depth -= 1
        if depth == 0:
            return match.end()
    raise ValueError("Unbalanced CASE/END in SQL text")


def _extract_trees_by_alias(sql: str) -> Dict[int, str]:
    trees: Dict[int, str] = {}
    pos = 0
    while True:
        case_match = CASE_WHEN_RE.search(sql, pos)
        if case_match is None:
            break
        case_start = case_match.start()
        case_end = _find_case_end(sql, case_start)
        tail = _skip_spaces(sql, case_end)
        alias_match = TREE_ALIAS_RE.match(sql, tail)
        if alias_match is not None:
            tree_idx = int(alias_match.group(1))
            trees[tree_idx] = sql[case_start:case_end].strip()
        pos = case_end
    return trees


def _strip_outer_parens(expr: str) -> str:
    text = expr.strip()
    while text.startswith("(") and text.endswith(")"):
        close = _find_matching_paren(text, 0)
        if close != len(text) - 1:
            break
        text = text[1:-1].strip()
    return text


def _split_top_level_plus(expr: str) -> List[str]:
    parts: List[str] = []
    start = 0
    depth = 0
    text = expr
    n = len(text)

    for i, ch in enumerate(text):
        if ch == "(":
            depth += 1
            continue
        if ch == ")":
            depth -= 1
            continue
        if ch != "+" or depth != 0:
            continue
        prev = text[i - 1] if i > 0 else ""
        if prev in {"e", "E"}:
            continue
        segment = text[start:i].strip()
        if segment:
            parts.append(segment)
        start = i + 1

    last = text[start:n].strip()
    if last:
        parts.append(last)
    return parts


def _extract_trees_by_margin(sql: str) -> Dict[int, str]:
    margin_match = EXP_MARGIN_RE.search(sql)
    if margin_match is None:
        return {}
    open_pos = margin_match.end() - 1
    close_pos = _find_matching_paren(sql, open_pos)
    margin_expr = sql[open_pos + 1 : close_pos]
    margin_expr = _strip_outer_parens(margin_expr)

    terms = _split_top_level_plus(margin_expr)
    trees = [
        _strip_outer_parens(term)
        for term in terms
        if CASE_WHEN_RE.search(term) is not None
    ]
    return {idx: tree for idx, tree in enumerate(trees)}


def _extract_trees(sql: str, mode: str) -> Tuple[Dict[int, str], str]:
    if mode == "alias":
        trees = _extract_trees_by_alias(sql)
        return trees, "alias"
    if mode == "margin":
        trees = _extract_trees_by_margin(sql)
        return trees, "margin"

    trees_alias = _extract_trees_by_alias(sql)
    trees_margin = _extract_trees_by_margin(sql)

    if len(trees_alias) >= len(trees_margin) and trees_alias:
        return trees_alias, "alias"
    if trees_margin:
        return trees_margin, "margin"
    return {}, "none"


def _extract_number_tokens(sql_fragment: str) -> List[str]:
    return NUMBER_RE.findall(sql_fragment)


def _tokenizer_self_check() -> Dict[str, object]:
    sample = "case when userinfo_14 <= 3.5 then -0.1 else 0 end"
    tokens = _extract_number_tokens(sample)
    return {
        "sample": sample,
        "tokens": tokens,
        "passed": tokens == ["3.5", "-0.1", "0"],
    }


def _canonical_decimal(token: str) -> str:
    value = Decimal(token).normalize()
    if value == 0:
        return "0"
    return str(value)


def _approx_bucket(token: str, significant_digits: int = 12) -> str:
    return format(float(token), f".{significant_digits}g")


def _counter_diff(
    counter_a: Counter[str],
    counter_b: Counter[str],
) -> Tuple[Counter[str], Counter[str], Counter[str]]:
    shared = counter_a & counter_b
    only_a = counter_a - counter_b
    only_b = counter_b - counter_a
    return shared, only_a, only_b


def _find_close_pairs(
    only_a: Counter[str],
    only_b: Counter[str],
    *,
    tolerance: float,
    limit: int = 20,
) -> List[Dict[str, object]]:
    values_b = sorted((float(v), v) for v in only_b.keys())
    values_b_float = [item[0] for item in values_b]

    rows: List[Dict[str, object]] = []
    for value_a_text, count_a in only_a.items():
        value_a = float(value_a_text)
        idx = bisect_left(values_b_float, value_a)
        candidates: List[Tuple[float, str]] = []
        if idx < len(values_b):
            candidates.append(values_b[idx])
        if idx > 0:
            candidates.append(values_b[idx - 1])

        for value_b, value_b_text in candidates:
            diff = abs(value_a - value_b)
            if diff <= tolerance:
                rows.append(
                    {
                        "value_a": value_a_text,
                        "value_b": value_b_text,
                        "abs_diff": diff,
                        "count_a": count_a,
                        "count_b": only_b[value_b_text],
                    }
                )
                break

        if len(rows) >= limit:
            break

    return rows


def _top_items(counter: Counter[str], limit: int) -> List[Tuple[str, int]]:
    return counter.most_common(limit)


def _is_threshold_mismatch_pair(value_a: str, value_b: str) -> bool:
    """Check whether pair is strict mismatch caused by 0 vs 1e-13 threshold."""
    try:
        a = Decimal(value_a).normalize()
        b = Decimal(value_b).normalize()
    except Exception:
        return False

    if a == 0 and abs(b) == MIN_THRESHOLD_DECIMAL:
        return True
    if b == 0 and abs(a) == MIN_THRESHOLD_DECIMAL:
        return True
    return False


def _compare_tree_values(
    tree_sql_a: str,
    tree_sql_b: str,
    *,
    max_values: int,
    close_tolerance: float,
) -> Dict[str, object]:
    tokens_a = _extract_number_tokens(tree_sql_a)
    tokens_b = _extract_number_tokens(tree_sql_b)

    exact_a = Counter(_canonical_decimal(v) for v in tokens_a)
    exact_b = Counter(_canonical_decimal(v) for v in tokens_b)
    exact_shared, exact_only_a, exact_only_b = _counter_diff(exact_a, exact_b)

    approx_a = Counter(_approx_bucket(v) for v in tokens_a)
    approx_b = Counter(_approx_bucket(v) for v in tokens_b)
    approx_shared, _, _ = _counter_diff(approx_a, approx_b)

    close_pairs = _find_close_pairs(
        exact_only_a,
        exact_only_b,
        tolerance=close_tolerance,
        limit=max_values,
    )
    threshold_mismatch_pairs = [
        pair
        for pair in close_pairs
        if _is_threshold_mismatch_pair(str(pair["value_a"]), str(pair["value_b"]))
    ]
    threshold_mismatch_count = sum(
        min(int(pair["count_a"]), int(pair["count_b"]))
        for pair in threshold_mismatch_pairs
    )

    return {
        "total_tokens_a": len(tokens_a),
        "total_tokens_b": len(tokens_b),
        "exact_shared_count": sum(exact_shared.values()),
        "exact_only_a_count": sum(exact_only_a.values()),
        "exact_only_b_count": sum(exact_only_b.values()),
        "approx_shared_count": sum(approx_shared.values()),
        "top_exact_only_a": _top_items(exact_only_a, max_values),
        "top_exact_only_b": _top_items(exact_only_b, max_values),
        "top_exact_shared": _top_items(exact_shared, max_values),
        "close_pairs": close_pairs,
        "threshold_mismatch_pairs": threshold_mismatch_pairs,
        "threshold_mismatch_count": threshold_mismatch_count,
    }


def _render_markdown(
    *,
    sql_a_path: Path,
    sql_b_path: Path,
    name_a: str,
    name_b: str,
    mode_a: str,
    mode_b: str,
    trees_a: Dict[int, str],
    trees_b: Dict[int, str],
    per_tree: Dict[int, Dict[str, object]],
    summary_rows: Sequence[TreeCompareSummary],
    tokenizer_guard: Dict[str, object],
    threshold_mismatch_tree_indices: Sequence[int],
    threshold_mismatch_total_count: int,
) -> str:
    lines: List[str] = [
        "# SQL Tree Value Diff Report",
        "",
        f"- sql_a: `{sql_a_path}`",
        f"- sql_b: `{sql_b_path}`",
        f"- name_a: `{name_a}`",
        f"- name_b: `{name_b}`",
        f"- extract_mode_a: `{mode_a}`",
        f"- extract_mode_b: `{mode_b}`",
        f"- trees_a: `{len(trees_a)}`",
        f"- trees_b: `{len(trees_b)}`",
        (
            "- tokenizer_identifier_digit_guard_passed: "
            f"`{tokenizer_guard.get('passed', False)}`"
        ),
        f"- tokenizer_guard_tokens: `{tokenizer_guard.get('tokens', [])}`",
        f"- threshold_mismatch_trees(0_vs_1e-13): `{len(threshold_mismatch_tree_indices)}`",
        f"- threshold_mismatch_total_count(0_vs_1e-13): `{threshold_mismatch_total_count}`",
        "",
        "## Tree Summary",
        "| tree_index | status | a_tokens | b_tokens | a_only | b_only | approx_shared | threshold_mismatch |",
        "|---:|---|---:|---:|---:|---:|---:|---:|",
    ]

    for row in summary_rows:
        lines.append(
            f"| {row.tree_index} | {row.status} | {row.total_tokens_a} | {row.total_tokens_b} | "
            f"{row.exact_only_a_count} | {row.exact_only_b_count} | {row.approx_shared_count} | "
            f"{row.threshold_mismatch_count} |"
        )

    lines.append("")
    lines.append("## Threshold Mismatch Trees")
    if threshold_mismatch_tree_indices:
        lines.append(
            "- tree_indices: " + ", ".join(str(idx) for idx in threshold_mismatch_tree_indices)
        )
    else:
        lines.append("- tree_indices: (empty)")

    lines.append("")
    lines.append("## Tree Details")

    for row in summary_rows:
        lines.append("")
        lines.append(f"### Tree {row.tree_index} ({row.status})")
        details = per_tree.get(row.tree_index, {})
        if row.status != "present_in_both":
            lines.append("- one side missing, skipped value diff")
            continue

        only_a = details.get("top_exact_only_a", [])
        only_b = details.get("top_exact_only_b", [])
        close_pairs = details.get("close_pairs", [])
        threshold_pairs = details.get("threshold_mismatch_pairs", [])

        lines.append(
            f"- exact_only_{name_a}_count: `{details.get('exact_only_a_count', 0)}`"
        )
        lines.append(
            f"- exact_only_{name_b}_count: `{details.get('exact_only_b_count', 0)}`"
        )
        lines.append(
            "- threshold_mismatch_count(0_vs_1e-13): "
            f"`{details.get('threshold_mismatch_count', 0)}`"
        )

        lines.append(f"- top_only_{name_a}:")
        if not only_a:
            lines.append("  - (empty)")
        else:
            for value, count in only_a:
                lines.append(f"  - `{value}` x {count}")

        lines.append(f"- top_only_{name_b}:")
        if not only_b:
            lines.append("  - (empty)")
        else:
            for value, count in only_b:
                lines.append(f"  - `{value}` x {count}")

        lines.append("- close_pairs(abs_diff <= tolerance):")
        if not close_pairs:
            lines.append("  - (empty)")
        else:
            for pair in close_pairs:
                lines.append(
                    "  - "
                    f"`{pair['value_a']}` vs `{pair['value_b']}` "
                    f"(diff={pair['abs_diff']:.16g}, a={pair['count_a']}, b={pair['count_b']})"
                )

        lines.append("- threshold_mismatch_pairs(0_vs_1e-13):")
        if not threshold_pairs:
            lines.append("  - (empty)")
        else:
            for pair in threshold_pairs:
                lines.append(
                    "  - "
                    f"`{pair['value_a']}` vs `{pair['value_b']}` "
                    f"(a={pair['count_a']}, b={pair['count_b']})"
                )

    lines.append("")
    return "\n".join(lines)


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two SQL files tree-by-tree and report which numeric values differ."
        )
    )
    parser.add_argument("--sql-a", required=True, help="Path to SQL file A.")
    parser.add_argument("--sql-b", required=True, help="Path to SQL file B.")
    parser.add_argument("--name-a", default="sql_a", help="Display name for SQL A.")
    parser.add_argument("--name-b", default="sql_b", help="Display name for SQL B.")
    parser.add_argument(
        "--mode-a",
        choices=["auto", "alias", "margin"],
        default="auto",
        help="Tree extraction mode for SQL A.",
    )
    parser.add_argument(
        "--mode-b",
        choices=["auto", "alias", "margin"],
        default="auto",
        help="Tree extraction mode for SQL B.",
    )
    parser.add_argument(
        "--max-values",
        type=int,
        default=20,
        help="Max number of mismatch values shown per tree side.",
    )
    parser.add_argument(
        "--close-tolerance",
        type=float,
        default=1e-12,
        help="Tolerance for listing close-but-not-exact numeric values.",
    )
    parser.add_argument(
        "--report-md-out",
        default="docs/sql_compare/sql_tree_value_diff_report.md",
        help="Output markdown report path.",
    )
    parser.add_argument(
        "--report-json-out",
        default="docs/sql_compare/sql_tree_value_diff_report.json",
        help="Output json report path.",
    )
    args = parser.parse_args()

    sql_a_path = Path(args.sql_a)
    sql_b_path = Path(args.sql_b)

    sql_a_text = _read_text(sql_a_path)
    sql_b_text = _read_text(sql_b_path)

    trees_a, mode_a = _extract_trees(sql_a_text, args.mode_a)
    trees_b, mode_b = _extract_trees(sql_b_text, args.mode_b)
    tokenizer_guard = _tokenizer_self_check()

    if not trees_a:
        raise ValueError(
            f"Cannot extract tree expressions from sql_a={sql_a_path} with mode={args.mode_a}"
        )
    if not trees_b:
        raise ValueError(
            f"Cannot extract tree expressions from sql_b={sql_b_path} with mode={args.mode_b}"
        )

    all_indices = sorted(set(trees_a.keys()) | set(trees_b.keys()))
    per_tree: Dict[int, Dict[str, object]] = {}
    summary_rows: List[TreeCompareSummary] = []

    for tree_idx in all_indices:
        expr_a = trees_a.get(tree_idx)
        expr_b = trees_b.get(tree_idx)

        if expr_a is None:
            summary_rows.append(
                TreeCompareSummary(
                    tree_index=tree_idx,
                    status="only_in_b",
                    total_tokens_a=0,
                    total_tokens_b=len(_extract_number_tokens(expr_b or "")),
                    exact_only_a_count=0,
                    exact_only_b_count=0,
                    approx_shared_count=0,
                    threshold_mismatch_count=0,
                )
            )
            continue
        if expr_b is None:
            summary_rows.append(
                TreeCompareSummary(
                    tree_index=tree_idx,
                    status="only_in_a",
                    total_tokens_a=len(_extract_number_tokens(expr_a)),
                    total_tokens_b=0,
                    exact_only_a_count=0,
                    exact_only_b_count=0,
                    approx_shared_count=0,
                    threshold_mismatch_count=0,
                )
            )
            continue

        compared = _compare_tree_values(
            expr_a,
            expr_b,
            max_values=args.max_values,
            close_tolerance=args.close_tolerance,
        )
        per_tree[tree_idx] = compared
        summary_rows.append(
            TreeCompareSummary(
                tree_index=tree_idx,
                status="present_in_both",
                total_tokens_a=int(compared["total_tokens_a"]),
                total_tokens_b=int(compared["total_tokens_b"]),
                exact_only_a_count=int(compared["exact_only_a_count"]),
                exact_only_b_count=int(compared["exact_only_b_count"]),
                approx_shared_count=int(compared["approx_shared_count"]),
                threshold_mismatch_count=int(compared["threshold_mismatch_count"]),
            )
        )

    mismatch_trees = sum(
        1
        for item in summary_rows
        if item.status != "present_in_both"
        or item.exact_only_a_count > 0
        or item.exact_only_b_count > 0
    )
    threshold_mismatch_tree_indices = [
        item.tree_index for item in summary_rows if item.threshold_mismatch_count > 0
    ]
    threshold_mismatch_total_count = sum(
        item.threshold_mismatch_count for item in summary_rows
    )

    report_json = {
        "sql_a": str(sql_a_path),
        "sql_b": str(sql_b_path),
        "name_a": args.name_a,
        "name_b": args.name_b,
        "extract_mode_a": mode_a,
        "extract_mode_b": mode_b,
        "trees_a": len(trees_a),
        "trees_b": len(trees_b),
        "tree_indices": all_indices,
        "mismatch_trees": mismatch_trees,
        "tokenizer_guard": tokenizer_guard,
        "threshold_mismatch_tree_indices": threshold_mismatch_tree_indices,
        "threshold_mismatch_total_count": threshold_mismatch_total_count,
        "summary_rows": [row.__dict__ for row in summary_rows],
        "per_tree": per_tree,
    }

    report_md = _render_markdown(
        sql_a_path=sql_a_path,
        sql_b_path=sql_b_path,
        name_a=args.name_a,
        name_b=args.name_b,
        mode_a=mode_a,
        mode_b=mode_b,
        trees_a=trees_a,
        trees_b=trees_b,
        per_tree=per_tree,
        summary_rows=summary_rows,
        tokenizer_guard=tokenizer_guard,
        threshold_mismatch_tree_indices=threshold_mismatch_tree_indices,
        threshold_mismatch_total_count=threshold_mismatch_total_count,
    )

    md_out = Path(args.report_md_out)
    json_out = Path(args.report_json_out)
    _write_text(md_out, report_md)
    _write_text(json_out, json.dumps(report_json, ensure_ascii=False, indent=2))

    print(
        json.dumps(
            {
                "status": "ok",
                "extract_mode_a": mode_a,
                "extract_mode_b": mode_b,
                "trees_a": len(trees_a),
                "trees_b": len(trees_b),
                "mismatch_trees": mismatch_trees,
                "threshold_mismatch_trees": len(threshold_mismatch_tree_indices),
                "threshold_mismatch_total_count": threshold_mismatch_total_count,
                "report_md": str(md_out),
                "report_json": str(json_out),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
