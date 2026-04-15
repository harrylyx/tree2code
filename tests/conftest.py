import pandas as pd
import pytest
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import os
import tempfile
import sys


@pytest.fixture(scope="session")
def dataset():
    X, y = make_classification(
        n_samples=10000,
        n_features=100,
        n_informative=4,
        n_redundant=2,
        random_state=42,
    )
    cols = [f"f{i}" for i in range(X.shape[1])]
    frame = pd.DataFrame(X, columns=cols)
    labels = pd.Series(y, name="label")
    return frame, labels


@pytest.fixture(scope="session")
def train_test(dataset):
    X, y = dataset
    return train_test_split(X, y, test_size=0.3, random_state=42)


@pytest.fixture(scope="session")
def xgb_model(train_test):
    import xgboost as xgb

    X_train, X_test, y_train, y_test = train_test
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.15,
        subsample=1.0,
        colsample_bytree=1.0,
        random_state=42,
        eval_metric="logloss",
        base_score=0.5,  # logit(0.5) = 0
    )
    model.fit(X_train, y_train)
    return model


@pytest.fixture(scope="session")
def lgb_model(train_test):
    import lightgbm as lgb

    X_train, X_test, y_train, y_test = train_test
    model = lgb.LGBMClassifier(
        n_estimators=300,
        max_depth=5,
        learning_rate=0.15,
        random_state=42,
        boost_from_average=False,  # initscore = 0
    )
    model.fit(X_train, y_train)
    return model


@pytest.fixture(scope="session")
def sample_rows(train_test):
    _, X_test, _, _ = train_test
    return X_test.reset_index(drop=True)


@pytest.fixture(scope="session")
def first_row(sample_rows):
    return sample_rows.iloc[0].to_dict()


@pytest.fixture(scope="session")
def score_params():
    return {
        "base_score": 600,
        "pdo": 50,
        "base_odds": 20,
        "score_scale": 3,
    }


@pytest.fixture(scope="session")
def categorical_dataset():
    size = 240
    frame = pd.DataFrame(
        {
            "num": [float(i % 50) for i in range(size)],
            "cat_a": pd.Categorical(
                ["a" if i % 3 == 0 else ("b" if i % 3 == 1 else "c") for i in range(size)]
            ),
            "cat_b": pd.Categorical(
                ["x" if i % 4 in {0, 1} else ("y" if i % 4 == 2 else "z") for i in range(size)]
            ),
        }
    )
    label = (
        (frame["cat_a"].isin(["a", "c"]).astype(int))
        ^ (frame["cat_b"].isin(["x"]).astype(int))
        ^ ((frame["num"] > 24).astype(int))
    ).astype(int)
    return train_test_split(frame, label, test_size=0.3, random_state=7)


@pytest.fixture(scope="session")
def lgb_categorical_model(categorical_dataset):
    import lightgbm as lgb

    x_train, x_test, y_train, y_test = categorical_dataset
    model = lgb.LGBMClassifier(
        n_estimators=12,
        max_depth=4,
        learning_rate=0.15,
        min_child_samples=5,
        random_state=7,
    )
    model.fit(x_train, y_train, categorical_feature=["cat_a", "cat_b"])
    return model


@pytest.fixture(scope="session")
def xgb_categorical_model(categorical_dataset):
    import xgboost as xgb

    x_train, x_test, y_train, y_test = categorical_dataset
    model = xgb.XGBClassifier(
        n_estimators=12,
        max_depth=4,
        learning_rate=0.15,
        tree_method="hist",
        enable_categorical=True,
        eval_metric="logloss",
        random_state=7,
    )
    model.fit(x_train, y_train)
    return model


@pytest.fixture(scope="session")
def categorical_sample_rows(categorical_dataset):
    _, x_test, _, _ = categorical_dataset
    return x_test.reset_index(drop=True)
@pytest.fixture(scope="session")
def spark():
    try:
        from pyspark.sql import SparkSession
    except ImportError:
        pytest.skip("pyspark not installed")

    # Set JAVA_HOME
    java_home = "/opt/homebrew/opt/openjdk/libexec/openjdk.jdk/Contents/Home"
    if os.path.exists(java_home):
        os.environ["JAVA_HOME"] = java_home
        os.environ["PATH"] = f"{java_home}/bin:" + os.environ["PATH"]

    warehouse_dir = tempfile.mkdtemp()
    spark = SparkSession.builder \
        .appName("Tree2CodeTest") \
        .master("local[1]") \
        .config("spark.driver.memory", "8g") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.sql.warehouse.dir", warehouse_dir) \
        .config("spark.ui.enabled", "false") \
        .getOrCreate()
    
    yield spark
    spark.stop()
