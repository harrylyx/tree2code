import math
import numpy as np
import pandas as pd
import pytest
from tree2code import convert

def test_lgb_spark_parity_with_nan(spark, lgb_model, sample_rows):
    """Verify LightGBM parity in Spark SQL, including NaN handling and precision."""
    # Inject some NaNs into the data
    df = sample_rows.copy()
    feature_names = list(df.columns)
    
    # Ensure at least one row has NaN for a feature used in a split
    df.iloc[0, 0] = np.nan
    df.iloc[1, 1] = np.nan
    
    native_probs = lgb_model.predict_proba(df)[:, 1]
    
    out = convert(
        lgb_model,
        to="sql",
        dialect="hive",
        sql_mode="select",
        table_name="temp_lgb",
        keep_columns=feature_names
    )
    sql_query = out["sql"]["select_sql"]
    
    spark.createDataFrame(df).createOrReplaceTempView("temp_lgb")
    spark_results = spark.sql(sql_query).toPandas()
    
    sql_probs = spark_results["score_p"].values
    
    diff = np.abs(native_probs - sql_probs)
    max_diff = np.max(diff)
    print(f"LGB Max Diff: {max_diff:.2e}")
    
    # Tight threshold for LightGBM
    assert max_diff < 1e-12, f"LightGBM Parity failed: Max Diff {max_diff:.2e}"

def test_xgb_spark_parity_with_nan(spark, xgb_model, sample_rows):
    """Verify XGBoost parity in Spark SQL, including NaN handling and float32 alignment."""
    df = sample_rows.copy()
    feature_names = list(df.columns)
    
    df.iloc[0, 0] = np.nan
    df.iloc[1, 1] = np.nan
    
    native_probs = xgb_model.predict_proba(df)[:, 1]
    
    out = convert(
        xgb_model,
        to="sql",
        dialect="hive",
        sql_mode="select",
        table_name="temp_xgb",
        keep_columns=feature_names
    )
    sql_query = out["sql"]["select_sql"]
    
    spark.createDataFrame(df).createOrReplaceTempView("temp_xgb")
    spark_results = spark.sql(sql_query).toPandas()
    
    sql_probs = spark_results["score_p"].values
    
    diff = np.abs(native_probs - sql_probs)
    max_diff = np.max(diff)
    
    # XGBoost uses float32 internal representation, so we allow a bit more error
    assert max_diff < 1e-6, f"XGBoost Parity failed: Max Diff {max_diff:.2e}"
