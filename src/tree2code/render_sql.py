from __future__ import annotations

from typing import Dict, Optional, Sequence

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


def _quote_ident(name: str, dialect: str) -> str:
    """Quote a SQL identifier based on the dialect.

    Args:
        name: The identifier name.
        dialect: SQL dialect ('psql' or 'hive').

    Returns:
        str: Quoted identifier.
    """
    if dialect == "psql":
        escaped = name.replace('"', '""')
        return f'"{escaped}"'
    escaped = name.replace("`", "``")
    return f"`{escaped}`"


def _missing_expr(column: str, missing_type: str) -> str:
    """Generate the SQL expression for checking if a column value is missing.

    Args:
        column: The quoted column name.
        missing_type: The type of missingness ('nan' or 'zero').

    Returns:
        str: SQL expression.
    """
    if missing_type == "zero":
        return f"({column} is null or {column} = 0)"
    return f"{column} is null"


def _not_missing_expr(column: str, missing_type: str) -> str:
    """Generate the SQL expression for checking if a column value is NOT missing.

    Args:
        column: The quoted column name.
        missing_type: The type of missingness ('nan' or 'zero').

    Returns:
        str: SQL expression.
    """
    if missing_type == "zero":
        return f"({column} is not null and {column} <> 0)"
    return f"{column} is not null"


def _indent(level: int) -> str:
    """Return a string of spaces for the given indentation level.

    Args:
        level: Number of levels (4 spaces each).

    Returns:
        str: The indentation string.
    """
    return "    " * level


def _render_tree(node: TreeNode, dialect: str, depth: int = 0) -> str:
    """Recursively render a tree node into SQL CASE WHEN expressions.

    Args:
        node: The tree node to render.
        dialect: SQL dialect.
        depth: Current indentation depth.

    Returns:
        str: Formatted SQL CASE WHEN expression.
    """
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

    if node.default_left:
        cond = f"({missing} or ({not_missing} and {col} {op} {threshold}))"
    else:
        cond = f"(({not_missing} and {col} {op} {threshold}))"

    nested_indent = _indent(depth + 1)
    current_indent = _indent(depth)

    left_expr = _render_tree(node.left, dialect, depth + 1)
    right_expr = _render_tree(node.right, dialect, depth + 1)

    return (
        f"(case when {cond} then\n"
        f"{nested_indent}{left_expr}\n"
        f"{current_indent}else\n"
        f"{nested_indent}{right_expr}\n"
        f"{current_indent}end)"
    )


def _build_abnormal_condition(
    feature_names: Sequence[str],
    dialect: str,
    abnormal_spec: AbnormalSpec,
) -> Optional[str]:
    """Generate the SQL condition for checking abnormal rules.

    Args:
        feature_names: List of all feature names in the model.
        dialect: SQL dialect.
        abnormal_spec: The abnormal rule specification.

    Returns:
        Optional[str]: The SQL condition, or None if no rule is active.
    """
    if not abnormal_spec.active:
        return None

    if not feature_names:
        return None

    cols = [_quote_ident(name, dialect) for name in feature_names]

    if abnormal_spec.rule == "all_null":
        # Using concat(...) is null as requested
        return f"concat({', '.join(cols)}) is null"

    if abnormal_spec.rule == "all_default":
        assert abnormal_spec.default_fill_value is not None
        default_literal = _fmt_num(float(abnormal_spec.default_fill_value))
        cols_csv = ", ".join(cols)
        return f"least({cols_csv}) = {default_literal} and greatest({cols_csv}) = {default_literal}"

    return None


def _score_expression(
    score_p_expr: str, score_spec: ScoreSpec, dialect: str, multi_line: bool = False
) -> str:
    """Generate the SQL expression to convert probability into a scorecard score.

    Args:
        score_p_expr: The SQL expression for probability.
        score_spec: Scorecard specification.
        dialect: SQL dialect.
        multi_line: Whether to use 'a' and 'b' variables (for DDL mode).

    Returns:
        str: SQL expression for the score.
    """
    p_lo = _fmt_num(score_spec.epsilon)
    p_hi = _fmt_num(1.0 - score_spec.epsilon)
    p_clamped = f"least(greatest(({score_p_expr}), {p_lo}), {p_hi})"
    odds = f"(({p_clamped}) / (1.0 - ({p_clamped})))"

    # In DDL mode, we use 'a' and 'b' from the subquery
    if multi_line:
        raw = f"(a - b * ln({odds}))"
    else:
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
    output_table: Optional[str],
    score_spec: Optional[ScoreSpec],
    abnormal_spec: AbnormalSpec,
) -> Dict[str, Optional[str]]:
    """Render the model IR into SQL code.

    Args:
        ir: The model intermediate representation.
        dialect: SQL dialect ('psql' or 'hive').
        sql_mode: SQL mode ('expression', 'select', or 'ddl').
        keep_columns: Columns to keep in SELECT/DDL.
        table_name: Source table name.
        output_table: Target table name for DDL.
        score_spec: Optional scorecard parameters.
        abnormal_spec: Abnormal rule specification.

    Returns:
        Dict[str, Optional[str]]: Generated SQL components.
    """
    if dialect not in {"psql", "hive"}:
        raise ValueError("dialect must be 'psql' or 'hive'")
    if sql_mode not in {"expression", "select", "ddl"}:
        raise ValueError("sql_mode must be 'expression', 'select' or 'ddl'")

    # Base Margin
    base_margin_val = _fmt_num(ir.base_margin)

    # Normal probability expression (Internal)
    tree_terms = [_render_tree(tree, dialect, 0) for tree in ir.trees]
    if tree_terms:
        margin_body = " + ".join(tree_terms)
    else:
        margin_body = "0.0"

    if abs(ir.base_margin) > 0:
        margin_expr = f"({margin_body} + {base_margin_val})"
    else:
        margin_expr = f"({margin_body})"

    def _wrap_float(expr: str) -> str:
        if ir.model_type == "xgboost":
            if dialect == "psql":
                return f"({expr})::real"
            else:
                return f"cast(({expr}) as float)"
        return expr

    normal_score_p_expr = _wrap_float(f"1.0 / (1.0 + exp(-({margin_expr})))")

    # Abnormal condition
    abnormal_cond = _build_abnormal_condition(ir.feature_names, dialect, abnormal_spec)
    abnormal_literal = (
        _fmt_num(float(abnormal_spec.abnormal_value))
        if abnormal_spec.active
        else "None"
    )

    # Final score_p expression for 'expression' and 'select' mode
    if abnormal_cond is not None:
        score_p_expr = f"(case when {abnormal_cond} then {abnormal_literal} else {normal_score_p_expr} end)"
    else:
        score_p_expr = normal_score_p_expr

    # Final score expression for 'expression' and 'select' mode
    score_expr: Optional[str] = None
    if score_spec is not None:
        normal_score_expr = _score_expression(normal_score_p_expr, score_spec, dialect)
        if abnormal_cond is not None:
            score_expr = f"(case when {abnormal_cond} then {abnormal_literal} else {normal_score_expr} end)"
        else:
            score_expr = normal_score_expr

    select_sql: Optional[str] = None
    if sql_mode == "select":
        lines = ["select"]
        fields = []
        for col in keep_columns or []:
            fields.append(_quote_ident(col, dialect))
        fields.append(f"{score_p_expr} as score_p")
        if score_expr is not None:
            fields.append(f"{score_expr} as score")

        for i, field in enumerate(fields):
            prefix = "    " if i == 0 else "    ,"
            lines.append(f"{prefix}{field}")
        lines.append(f"from {table_name}")
        select_sql = "\n".join(lines)

    ddl_sql: Optional[str] = None
    if sql_mode == "ddl":
        out_name = output_table or "output_table"
        stored_as = " stored as orc" if dialect == "hive" else ""

        # Tree scores projection
        tree_score_fields = []
        for idx, tree in enumerate(ir.trees):
            tree_expr = _render_tree(tree, dialect, 3)
            tree_score_fields.append(
                f"            --tree{idx}\n            ,{tree_expr} as tree_{idx}_score"
            )

        tree_sum = (
            " + ".join([f"tree_{i}_score" for i in range(len(ir.trees))])
            if ir.trees
            else "0.0"
        )
        margin_sum_expr = f"({tree_sum}) + ({base_margin_val})"
        inner_score_p_expr = _wrap_float(f"1 / (1 + exp(-({margin_sum_expr})))")

        # Top level select fields
        top_fields = []
        for col in keep_columns or []:
            top_fields.append(_quote_ident(col, dialect))
        top_fields.append("score_p")

        if score_spec is not None:
            # Reconstruct score logic using a and b
            score_final_logic = _score_expression(
                "score_p", score_spec, dialect, multi_line=True
            )
            if abnormal_cond is not None:
                top_fields.append(
                    f"case when {abnormal_cond} then {abnormal_literal} else {score_final_logic} end as score"
                )
            else:
                top_fields.append(f"{score_final_logic} as score")

        top_fields_str = "\n    ".join(
            [("" if i == 0 else ",") + f"{f}" for i, f in enumerate(top_fields)]
        )

        core_score_p = (
            f"case when {abnormal_cond} then {abnormal_literal} else {inner_score_p_expr} end"
            if abnormal_cond
            else inner_score_p_expr
        )

        ddl_lines = [
            f"drop table if exists {out_name};",
            f"create table {out_name}{stored_as} as",
            "select",
            f"    {top_fields_str}",
            "from (",
            "    select",
            "        *",
            f"        ,{_fmt_num(score_spec.pdo)} / ln(2) as b" if score_spec else "",
            (
                f"        ,{_fmt_num(score_spec.base_score)} + ({_fmt_num(score_spec.pdo)} / ln(2)) * ln(1 / {_fmt_num(score_spec.base_odds)}) as a"
                if score_spec
                else ""
            ),
            f"        ,{core_score_p} as score_p",
            "    from (",
            "        select",
            "            *",
            "\n".join(tree_score_fields),
            f"        from {table_name}",
            "    ) t",
            ") t2;",
        ]
        # Clean up empty strings from optional parts
        ddl_sql = "\n".join(
            [line for line in ddl_lines if line.strip() or not line.endswith(" ")]
        )

    return {
        "dialect": dialect,
        "score_p_expr": score_p_expr,
        "score_expr": score_expr,
        "select_sql": select_sql,
        "ddl_sql": ddl_sql,
    }
