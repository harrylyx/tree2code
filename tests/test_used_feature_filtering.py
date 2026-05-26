import json

from tree2code import convert


class _FakeXgbBooster:
    feature_names = ["used", "unused"]

    def save_config(self):
        return json.dumps(
            {
                "learner": {
                    "objective": {"name": "binary:logistic"},
                    "learner_model_param": {"base_score": "0.5"},
                }
            }
        )

    def get_dump(self, dump_format):
        assert dump_format == "json"
        return [
            json.dumps(
                {
                    "nodeid": 0,
                    "split": "used",
                    "split_condition": 1.0,
                    "yes": 1,
                    "no": 2,
                    "missing": 1,
                    "children": [
                        {"nodeid": 1, "leaf": 0.25},
                        {"nodeid": 2, "leaf": -0.25},
                    ],
                }
            )
        ]


class _FakeLgbBooster:
    def dump_model(self):
        return {
            "objective": "binary",
            "feature_names": ["used", "unused"],
            "tree_info": [
                {
                    "tree_structure": {
                        "split_feature": 0,
                        "decision_type": "<=",
                        "threshold": 1.0,
                        "missing_type": "NaN",
                        "default_left": True,
                        "left_child": {"leaf_value": 0.25},
                        "right_child": {"leaf_value": -0.25},
                    }
                }
            ],
        }


def test_xgboost_convert_omits_declared_features_not_used_by_trees():
    out = convert(
        _FakeXgbBooster(),
        to="sql",
        dialect="psql",
        sql_mode="expression",
        abnormal_rule="all_null",
        abnormal_value=-2,
    )

    assert out["meta"]["feature_names"] == ["used"]
    assert '"used"' in out["sql"]["score_p_expr"]
    assert "unused" not in out["sql"]["score_p_expr"]


def test_lightgbm_convert_omits_declared_features_not_used_by_trees():
    out = convert(
        _FakeLgbBooster(),
        to="sql",
        dialect="psql",
        sql_mode="expression",
        abnormal_rule="all_null",
        abnormal_value=-2,
    )

    assert out["meta"]["feature_names"] == ["used"]
    assert '"used"' in out["sql"]["score_p_expr"]
    assert "unused" not in out["sql"]["score_p_expr"]
