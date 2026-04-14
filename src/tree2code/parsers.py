from __future__ import annotations

import json
import math
from typing import Any, Dict, List

from .ir import ModelIR, TreeNode, collect_feature_names


def _extract_first_float(value: Any) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, list):
        if not value:
            raise ValueError("empty list cannot be parsed as float")
        return _extract_first_float(value[0])

    text = str(value).strip()
    if text.startswith("[") and text.endswith("]"):
        text = text[1:-1]
    if "," in text:
        text = text.split(",")[0]
    return float(text)


def _parse_xgb_tree_node(node: Dict[str, Any]) -> TreeNode:
    if "leaf" in node:
        return TreeNode(leaf_value=float(node["leaf"]))

    children = {child["nodeid"]: child for child in node["children"]}
    yes_id = node["yes"]
    no_id = node["no"]

    left = _parse_xgb_tree_node(children[yes_id])
    right = _parse_xgb_tree_node(children[no_id])

    return TreeNode(
        feature=str(node["split"]),
        threshold=float(node["split_condition"]),
        left=left,
        right=right,
        default_left=(node["missing"] == yes_id),
        operator="<",
        missing_type="nan",
    )


def _parse_xgboost(model: Any) -> ModelIR:
    booster = model.get_booster() if hasattr(model, "get_booster") else model

    config = json.loads(booster.save_config())
    objective = config.get("learner", {}).get("objective", {}).get("name", "")
    if objective and "binary:" not in objective:
        raise NotImplementedError("Only binary XGBoost models are supported")

    base_raw = config["learner"]["learner_model_param"]["base_score"]
    base_prob = _extract_first_float(base_raw)
    if base_prob <= 0 or base_prob >= 1:
        raise ValueError("xgboost base_score must be in (0, 1) for binary conversion")
    base_margin = math.log(base_prob / (1.0 - base_prob))

    dumps = booster.get_dump(dump_format="json")
    trees: List[TreeNode] = [_parse_xgb_tree_node(json.loads(text)) for text in dumps]

    feature_names = list(getattr(booster, "feature_names", None) or [])
    if not feature_names:
        feature_names = collect_feature_names(trees)

    return ModelIR(
        model_type="xgboost",
        feature_names=feature_names,
        trees=trees,
        base_margin=base_margin,
    )


def _parse_lgb_tree_node(node: Dict[str, Any], feature_names: List[str]) -> TreeNode:
    if "leaf_value" in node or "leaf_index" in node:
        return TreeNode(leaf_value=float(node["leaf_value"]))

    decision_type = str(node.get("decision_type", "<="))
    if decision_type in {"<=", "<", "no_greater"}:
        operator = "<="
    else:
        raise NotImplementedError("Only numeric split LightGBM models are supported")

    split_idx = int(node["split_feature"])
    feature = feature_names[split_idx]

    missing_type = str(node.get("missing_type", "None")).lower()
    normalized_missing_type = "zero" if "zero" in missing_type else "nan"

    left = _parse_lgb_tree_node(node["left_child"], feature_names)
    right = _parse_lgb_tree_node(node["right_child"], feature_names)

    return TreeNode(
        feature=feature,
        threshold=float(node["threshold"]),
        left=left,
        right=right,
        default_left=bool(node.get("default_left", True)),
        operator=operator,
        missing_type=normalized_missing_type,
    )


def _parse_lightgbm(model: Any) -> ModelIR:
    if hasattr(model, "booster_"):
        booster = model.booster_
    elif hasattr(model, "_Booster"):
        booster = model._Booster
    else:
        booster = model

    dump = booster.dump_model()
    objective = str(dump.get("objective", ""))
    if objective and "binary" not in objective:
        raise NotImplementedError("Only binary LightGBM models are supported")

    feature_names = list(dump["feature_names"])
    trees = [_parse_lgb_tree_node(t["tree_structure"], feature_names) for t in dump["tree_info"]]

    return ModelIR(
        model_type="lightgbm",
        feature_names=feature_names,
        trees=trees,
        base_margin=0.0,
    )


def parse_model(model: Any) -> ModelIR:
    if hasattr(model, "get_booster") or (
        hasattr(model, "save_config") and hasattr(model, "get_dump")
    ):
        return _parse_xgboost(model)

    if hasattr(model, "booster_") or hasattr(model, "_Booster") or hasattr(model, "dump_model"):
        return _parse_lightgbm(model)

    raise TypeError("Unsupported model object. Expected XGBoost or LightGBM binary model")
