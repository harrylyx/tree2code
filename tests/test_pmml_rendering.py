import math
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd
import pytest

from tree2code import convert


PMML_VERSION_CASES = {
    "4.4.1": ("4.4.1", "https://www.dmg.org/PMML-4_4"),
    "4.3": ("4.3", "https://www.dmg.org/PMML-4_3"),
    "4.2.1": ("4.2", "https://www.dmg.org/PMML-4_2"),
}


def _namespace(root: ET.Element) -> str:
    return root.tag[1:].split("}", 1)[0]


def _row_dict(row: pd.Series) -> dict:
    output = {}
    for key, value in row.to_dict().items():
        if hasattr(value, "item"):
            value = value.item()
        output[key] = value
    return output


def test_pmml_versions_generate_parseable_xml(lgb_model):
    for requested_version, (pmml_version, namespace) in PMML_VERSION_CASES.items():
        result = convert(lgb_model, to="pmml", pmml_version=requested_version)
        root = ET.fromstring(result["pmml"])

        assert root.tag == f"{{{namespace}}}PMML"
        assert root.attrib["version"] == pmml_version
        assert root.find(f".//{{{namespace}}}MiningModel") is not None
        assert root.find(f".//{{{namespace}}}TreeModel") is not None
        assert root.find(f".//{{{namespace}}}RegressionModel") is not None


def test_pmml_rejects_unsupported_version(lgb_model):
    with pytest.raises(ValueError, match="pmml_version"):
        convert(lgb_model, to="pmml", pmml_version="4.1")


def test_pmml_421_omits_pmml_43_output_attributes(lgb_model):
    result = convert(lgb_model, to="pmml", pmml_version="4.2.1")

    assert "isFinalResult" not in result["pmml"]


def test_pmml_can_be_returned_with_other_outputs(lgb_model):
    result = convert(lgb_model, to=["pmml", "python"])

    assert "pmml" in result
    assert "python" in result
    assert "score_p" in result["pmml"]


def _load_pmml_predictor(pmml: str, tmp_path: Path):
    pypmml = pytest.importorskip("pypmml")
    path = tmp_path / "model.pmml"
    path.write_text(pmml, encoding="utf-8")
    return pypmml.Model.load(str(path))


def _assert_pmml_parity(model, frame, tmp_path: Path, tolerance: float) -> None:
    out = convert(model, to="pmml", compatible_mode=True)
    pmml_model = _load_pmml_predictor(out["pmml"], tmp_path)

    native_probs = model.predict_proba(frame)[:, 1]
    for idx in range(min(20, len(frame))):
        pred = pmml_model.predict(_row_dict(frame.iloc[idx]))["score_p"]
        assert math.isclose(
            float(pred),
            float(native_probs[idx]),
            rel_tol=0.0,
            abs_tol=tolerance,
        )


def test_lgb_pmml_pypmml_loads_supported_versions(lgb_model, sample_rows, tmp_path):
    expected = float(lgb_model.predict_proba(sample_rows.head(1))[0, 1])
    for version in PMML_VERSION_CASES:
        out = convert(lgb_model, to="pmml", pmml_version=version)
        pmml_model = _load_pmml_predictor(out["pmml"], tmp_path)
        pred = float(pmml_model.predict(_row_dict(sample_rows.iloc[0]))["score_p"])

        assert math.isclose(pred, expected, rel_tol=0.0, abs_tol=1e-12)


def test_lgb_pmml_pypmml_probability_parity(lgb_model, sample_rows, tmp_path):
    _assert_pmml_parity(lgb_model, sample_rows.head(40), tmp_path, tolerance=1e-12)


def test_xgb_pmml_pypmml_probability_parity(xgb_model, sample_rows, tmp_path):
    _assert_pmml_parity(xgb_model, sample_rows.head(40), tmp_path, tolerance=1e-7)


def test_lgb_categorical_pmml_pypmml_probability_parity(
    lgb_categorical_model, categorical_sample_rows, tmp_path
):
    _assert_pmml_parity(
        lgb_categorical_model,
        categorical_sample_rows.head(40),
        tmp_path,
        tolerance=1e-12,
    )


def test_xgb_categorical_pmml_pypmml_probability_parity(
    xgb_categorical_model, categorical_sample_rows, tmp_path
):
    _assert_pmml_parity(
        xgb_categorical_model,
        categorical_sample_rows.head(40),
        tmp_path,
        tolerance=1e-7,
    )
