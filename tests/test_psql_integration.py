import math
import os

import psycopg
import pytest

from tree2code import convert


def _prepare_table(conn, table_name, frame):
    with conn.cursor() as cur:
        cur.execute(f"drop table if exists {table_name}")
        cols = [f'"{c}" double precision' for c in frame.columns]
        cur.execute(f"create table {table_name} (id bigint primary key, {', '.join(cols)})")
        rows = []
        for idx, row in frame.iterrows():
            rows.append((idx, *[float(row[c]) for c in frame.columns]))
        placeholders = ",".join(["%s"] * (len(frame.columns) + 1))
        quoted_cols = ", ".join(["id"] + [f'"{c}"' for c in frame.columns])
        cur.executemany(
            f"insert into {table_name} ({quoted_cols}) values ({placeholders})",
            rows,
        )
    conn.commit()


def _pg_dsn() -> str:
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

    return (
        f"host={host} port={port} user={user} password={password} dbname={database}"
    )


def test_xgb_sql_matches_python_and_score_rule(xgb_model, sample_rows, score_params):
    table_name = "tmp_tree2code_xgb"
    out = convert(
        xgb_model,
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

    ref_prob = xgb_model.predict_proba(sample_rows)[:, 1]

    with psycopg.connect(_pg_dsn()) as conn:
        _prepare_table(conn, table_name, sample_rows)
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    assert len(rows) == len(sample_rows)
    by_id = {row[0]: row for row in rows}
    for idx in range(len(sample_rows)):
        _, score_p, score = by_id[idx]
        assert math.isclose(float(score_p), float(ref_prob[idx]), rel_tol=0.0, abs_tol=1e-7)
        assert float(f"{score:.3f}") == float(score)


def test_lgb_sql_matches_python_and_score_rule(lgb_model, sample_rows, score_params):
    table_name = "tmp_tree2code_lgb"
    out = convert(
        lgb_model,
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

    ref_prob = lgb_model.predict_proba(sample_rows)[:, 1]

    with psycopg.connect(_pg_dsn()) as conn:
        _prepare_table(conn, table_name, sample_rows)
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    assert len(rows) == len(sample_rows)
    by_id = {row[0]: row for row in rows}
    for idx in range(len(sample_rows)):
        _, score_p, score = by_id[idx]
        assert math.isclose(float(score_p), float(ref_prob[idx]), rel_tol=0.0, abs_tol=1e-12)
        assert float(f"{score:.3f}") == float(score)
