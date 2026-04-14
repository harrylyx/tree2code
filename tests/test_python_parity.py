import math

from tree2code import convert


def _load_predictor(code: str):
    namespace = {}
    exec(code, namespace)
    return namespace["predict_row"]


def test_xgb_python_probability_parity(xgb_model, sample_rows):
    result = convert(xgb_model, to="python")
    predict_row = _load_predictor(result["python"])

    py_ref = xgb_model.predict_proba(sample_rows)[:, 1]
    for idx in range(min(120, len(sample_rows))):
        row = sample_rows.iloc[idx].to_dict()
        pred = predict_row(row)["score_p"]
        assert math.isclose(pred, float(py_ref[idx]), rel_tol=0.0, abs_tol=1e-7)


def test_lgb_python_probability_parity(lgb_model, sample_rows):
    result = convert(lgb_model, to="python")
    predict_row = _load_predictor(result["python"])

    py_ref = lgb_model.predict_proba(sample_rows)[:, 1]
    for idx in range(min(120, len(sample_rows))):
        row = sample_rows.iloc[idx].to_dict()
        pred = predict_row(row)["score_p"]
        assert math.isclose(pred, float(py_ref[idx]), rel_tol=0.0, abs_tol=1e-12)
