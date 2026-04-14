import math
import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from tree2code import convert


def _psycopg():
    return pytest.importorskip("psycopg")


def _load_dotenv_if_present() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        if not key:
            continue

        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]

        os.environ.setdefault(key, value)


def _is_numeric_series(series: pd.Series) -> bool:
    return pd.api.types.is_numeric_dtype(series.dtype)


def _column_sql_type(series: pd.Series) -> str:
    if _is_numeric_series(series):
        return "double precision"
    return "text"


def _normalize_cell(value, *, numeric: bool):
    if pd.isna(value):
        return None
    if numeric:
        return float(value)
    return str(value)


def _prepare_table(conn, table_name, frame: pd.DataFrame):
    frame = frame.reset_index(drop=True)
    with conn.cursor() as cur:
        cur.execute(f"drop table if exists {table_name}")
        cols = [
            f'"{col}" {_column_sql_type(frame[col])}'
            for col in frame.columns
        ]
        cur.execute(
            f"create table {table_name} (id bigint primary key, {', '.join(cols)})"
        )
        rows = []
        for idx, row in frame.iterrows():
            values = []
            for col in frame.columns:
                values.append(
                    _normalize_cell(row[col], numeric=_is_numeric_series(frame[col]))
                )
            rows.append((int(idx), *values))
        placeholders = ",".join(["%s"] * (len(frame.columns) + 1))
        quoted_cols = ", ".join(["id"] + [f'"{c}"' for c in frame.columns])
        cur.executemany(
            f"insert into {table_name} ({quoted_cols}) values ({placeholders})",
            rows,
        )
    conn.commit()


def _pg_dsn() -> str:
    _load_dotenv_if_present()

    host = os.getenv("TREE2CODE_PGHOST")
    port = os.getenv("TREE2CODE_PGPORT")
    user = os.getenv("TREE2CODE_PGUSER")
    password = os.getenv("TREE2CODE_PGPASSWORD")
    database = os.getenv("TREE2CODE_PGDATABASE")

    missing = []
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
        pytest.skip(
            "PostgreSQL integration test skipped. Missing env: " + ", ".join(missing)
        )

    return f"host={host} port={port} user={user} password={password} dbname={database}"


def _run_psql_sql_parity(
    model,
    frame: pd.DataFrame,
    *,
    tolerance: float,
    table_name: str,
    score_params: dict,
) -> None:
    psycopg = _psycopg()
    frame = frame.reset_index(drop=True)
    native_probs = model.predict_proba(frame)[:, 1]

    out = convert(
        model,
        to="sql",
        dialect="psql",
        sql_mode="select",
        keep_columns=["id"],
        table_name=table_name,
        base_score=score_params["base_score"],
        pdo=score_params["pdo"],
        base_odds=score_params["base_odds"],
        score_scale=3,
    )
    sql = out["sql"]["select_sql"]

    with psycopg.connect(_pg_dsn()) as conn:
        _prepare_table(conn, table_name, frame)
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    assert len(rows) == len(frame)
    by_id = {row[0]: row for row in rows}
    for idx in range(len(frame)):
        _, score_p, score = by_id[idx]
        assert math.isclose(
            float(score_p), float(native_probs[idx]), rel_tol=0.0, abs_tol=tolerance
        )
        assert float(f"{score:.3f}") == float(score)


def test_xgb_sql_matches_python_and_score_rule(xgb_model, sample_rows, score_params):
    _run_psql_sql_parity(
        xgb_model,
        sample_rows,
        tolerance=1e-7,
        table_name="tmp_tree2code_xgb_num",
        score_params=score_params,
    )


def test_lgb_sql_matches_python_and_score_rule(lgb_model, sample_rows, score_params):
    _run_psql_sql_parity(
        lgb_model,
        sample_rows,
        tolerance=1e-12,
        table_name="tmp_tree2code_lgb_num",
        score_params=score_params,
    )


def test_lgb_categorical_sql_matches_python_and_score_rule(
    lgb_categorical_model, categorical_sample_rows, score_params
):
    df = categorical_sample_rows.copy()
    df.iloc[0, df.columns.get_loc("cat_a")] = np.nan
    df.iloc[1, df.columns.get_loc("cat_b")] = np.nan
    _run_psql_sql_parity(
        lgb_categorical_model,
        df,
        tolerance=1e-12,
        table_name="tmp_tree2code_lgb_cat",
        score_params=score_params,
    )


def test_xgb_categorical_sql_matches_python_and_score_rule(
    xgb_categorical_model, categorical_sample_rows, score_params
):
    df = categorical_sample_rows.copy()
    df.iloc[0, df.columns.get_loc("cat_a")] = np.nan
    df.iloc[1, df.columns.get_loc("cat_b")] = np.nan
    _run_psql_sql_parity(
        xgb_categorical_model,
        df,
        tolerance=1e-6,
        table_name="tmp_tree2code_xgb_cat",
        score_params=score_params,
    )
