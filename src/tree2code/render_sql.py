from __future__ import annotations

import math
from typing import Dict, List, Optional, Sequence

from .ir import ModelIR, TreeNode
from .scoring import AbnormalSpec, ScoreSpec


def _fmt_num(value: float) -> str:
    return format(float(value), ".17g")


def _quote_ident(name: str, dialect: str) -> str:
    if dialect == "psql":
        escaped = name.replace('"', '""')
        return f'"{escaped}"'
    escaped = name.replace("`", "``")
    return f"`{escaped}`"


def _missing_expr(column: str, missing_type: str) -> str:
    if missing_type == "zero":
        return f"({column} is null or {column} = 0)"
    return f"{column} is null"


def _not_missing_expr(column: str, missing_type: str) -> str:
    if missing_type == "zero":
        return f"({column} is not null and {column} <> 0)"
    return f"{column} is not null"


def _render_tree(node: TreeNode, dialect: str) -> str:
    if node.is_leaf:
        assert node.leaf_value is not None
        return _fmt_num(node.leaf_value)

    assert node.feature is not None
    assert node.threshold is not None
    assert node.left is not None
    assert node.right is not None

    col = _quote_ident(node.feature, dialect)
    threshold = _fmt_num(node.threshold)
    op = "<=" if node.operator == "<=" else "<"

    missing = _missing_expr(col, node.missing_type)
    not_missing = _not_missing_expr(col, node.missing_type)

    left_expr = _render_tree(node.left, dialect)
    right_expr = _render_tree(node.right, dialect)

    if node.default_left:
        cond = f"({missing} or ({not_missing} and {col} {op} {threshold}))"
    else:
        cond = f"(({not_missing} and {col} {op} {threshold}))"

    return f"(case when {cond} then {left_expr} else {right_expr} end)"


def _build_abnormal_condition(
    feature_names: Sequence[str],
    dialect: str,
    abnormal_spec: AbnormalSpec,
) -> Optional[str]:
    if not abnormal_spec.active:
        return None

    if not feature_names:
        return None

    parts: List[str] = []
    if abnormal_spec.rule == "all_null":
        for name in feature_names:
            col = _quote_ident(name, dialect)
            parts.append(f"{col} is null")
        return " and ".join(parts)

    if abnormal_spec.rule == "all_default":
        assert abnormal_spec.default_fill_value is not None
        default_literal = _fmt_num(float(abnormal_spec.default_fill_value))
        for name in feature_names:
            col = _quote_ident(name, dialect)
            parts.append(f"{col} = {default_literal}")
        return " and ".join(parts)

    return None


def _score_expression(score_p_expr: str, score_spec: ScoreSpec, dialect: str) -> str:
    p_lo = _fmt_num(score_spec.epsilon)
    p_hi = _fmt_num(1.0 - score_spec.epsilon)
    p_clamped = f"least(greatest(({score_p_expr}), {p_lo}), {p_hi})"
    odds = f"(({p_clamped}) / (1.0 - ({p_clamped})))"
    raw = f"({_fmt_num(score_spec.offset)} - {_fmt_num(score_spec.factor)} * ln({odds}))"

    if dialect == "psql":
        return f"round(({raw})::numeric, {score_spec.score_scale})"
    return f"round({raw}, {score_spec.score_scale})"


def render_sql(
    ir: ModelIR,
    dialect: str,
    sql_mode: str,
    keep_columns: Optional[Sequence[str]],
    table_name: str,
    score_spec: Optional[ScoreSpec],
    abnormal_spec: AbnormalSpec,
) -> Dict[str, Optional[str]]:
    if dialect not in {"psql", "hive"}:
        raise ValueError("dialect must be 'psql' or 'hive'")
    if sql_mode not in {"expression", "select"}:
        raise ValueError("sql_mode must be 'expression' or 'select'")

    tree_terms = [_render_tree(tree, dialect) for tree in ir.trees]
    if tree_terms:
        margin_body = " + ".join(tree_terms)
    else:
        margin_body = "0.0"

    if abs(ir.base_margin) > 0:
        margin_expr = f"({margin_body} + {_fmt_num(ir.base_margin)})"
    else:
        margin_expr = f"({margin_body})"

    normal_score_p_expr = f"(1.0 / (1.0 + exp(-({margin_expr}))))"
    if ir.model_type == "xgboost":
        if dialect == "psql":
            normal_score_p_expr = f"(({normal_score_p_expr})::real)"
        else:
            normal_score_p_expr = f"(cast(({normal_score_p_expr}) as float))"

    abnormal_cond = _build_abnormal_condition(ir.feature_names, dialect, abnormal_spec)
    if abnormal_cond is not None:
        abnormal_literal = _fmt_num(float(abnormal_spec.abnormal_value))
        score_p_expr = f"(case when ({abnormal_cond}) then {abnormal_literal} else {normal_score_p_expr} end)"
    else:
        score_p_expr = normal_score_p_expr

    score_expr: Optional[str] = None
    if score_spec is not None:
        normal_score_expr = _score_expression(normal_score_p_expr, score_spec, dialect)
        if abnormal_cond is not None:
            abnormal_literal = _fmt_num(float(abnormal_spec.abnormal_value))
            score_expr = f"(case when ({abnormal_cond}) then {abnormal_literal} else {normal_score_expr} end)"
        else:
            score_expr = normal_score_expr

    select_sql: Optional[str] = None
    if sql_mode == "select":
        select_fields: List[str] = []
        for col in keep_columns or []:
            select_fields.append(col)
        select_fields.append(f"{score_p_expr} as score_p")
        if score_expr is not None:
            select_fields.append(f"{score_expr} as score")

        select_sql = "select " + ", ".join(select_fields) + f"\nfrom {table_name}"

    return {
        "dialect": dialect,
        "score_p_expr": score_p_expr,
        "score_expr": score_expr,
        "select_sql": select_sql,
    }
