from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

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


def _collect_tree_metadata(
    nodes: Sequence[TreeNode],
) -> Tuple[List[str], List[str], List[str], List[str]]:
    """Traverse tree nodes to collect feature classification metadata.

    Returns:
        Tuple[List[str], List[str], List[str], List[str]]:
            (numeric_features, categorical_features, zero_missing_features, none_missing_features)
    """
    numeric_features = set()
    categorical_features = set()
    zero_missing_features = set()
    none_missing_features = set()

    def _visit(node: TreeNode) -> None:
        if node.is_leaf:
            return
        if node.feature:
            if node.split_type == "categorical":
                categorical_features.add(node.feature)
            else:
                numeric_features.add(node.feature)

            if node.missing_type == "zero":
                zero_missing_features.add(node.feature)
            elif node.missing_type == "none":
                none_missing_features.add(node.feature)

        if node.left:
            _visit(node.left)
        if node.right:
            _visit(node.right)

    for n in nodes:
        _visit(n)

    return (
        sorted(numeric_features),
        sorted(categorical_features),
        sorted(zero_missing_features),
        sorted(none_missing_features),
    )


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

    lines.append(f"{prefix}v = row[{node.feature!r}]")
    lines.append(f"{prefix}missing = isinstance(v, float) and math.isnan(v)")

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
        if node.float32_compare:
            cmp_expr = f"_f32(v) {op} _f32({_fmt_num(node.threshold)})"
        else:
            cmp_expr = f"v {op} {_fmt_num(node.threshold)}"

        if node.default_left:
            cond = f"missing or ((not missing) and ({cmp_expr}))"
        else:
            cond = f"(not missing) and ({cmp_expr})"

    lines.append(f"{prefix}if {cond}:")
    _render_node(lines, node.left, depth + 1)
    lines.append(f"{prefix}else:")
    _render_node(lines, node.right, depth + 1)


def render_python(
    ir: ModelIR,
    score_spec: Optional[ScoreSpec],
    abnormal_spec: AbnormalSpec,
    compatible_mode: bool = False,
) -> str:
    """Render the model IR into a pure Python scoring script.

    Args:
        ir: The model intermediate representation.
        score_spec: Optional scorecard parameters.
        abnormal_spec: Abnormal rule specification.
        compatible_mode: Kept for signature compatibility (Python is independent).

    Returns:
        str: The complete Python source code for scoring.
    """
    lines: List[str] = []
    lines.append("import math")
    lines.append("import struct")
    if ir.model_type == "xgboost":
        lines.append("import ctypes")
        lines.append("import ctypes.util")
    lines.append("from decimal import Decimal, ROUND_HALF_UP")
    lines.append("")
    lines.append("MISSING_TEXT_VALUES = {'', 'nan', 'null', 'none'}")
    lines.append("")

    if score_spec is not None:
        lines.append(f"_SCORE_FACTOR = {_fmt_num(score_spec.factor)}")
        lines.append(f"_SCORE_OFFSET = {_fmt_num(score_spec.offset)}")
        lines.append(f"_SCORE_SCALE = {int(score_spec.score_scale)}")
        lines.append(f"_SCORE_EPS = {_fmt_num(score_spec.epsilon)}")
        lines.append("")

    lines.append("def _is_raw_missing(value):")
    lines.append(f"{_indent(1)}if value is None:")
    lines.append(f"{_indent(2)}return True")
    lines.append(f"{_indent(1)}if isinstance(value, float) and math.isnan(value):")
    lines.append(f"{_indent(2)}return True")
    lines.append(f"{_indent(1)}if isinstance(value, str):")
    lines.append(f"{_indent(2)}if value.strip().lower() in MISSING_TEXT_VALUES:")
    lines.append(f"{_indent(3)}return True")
    lines.append(f"{_indent(1)}return False")
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

    if ir.model_type == "xgboost":
        lines.append("def _load_expf():")
        lines.append(
            f"{_indent(1)}for name in (None, ctypes.util.find_library('m'), 'msvcrt'):"
        )
        lines.append(f"{_indent(2)}try:")
        lines.append(f"{_indent(3)}if name is None:")
        lines.append(f"{_indent(4)}library = ctypes.CDLL(None)")
        lines.append(f"{_indent(3)}else:")
        lines.append(f"{_indent(4)}library = ctypes.CDLL(name)")
        lines.append(f"{_indent(3)}expf = library.expf")
        lines.append(f"{_indent(3)}expf.argtypes = [ctypes.c_float]")
        lines.append(f"{_indent(3)}expf.restype = ctypes.c_float")
        lines.append(f"{_indent(3)}return expf")
        lines.append(f"{_indent(2)}except Exception:")
        lines.append(f"{_indent(3)}pass")
        lines.append(f"{_indent(1)}return None")
        lines.append("")
        lines.append("_EXPF = _load_expf()")
        lines.append("")

        lines.append("def _xgb_sigmoid(value):")
        lines.append(f"{_indent(1)}if _EXPF is None:")
        lines.append(f"{_indent(2)}return _f32(1.0 / (1.0 + math.exp(-value)))")
        lines.append(f"{_indent(1)}exp_value = _EXPF(ctypes.c_float(-value))")
        lines.append(f"{_indent(1)}denom = _f32(_f32(1.0) + exp_value)")
        lines.append(f"{_indent(1)}return _f32(_f32(1.0) / denom)")
        lines.append("")

    if score_spec is not None:
        lines.append("def _round_half_up(value, scale):")
        lines.append(f"{_indent(1)}quant = Decimal('1').scaleb(-scale)")
        lines.append(
            f"{_indent(1)}return float(Decimal(str(value)).quantize(quant, rounding=ROUND_HALF_UP))"
        )
        lines.append("")

        lines.append("def _probability_to_score(score_p):")
        lines.append(f"{_indent(1)}odds = score_p / (1.0 - score_p)")
        lines.append(
            f"{_indent(1)}score = _SCORE_OFFSET - _SCORE_FACTOR * math.log(odds)"
        )
        lines.append(f"{_indent(1)}return _round_half_up(score, _SCORE_SCALE)")
        lines.append("")

    req_feats = list(ir.feature_names)
    (
        num_feats,
        cat_feats,
        zero_missing_feats,
        none_missing_feats,
    ) = _collect_tree_metadata(ir.trees)

    lines.append("def _prepare_input(row):")
    lines.append(f"{_indent(1)}# 1. 检查必需特征")
    lines.append(f"{_indent(1)}req_features = {req_feats!r}")
    lines.append(f"{_indent(1)}missing_keys = [k for k in req_features if k not in row]")
    lines.append(f"{_indent(1)}if missing_keys:")
    lines.append(
        f"{_indent(2)}raise KeyError(f\"Missing required feature(s): {{', '.join(missing_keys)}}\")"
    )
    lines.append("")

    lines.append(f"{_indent(1)}# 2. 识别缺失值与异常规则处理")
    lines.append(f"{_indent(1)}prepared = {{}}")

    if abnormal_spec.rule == "all_null":
        lines.append(f"{_indent(1)}all_missing = True")
        lines.append(f"{_indent(1)}for k in req_features:")
        lines.append(f"{_indent(2)}v = row[k]")
        lines.append(f"{_indent(2)}if _is_raw_missing(v):")
        lines.append(f"{_indent(3)}prepared[k] = float('nan')")
        lines.append(f"{_indent(2)}else:")
        lines.append(f"{_indent(3)}prepared[k] = v")
        lines.append(f"{_indent(3)}all_missing = False")
        lines.append(f"{_indent(1)}if all_missing:")
        lines.append(f"{_indent(2)}return prepared, True")
    elif abnormal_spec.rule == "all_default":
        assert abnormal_spec.default_fill_value is not None
        fill_val = float(abnormal_spec.default_fill_value)
        lines.append(f"{_indent(1)}fill_value = {fill_val!r}")
        lines.append(f"{_indent(1)}all_default_hit = True")
        lines.append(f"{_indent(1)}for k in req_features:")
        lines.append(f"{_indent(2)}v = row[k]")
        lines.append(f"{_indent(2)}if _is_raw_missing(v):")
        lines.append(f"{_indent(3)}prepared[k] = fill_value")
        lines.append(f"{_indent(2)}else:")
        lines.append(f"{_indent(3)}prepared[k] = v")
        lines.append(f"{_indent(2)}cur_v = prepared[k]")
        lines.append(f"{_indent(2)}is_def = False")
        lines.append(f"{_indent(2)}if cur_v == fill_value:")
        lines.append(f"{_indent(3)}is_def = True")
        lines.append(f"{_indent(2)}else:")
        lines.append(f"{_indent(3)}try:")
        lines.append(f"{_indent(4)}if float(cur_v) == fill_value:")
        lines.append(f"{_indent(5)}is_def = True")
        lines.append(f"{_indent(3)}except (TypeError, ValueError):")
        lines.append(f"{_indent(4)}pass")
        lines.append(f"{_indent(2)}if not is_def:")
        lines.append(f"{_indent(3)}all_default_hit = False")
        lines.append(f"{_indent(1)}if all_default_hit:")
        lines.append(f"{_indent(2)}return prepared, True")
    else:
        lines.append(f"{_indent(1)}for k in req_features:")
        lines.append(f"{_indent(2)}v = row[k]")
        lines.append(f"{_indent(2)}if _is_raw_missing(v):")
        lines.append(f"{_indent(3)}prepared[k] = float('nan')")
        lines.append(f"{_indent(2)}else:")
        lines.append(f"{_indent(3)}prepared[k] = v")

    lines.append("")
    lines.append(f"{_indent(1)}# 3. 数值类型转换")
    lines.append(f"{_indent(1)}num_features = {num_feats!r}")
    lines.append(f"{_indent(1)}invalid_entries = []")
    lines.append(f"{_indent(1)}for k in num_features:")
    lines.append(f"{_indent(2)}v = prepared[k]")
    lines.append(f"{_indent(2)}if isinstance(v, float) and math.isnan(v):")
    lines.append(f"{_indent(3)}continue")
    lines.append(f"{_indent(2)}try:")
    lines.append(f"{_indent(3)}prepared[k] = float(v)")
    lines.append(f"{_indent(2)}except (TypeError, ValueError):")
    lines.append(f"{_indent(3)}invalid_entries.append((k, v))")
    lines.append(f"{_indent(1)}if invalid_entries:")
    lines.append(
        f"{_indent(2)}err_msg = ', '.join(f'{{k}}={{v!r}}' for k, v in invalid_entries)"
    )
    lines.append(
        f"{_indent(2)}raise ValueError(f\"Invalid numeric value(s): {{err_msg}}\")"
    )

    lines.append("")
    lines.append(f"{_indent(1)}# 4. 模型特定的缺失值标准化")
    if zero_missing_feats:
        lines.append(f"{_indent(1)}zero_missing_feats = {zero_missing_feats!r}")
        lines.append(f"{_indent(1)}for k in zero_missing_feats:")
        lines.append(f"{_indent(2)}v = prepared[k]")
        lines.append(
            f"{_indent(2)}if not (isinstance(v, float) and math.isnan(v)) and v == 0:"
        )
        lines.append(f"{_indent(3)}prepared[k] = float('nan')")
    if none_missing_feats:
        lines.append(f"{_indent(1)}none_missing_feats = {none_missing_feats!r}")
        lines.append(f"{_indent(1)}for k in none_missing_feats:")
        lines.append(f"{_indent(2)}v = prepared[k]")
        lines.append(f"{_indent(2)}if isinstance(v, float) and math.isnan(v):")
        lines.append(f"{_indent(3)}prepared[k] = 0.0")

    lines.append("")
    lines.append(f"{_indent(1)}return prepared, False")
    lines.append("")

    for idx, tree in enumerate(ir.trees):
        lines.append(f"def _tree_{idx}(row):")
        _render_node(lines, tree, 1)
        lines.append("")

    lines.append("def predict(row):")
    lines.append(f"{_indent(1)}prepared, is_abnormal = _prepare_input(row)")
    if abnormal_spec.active:
        assert abnormal_spec.abnormal_value is not None
        abnormal_literal = _fmt_num(float(abnormal_spec.abnormal_value))
        lines.append(f"{_indent(1)}if is_abnormal:")
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
                f"{_indent(1)}margin = _f32(margin + _f32(_tree_{idx}(prepared)))"
            )
        lines.append(f"{_indent(1)}score_p = _xgb_sigmoid(margin)")
    else:
        lines.append(f"{_indent(1)}margin = {_fmt_num(ir.base_margin)}")
        for idx in range(len(ir.trees)):
            lines.append(f"{_indent(1)}margin += _tree_{idx}(prepared)")
        lines.append(f"{_indent(1)}score_p = 1.0 / (1.0 + math.exp(-margin))")

    if score_spec is not None:
        lines.append(f"{_indent(1)}score = _probability_to_score(score_p)")
        lines.append(f"{_indent(1)}return {{'score_p': score_p, 'score': score}}")
    else:
        lines.append(f"{_indent(1)}return {{'score_p': score_p}}")

    return "\n".join(lines) + "\n"
