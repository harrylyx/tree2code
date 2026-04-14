import pytest

from tree2code import convert


def test_sql_expression_and_select_forms(xgb_model):
    expr_result = convert(
        xgb_model,
        to="sql",
        dialect="psql",
        sql_mode="expression",
    )
    assert "sql" in expr_result
    assert "score_p_expr" in expr_result["sql"]
    assert "exp(" in expr_result["sql"]["score_p_expr"]

    select_result = convert(
        xgb_model,
        to="sql",
        dialect="psql",
        sql_mode="select",
        keep_columns=["id"],
        table_name="model_input",
    )
    select_sql = select_result["sql"]["select_sql"]
    assert "from model_input" in select_sql.lower()
    assert "score_p" in select_sql


def test_python_output_contains_predict_function(lgb_model, score_params):
    out = convert(
        lgb_model,
        to="python",
        base_score=score_params["base_score"],
        pdo=score_params["pdo"],
        base_odds=score_params["base_odds"],
        score_scale=score_params["score_scale"],
    )
    code = out["python"]
    assert "def predict_row" in code
    assert "score_p" in code
    assert "score" in code


def test_invalid_partial_score_params_raise(xgb_model):
    with pytest.raises(ValueError):
        convert(xgb_model, to="python", base_score=600, pdo=50)
