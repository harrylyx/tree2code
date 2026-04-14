#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import pickle
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

import numpy as np
import pandas as pd
from pyspark.sql import DataFrame, SparkSession

from tree2code import convert
from tree2code.scoring import build_score_spec, probability_to_score


ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "test_data"
HOMEBREW_JAVA_HOME = Path("/opt/homebrew/opt/openjdk/libexec/openjdk.jdk/Contents/Home")
HOMEBREW_JAVA_BIN = Path("/opt/homebrew/opt/openjdk/bin")


@dataclass
class ScoreParams:
    base_score: float = 600.0
    pdo: float = 50.0
    base_odds: float = 20.0
    score_scale: int = 3


def _load_tree_diff_module():
    module_path = ROOT_DIR / "scripts" / "compare_sql_tree_values.py"
    spec = importlib.util.spec_from_file_location("compare_sql_tree_values", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _ensure_java_env() -> None:
    """Best-effort setup for Java runtime on macOS Homebrew installs."""
    if not os.environ.get("JAVA_HOME") and HOMEBREW_JAVA_HOME.exists():
        os.environ["JAVA_HOME"] = str(HOMEBREW_JAVA_HOME)

    current_path = os.environ.get("PATH", "")
    java_bin = str(HOMEBREW_JAVA_BIN)
    if HOMEBREW_JAVA_BIN.exists() and java_bin not in current_path.split(":"):
        os.environ["PATH"] = java_bin + ":" + current_path


def _feature_names_from_lgb_model(model: Any) -> List[str]:
    if hasattr(model, "feature_name"):
        names = list(model.feature_name())
        if names:
            return names
    if hasattr(model, "booster_"):
        return list(model.booster_.feature_name())
    if hasattr(model, "_Booster"):
        return list(model._Booster.feature_name())
    raise RuntimeError("Unable to infer LightGBM feature names")


def _native_predict_proba(model: Any, frame: pd.DataFrame) -> np.ndarray:
    if hasattr(model, "predict_proba"):
        return np.asarray(model.predict_proba(frame)[:, 1], dtype=float)
    return np.asarray(model.predict(frame), dtype=float)


def _probability_to_score_array(probability: np.ndarray, params: ScoreParams) -> np.ndarray:
    spec = build_score_spec(
        params.base_score,
        params.pdo,
        params.base_odds,
        params.score_scale,
    )
    assert spec is not None
    return np.asarray(
        [probability_to_score(float(p), spec) for p in probability],
        dtype=float,
    )


def _metrics(got: np.ndarray, expected: np.ndarray) -> Dict[str, Any]:
    diff = np.abs(got - expected)
    return {
        "max_abs": float(np.max(diff)),
        "p99_abs": float(np.percentile(diff, 99)),
        "mean_abs": float(np.mean(diff)),
        "count_ge_1e_4": int(np.sum(diff >= 1e-4)),
        "count_ge_1e_6": int(np.sum(diff >= 1e-6)),
    }


def _score_scale_mismatch(got: np.ndarray, expected: np.ndarray, scale: int) -> int:
    fmt = f".{{scale}}f".format(scale=scale)
    mismatches = 0
    for g, e in zip(got, expected):
        if format(float(g), fmt) != format(float(e), fmt):
            mismatches += 1
    return mismatches


def _normalize_query_result(
    result_pdf: pd.DataFrame,
    params: ScoreParams,
) -> pd.DataFrame:
    cols = {c.lower(): c for c in result_pdf.columns}
    if "idx" not in cols:
        raise RuntimeError("SQL result must contain idx")

    idx_col = cols["idx"]
    if "score_p" in cols:
        score_p_col = cols["score_p"]
        prob = result_pdf[score_p_col].astype(float).to_numpy()
        if "score" in cols:
            score = result_pdf[cols["score"]].astype(float).to_numpy()
        else:
            score = _probability_to_score_array(prob, params)
    elif "score" in cols:
        # treemodel2sql output usually names probability as score
        prob = result_pdf[cols["score"]].astype(float).to_numpy()
        score = _probability_to_score_array(prob, params)
    else:
        raise RuntimeError("SQL result must contain score_p or score")

    return pd.DataFrame(
        {
            "idx": result_pdf[idx_col].to_numpy(),
            "score_p": prob,
            "score": score,
        }
    )


def _run_spark_sql(
    spark: SparkSession,
    sql_text: str,
    source_pdf: pd.DataFrame,
    params: ScoreParams,
) -> pd.DataFrame:
    spark_df = spark.createDataFrame(source_pdf)
    spark_df.createOrReplaceTempView("input_table")
    result_df: DataFrame = spark.sql(sql_text)
    result_pdf = result_df.toPandas()
    return _normalize_query_result(result_pdf, params)


def _align_by_idx(order_idx: Sequence[Any], result_pdf: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
    by_idx = {
        row["idx"]: (float(row["score_p"]), float(row["score"]))
        for _, row in result_pdf.iterrows()
    }
    prob = np.asarray([by_idx[idx][0] for idx in order_idx], dtype=float)
    score = np.asarray([by_idx[idx][1] for idx in order_idx], dtype=float)
    return prob, score


def _tree_threshold_mismatch_summary(
    tree2code_sql: str,
    treemodel2sql_sql: str,
) -> Dict[str, Any]:
    mod = _load_tree_diff_module()
    trees_a, _ = mod._extract_trees(tree2code_sql, "auto")
    trees_b, _ = mod._extract_trees(treemodel2sql_sql, "auto")
    common = sorted(set(trees_a.keys()) & set(trees_b.keys()))

    mismatch_indices: List[int] = []
    mismatch_count = 0
    for idx in common:
        compared = mod._compare_tree_values(
            trees_a[idx],
            trees_b[idx],
            max_values=20,
            close_tolerance=1e-12,
        )
        cnt = int(compared.get("threshold_mismatch_count", 0))
        if cnt > 0:
            mismatch_indices.append(idx)
            mismatch_count += cnt

    return {
        "tree_count_common": len(common),
        "threshold_mismatch_tree_indices": mismatch_indices,
        "threshold_mismatch_tree_count": len(mismatch_indices),
        "threshold_mismatch_total_count": mismatch_count,
    }


def _build_markdown_report(
    *,
    raw_rows: int,
    dedup_rows: int,
    params: ScoreParams,
    tree2code_prob_metrics: Dict[str, Any],
    tree2code_score_metrics: Dict[str, Any],
    tree2code_score_mismatch: int,
    tms_prob_metrics: Dict[str, Any],
    tms_score_metrics: Dict[str, Any],
    tms_score_mismatch: int,
    tms_worse_rows: int,
    tree2code_worse_rows: int,
    equal_rows: int,
    threshold_summary: Dict[str, Any],
) -> str:
    if tms_prob_metrics["max_abs"] > tree2code_prob_metrics["max_abs"]:
        worse_by_prob = "treemodel2sql"
    elif tms_prob_metrics["max_abs"] < tree2code_prob_metrics["max_abs"]:
        worse_by_prob = "tree2code"
    else:
        worse_by_prob = "tie"

    if tms_score_mismatch > tree2code_score_mismatch:
        worse_by_score = "treemodel2sql"
    elif tms_score_mismatch < tree2code_score_mismatch:
        worse_by_score = "tree2code"
    else:
        worse_by_score = "tie"

    lines: List[str] = [
        "# PySpark Parity Report",
        "",
        f"- generated_at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "- data_source: `test_data/all_data.pq`",
        "- dedupe_key: `idx` (keep first)",
        f"- raw_rows: {raw_rows}",
        f"- dedup_rows: {dedup_rows}",
        "- gold_standard: native LightGBM prediction",
        "- spark_mode: `local[*]`",
        (
            "- score_params: "
            f"base_score={params.base_score}, pdo={params.pdo}, "
            f"base_odds={params.base_odds}, scale={params.score_scale}"
        ),
        "",
        "## tree2code SQL vs Native (`score_p`)",
        f"- max_abs: {tree2code_prob_metrics['max_abs']:.16g}",
        f"- p99_abs: {tree2code_prob_metrics['p99_abs']:.16g}",
        f"- mean_abs: {tree2code_prob_metrics['mean_abs']:.16g}",
        f"- count_ge_1e_4: {tree2code_prob_metrics['count_ge_1e_4']}",
        "",
        "## tree2code SQL vs Native (`score`)",
        f"- max_abs: {tree2code_score_metrics['max_abs']:.16g}",
        f"- p99_abs: {tree2code_score_metrics['p99_abs']:.16g}",
        f"- mean_abs: {tree2code_score_metrics['mean_abs']:.16g}",
        f"- score_scale_mismatch: {tree2code_score_mismatch}",
        "",
        "## treemodel2sql SQL vs Native (`score_p`)",
        f"- max_abs: {tms_prob_metrics['max_abs']:.16g}",
        f"- p99_abs: {tms_prob_metrics['p99_abs']:.16g}",
        f"- mean_abs: {tms_prob_metrics['mean_abs']:.16g}",
        f"- count_ge_1e_4: {tms_prob_metrics['count_ge_1e_4']}",
        "",
        "## treemodel2sql SQL vs Native (`score`)",
        f"- max_abs: {tms_score_metrics['max_abs']:.16g}",
        f"- p99_abs: {tms_score_metrics['p99_abs']:.16g}",
        f"- mean_abs: {tms_score_metrics['mean_abs']:.16g}",
        f"- score_scale_mismatch: {tms_score_mismatch}",
        "",
        "## SQL Pair Comparison",
        f"- rows_treemodel2sql_worse_than_tree2code: {tms_worse_rows}",
        f"- rows_tree2code_worse_than_treemodel2sql: {tree2code_worse_rows}",
        f"- rows_equal_error: {equal_rows}",
        "",
        "## Threshold Mismatch (0 vs 1e-13)",
        f"- common_trees: {threshold_summary['tree_count_common']}",
        f"- mismatch_tree_count: {threshold_summary['threshold_mismatch_tree_count']}",
        f"- mismatch_total_count: {threshold_summary['threshold_mismatch_total_count']}",
    ]

    indices = threshold_summary["threshold_mismatch_tree_indices"]
    if indices:
        lines.append("- mismatch_tree_indices: " + ", ".join(str(v) for v in indices))
    else:
        lines.append("- mismatch_tree_indices: (empty)")

    lines.extend(
        [
            "",
            "## Conclusion",
            f"- worse_sql_by_score_p_max_abs: {worse_by_prob}",
            f"- worse_sql_by_score_scale_mismatch: {worse_by_score}",
        ]
    )
    return "\n".join(lines) + "\n"


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run PySpark parity comparison for LGB SQL vs native model."
    )
    parser.add_argument(
        "--data-path",
        default=str(DATA_DIR / "all_data.pq"),
        help="Input parquet path.",
    )
    parser.add_argument(
        "--model-path",
        default=str(DATA_DIR / "lgb_model.pkl"),
        help="Pickled LightGBM model path.",
    )
    parser.add_argument(
        "--output-md",
        default=str(ROOT_DIR / "docs" / "pyspark_parity_report.md"),
        help="Markdown output path.",
    )
    parser.add_argument(
        "--output-json",
        default=str(ROOT_DIR / "docs" / "pyspark_parity_report.json"),
        help="JSON output path.",
    )
    args = parser.parse_args()

    params = ScoreParams()
    _ensure_java_env()
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

    data = pd.read_parquet(args.data_path)
    raw_rows = int(len(data))
    dedup = data.drop_duplicates(subset=["idx"], keep="first").reset_index(drop=True)
    dedup_rows = int(len(dedup))

    model = pickle.load(open(args.model_path, "rb"))
    feature_names = _feature_names_from_lgb_model(model)
    frame = dedup[feature_names].copy()
    order_idx = dedup["idx"].tolist()

    native_prob = _native_predict_proba(model, frame)
    native_score = _probability_to_score_array(native_prob, params)

    tree2code_sql = convert(
        model,
        to="sql",
        dialect="hive",
        sql_mode="select",
        keep_columns=["idx"],
        table_name="input_table",
        base_score=params.base_score,
        pdo=params.pdo,
        base_odds=params.base_odds,
        score_scale=params.score_scale,
    )["sql"]["select_sql"]

    from treemodel2sql import Lgb2Sql

    treemodel2sql_sql = Lgb2Sql().transform(
        model,
        keep_columns=["idx"],
        table_name="input_table",
        sql_is_format=True,
    )

    source_pdf = dedup[["idx"] + feature_names].copy()

    spark = (
        SparkSession.builder.master("local[*]")
        .appName("tree2code-pyspark-parity")
        .config("spark.sql.session.timeZone", "UTC")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .config("spark.driver.host", "127.0.0.1")
        .enableHiveSupport()
        .getOrCreate()
    )

    try:
        tree2code_result = _run_spark_sql(spark, tree2code_sql, source_pdf, params)
        treemodel2sql_result = _run_spark_sql(
            spark, treemodel2sql_sql, source_pdf, params
        )
    finally:
        spark.stop()

    tree2code_prob, tree2code_score = _align_by_idx(order_idx, tree2code_result)
    treemodel2sql_prob, treemodel2sql_score = _align_by_idx(order_idx, treemodel2sql_result)

    tree2code_prob_metrics = _metrics(tree2code_prob, native_prob)
    tree2code_score_metrics = _metrics(tree2code_score, native_score)
    tree2code_score_mismatch = _score_scale_mismatch(
        tree2code_score, native_score, params.score_scale
    )

    tms_prob_metrics = _metrics(treemodel2sql_prob, native_prob)
    tms_score_metrics = _metrics(treemodel2sql_score, native_score)
    tms_score_mismatch = _score_scale_mismatch(
        treemodel2sql_score, native_score, params.score_scale
    )

    err_tree2code = np.abs(tree2code_prob - native_prob)
    err_tms = np.abs(treemodel2sql_prob - native_prob)
    tms_worse_rows = int(np.sum(err_tms > err_tree2code))
    tree2code_worse_rows = int(np.sum(err_tree2code > err_tms))
    equal_rows = int(len(err_tms) - tms_worse_rows - tree2code_worse_rows)

    threshold_summary = _tree_threshold_mismatch_summary(
        tree2code_sql=tree2code_sql,
        treemodel2sql_sql=treemodel2sql_sql,
    )

    report_md = _build_markdown_report(
        raw_rows=raw_rows,
        dedup_rows=dedup_rows,
        params=params,
        tree2code_prob_metrics=tree2code_prob_metrics,
        tree2code_score_metrics=tree2code_score_metrics,
        tree2code_score_mismatch=tree2code_score_mismatch,
        tms_prob_metrics=tms_prob_metrics,
        tms_score_metrics=tms_score_metrics,
        tms_score_mismatch=tms_score_mismatch,
        tms_worse_rows=tms_worse_rows,
        tree2code_worse_rows=tree2code_worse_rows,
        equal_rows=equal_rows,
        threshold_summary=threshold_summary,
    )

    output_md = Path(args.output_md)
    output_json = Path(args.output_json)
    _write_text(output_md, report_md)

    report_json = {
        "data_path": str(args.data_path),
        "model_path": str(args.model_path),
        "raw_rows": raw_rows,
        "dedup_rows": dedup_rows,
        "score_params": {
            "base_score": params.base_score,
            "pdo": params.pdo,
            "base_odds": params.base_odds,
            "score_scale": params.score_scale,
        },
        "tree2code": {
            "score_p": tree2code_prob_metrics,
            "score": tree2code_score_metrics,
            "score_scale_mismatch": tree2code_score_mismatch,
        },
        "treemodel2sql": {
            "score_p": tms_prob_metrics,
            "score": tms_score_metrics,
            "score_scale_mismatch": tms_score_mismatch,
        },
        "row_error_compare": {
            "treemodel2sql_worse_rows": tms_worse_rows,
            "tree2code_worse_rows": tree2code_worse_rows,
            "equal_rows": equal_rows,
        },
        "threshold_summary": threshold_summary,
    }
    _write_text(output_json, json.dumps(report_json, ensure_ascii=False, indent=2))

    print(
        json.dumps(
            {
                "status": "ok",
                "output_md": str(output_md),
                "output_json": str(output_json),
                "threshold_mismatch_trees": threshold_summary[
                    "threshold_mismatch_tree_count"
                ],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
