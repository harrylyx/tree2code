from tree2code import convert
from tree2code.ir import ModelIR, TreeNode
from tree2code.render_sql import render_sql
from tree2code.scoring import AbnormalSpec


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
    assert '"id"' in sql
    assert '"group_id"' in sql
    assert "from source_table" in sql


def test_hive_small_split_threshold_is_clamped():
    ir = ModelIR(
        model_type="lightgbm",
        feature_names=["f0"],
        trees=[
            TreeNode(
                feature="f0",
                split_type="numeric",
                threshold=1.0000000180025095e-35,
                left=TreeNode(leaf_value=1.0),
                right=TreeNode(leaf_value=0.0),
                default_left=True,
                operator="<=",
                missing_type="nan",
            )
        ],
        base_margin=0.0,
    )

    hive_sql = render_sql(
        ir,
        dialect="hive",
        sql_mode="expression",
        keep_columns=None,
        table_name="input_table",
        output_table=None,
        score_spec=None,
        abnormal_spec=AbnormalSpec(),
    )["score_p_expr"]
    assert hive_sql is not None
    assert "1e-13" in hive_sql.lower()
    assert "1.0000000180025095e-35" not in hive_sql.lower()

    psql_sql = render_sql(
        ir,
        dialect="psql",
        sql_mode="expression",
        keep_columns=None,
        table_name="input_table",
        output_table=None,
        score_spec=None,
        abnormal_spec=AbnormalSpec(),
    )["score_p_expr"]
    assert psql_sql is not None
    assert "1.0000000180025095e-35" in psql_sql.lower()


def test_missing_type_none_sql_normalizes_nan_to_zero():
    ir = ModelIR(
        model_type="lightgbm",
        feature_names=["f0"],
        trees=[
            TreeNode(
                feature="f0",
                split_type="numeric",
                threshold=0.1,
                left=TreeNode(leaf_value=1.0),
                right=TreeNode(leaf_value=0.0),
                default_left=True,
                operator="<=",
                missing_type="none",
            )
        ],
        base_margin=0.0,
    )

    hive_expr = render_sql(
        ir,
        dialect="hive",
        sql_mode="expression",
        keep_columns=None,
        table_name="input_table",
        output_table=None,
        score_spec=None,
        abnormal_spec=AbnormalSpec(),
    )["score_p_expr"]
    assert hive_expr is not None
    lower_expr = hive_expr.lower()
    assert "case when" in lower_expr
    assert "is null or isnan(" in lower_expr
    assert "then 0.00000000000000000e+00" in lower_expr
