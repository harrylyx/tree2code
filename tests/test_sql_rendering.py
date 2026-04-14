from tree2code import convert


def test_hive_sql_expression_uses_portable_functions(lgb_model, score_params):
    out = convert(
        lgb_model,
        to="sql",
        dialect="hive",
        sql_mode="expression",
        base_score=score_params["base_score"],
        pdo=score_params["pdo"],
        base_odds=score_params["base_odds"],
        abnormal_rule="all_null",
        abnormal_value=-2,
    )
    score_p_expr = out["sql"]["score_p_expr"].lower()
    score_expr = out["sql"]["score_expr"].lower()

    assert "exp(" in score_p_expr
    assert "ln(" in score_expr
    assert "::" not in score_p_expr
    assert "::" not in score_expr


def test_sql_select_contains_keep_columns(xgb_model):
    out = convert(
        xgb_model,
        to="sql",
        dialect="psql",
        sql_mode="select",
        keep_columns=["id", "group_id"],
        table_name="source_table",
    )
    sql = out["sql"]["select_sql"].lower()
    assert "select id, group_id" in sql
    assert "from source_table" in sql
