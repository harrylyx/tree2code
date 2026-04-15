import math

import pandas as pd

from tree2code import convert
from tree2code.parsers import parse_model


def _load_predictor(code: str):
    namespace = {}
    exec(code, namespace)
    return namespace["predict_row"]


def _iter_split_nodes(node):
    stack = [node]
    while stack:
        current = stack.pop()
        if current.is_leaf:
            continue
        yield current
        assert current.left is not None
        assert current.right is not None
        stack.append(current.left)
        stack.append(current.right)


def test_lgb_categorical_tree_is_parsed_with_categories(lgb_categorical_model):
    ir = parse_model(lgb_categorical_model)
    categorical_nodes = []
    for tree in ir.trees:
        categorical_nodes.extend(
            [node for node in _iter_split_nodes(tree) if node.split_type == "categorical"]
        )

    assert categorical_nodes
    assert any(
        any(isinstance(v, str) for v in (node.categories or []))
        for node in categorical_nodes
    )


def test_xgb_categorical_tree_is_parsed_with_categories(xgb_categorical_model):
    ir = parse_model(xgb_categorical_model)
    categorical_nodes = []
    for tree in ir.trees:
        categorical_nodes.extend(
            [node for node in _iter_split_nodes(tree) if node.split_type == "categorical"]
        )

    assert categorical_nodes
    assert all(node.categories for node in categorical_nodes)


def test_lgb_missing_type_none_is_parsed(lgb_model):
    ir = parse_model(lgb_model)
    missing_types = []
    for tree in ir.trees:
        missing_types.extend([node.missing_type for node in _iter_split_nodes(tree)])

    assert "none" in missing_types


def test_lgb_categorical_python_parity(lgb_categorical_model, categorical_sample_rows):
    result = convert(lgb_categorical_model, to="python")
    predict_row = _load_predictor(result["python"])

    reference = lgb_categorical_model.predict_proba(categorical_sample_rows)[:, 1]
    for idx in range(min(120, len(categorical_sample_rows))):
        row = categorical_sample_rows.iloc[idx].to_dict()
        pred = predict_row(row)["score_p"]
        assert math.isclose(pred, float(reference[idx]), rel_tol=0.0, abs_tol=1e-12)


def test_xgb_categorical_python_parity(xgb_categorical_model, categorical_sample_rows):
    result = convert(xgb_categorical_model, to="python")
    predict_row = _load_predictor(result["python"])

    reference = xgb_categorical_model.predict_proba(categorical_sample_rows)[:, 1]
    for idx in range(min(120, len(categorical_sample_rows))):
        row = categorical_sample_rows.iloc[idx].to_dict()
        pred = predict_row(row)["score_p"]
        assert math.isclose(pred, float(reference[idx]), rel_tol=0.0, abs_tol=1e-6)


def test_sql_categorical_expression_uses_cast_for_text_categories(lgb_categorical_model):
    out = convert(
        lgb_categorical_model,
        to="sql",
        dialect="psql",
        sql_mode="expression",
    )
    expr = out["sql"]["score_p_expr"].lower()
    assert "cast((\"cat_" in expr or "cast((`cat_" in expr


def test_score_case_expression_is_multiline_formatted(xgb_model, score_params):
    out = convert(
        xgb_model,
        to="sql",
        dialect="psql",
        sql_mode="expression",
        base_score=score_params["base_score"],
        pdo=score_params["pdo"],
        base_odds=score_params["base_odds"],
        abnormal_rule="all_null",
        abnormal_value=-2,
    )
    score_expr = out["sql"]["score_expr"]
    assert score_expr is not None
    assert "then\n" in score_expr
    assert "\nelse\n" in score_expr


def test_python_missing_nan_is_treated_as_missing(xgb_model, sample_rows):
    out = convert(xgb_model, to="python")
    predict_row = _load_predictor(out["python"])

    row = sample_rows.iloc[0].to_dict()
    row["f0"] = float("nan")

    pred = float(predict_row(row)["score_p"])
    expected = float(xgb_model.predict_proba(pd.DataFrame([row]))[0, 1])
    assert math.isclose(pred, expected, rel_tol=0.0, abs_tol=1e-6)


def test_lgb_python_missing_type_none_matches_native(lgb_model, sample_rows):
    out = convert(lgb_model, to="python")
    predict_row = _load_predictor(out["python"])

    row = sample_rows.iloc[0].to_dict()
    row["f0"] = float("nan")

    pred = float(predict_row(row)["score_p"])
    expected = float(lgb_model.predict_proba(pd.DataFrame([row]))[0, 1])
    assert math.isclose(pred, expected, rel_tol=0.0, abs_tol=1e-12)


def test_xgb_python_code_uses_float32_branch_compare(xgb_model):
    out = convert(xgb_model, to="python")
    code = out["python"]
    assert "_safe_numeric_compare(" in code
    assert "True, 'nan')" in code


def test_sql_missing_expression_contains_nan_check(xgb_model):
    out_psql = convert(xgb_model, to="sql", dialect="psql", sql_mode="expression")
    expr_psql = out_psql["sql"]["score_p_expr"]
    assert "'NaN'::double precision" in expr_psql

    out_hive = convert(xgb_model, to="sql", dialect="hive", sql_mode="expression")
    expr_hive = out_hive["sql"]["score_p_expr"]
    assert "isnan(" not in expr_hive.lower()
    assert "is null" in expr_hive.lower()
    assert "cast(" in expr_hive.lower()
    assert "= 'nan'" in expr_hive.lower()
