import numpy as np
import pandas as pd
from tree2code import convert


def _run_spark_sql_parity(
    spark,
    model,
    frame: pd.DataFrame,
    table_name: str,
    tolerance: float,
    *,
    literal_format: str = "scientific",
    spark_nan_as_null: bool = False,
) -> None:
    """Run SQL in Spark and compare score_p against native model output by explicit row id."""
    native_input = frame.reset_index(drop=True).copy()
    native_probs = model.predict_proba(native_input)[:, 1]

    spark_input = native_input.copy()
    if spark_nan_as_null:
        spark_input = spark_input.astype(object).where(pd.notna(spark_input), None)
    spark_input.insert(0, "__row_id", np.arange(len(spark_input), dtype=int))

    # Spark handles object/string columns better than pandas Categorical directly.
    for col in spark_input.columns:
        if str(spark_input[col].dtype) == "category":
            spark_input[col] = spark_input[col].astype(object)

    spark.createDataFrame(spark_input).createOrReplaceTempView(table_name)
    out = convert(
        model,
        to="sql",
        dialect="hive",
        sql_mode="select",
        literal_format=literal_format,
        table_name=table_name,
        keep_columns=["__row_id"],
    )
    spark_results = spark.sql(out["sql"]["select_sql"]).toPandas()

    expected = pd.DataFrame(
        {
            "__row_id": np.arange(len(native_probs), dtype=int),
            "native_score_p": native_probs,
        }
    )
    merged = expected.merge(
        spark_results[["__row_id", "score_p"]],
        on="__row_id",
        how="left",
    )

    assert len(merged) == len(expected)
    assert merged["score_p"].notna().all()

    diff = np.abs(merged["native_score_p"].to_numpy() - merged["score_p"].to_numpy())
    max_diff = float(np.max(diff))
    assert max_diff < tolerance, f"Spark parity failed: max diff={max_diff:.2e}"


def test_lgb_spark_parity_with_nan(spark, lgb_model, sample_rows):
    """Verify LightGBM numeric SQL parity in Spark with NaN values."""
    df = sample_rows.copy()
    df.iloc[0, 0] = np.nan
    df.iloc[1, 1] = np.nan
    _run_spark_sql_parity(spark, lgb_model, df, "temp_lgb_num", tolerance=1e-12)


def test_xgb_spark_parity_with_nan(spark, xgb_model, sample_rows):
    """Verify XGBoost numeric SQL parity in Spark with NaN values."""
    df = sample_rows.copy()
    df.iloc[0, 0] = np.nan
    df.iloc[1, 1] = np.nan
    _run_spark_sql_parity(spark, xgb_model, df, "temp_xgb_num", tolerance=1e-6)


def test_xgb_spark_parity_with_standard_literals(spark, xgb_model, sample_rows):
    """Verify Hive SQL executes and aligns in non-scientific literal format."""
    df = sample_rows.head(300).copy()
    df.iloc[0, 0] = np.nan
    df.iloc[1, 1] = np.nan
    _run_spark_sql_parity(
        spark,
        xgb_model,
        df,
        "temp_xgb_num_std",
        tolerance=1e-6,
        literal_format="standard",
    )


def test_lgb_spark_parity_with_standard_literals(spark, lgb_model, sample_rows):
    """Verify LightGBM aligns in non-scientific literal format."""
    df = sample_rows.head(300).copy()
    df.iloc[0, 0] = np.nan
    df.iloc[1, 1] = np.nan
    _run_spark_sql_parity(
        spark,
        lgb_model,
        df,
        "temp_lgb_num_std",
        tolerance=1e-12,
        literal_format="standard",
    )


def test_lgb_spark_parity_with_categorical_and_missing(
    spark, lgb_categorical_model, categorical_sample_rows
):
    """Verify LightGBM categorical SQL parity in Spark with category missing values."""
    df = categorical_sample_rows.copy()
    df.iloc[0, df.columns.get_loc("cat_a")] = np.nan
    df.iloc[1, df.columns.get_loc("cat_b")] = np.nan
    _run_spark_sql_parity(spark, lgb_categorical_model, df, "temp_lgb_cat", tolerance=1e-12)


def test_xgb_spark_parity_with_categorical_and_missing(
    spark, xgb_categorical_model, categorical_sample_rows
):
    """Verify XGBoost categorical SQL parity in Spark with category missing values."""
    df = categorical_sample_rows.copy()
    df.iloc[0, df.columns.get_loc("cat_a")] = np.nan
    df.iloc[1, df.columns.get_loc("cat_b")] = np.nan
    _run_spark_sql_parity(spark, xgb_categorical_model, df, "temp_xgb_cat", tolerance=1e-6)
