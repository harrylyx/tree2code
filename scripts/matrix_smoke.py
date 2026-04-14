#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from typing import Dict


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


def _build_data(seed: int = 2026):
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    import pandas as pd

    x, y = make_classification(
        n_samples=240,
        n_features=8,
        n_informative=4,
        n_redundant=2,
        random_state=seed,
    )
    frame = pd.DataFrame(x, columns=[f"f{i}" for i in range(x.shape[1])])
    return train_test_split(frame, y, test_size=0.3, random_state=seed)


def _assert_close(name: str, got: float, expected: float, tol: float) -> None:
    if not math.isclose(got, expected, rel_tol=0.0, abs_tol=tol):
        raise AssertionError(
            f"{name} mismatch: got={got:.16f}, expected={expected:.16f}, abs_tol={tol}"
        )


def run_backend(backend: str) -> Dict[str, object]:
    from tree2code import convert

    x_train, x_test, y_train, y_test = _build_data()

    if backend == "xgboost":
        import xgboost as xgb

        model = xgb.XGBClassifier(
            n_estimators=4,
            max_depth=3,
            learning_rate=0.12,
            random_state=2026,
            eval_metric="logloss",
        )
        model.fit(x_train, y_train)
        reference = model.predict_proba(x_test)[:, 1]
        abs_tol = 1e-7
    elif backend == "lightgbm":
        import lightgbm as lgb

        model = lgb.LGBMClassifier(
            n_estimators=4,
            max_depth=3,
            learning_rate=0.12,
            random_state=2026,
        )
        model.fit(x_train, y_train)
        reference = model.predict_proba(x_test)[:, 1]
        abs_tol = 1e-12
    else:
        raise ValueError("backend must be xgboost or lightgbm")

    py_out = convert(
        model,
        to="python",
        base_score=600,
        pdo=50,
        base_odds=20,
        score_scale=3,
        abnormal_rule="all_null",
        abnormal_value=-2,
    )
    namespace: Dict[str, object] = {}
    exec(py_out["python"], namespace)
    predict_row = namespace["predict_row"]

    for idx in range(min(80, len(x_test))):
        row = x_test.iloc[idx].to_dict()
        got = float(predict_row(row)["score_p"])
        _assert_close(f"python_prob[{idx}]", got, float(reference[idx]), abs_tol)

    abnormal_row = {name: None for name in py_out["meta"]["feature_names"]}
    abnormal_res = predict_row(abnormal_row)
    if abnormal_res["score_p"] != -2 or abnormal_res["score"] != -2:
        raise AssertionError("abnormal override failed")

    sql_out = convert(
        model,
        to="sql",
        dialect="psql",
        sql_mode="expression",
        base_score=600,
        pdo=50,
        base_odds=20,
    )
    hive_out = convert(
        model,
        to="sql",
        dialect="hive",
        sql_mode="expression",
        base_score=600,
        pdo=50,
        base_odds=20,
    )

    if "exp(" not in sql_out["sql"]["score_p_expr"].lower():
        raise AssertionError("missing exp in psql score expression")
    if "ln(" not in sql_out["sql"]["score_expr"].lower():
        raise AssertionError("missing ln in psql score expression")
    if "::" in hive_out["sql"]["score_p_expr"]:
        raise AssertionError("hive expression contains postgres cast")

    return {
        "backend": backend,
        "rows_checked": min(80, len(x_test)),
        "abs_tol": abs_tol,
        "status": "ok",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=["xgboost", "lightgbm"], required=True)
    args = parser.parse_args()

    result = run_backend(args.backend)
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
