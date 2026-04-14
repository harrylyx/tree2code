import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


@pytest.fixture(scope="session")
def dataset():
    X, y = make_classification(
        n_samples=400,
        n_features=8,
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
        n_estimators=5,
        max_depth=3,
        learning_rate=0.15,
        subsample=1.0,
        colsample_bytree=1.0,
        random_state=42,
        eval_metric="logloss",
    )
    model.fit(X_train, y_train)
    return model


@pytest.fixture(scope="session")
def lgb_model(train_test):
    import lightgbm as lgb

    X_train, X_test, y_train, y_test = train_test
    model = lgb.LGBMClassifier(
        n_estimators=5,
        max_depth=3,
        learning_rate=0.15,
        random_state=42,
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
