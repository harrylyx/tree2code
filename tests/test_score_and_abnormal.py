import math

from tree2code import convert


def _load_predictor(code: str):
    namespace = {}
    exec(code, namespace)
    return namespace["predict_row"]


def test_abnormal_all_null_overrides_probability_and_score(xgb_model, score_params):
    out = convert(
        xgb_model,
        to="python",
        base_score=score_params["base_score"],
        pdo=score_params["pdo"],
        base_odds=score_params["base_odds"],
        abnormal_rule="all_null",
        abnormal_value=-2,
    )
    predict_row = _load_predictor(out["python"])

    feature_names = out["meta"]["feature_names"]
    row = {name: None for name in feature_names}
    result = predict_row(row)
    assert result["score_p"] == -2
    assert result["score"] == -2


def test_abnormal_all_default_overrides_probability_and_score(xgb_model, score_params):
    out = convert(
        xgb_model,
        to="python",
        base_score=score_params["base_score"],
        pdo=score_params["pdo"],
        base_odds=score_params["base_odds"],
        abnormal_rule="all_default",
        default_fill_value=-999.0,
        abnormal_value=-2,
    )
    predict_row = _load_predictor(out["python"])

    feature_names = out["meta"]["feature_names"]
    row = {name: -999.0 for name in feature_names}
    result = predict_row(row)
    assert result["score_p"] == -2
    assert result["score"] == -2


def test_score_rounding_is_stable_and_present(xgb_model, first_row, score_params):
    out = convert(
        xgb_model,
        to="python",
        base_score=score_params["base_score"],
        pdo=score_params["pdo"],
        base_odds=score_params["base_odds"],
        score_scale=3,
    )
    predict_row = _load_predictor(out["python"])
    result = predict_row(first_row)

    assert isinstance(result["score"], float)
    as_text = f"{result['score']:.3f}"
    assert float(as_text) == result["score"]
    assert math.isfinite(result["score"])
