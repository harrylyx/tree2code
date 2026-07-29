import math

from tree2code import convert


def _load_predictor(code: str):
    namespace = {}
    exec(code, namespace)
    return namespace["predict"]


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
    predict = _load_predictor(out["python"])

    feature_names = out["meta"]["feature_names"]
    row = {name: None for name in feature_names}
    result = predict(row)
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
    predict = _load_predictor(out["python"])

    feature_names = out["meta"]["feature_names"]
    row = {name: -999.0 for name in feature_names}
    result = predict(row)
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
    predict = _load_predictor(out["python"])
    result = predict(first_row)

    assert isinstance(result["score"], float)
    as_text = f"{result['score']:.3f}"
    assert float(as_text) == result["score"]
    assert math.isfinite(result["score"])


def test_base_odds_100_score_regression(xgb_model, first_row):
    base_score, pdo, base_odds = 600.0, 60.0, 100.0
    out = convert(
        xgb_model,
        to="python",
        base_score=base_score,
        pdo=pdo,
        base_odds=base_odds,
        score_scale=3,
    )
    predict = _load_predictor(out["python"])
    res = predict(first_row)
    prob = res["score_p"]
    
    # Reference formula:
    factor = pdo / math.log(2.0)
    offset = base_score - factor * math.log(base_odds)
    odds = prob / (1.0 - prob)
    raw_expected = offset - factor * math.log(odds)
    from decimal import Decimal, ROUND_HALF_UP
    expected_score = float(Decimal(str(raw_expected)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))
    
    assert res["score"] == expected_score
    # Verify historical offset error is absent (historical was offset by ~398.63)
    wrong_offset = base_score + factor * math.log(base_odds)
    wrong_expected = float(Decimal(str(wrong_offset - factor * math.log(odds))).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))
    assert abs(res["score"] - wrong_expected) > 300.0


def test_missing_required_keys_raises_key_error(xgb_model):
    out = convert(xgb_model, to="python")
    predict = _load_predictor(out["python"])
    req = out["meta"]["feature_names"]
    
    # Pass empty dict
    import pytest
    with pytest.raises(KeyError) as exc_info:
        predict({})
    for key in req:
        assert key in str(exc_info.value)


def test_invalid_numeric_values_raises_value_error(xgb_model, first_row):
    out = convert(xgb_model, to="python")
    predict = _load_predictor(out["python"])
    req = out["meta"]["feature_names"]
    
    bad_row = dict(first_row)
    bad_row[req[0]] = "invalid_number_abc"
    if len(req) > 1:
        bad_row[req[1]] = [1, 2]
    
    import pytest
    with pytest.raises(ValueError) as exc_info:
        predict(bad_row)
    assert req[0] in str(exc_info.value)
    assert "invalid_number_abc" in str(exc_info.value)


def test_raw_missing_markers_and_editable_text_set(xgb_model, first_row):
    out = convert(xgb_model, to="python")
    ns = {}
    exec(out["python"], ns)
    predict = ns["predict"]
    req = out["meta"]["feature_names"]
    
    # Test built-in markers produce same output as None
    row_none = dict(first_row)
    row_none[req[0]] = None
    res_none = predict(row_none)
    
    for marker in ["", "nan", "NULL", " None "]:
        r = dict(first_row)
        r[req[0]] = marker
        res_m = predict(r)
        assert res_m["score_p"] == res_none["score_p"]
        
    # Extend missing text set
    ns["MISSING_TEXT_VALUES"].add("na")
    r_na = dict(first_row)
    r_na[req[0]] = " NA "
    res_na = predict(r_na)
    assert res_na["score_p"] == res_none["score_p"]

