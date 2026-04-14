import xgboost as xgb
from sklearn.datasets import make_classification
from tree2code import convert

# 1. Create a dummy model
X, y = make_classification(n_samples=100, n_features=4, n_informative=2, random_state=42)
model = xgb.XGBClassifier(n_estimators=2, max_depth=2, random_state=42)
model.fit(X, y)

# 2. Convert to DDL
out = convert(
    model,
    to="sql",
    dialect="hive",
    sql_mode="ddl",
    output_table="my_score_table",
    table_name="source_table",
    keep_columns=["id"],
    base_score=600,
    pdo=50,
    base_odds=20,
    abnormal_rule="all_default",
    default_fill_value=-999999,
    abnormal_value=-1
)

print("-" * 40)
print("GENERATED DDL SQL:")
print("-" * 40)
print(out["sql"]["ddl_sql"])
print("-" * 40)

# 3. Test with all_null
out_null = convert(
    model,
    to="sql",
    dialect="psql",
    sql_mode="ddl",
    output_table="my_psql_table",
    table_name="source_table",
    keep_columns=["id"],
    base_score=600,
    pdo=50,
    base_odds=20,
    abnormal_rule="all_null",
    abnormal_value=-1
)

print("\n" + "-" * 40)
print("GENERATED PSQL ALL_NULL SQL:")
print("-" * 40)
print(out_null["sql"]["ddl_sql"])
print("-" * 40)
