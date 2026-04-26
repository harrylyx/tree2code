#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
import pickle
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

DEFAULT_MODELS = {
    "xgb": "xgb_model.pkl",
    "lgb": "lgb_model.pkl",
    "all": "all_model.pkl",
}


def _load_pickle(path: Path) -> Any:
    with path.open("rb") as f:
        return pickle.load(f)


def _feature_names(model: Any) -> List[str]:
    from tree2code.parsers import parse_model

    return list(parse_model(model).feature_names)


def _read_rows(path: Path, columns: Sequence[str], rows: int):
    import pyarrow.parquet as pq

    parquet_file = pq.ParquetFile(path)
    batch_iter = parquet_file.iter_batches(
        batch_size=rows,
        columns=list(columns),
    )
    try:
        batch = next(batch_iter)
    except StopIteration as exc:
        raise ValueError(f"No rows found in {path}") from exc
    return batch.to_pandas().head(rows).reset_index(drop=True)


def _as_pmml_value(value: Any) -> Any:
    if hasattr(value, "item"):
        value = value.item()
    try:
        if value is None or math.isnan(float(value)):
            return None
    except (TypeError, ValueError):
        pass
    return value


def _as_pmml_row(row: Any) -> Dict[str, Any]:
    return {key: _as_pmml_value(value) for key, value in row.to_dict().items()}


def _native_predict(model: Any, frame: Any, feature_names: Sequence[str]) -> List[float]:
    module = type(model).__module__
    if module.startswith("xgboost"):
        import xgboost as xgb

        matrix = xgb.DMatrix(frame.loc[:, list(feature_names)], feature_names=list(feature_names))
        return [float(value) for value in model.predict(matrix)]

    if module.startswith("lightgbm"):
        values = model.predict(frame.loc[:, list(feature_names)])
        return [float(value) for value in values]

    if hasattr(model, "predict_proba"):
        values = model.predict_proba(frame.loc[:, list(feature_names)])[:, 1]
        return [float(value) for value in values]

    raise TypeError(f"Unsupported model type for native prediction: {type(model)!r}")


def _pmml_predict(pmml_text: str, frame: Any) -> List[float]:
    from pypmml import Model

    with tempfile.TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "model.pmml"
        path.write_text(pmml_text, encoding="utf-8")
        pmml_model = Model.load(str(path))
        predictions = []
        for idx in range(len(frame)):
            result = pmml_model.predict(_as_pmml_row(frame.iloc[idx]))
            predictions.append(float(result["score_p"]))
        return predictions


def _assert_close(
    model_key: str,
    native: Sequence[float],
    pmml: Sequence[float],
    tolerance: float,
) -> float:
    max_diff = 0.0
    for idx, (expected, got) in enumerate(zip(native, pmml)):
        diff = abs(float(expected) - float(got))
        max_diff = max(max_diff, diff)
        if not math.isclose(float(got), float(expected), rel_tol=0.0, abs_tol=tolerance):
            raise AssertionError(
                f"{model_key} row {idx} mismatch: "
                f"pmml={got:.16f}, native={expected:.16f}, diff={diff:.3e}, "
                f"tolerance={tolerance:.3e}"
            )
    return max_diff


def _model_tolerance(model_key: str, args: argparse.Namespace) -> float:
    return float(args.xgb_tolerance if model_key == "xgb" else args.lgb_tolerance)


def _run_one(
    model_key: str,
    model_path: Path,
    data_path: Path,
    rows: int,
    pmml_version: str,
    args: argparse.Namespace,
) -> Dict[str, Any]:
    from tree2code import convert

    model = _load_pickle(model_path)
    features = _feature_names(model)
    frame = _read_rows(data_path, features, rows)

    native = _native_predict(model, frame, features)
    pmml_text = convert(model, to="pmml", pmml_version=pmml_version)["pmml"]
    pmml = _pmml_predict(pmml_text, frame)

    tolerance = _model_tolerance(model_key, args)
    max_diff = _assert_close(model_key, native, pmml, tolerance)

    return {
        "model": model_key,
        "model_path": str(model_path),
        "rows_checked": len(frame),
        "features": len(features),
        "pmml_version": pmml_version,
        "max_abs_diff": max_diff,
        "abs_tolerance": tolerance,
        "status": "ok",
    }


def _parse_models(values: Iterable[str]) -> List[str]:
    selected: List[str] = []
    for value in values:
        for item in value.split(","):
            key = item.strip()
            if not key:
                continue
            if key == "all-models":
                keys = list(DEFAULT_MODELS)
            elif key in DEFAULT_MODELS:
                keys = [key]
            else:
                allowed = ", ".join([*DEFAULT_MODELS, "all-models"])
                raise ValueError(f"Unknown model '{key}'. Allowed values: {allowed}")
            for model_key in keys:
                if model_key not in selected:
                    selected.append(model_key)
    return selected


def run(args: argparse.Namespace) -> Dict[str, Any]:
    test_data_dir = Path(args.test_data_dir)
    data_path = Path(args.data) if args.data else test_data_dir / "all_data.pq"
    model_keys = _parse_models(args.model or ["all-models"])

    results = []
    for model_key in model_keys:
        model_path = test_data_dir / DEFAULT_MODELS[model_key]
        results.append(
            _run_one(
                model_key=model_key,
                model_path=model_path,
                data_path=data_path,
                rows=args.rows,
                pmml_version=args.pmml_version,
                args=args,
            )
        )

    return {
        "data_path": str(data_path),
        "results": results,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate generated PMML against real files in test_data."
    )
    parser.add_argument(
        "--test-data-dir",
        default=os.fspath(ROOT_DIR / "test_data"),
        help="Directory containing all_data.pq and model pickle files.",
    )
    parser.add_argument(
        "--data",
        default=None,
        help="Parquet data file. Defaults to <test-data-dir>/all_data.pq.",
    )
    parser.add_argument(
        "--model",
        action="append",
        default=None,
        help="Model key to check: xgb, lgb, all, or all-models. Can be repeated.",
    )
    parser.add_argument(
        "--rows",
        type=int,
        default=100,
        help="Number of leading rows to validate.",
    )
    parser.add_argument(
        "--pmml-version",
        default="4.4.1",
        help="PMML version to generate: 4.4.1, 4.3, or 4.2.1.",
    )
    parser.add_argument(
        "--xgb-tolerance",
        type=float,
        default=1e-6,
        help="Absolute tolerance for XGBoost probability checks.",
    )
    parser.add_argument(
        "--lgb-tolerance",
        type=float,
        default=1e-12,
        help="Absolute tolerance for LightGBM probability checks.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.rows <= 0:
        parser.error("--rows must be positive")

    try:
        result = run(args)
    except Exception as exc:
        print(f"PMML real-data validation failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
