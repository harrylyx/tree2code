#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pickle
import re
from bisect import bisect_left
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from tree2code import convert

try:
    from treemodel2sql import Lgb2Sql
except Exception as exc:  # pragma: no cover - runtime dependency check
    raise RuntimeError(
        "treemodel2sql is required for this script. "
        "Install it first, e.g. `pip install treemodel2sql`."
    ) from exc


NUMBER_RE = re.compile(
    r"(?<![A-Za-z_])[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?"
)


@dataclass
class CompareResult:
    total_tokens_a: int
    total_tokens_b: int
    unique_values_a: int
    unique_values_b: int
    exact_shared_count: int
    exact_only_a_count: int
    exact_only_b_count: int
    approx_shared_count: int
    approx_only_a_count: int
    approx_only_b_count: int


def _normalize_sql(sql: str) -> str:
    return " ".join(sql.lower().split())


def _extract_number_tokens(sql: str) -> List[str]:
    return NUMBER_RE.findall(sql)


def _to_decimal(token: str) -> Decimal:
    return Decimal(token)


def _canonical_decimal(token: str) -> str:
    dec = _to_decimal(token).normalize()
    if dec == 0:
        return "0"
    return str(dec)


def _approx_bucket(token: str, significant_digits: int = 12) -> str:
    value = float(token)
    return format(value, f".{significant_digits}g")


def _top_counter_items(counter: Counter[str], limit: int = 20) -> List[Tuple[str, int]]:
    return counter.most_common(limit)


def _counter_diff(
    counter_a: Counter[str],
    counter_b: Counter[str],
) -> Tuple[Counter[str], Counter[str], Counter[str]]:
    shared = counter_a & counter_b
    only_a = counter_a - counter_b
    only_b = counter_b - counter_a
    return shared, only_a, only_b


def _find_close_values(
    only_a: Counter[str],
    only_b: Counter[str],
    *,
    tolerance: float = 1e-12,
    limit: int = 30,
) -> List[Dict[str, object]]:
    """Find numerically close but not exactly-equal values."""
    values_b = sorted([(float(k), k) for k in only_b.keys()], key=lambda x: x[0])
    values_b_float = [item[0] for item in values_b]

    results: List[Dict[str, object]] = []
    for key_a, count_a in only_a.items():
        value_a = float(key_a)
        idx = bisect_left(values_b_float, value_a)
        candidates: List[Tuple[float, str]] = []
        if idx < len(values_b):
            candidates.append(values_b[idx])
        if idx > 0:
            candidates.append(values_b[idx - 1])

        for value_b, key_b in candidates:
            diff = abs(value_a - value_b)
            if diff <= tolerance:
                results.append(
                    {
                        "tree2code_value": key_a,
                        "treemodel2sql_value": key_b,
                        "abs_diff": diff,
                        "tree2code_count": count_a,
                        "treemodel2sql_count": only_b[key_b],
                    }
                )
                break

        if len(results) >= limit:
            break

    return results


def _compare_number_tokens(tokens_a: Sequence[str], tokens_b: Sequence[str]) -> Dict[str, object]:
    exact_a = Counter(_canonical_decimal(token) for token in tokens_a)
    exact_b = Counter(_canonical_decimal(token) for token in tokens_b)
    exact_shared, exact_only_a, exact_only_b = _counter_diff(exact_a, exact_b)

    approx_a = Counter(_approx_bucket(token) for token in tokens_a)
    approx_b = Counter(_approx_bucket(token) for token in tokens_b)
    approx_shared, approx_only_a, approx_only_b = _counter_diff(approx_a, approx_b)

    summary = CompareResult(
        total_tokens_a=len(tokens_a),
        total_tokens_b=len(tokens_b),
        unique_values_a=len(exact_a),
        unique_values_b=len(exact_b),
        exact_shared_count=sum(exact_shared.values()),
        exact_only_a_count=sum(exact_only_a.values()),
        exact_only_b_count=sum(exact_only_b.values()),
        approx_shared_count=sum(approx_shared.values()),
        approx_only_a_count=sum(approx_only_a.values()),
        approx_only_b_count=sum(approx_only_b.values()),
    )

    close_values = _find_close_values(exact_only_a, exact_only_b, tolerance=1e-12)

    return {
        "summary": summary.__dict__,
        "top_exact_shared": _top_counter_items(exact_shared, limit=20),
        "top_exact_only_tree2code": _top_counter_items(exact_only_a, limit=20),
        "top_exact_only_treemodel2sql": _top_counter_items(exact_only_b, limit=20),
        "top_approx_shared": _top_counter_items(approx_shared, limit=20),
        "close_but_not_exact": close_values,
    }


def _render_counter_table(title: str, rows: Sequence[Tuple[str, int]]) -> List[str]:
    lines: List[str] = [f"### {title}"]
    if not rows:
        lines.append("- (empty)")
        lines.append("")
        return lines

    lines.append("| value | count |")
    lines.append("|---|---:|")
    for value, count in rows:
        lines.append(f"| `{value}` | {count} |")
    lines.append("")
    return lines


def _render_markdown_report(
    *,
    model_path: Path,
    keep_columns: Sequence[str],
    table_name: str,
    tree2code_sql_path: Path,
    treemodel2sql_sql_path: Path,
    tree2code_sql: str,
    treemodel2sql_sql: str,
    number_compare: Dict[str, object],
) -> str:
    summary = number_compare["summary"]

    lines: List[str] = [
        "# LGB SQL Consistency Report",
        "",
        f"- model_path: `{model_path}`",
        f"- keep_columns: `{','.join(keep_columns)}`",
        f"- table_name: `{table_name}`",
        f"- tree2code_sql: `{tree2code_sql_path}`",
        f"- treemodel2sql_sql: `{treemodel2sql_sql_path}`",
        f"- normalized_sql_equal: `{_normalize_sql(tree2code_sql) == _normalize_sql(treemodel2sql_sql)}`",
        f"- tree2code_sql_length: `{len(tree2code_sql)}`",
        f"- treemodel2sql_sql_length: `{len(treemodel2sql_sql)}`",
        "",
        "## Numeric Token Summary",
        f"- tree2code_total_numeric_tokens: `{summary['total_tokens_a']}`",
        f"- treemodel2sql_total_numeric_tokens: `{summary['total_tokens_b']}`",
        f"- tree2code_unique_numeric_values: `{summary['unique_values_a']}`",
        f"- treemodel2sql_unique_numeric_values: `{summary['unique_values_b']}`",
        f"- exact_shared_count: `{summary['exact_shared_count']}`",
        f"- exact_only_tree2code_count: `{summary['exact_only_a_count']}`",
        f"- exact_only_treemodel2sql_count: `{summary['exact_only_b_count']}`",
        f"- approx_shared_count(12_sig_digits): `{summary['approx_shared_count']}`",
        f"- approx_only_tree2code_count(12_sig_digits): `{summary['approx_only_a_count']}`",
        f"- approx_only_treemodel2sql_count(12_sig_digits): `{summary['approx_only_b_count']}`",
        "",
    ]

    lines.extend(
        _render_counter_table(
            "Top Exact Shared Numeric Values",
            number_compare["top_exact_shared"],
        )
    )
    lines.extend(
        _render_counter_table(
            "Top Exact-Only Values In tree2code",
            number_compare["top_exact_only_tree2code"],
        )
    )
    lines.extend(
        _render_counter_table(
            "Top Exact-Only Values In treemodel2sql",
            number_compare["top_exact_only_treemodel2sql"],
        )
    )

    close_rows: List[Dict[str, object]] = number_compare["close_but_not_exact"]
    lines.append("### Close But Not Exact (abs_diff <= 1e-12)")
    if not close_rows:
        lines.append("- (empty)")
    else:
        lines.append(
            "| tree2code_value | treemodel2sql_value | abs_diff | tree2code_count | treemodel2sql_count |"
        )
        lines.append("|---|---|---:|---:|---:|")
        for row in close_rows:
            lines.append(
                f"| `{row['tree2code_value']}` | `{row['treemodel2sql_value']}` | "
                f"{row['abs_diff']:.16g} | {row['tree2code_count']} | {row['treemodel2sql_count']} |"
            )
    lines.append("")

    return "\n".join(lines)


def _parse_keep_columns(value: str) -> List[str]:
    cols = [item.strip() for item in value.split(",") if item.strip()]
    if not cols:
        raise ValueError("keep-columns cannot be empty")
    return cols


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate LGB SQL from tree2code (Hive) and treemodel2sql, "
            "then compare numeric consistency."
        )
    )
    parser.add_argument(
        "--model-path",
        default="test_data/lgb_model.pkl",
        help="Path to pickled LightGBM model.",
    )
    parser.add_argument(
        "--keep-columns",
        default="idx",
        help="Comma separated columns kept in SELECT output.",
    )
    parser.add_argument(
        "--table-name",
        default="input_table",
        help="Source table name for SQL generation.",
    )
    parser.add_argument(
        "--tree2code-sql-out",
        default="docs/sql_compare/lgb_tree2code_hive.sql",
        help="Output path for tree2code hive SQL.",
    )
    parser.add_argument(
        "--treemodel2sql-out",
        default="docs/sql_compare/lgb_treemodel2sql.sql",
        help="Output path for treemodel2sql SQL.",
    )
    parser.add_argument(
        "--report-md-out",
        default="docs/sql_compare/lgb_sql_consistency_report.md",
        help="Output path for markdown report.",
    )
    parser.add_argument(
        "--report-json-out",
        default="docs/sql_compare/lgb_sql_consistency_report.json",
        help="Output path for JSON report.",
    )
    args = parser.parse_args()

    model_path = Path(args.model_path)
    keep_columns = _parse_keep_columns(args.keep_columns)
    table_name = args.table_name

    tree2code_sql_path = Path(args.tree2code_sql_out)
    treemodel2sql_sql_path = Path(args.treemodel2sql_out)
    report_md_path = Path(args.report_md_out)
    report_json_path = Path(args.report_json_out)

    model = pickle.load(open(model_path, "rb"))

    tree2code_sql = convert(
        model,
        to="sql",
        dialect="hive",
        sql_mode="select",
        keep_columns=keep_columns,
        table_name=table_name,
    )["sql"]["select_sql"]

    treemodel2sql_sql = Lgb2Sql().transform(
        model,
        keep_columns=keep_columns,
        table_name=table_name,
        sql_is_format=True,
    )

    _write_text(tree2code_sql_path, tree2code_sql)
    _write_text(treemodel2sql_sql_path, treemodel2sql_sql)

    number_tokens_tree2code = _extract_number_tokens(tree2code_sql)
    number_tokens_tms = _extract_number_tokens(treemodel2sql_sql)
    number_compare = _compare_number_tokens(
        number_tokens_tree2code,
        number_tokens_tms,
    )

    report_md = _render_markdown_report(
        model_path=model_path,
        keep_columns=keep_columns,
        table_name=table_name,
        tree2code_sql_path=tree2code_sql_path,
        treemodel2sql_sql_path=treemodel2sql_sql_path,
        tree2code_sql=tree2code_sql,
        treemodel2sql_sql=treemodel2sql_sql,
        number_compare=number_compare,
    )
    _write_text(report_md_path, report_md)

    report_json = {
        "model_path": str(model_path),
        "keep_columns": keep_columns,
        "table_name": table_name,
        "tree2code_sql_path": str(tree2code_sql_path),
        "treemodel2sql_sql_path": str(treemodel2sql_sql_path),
        "normalized_sql_equal": _normalize_sql(tree2code_sql)
        == _normalize_sql(treemodel2sql_sql),
        "tree2code_sql_length": len(tree2code_sql),
        "treemodel2sql_sql_length": len(treemodel2sql_sql),
        "number_compare": number_compare,
    }
    _write_text(
        report_json_path,
        json.dumps(report_json, ensure_ascii=False, indent=2),
    )

    print(
        json.dumps(
            {
                "status": "ok",
                "tree2code_sql": str(tree2code_sql_path),
                "treemodel2sql_sql": str(treemodel2sql_sql_path),
                "report_md": str(report_md_path),
                "report_json": str(report_json_path),
                "normalized_sql_equal": report_json["normalized_sql_equal"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
