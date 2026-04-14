from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence

from .ir import ModelIR, TreeNode
from .scoring import AbnormalSpec, ScoreSpec

HIVE_MIN_NONZERO_THRESHOLD = 1e-13


def _fmt_num(value: float, dialect: str) -> str:
    """Format a float to a high-precision string.

    Args:
        value: The float to format.
        dialect: SQL dialect ('psql' or 'hive').

    Returns:
        str: The formatted string.
    """
    if dialect == "hive":
        # Using scientific notation to force Spark to parse as DOUBLE
        # otherwise a literal like 0.1 is parsed as DECIMAL.
        return format(float(value), ".17e")
    return format(float(value), ".17g")


def _fmt_split_threshold(value: float, dialect: str) -> str:
    """Format numeric split threshold with dialect-specific safeguards."""
    threshold = float(value)
    if (
        dialect == "hive"
        and threshold != 0.0
        and abs(threshold) < HIVE_MIN_NONZERO_THRESHOLD
    ):
        return "1e-13" if threshold > 0 else "-1e-13"
    return _fmt_num(threshold, dialect)


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


def _indent(level: int) -> str:
    """Return a string of spaces for the given indentation level.

    Args:
        level: Number of levels (4 spaces each).

    Returns:
        str: The indentation string.
    """
    return "    " * level


def _sql_string_literal(value: str) -> str:
    """Escape a SQL string literal."""
    return "'" + value.replace("'", "''") + "'"


def _cast_text(expr: str, dialect: str) -> str:
    """Cast expression to text/string for category matching."""
    if dialect == "psql":
        return f"cast(({expr}) as text)"
    return f"cast(({expr}) as string)"


def _float32_cast_expr(expr: str, dialect: str) -> str:
    """Cast expression to float32-equivalent SQL type."""
    if dialect == "psql":
        return f"cast(({expr}) as real)"
    return f"cast(({expr}) as float)"


def _nan_check_expr(column: str, dialect: str) -> str:
    """Generate a dialect-specific SQL expression to detect NaN.

    The naive ``col <> col`` trick does NOT work in PostgreSQL or
    Spark/Hive because both engines treat ``NaN = NaN`` as *true*
    (non-IEEE-754 semantics), so ``col <> col`` returns *false*
    for NaN values.
    """
    if dialect == "psql":
        return f"({column} = 'NaN'::double precision)"
    return f"isnan({column})"


def _missing_expr(column: str, missing_type: str, dialect: str) -> str:
    """Generate SQL expression for missing-value check.

    This treats both NULL and NaN as missing.
    """
    if missing_type == "none":
        return "false"

    nan_check = _nan_check_expr(column, dialect)
    if missing_type == "zero":
        return f"({column} is null or {nan_check} or {column} = 0)"
    return f"({column} is null or {nan_check})"


def _not_missing_expr(column: str, missing_type: str, dialect: str) -> str:
    """Generate SQL expression for non-missing-value check."""
    return f"(not {_missing_expr(column, missing_type, dialect)})"


def _render_case_when(
    condition: str,
    true_expr: str,
    false_expr: str,
    depth: int = 0,
    wrap: bool = True,
) -> str:
    """Render a multi-line CASE WHEN expression."""
    current_indent = _indent(depth)
    nested_indent = _indent(depth + 1)

    body = (
        f"case when {condition} then\n"
        f"{nested_indent}{true_expr}\n"
        f"{current_indent}else\n"
        f"{nested_indent}{false_expr}\n"
        f"{current_indent}end"
    )

    if wrap:
        return f"({body})"
    return body


def _is_numeric_category(value: Any) -> bool:
    """Check whether a category literal should be rendered as numeric."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _categorical_match_expr(column: str, categories: Sequence[Any], dialect: str) -> str:
    """Render SQL membership check for categorical split."""
    if not categories:
        return "false"

    if all(_is_numeric_category(v) for v in categories):
        literals = ", ".join(_fmt_num(float(v), dialect) for v in categories)
        return f"{column} in ({literals})"

    casted = _cast_text(column, dialect)
    literals = ", ".join(_sql_string_literal(str(v)) for v in categories)
    return f"{casted} in ({literals})"


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
        return _fmt_num(node.leaf_value, dialect)

    assert node.feature is not None
    assert node.left is not None
    assert node.right is not None

    col = _quote_ident(node.feature, dialect)

    missing = _missing_expr(col, node.missing_type, dialect)
    not_missing = _not_missing_expr(col, node.missing_type, dialect)

    if node.split_type == "categorical":
        cat_match = _categorical_match_expr(col, node.categories or [], dialect)
        if node.default_left:
            cond = f"({missing} or ({not_missing} and {cat_match}))"
        else:
            cond = f"({not_missing} and {cat_match})"
    else:
        assert node.threshold is not None
        threshold = _fmt_split_threshold(node.threshold, dialect)
        op = "<=" if node.operator == "<=" else "<"

        if node.float32_compare:
            cmp_expr = (
                f"{_float32_cast_expr(col, dialect)} {op} "
                f"{_float32_cast_expr(threshold, dialect)}"
            )
        else:
            cmp_expr = f"{col} {op} {threshold}"

        if node.default_left:
            cond = f"({missing} or ({not_missing} and {cmp_expr}))"
        else:
            cond = f"({not_missing} and {cmp_expr})"

    left_expr = _render_tree(node.left, dialect, depth + 1)
    right_expr = _render_tree(node.right, dialect, depth + 1)
    return _render_case_when(cond, left_expr, right_expr, depth=depth, wrap=True)


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
        checks = [_missing_expr(col, "nan", dialect) for col in cols]
        return " and ".join(f"({check})" for check in checks)

    if abnormal_spec.rule == "all_default":
        assert abnormal_spec.default_fill_value is not None
        default_literal = _fmt_num(float(abnormal_spec.default_fill_value), dialect)
        cols_csv = ", ".join(cols)
        return (
            f"least({cols_csv}) = {default_literal} and "
            f"greatest({cols_csv}) = {default_literal}"
        )

    return None


def _score_expression(
    score_p_expr: str, score_spec: ScoreSpec, dialect: str, multi_line: bool = False
) -> str:
    """Generate SQL expression to convert probability into a scorecard score.

    Args:
        score_p_expr: The SQL expression for probability.
        score_spec: Scorecard specification.
        dialect: SQL dialect.
        multi_line: Whether to use 'a' and 'b' variables (for DDL mode).

    Returns:
        str: SQL expression for the score.
    """
    p_lo = _fmt_num(score_spec.epsilon, dialect)
    p_hi = _fmt_num(1.0 - score_spec.epsilon, dialect)
    p_clamped = f"least(greatest(({score_p_expr}), {p_lo}), {p_hi})"
    odds = f"(({p_clamped}) / (1.0 - ({p_clamped})))"

    if multi_line:
        raw = f"(a - b * ln({odds}))"
    else:
        raw = f"({_fmt_num(score_spec.offset, dialect)} - {_fmt_num(score_spec.factor, dialect)} * ln({odds}))"

    if dialect == "psql":
        return f"round(({raw})::numeric, {score_spec.score_scale})"
    return f"round({raw}, {score_spec.score_scale})"


def _append_multiline_field(
    lines: List[str],
    field: str,
    *,
    is_first: bool,
    base_prefix: str = "    ",
) -> None:
    """Append a possibly multi-line field preserving indentation."""
    first_prefix = base_prefix if is_first else base_prefix + ","
    rest_prefix = base_prefix if is_first else base_prefix + " "

    parts = field.splitlines()
    lines.append(first_prefix + parts[0])
    for part in parts[1:]:
        lines.append(rest_prefix + part)


def _suffix_last_line(expr: str, suffix: str) -> str:
    """Append suffix to the last line of a multi-line expression."""
    parts = expr.splitlines()
    if not parts:
        return suffix
    parts[-1] = parts[-1] + suffix
    return "\n".join(parts)


def _xgb_margin_expr(tree_terms: Sequence[str], base_margin: str, dialect: str) -> str:
    """Build XGBoost margin expression with float32-aligned accumulation."""
    margin_expr = _float32_cast_expr(base_margin, dialect)
    for term in tree_terms:
        margin_expr = _float32_cast_expr(
            f"{margin_expr} + {_float32_cast_expr(term, dialect)}",
            dialect,
        )
    return margin_expr


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

    base_margin_val = _fmt_num(ir.base_margin, dialect)

    tree_terms = [_render_tree(tree, dialect, 0) for tree in ir.trees]
    margin_body = " + ".join(tree_terms) if tree_terms else "0.0"

    if ir.model_type == "xgboost":
        margin_expr = _xgb_margin_expr(tree_terms, base_margin_val, dialect)
    elif abs(ir.base_margin) > 0:
        margin_expr = f"({margin_body} + {base_margin_val})"
    else:
        margin_expr = f"({margin_body})"

    def _wrap_float(expr: str) -> str:
        if ir.model_type == "xgboost":
            return _float32_cast_expr(expr, dialect)
        return expr

    normal_score_p_expr = _wrap_float(f"1.0 / (1.0 + exp(-({margin_expr})))")

    abnormal_cond = _build_abnormal_condition(ir.feature_names, dialect, abnormal_spec)
    abnormal_literal = (
        _fmt_num(float(abnormal_spec.abnormal_value), dialect)
        if abnormal_spec.active
        else "None"
    )

    if abnormal_cond is not None:
        score_p_expr = _render_case_when(
            abnormal_cond,
            abnormal_literal,
            normal_score_p_expr,
            depth=0,
            wrap=True,
        )
    else:
        score_p_expr = normal_score_p_expr

    score_expr: Optional[str] = None
    if score_spec is not None:
        normal_score_expr = _score_expression(normal_score_p_expr, score_spec, dialect)
        if abnormal_cond is not None:
            score_expr = _render_case_when(
                abnormal_cond,
                abnormal_literal,
                normal_score_expr,
                depth=0,
                wrap=True,
            )
        else:
            score_expr = normal_score_expr

    select_sql: Optional[str] = None
    if sql_mode == "select":
        lines: List[str] = ["select"]
        fields: List[str] = []

        for col in keep_columns or []:
            fields.append(_quote_ident(col, dialect))
        fields.append(f"{score_p_expr} as score_p")
        if score_expr is not None:
            fields.append(f"{score_expr} as score")

        for idx, field in enumerate(fields):
            _append_multiline_field(lines, field, is_first=(idx == 0), base_prefix="    ")

        lines.append(f"from {table_name}")
        select_sql = "\n".join(lines)

    ddl_sql: Optional[str] = None
    if sql_mode == "ddl":
        out_name = output_table or "output_table"
        stored_as = " stored as orc" if dialect == "hive" else ""

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
        if ir.model_type == "xgboost":
            tree_terms_ddl = [f"tree_{i}_score" for i in range(len(ir.trees))]
            margin_sum_expr = _xgb_margin_expr(tree_terms_ddl, base_margin_val, dialect)
        else:
            margin_sum_expr = f"({tree_sum}) + ({base_margin_val})"
        inner_score_p_expr = _wrap_float(f"1 / (1 + exp(-({margin_sum_expr})))")

        top_fields: List[str] = []
        for col in keep_columns or []:
            top_fields.append(_quote_ident(col, dialect))
        top_fields.append("score_p")

        if score_spec is not None:
            score_final_logic = _score_expression(
                "score_p", score_spec, dialect, multi_line=True
            )
            if abnormal_cond is not None:
                score_case = _render_case_when(
                    abnormal_cond,
                    abnormal_literal,
                    score_final_logic,
                    depth=0,
                    wrap=False,
                )
                top_fields.append(_suffix_last_line(score_case, " as score"))
            else:
                top_fields.append(f"{score_final_logic} as score")

        core_score_p = (
            _render_case_when(
                abnormal_cond,
                abnormal_literal,
                inner_score_p_expr,
                depth=0,
                wrap=False,
            )
            if abnormal_cond
            else inner_score_p_expr
        )

        ddl_lines: List[str] = [
            f"drop table if exists {out_name};",
            f"create table {out_name}{stored_as} as",
            "select",
        ]

        for idx, field in enumerate(top_fields):
            _append_multiline_field(ddl_lines, field, is_first=(idx == 0), base_prefix="    ")

        ddl_lines.extend(
            [
                "from (",
                "    select",
                "        *",
                f"        ,{_fmt_num(score_spec.pdo, dialect)} / ln(2) as b" if score_spec else "",
                (
                    f"        ,{_fmt_num(score_spec.base_score, dialect)} + ({_fmt_num(score_spec.pdo, dialect)} / ln(2)) * "
                    f"ln(1 / {_fmt_num(score_spec.base_odds, dialect)}) as a"
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
        )

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
