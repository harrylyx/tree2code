from __future__ import annotations

from typing import Any, List, Optional

from .ir import ModelIR, TreeNode
from .scoring import AbnormalSpec, ScoreSpec


def _fmt_num(value: float) -> str:
    """Format a float to a high-precision string.

    Args:
        value: The float to format.

    Returns:
        str: The formatted string.
    """
    return format(float(value), ".17g")


def _indent(level: int) -> str:
    """Return a string of spaces for the given indentation level.

    Args:
        level: Number of levels (4 spaces each).

    Returns:
        str: The indentation string.
    """
    return " " * (4 * level)


def _render_node(lines: List[str], node: TreeNode, depth: int) -> None:
    """Recursively render a tree node into Python code lines.

    Args:
        lines: The list to append generated Python lines to.
        node: The tree node to render.
        depth: Current indentation depth.
    """
    prefix = _indent(depth)

    if node.is_leaf:
        assert node.leaf_value is not None
        lines.append(f"{prefix}return {_fmt_num(node.leaf_value)}")
        return

    assert node.feature is not None
    assert node.left is not None
    assert node.right is not None

    lines.append(f"{prefix}v = row.get({node.feature!r})")
    lines.append(f"{prefix}missing = _is_missing(v, {node.missing_type!r})")

    if node.split_type == "categorical":
        categories = tuple(node.categories or [])
        lines.append(f"{prefix}cat_hit = _in_categories(v, {categories!r})")
        if node.default_left:
            cond = "missing or ((not missing) and cat_hit)"
        else:
            cond = "(not missing) and cat_hit"
    else:
        assert node.threshold is not None
        op = "<=" if node.operator == "<=" else "<"
        cmp_expr = (
            f"_safe_numeric_compare(v, {_fmt_num(node.threshold)}, {op!r}, "
            f"{repr(bool(node.float32_compare))})"
        )

        if node.default_left:
            cond = f"missing or ((not missing) and ({cmp_expr}))"
        else:
            cond = f"(not missing) and ({cmp_expr})"

    lines.append(f"{prefix}if {cond}:")
    _render_node(lines, node.left, depth + 1)
    lines.append(f"{prefix}else:")
    _render_node(lines, node.right, depth + 1)


def _abnormal_python_condition(
    feature_names: List[str], abnormal_spec: AbnormalSpec
) -> Optional[str]:
    """Generate the Python condition for checking abnormal rules.

    Args:
        feature_names: List of all feature names in the model.
        abnormal_spec: The abnormal rule specification.

    Returns:
        Optional[str]: The Python boolean expression, or None if no rule is active.
    """
    if not abnormal_spec.active or not feature_names:
        return None

    if abnormal_spec.rule == "all_null":
        checks = [f"_is_missing(row.get({name!r}), 'nan')" for name in feature_names]
        return " and ".join(checks)

    if abnormal_spec.rule == "all_default":
        assert abnormal_spec.default_fill_value is not None
        checks = [
            f"row.get({name!r}) == {_fmt_num(float(abnormal_spec.default_fill_value))}"
            for name in feature_names
        ]
        return " and ".join(checks)

    return None


def render_python(
    ir: ModelIR,
    score_spec: Optional[ScoreSpec],
    abnormal_spec: AbnormalSpec,
) -> str:
    """Render the model IR into a pure Python scoring script.

    Args:
        ir: The model intermediate representation.
        score_spec: Optional scorecard parameters.
        abnormal_spec: Abnormal rule specification.

    Returns:
        str: The complete Python source code for scoring.
    """
    lines: List[str] = []
    lines.append("import math")
    lines.append("import struct")
    lines.append("from decimal import Decimal, ROUND_HALF_UP")
    lines.append("")

    if score_spec is not None:
        lines.append(f"_SCORE_FACTOR = {_fmt_num(score_spec.factor)}")
        lines.append(f"_SCORE_OFFSET = {_fmt_num(score_spec.offset)}")
        lines.append(f"_SCORE_SCALE = {int(score_spec.score_scale)}")
        lines.append(f"_SCORE_EPS = {_fmt_num(score_spec.epsilon)}")
        lines.append("")

    lines.append("def _is_missing(value, missing_type):")
    lines.append(f"{_indent(1)}if missing_type == 'none':")
    lines.append(f"{_indent(2)}return False")
    lines.append(f"{_indent(1)}if value is None:")
    lines.append(f"{_indent(2)}return True")
    lines.append(f"{_indent(1)}try:")
    lines.append(f"{_indent(2)}if math.isnan(float(value)):")
    lines.append(f"{_indent(3)}return True")
    lines.append(f"{_indent(1)}except (TypeError, ValueError):")
    lines.append(f"{_indent(2)}pass")
    lines.append(f"{_indent(1)}if missing_type == 'zero' and value == 0:")
    lines.append(f"{_indent(2)}return True")
    lines.append(f"{_indent(1)}return False")
    lines.append("")

    lines.append("def _safe_numeric_compare(value, threshold, op, use_f32):")
    lines.append(f"{_indent(1)}try:")
    lines.append(f"{_indent(2)}left = _f32(value) if use_f32 else float(value)")
    lines.append(f"{_indent(1)}except (TypeError, ValueError):")
    lines.append(f"{_indent(2)}return False")
    lines.append(f"{_indent(1)}right = _f32(threshold) if use_f32 else float(threshold)")
    lines.append(f"{_indent(1)}if math.isnan(left):")
    lines.append(f"{_indent(2)}return False")
    lines.append(f"{_indent(1)}if op == '<=':")
    lines.append(f"{_indent(2)}return left <= right")
    lines.append(f"{_indent(1)}return left < right")
    lines.append("")

    lines.append("def _normalize_category(value):")
    lines.append(f"{_indent(1)}if hasattr(value, 'item'):")
    lines.append(f"{_indent(2)}try:")
    lines.append(f"{_indent(3)}value = value.item()")
    lines.append(f"{_indent(2)}except Exception:")
    lines.append(f"{_indent(3)}pass")
    lines.append(f"{_indent(1)}if isinstance(value, bool):")
    lines.append(f"{_indent(2)}return value")
    lines.append(f"{_indent(1)}if isinstance(value, int):")
    lines.append(f"{_indent(2)}return value")
    lines.append(f"{_indent(1)}if isinstance(value, float):")
    lines.append(f"{_indent(2)}if value.is_integer():")
    lines.append(f"{_indent(3)}return int(value)")
    lines.append(f"{_indent(2)}return value")
    lines.append(f"{_indent(1)}return value")
    lines.append("")

    lines.append("def _in_categories(value, categories):")
    lines.append(f"{_indent(1)}return _normalize_category(value) in categories")
    lines.append("")

    lines.append("def _f32(value):")
    lines.append(
        f"{_indent(1)}return struct.unpack('!f', struct.pack('!f', float(value)))[0]"
    )
    lines.append("")

    if score_spec is not None:
        lines.append("def _round_half_up(value, scale):")
        lines.append(f"{_indent(1)}quant = Decimal('1').scaleb(-scale)")
        lines.append(
            f"{_indent(1)}return float(Decimal(str(value)).quantize(quant, rounding=ROUND_HALF_UP))"
        )
        lines.append("")

        lines.append("def _probability_to_score(score_p):")
        lines.append(
            f"{_indent(1)}p = min(max(float(score_p), _SCORE_EPS), 1.0 - _SCORE_EPS)"
        )
        lines.append(f"{_indent(1)}odds = p / (1.0 - p)")
        lines.append(
            f"{_indent(1)}score = _SCORE_OFFSET - _SCORE_FACTOR * math.log(odds)"
        )
        lines.append(f"{_indent(1)}return _round_half_up(score, _SCORE_SCALE)")
        lines.append("")

    for idx, tree in enumerate(ir.trees):
        lines.append(f"def _tree_{idx}(row):")
        _render_node(lines, tree, 1)
        lines.append("")

    lines.append("def predict_row(row):")

    abnormal_cond = _abnormal_python_condition(ir.feature_names, abnormal_spec)
    if abnormal_cond is not None:
        abnormal_literal = _fmt_num(float(abnormal_spec.abnormal_value))
        lines.append(f"{_indent(1)}if {abnormal_cond}:")
        if score_spec is not None:
            lines.append(
                f"{_indent(2)}return {{'score_p': {abnormal_literal}, 'score': {abnormal_literal}}}"
            )
        else:
            lines.append(f"{_indent(2)}return {{'score_p': {abnormal_literal}}}")

    if ir.model_type == "xgboost":
        lines.append(f"{_indent(1)}margin = _f32({_fmt_num(ir.base_margin)})")
        for idx in range(len(ir.trees)):
            lines.append(
                f"{_indent(1)}margin = _f32(margin + _f32(_tree_{idx}(row)))"
            )
        lines.append(f"{_indent(1)}score_p = _f32(1.0 / (1.0 + math.exp(-margin)))")
    else:
        lines.append(f"{_indent(1)}margin = {_fmt_num(ir.base_margin)}")
        for idx in range(len(ir.trees)):
            lines.append(f"{_indent(1)}margin += _tree_{idx}(row)")
        lines.append(f"{_indent(1)}score_p = 1.0 / (1.0 + math.exp(-margin))")

    if score_spec is not None:
        lines.append(f"{_indent(1)}score = _probability_to_score(score_p)")
        lines.append(f"{_indent(1)}return {{'score_p': score_p, 'score': score}}")
    else:
        lines.append(f"{_indent(1)}return {{'score_p': score_p}}")

    return "\n".join(lines) + "\n"
