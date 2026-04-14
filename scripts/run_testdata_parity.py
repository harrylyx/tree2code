#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
import pickle
import struct
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
import psycopg
import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from tree2code import convert
from tree2code.scoring import build_score_spec, probability_to_score


ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "test_data"


@dataclass
class ScoreParams:
    base_score: float = 600.0
    pdo: float = 50.0
    base_odds: float = 20.0
    score_scale: int = 3


def _load_dotenv(dotenv_path: Path) -> None:
    """Load simple KEY=VALUE pairs from .env if env vars are missing."""
    if not dotenv_path.exists():
        return

    for line in dotenv_path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if not text or text.startswith("#") or "=" not in text:
            continue
        key, value = text.split("=", 1)
        key = key.strip()
        value = value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


def _pg_dsn() -> str:
    """Build PostgreSQL DSN from env vars."""
    host = os.getenv("TREE2CODE_PGHOST")
    port = os.getenv("TREE2CODE_PGPORT")
    user = os.getenv("TREE2CODE_PGUSER")
    password = os.getenv("TREE2CODE_PGPASSWORD")
    database = os.getenv("TREE2CODE_PGDATABASE")

    missing: List[str] = []
    if not host:
        missing.append("TREE2CODE_PGHOST")
    if not port:
        missing.append("TREE2CODE_PGPORT")
    if not user:
        missing.append("TREE2CODE_PGUSER")
    if password is None:
        missing.append("TREE2CODE_PGPASSWORD")
    if not database:
        missing.append("TREE2CODE_PGDATABASE")

    if missing:
        raise RuntimeError("Missing PostgreSQL env vars: " + ", ".join(missing))

    return (
        f"host={host} port={port} user={user} "
        f"password={password} dbname={database}"
    )


def _feature_names_from_model(model: Any, backend: str) -> List[str]:
    """Extract feature names from model object."""
    if backend == "xgb":
        if hasattr(model, "feature_names") and model.feature_names:
            return list(model.feature_names)
        booster = model.get_booster() if hasattr(model, "get_booster") else model
        return list(getattr(booster, "feature_names", []) or [])

    if hasattr(model, "feature_name"):
        names = list(model.feature_name())
        if names:
            return names
    if hasattr(model, "booster_"):
        return list(model.booster_.feature_name())
    if hasattr(model, "_Booster"):
        return list(model._Booster.feature_name())

    raise RuntimeError(f"Unable to infer feature names for backend={backend}")


def _native_predict_proba(model: Any, backend: str, frame: pd.DataFrame) -> np.ndarray:
    """Run native model probability prediction."""
    if backend == "xgb":
        if hasattr(model, "predict_proba"):
            return np.asarray(model.predict_proba(frame)[:, 1], dtype=float)

        dmat = xgb.DMatrix(frame, feature_names=list(frame.columns))
        return np.asarray(model.predict(dmat), dtype=float)

    if hasattr(model, "predict_proba"):
        return np.asarray(model.predict_proba(frame)[:, 1], dtype=float)

    return np.asarray(model.predict(frame), dtype=float)


def _predict_python(code: str, frame: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
    """Run generated Python scorer and return score_p and score arrays."""
    namespace: Dict[str, Any] = {}
    exec(code, namespace)
    predict_row = namespace["predict_row"]

    columns = list(frame.columns)
    prob: List[float] = []
    score: List[float] = []

    for values in frame.itertuples(index=False, name=None):
        row = dict(zip(columns, values))
        result = predict_row(row)
        prob.append(float(result["score_p"]))
        score.append(float(result["score"]))

    return np.asarray(prob, dtype=float), np.asarray(score, dtype=float)


def _sql_type_for_series(series: pd.Series) -> str:
    """Map pandas dtype to PostgreSQL column type."""
    dtype_text = str(series.dtype)
    if dtype_text == "bool":
        return "boolean"
    if dtype_text in {"object", "string", "str", "category", "datetime64[us]"}:
        return "text"
    return "double precision"


def _sql_value(value: Any) -> Any:
    """Normalize python value for SQL insertion."""
    if value is None:
        return None

    try:
        if pd.isna(value):
            return None
    except Exception:
        pass

    if isinstance(value, bool):
        return bool(value)

    if hasattr(value, "item"):
        try:
            value = value.item()
        except Exception:
            pass

    if isinstance(value, (int, float)):
        return float(value)

    return str(value)


def _prepare_table(
    conn: psycopg.Connection,
    table_name: str,
    frame: pd.DataFrame,
    *,
    batch_size: int = 1000,
) -> None:
    """Create table and insert frame rows into PostgreSQL."""
    columns = list(frame.columns)

    with conn.cursor() as cur:
        cur.execute(f"drop table if exists {table_name}")
        col_defs = [
            f'"{name}" {_sql_type_for_series(frame[name])}'
            for name in columns
        ]
        cur.execute(
            f"create table {table_name} (rid bigint primary key, {', '.join(col_defs)})"
        )

        placeholders = ",".join(["%s"] * (len(columns) + 1))
        quoted_cols = ", ".join(["rid"] + [f'"{c}"' for c in columns])

        total = len(frame)
        for start in range(0, total, batch_size):
            stop = min(start + batch_size, total)
            part = frame.iloc[start:stop]

            rows = []
            for local_idx, values in enumerate(part.itertuples(index=False, name=None)):
                rid = start + local_idx
                rows.append((rid, *[_sql_value(v) for v in values]))

            cur.executemany(
                f"insert into {table_name} ({quoted_cols}) values ({placeholders})",
                rows,
            )

    conn.commit()


def _predict_sql(
    dsn: str,
    backend: str,
    frame: pd.DataFrame,
    model: Any,
    score_params: ScoreParams,
) -> Tuple[np.ndarray, np.ndarray]:
    """Run generated SQL scorer in PostgreSQL."""
    table_name = f"tmp_tree2code_{backend}_{int(time.time())}"

    sql_out = convert(
        model,
        to="sql",
        dialect="psql",
        sql_mode="select",
        keep_columns=["rid"],
        table_name=table_name,
        base_score=score_params.base_score,
        pdo=score_params.pdo,
        base_odds=score_params.base_odds,
        score_scale=score_params.score_scale,
    )
    query = sql_out["sql"]["select_sql"]

    with psycopg.connect(dsn) as conn:
        _prepare_table(conn, table_name, frame)
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()

        with conn.cursor() as cur:
            cur.execute(f"drop table if exists {table_name}")
        conn.commit()

    by_id = {int(row[0]): row for row in rows}
    prob = np.asarray([float(by_id[idx][1]) for idx in range(len(frame))], dtype=float)
    score = np.asarray([float(by_id[idx][2]) for idx in range(len(frame))], dtype=float)
    return prob, score


def _probability_to_score_array(probability: np.ndarray, params: ScoreParams) -> np.ndarray:
    """Convert probability array into score array."""
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


def _f32(value: float) -> float:
    """Cast float to float32 precision."""
    return struct.unpack("!f", struct.pack("!f", float(value)))[0]


def _metrics(got: np.ndarray, expected: np.ndarray) -> Dict[str, Any]:
    """Build absolute-difference metrics."""
    diff = np.abs(got - expected)
    return {
        "max_abs": float(np.max(diff)),
        "p99_abs": float(np.percentile(diff, 99)),
        "mean_abs": float(np.mean(diff)),
        "count_ge_1e_4": int(np.sum(diff >= 1e-4)),
        "count_ge_1e_6": int(np.sum(diff >= 1e-6)),
    }


def _score_scale_mismatch(
    got: np.ndarray,
    expected: np.ndarray,
    scale: int,
) -> int:
    """Count rows whose rounded score text differs at target scale."""
    fmt = f".{{scale}}f".format(scale=scale)
    mismatches = 0
    for g, e in zip(got, expected):
        if format(float(g), fmt) != format(float(e), fmt):
            mismatches += 1
    return mismatches


def _run_backend_parity(
    *,
    backend: str,
    model: Any,
    data: pd.DataFrame,
    dsn: str,
    score_params: ScoreParams,
) -> Dict[str, Any]:
    """Run native vs generated Python/SQL parity for one backend."""
    features = _feature_names_from_model(model, backend)
    frame = data[features].copy()

    native_prob = _native_predict_proba(model, backend, frame)
    score_input_prob = native_prob
    if backend == "xgb":
        score_input_prob = np.asarray([_f32(v) for v in native_prob], dtype=float)
    native_score = _probability_to_score_array(score_input_prob, score_params)

    py_out = convert(
        model,
        to="python",
        base_score=score_params.base_score,
        pdo=score_params.pdo,
        base_odds=score_params.base_odds,
        score_scale=score_params.score_scale,
    )
    py_prob, py_score = _predict_python(py_out["python"], frame)

    sql_prob, sql_score = _predict_sql(dsn, backend, frame, model, score_params)

    py_prob_metrics = _metrics(py_prob, native_prob)
    py_score_metrics = _metrics(py_score, native_score)
    sql_prob_metrics = _metrics(sql_prob, native_prob)
    sql_score_metrics = _metrics(sql_score, native_score)

    py_score_scale_mismatch = _score_scale_mismatch(
        py_score,
        native_score,
        score_params.score_scale,
    )
    sql_score_scale_mismatch = _score_scale_mismatch(
        sql_score,
        native_score,
        score_params.score_scale,
    )

    return {
        "backend": backend,
        "rows": int(len(frame)),
        "features": int(len(features)),
        "python": {
            "score_p": py_prob_metrics,
            "score": py_score_metrics,
            "score_scale_mismatch": py_score_scale_mismatch,
        },
        "sql": {
            "score_p": sql_prob_metrics,
            "score": sql_score_metrics,
            "score_scale_mismatch": sql_score_scale_mismatch,
        },
    }


def _normalize_sql(sql: str) -> str:
    """Normalize SQL string for coarse comparison."""
    return " ".join(sql.lower().split())


def _run_treemodel2sql_comparison(xgb_model: Any, lgb_model: Any) -> Dict[str, Any]:
    """Build side-by-side SQL comparison summary."""
    summary: Dict[str, Any] = {"available": False}

    try:
        from treemodel2sql import Lgb2Sql, XGBoost2Sql
    except Exception as exc:
        summary["error"] = str(exc)
        return summary

    summary["available"] = True

    xgb_tree2code = convert(
        xgb_model,
        to="sql",
        dialect="psql",
        sql_mode="select",
        keep_columns=["rid"],
        table_name="input_table",
    )["sql"]["select_sql"]
    lgb_tree2code = convert(
        lgb_model,
        to="sql",
        dialect="psql",
        sql_mode="select",
        keep_columns=["rid"],
        table_name="input_table",
    )["sql"]["select_sql"]

    xgb_tms = XGBoost2Sql().transform(
        xgb_model,
        keep_columns=["rid"],
        table_name="input_table",
        sql_is_format=True,
    )
    lgb_tms = Lgb2Sql().transform(
        lgb_model,
        keep_columns=["rid"],
        table_name="input_table",
        sql_is_format=True,
    )

    summary["xgb"] = {
        "tree2code_len": len(xgb_tree2code),
        "treemodel2sql_len": len(xgb_tms),
        "normalized_equal": _normalize_sql(xgb_tree2code) == _normalize_sql(xgb_tms),
        "treemodel2sql_has_and_is_null_pattern": " and " in xgb_tms.lower()
        and " is null" in xgb_tms.lower(),
    }
    summary["lgb"] = {
        "tree2code_len": len(lgb_tree2code),
        "treemodel2sql_len": len(lgb_tms),
        "normalized_equal": _normalize_sql(lgb_tree2code) == _normalize_sql(lgb_tms),
        "treemodel2sql_has_and_is_null_pattern": " and " in lgb_tms.lower()
        and " is null" in lgb_tms.lower(),
    }

    return summary


def _run_lgb_stress_check(dsn: str, score_params: ScoreParams) -> Dict[str, Any]:
    """Run stress check for LGBM n_estimators=500, num_leaves=16."""
    import lightgbm as lgb

    x, y = make_classification(
        n_samples=12000,
        n_features=30,
        n_informative=12,
        n_redundant=8,
        random_state=20260414,
    )
    frame = pd.DataFrame(x, columns=[f"f{i}" for i in range(x.shape[1])])

    rng = np.random.default_rng(20260414)
    missing_mask = rng.random(frame.shape) < 0.03
    frame = frame.mask(missing_mask)

    x_train, x_test, y_train, y_test = train_test_split(
        frame,
        y,
        test_size=0.25,
        random_state=20260414,
    )

    model = lgb.LGBMClassifier(
        n_estimators=500,
        num_leaves=16,
        learning_rate=0.05,
        random_state=20260414,
    )
    model.fit(x_train, y_train)

    report = _run_backend_parity(
        backend="lgb",
        model=model,
        data=x_test.reset_index(drop=True),
        dsn=dsn,
        score_params=score_params,
    )

    report["config"] = {
        "n_estimators": 500,
        "num_leaves": 16,
        "rows": int(len(x_test)),
    }
    return report


def _render_metrics_block(metrics: Dict[str, Any]) -> List[str]:
    """Render metric dict into markdown bullet lines."""
    lines = [
        f"- max_abs: {metrics['max_abs']:.16g}",
        f"- p99_abs: {metrics['p99_abs']:.16g}",
        f"- mean_abs: {metrics['mean_abs']:.16g}",
        f"- count_ge_1e_4: {metrics['count_ge_1e_4']}",
        f"- count_ge_1e_6: {metrics['count_ge_1e_6']}",
    ]
    return lines


def _render_backend_section(report: Dict[str, Any]) -> List[str]:
    """Render one backend report block."""
    lines: List[str] = []
    lines.append(f"## {report['backend'].upper()} Parity")
    lines.append(f"- rows: {report['rows']}")
    lines.append(f"- features: {report['features']}")
    lines.append("")

    lines.append("### Python vs Native (`score_p`)")
    lines.extend(_render_metrics_block(report["python"]["score_p"]))
    lines.append("")

    lines.append("### Python vs Native (`score`)")
    lines.extend(_render_metrics_block(report["python"]["score"]))
    lines.append(
        f"- score_scale_mismatch: {report['python']['score_scale_mismatch']}"
    )
    lines.append("")

    lines.append("### SQL vs Native (`score_p`)")
    lines.extend(_render_metrics_block(report["sql"]["score_p"]))
    lines.append("")

    lines.append("### SQL vs Native (`score`)")
    lines.extend(_render_metrics_block(report["sql"]["score"]))
    lines.append(f"- score_scale_mismatch: {report['sql']['score_scale_mismatch']}")
    lines.append("")

    return lines


def _render_treemodel2sql_section(summary: Dict[str, Any]) -> List[str]:
    """Render tree2code vs treemodel2sql comparison section."""
    lines: List[str] = ["## tree2code vs treemodel2sql SQL Comparison"]

    if not summary.get("available"):
        lines.append("- treemodel2sql not available in this environment")
        if "error" in summary:
            lines.append(f"- error: {summary['error']}")
        lines.append("")
        return lines

    lines.append("| backend | tree2code_len | treemodel2sql_len | normalized_equal | has_and_is_null_pattern |")
    lines.append("|---|---:|---:|---|---|")
    for backend in ["xgb", "lgb"]:
        row = summary[backend]
        lines.append(
            f"| {backend} | {row['tree2code_len']} | {row['treemodel2sql_len']} | "
            f"{row['normalized_equal']} | {row['treemodel2sql_has_and_is_null_pattern']} |"
        )

    lines.append("")
    lines.append(
        "- `normalized_equal` compares SQL strings after lowercasing and whitespace normalization only."
    )
    lines.append("")

    return lines


def _render_stress_section(stress: Dict[str, Any]) -> List[str]:
    """Render LGB stress-check section."""
    lines: List[str] = ["## LGB Stress Check (500 Trees, 16 Leaves)"]
    cfg = stress["config"]
    lines.append(f"- n_estimators: {cfg['n_estimators']}")
    lines.append(f"- num_leaves: {cfg['num_leaves']}")
    lines.append(f"- rows: {cfg['rows']}")
    lines.append("")

    lines.append("### SQL vs Native (`score_p`)")
    lines.extend(_render_metrics_block(stress["sql"]["score_p"]))
    lines.append("")

    lines.append("### SQL vs Native (`score`)")
    lines.extend(_render_metrics_block(stress["sql"]["score"]))
    lines.append(f"- score_scale_mismatch: {stress['sql']['score_scale_mismatch']}")
    lines.append("")

    lines.append("### Python vs Native (`score_p`)")
    lines.extend(_render_metrics_block(stress["python"]["score_p"]))
    lines.append("")

    return lines


def _build_report_markdown(
    *,
    raw_rows: int,
    dedup_rows: int,
    xgb_report: Dict[str, Any],
    lgb_report: Dict[str, Any],
    stress_report: Dict[str, Any],
    sql_cmp_summary: Dict[str, Any],
) -> str:
    """Build final markdown report body."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: List[str] = [
        "# testdata Parity Report",
        "",
        f"- generated_at: {now}",
        "- data_source: `test_data/all_data.pq`",
        "- dedupe_key: `idx` (keep first)",
        f"- raw_rows: {raw_rows}",
        f"- dedup_rows: {dedup_rows}",
        "- acceptance_score_p: no row with abs error >= 1e-4",
        "- acceptance_score: exact match at configured score scale",
        "",
    ]

    lines.extend(_render_backend_section(xgb_report))
    lines.extend(_render_backend_section(lgb_report))
    lines.extend(_render_stress_section(stress_report))
    lines.extend(_render_treemodel2sql_section(sql_cmp_summary))

    lines.append("## Acceptance Summary")

    def _ok_prob(section: Dict[str, Any]) -> bool:
        return section["python"]["score_p"]["count_ge_1e_4"] == 0 and section["sql"]["score_p"][
            "count_ge_1e_4"
        ] == 0

    def _ok_score(section: Dict[str, Any]) -> bool:
        return (
            section["python"]["score_scale_mismatch"] == 0
            and section["sql"]["score_scale_mismatch"] == 0
        )

    lines.append(f"- XGB score_p criterion: {_ok_prob(xgb_report)}")
    lines.append(f"- XGB score criterion: {_ok_score(xgb_report)}")
    lines.append(f"- LGB score_p criterion: {_ok_prob(lgb_report)}")
    lines.append(f"- LGB score criterion: {_ok_score(lgb_report)}")
    lines.append(
        "- LGB stress score_p criterion: "
        f"{stress_report['python']['score_p']['count_ge_1e_4'] == 0 and stress_report['sql']['score_p']['count_ge_1e_4'] == 0}"
    )
    lines.append(
        "- LGB stress score criterion: "
        f"{stress_report['python']['score_scale_mismatch'] == 0 and stress_report['sql']['score_scale_mismatch'] == 0}"
    )
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="docs/testdata_parity_report.md",
        help="Path to save markdown report",
    )
    args = parser.parse_args()

    _load_dotenv(ROOT_DIR / ".env")
    dsn = _pg_dsn()

    score_params = ScoreParams()

    t0 = time.time()
    data = pd.read_parquet(DATA_DIR / "all_data.pq")
    raw_rows = int(len(data))
    dedup = data.drop_duplicates(subset=["idx"], keep="first").reset_index(drop=True)
    dedup_rows = int(len(dedup))

    xgb_model = pickle.load(open(DATA_DIR / "xgb_model.pkl", "rb"))
    lgb_model = pickle.load(open(DATA_DIR / "lgb_model.pkl", "rb"))

    xgb_report = _run_backend_parity(
        backend="xgb",
        model=xgb_model,
        data=dedup,
        dsn=dsn,
        score_params=score_params,
    )
    lgb_report = _run_backend_parity(
        backend="lgb",
        model=lgb_model,
        data=dedup,
        dsn=dsn,
        score_params=score_params,
    )

    stress_report = _run_lgb_stress_check(dsn, score_params)
    sql_cmp_summary = _run_treemodel2sql_comparison(xgb_model, lgb_model)

    report_markdown = _build_report_markdown(
        raw_rows=raw_rows,
        dedup_rows=dedup_rows,
        xgb_report=xgb_report,
        lgb_report=lgb_report,
        stress_report=stress_report,
        sql_cmp_summary=sql_cmp_summary,
    )

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT_DIR / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_markdown, encoding="utf-8")

    total_seconds = round(time.time() - t0, 2)
    print(json.dumps({"status": "ok", "output": str(output_path), "seconds": total_seconds}))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
