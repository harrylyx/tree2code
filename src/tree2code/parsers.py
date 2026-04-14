from __future__ import annotations

import json
import math
from typing import Any, Dict, List, Optional

from .ir import ModelIR, TreeNode, collect_feature_names


def _extract_first_float(value: Any) -> float:
    """Extract a float from a potentially complex object (like a list in string form).

    Args:
        value: The value to extract from.

    Returns:
        float: The extracted float value.

    Raises:
        ValueError: If extraction fails.
    """
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


def _normalize_category_value(value: Any) -> Any:
    """Normalize parsed category value to Python primitive."""
    if hasattr(value, "as_py"):
        try:
            value = value.as_py()
        except Exception:
            pass

    if hasattr(value, "item"):
        try:
            value = value.item()
        except Exception:
            pass

    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if math.isnan(value):
            return value
        if value.is_integer():
            return int(value)
        return float(value)

    return value


def _parse_xgb_category_maps(booster: Any) -> Dict[str, Dict[int, Any]]:
    """Extract XGBoost categorical id -> label map when available."""
    get_categories = getattr(booster, "get_categories", None)
    if get_categories is None:
        return {}

    try:
        categories_obj = get_categories(export_to_arrow=True)
        category_pairs = categories_obj.to_arrow()
    except Exception:
        return {}

    output: Dict[str, Dict[int, Any]] = {}
    for feature_name, values in category_pairs:
        if values is None:
            continue

        try:
            raw_values = values.to_pylist()
        except Exception:
            try:
                raw_values = list(values)
            except Exception:
                continue

        mapping: Dict[int, Any] = {}
        for idx, raw in enumerate(raw_values):
            mapping[int(idx)] = _normalize_category_value(raw)

        output[str(feature_name)] = mapping

    return output


def _parse_xgb_category_values(
    feature_name: str,
    split_condition: Any,
    category_maps: Dict[str, Dict[int, Any]],
) -> Optional[List[Any]]:
    """Parse XGBoost categorical split condition into comparable values."""
    if not isinstance(split_condition, list):
        return None

    codes: List[int] = [int(_extract_first_float(v)) for v in split_condition]
    mapping = category_maps.get(feature_name)

    output: List[Any] = []
    for code in codes:
        if mapping is not None and code in mapping:
            output.append(mapping[code])
        else:
            output.append(code)

    # keep order but deduplicate
    uniq: List[Any] = []
    for item in output:
        if item not in uniq:
            uniq.append(item)
    return uniq


def _parse_xgb_tree_node(
    node: Dict[str, Any],
    category_maps: Dict[str, Dict[int, Any]],
) -> TreeNode:
    """Recursively parse an XGBoost JSON tree node.

    Args:
        node: The JSON representation of an XGBoost tree node.
        category_maps: Feature-level id -> label category mapping.

    Returns:
        TreeNode: The parsed IR tree node.
    """
    if "leaf" in node:
        return TreeNode(leaf_value=float(node["leaf"]))

    children = {child["nodeid"]: child for child in node["children"]}
    yes_id = node["yes"]
    no_id = node["no"]

    left = _parse_xgb_tree_node(children[yes_id], category_maps)
    right = _parse_xgb_tree_node(children[no_id], category_maps)

    feature_name = str(node["split"])
    category_values = _parse_xgb_category_values(
        feature_name,
        node["split_condition"],
        category_maps,
    )

    if category_values is not None:
        return TreeNode(
            feature=feature_name,
            split_type="categorical",
            categories=category_values,
            left=left,
            right=right,
            default_left=(node["missing"] == yes_id),
            missing_type="nan",
        )

    return TreeNode(
        feature=feature_name,
        split_type="numeric",
        threshold=float(node["split_condition"]),
        left=left,
        right=right,
        default_left=(node["missing"] == yes_id),
        operator="<",
        missing_type="nan",
        float32_compare=True,
    )


def _parse_xgboost(model: Any) -> ModelIR:
    """Parse an XGBoost model into an IR.

    Args:
        model: The XGBoost model object.

    Returns:
        ModelIR: The parsed IR.

    Raises:
        NotImplementedError: If the model is not a binary classifier.
        ValueError: If base_score is invalid.
    """
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

    category_maps = _parse_xgb_category_maps(booster)

    dumps = booster.get_dump(dump_format="json")
    trees: List[TreeNode] = [
        _parse_xgb_tree_node(json.loads(text), category_maps) for text in dumps
    ]

    feature_names = list(getattr(booster, "feature_names", None) or [])
    if not feature_names:
        feature_names = collect_feature_names(trees)

    return ModelIR(
        model_type="xgboost",
        feature_names=feature_names,
        trees=trees,
        base_margin=base_margin,
    )


def _parse_lgb_category_codes(threshold: Any) -> List[int]:
    """Parse LightGBM categorical threshold string (e.g. '1||3||5')."""
    text = str(threshold)
    parts = [p.strip() for p in text.split("||") if p.strip()]
    if not parts:
        return []
    return [int(_extract_first_float(p)) for p in parts]


def _build_lgb_category_maps(dump: Dict[str, Any]) -> Dict[str, List[Any]]:
    """Build LightGBM feature -> raw category labels map when available."""
    feature_names = list(dump.get("feature_names", []))
    feature_infos = dump.get("feature_infos", {})
    pandas_categories = list(dump.get("pandas_categorical") or [])

    categorical_features: List[str] = []
    for feature_name in feature_names:
        info = feature_infos.get(feature_name, {})
        values = info.get("values")
        if isinstance(values, list) and len(values) > 0:
            categorical_features.append(feature_name)

    output: Dict[str, List[Any]] = {}
    for idx, feature_name in enumerate(categorical_features):
        if idx >= len(pandas_categories):
            break
        values = pandas_categories[idx]
        if not isinstance(values, list):
            continue
        output[feature_name] = [_normalize_category_value(v) for v in values]

    return output


def _parse_lgb_category_values(
    feature_name: str,
    threshold: Any,
    category_maps: Dict[str, List[Any]],
) -> List[Any]:
    """Resolve LightGBM categorical split ids to values if map exists."""
    codes = _parse_lgb_category_codes(threshold)
    raw_map = category_maps.get(feature_name)
    if not raw_map:
        return codes

    output: List[Any] = []
    for code in codes:
        if 0 <= code < len(raw_map):
            output.append(raw_map[code])
        else:
            output.append(code)

    uniq: List[Any] = []
    for item in output:
        if item not in uniq:
            uniq.append(item)
    return uniq


def _parse_lgb_tree_node(
    node: Dict[str, Any],
    feature_names: List[str],
    category_maps: Dict[str, List[Any]],
) -> TreeNode:
    """Recursively parse a LightGBM JSON tree node.

    Args:
        node: The JSON representation of a LightGBM tree node.
        feature_names: List of all feature names for mapping indices.
        category_maps: Feature-level category code -> raw value mapping.

    Returns:
        TreeNode: The parsed IR tree node.

    Raises:
        NotImplementedError: If the decision type is not supported.
    """
    if "leaf_value" in node or "leaf_index" in node:
        return TreeNode(leaf_value=float(node["leaf_value"]))

    split_idx = int(node["split_feature"])
    feature_name = feature_names[split_idx]

    decision_type = str(node.get("decision_type", "<="))

    missing_type = str(node.get("missing_type", "None")).lower()
    if "zero" in missing_type:
        normalized_missing_type = "zero"
    elif "none" in missing_type:
        normalized_missing_type = "none"
    else:
        normalized_missing_type = "nan"

    left = _parse_lgb_tree_node(node["left_child"], feature_names, category_maps)
    right = _parse_lgb_tree_node(node["right_child"], feature_names, category_maps)

    if decision_type in {"<=", "<", "no_greater"}:
        return TreeNode(
            feature=feature_name,
            split_type="numeric",
            threshold=float(node["threshold"]),
            left=left,
            right=right,
            default_left=bool(node.get("default_left", True)),
            operator="<=",
            missing_type=normalized_missing_type,
        )

    if decision_type in {"==", "in"}:
        return TreeNode(
            feature=feature_name,
            split_type="categorical",
            categories=_parse_lgb_category_values(
                feature_name,
                node["threshold"],
                category_maps,
            ),
            left=left,
            right=right,
            default_left=bool(node.get("default_left", True)),
            missing_type=normalized_missing_type,
        )

    raise NotImplementedError("Unsupported LightGBM decision_type: {0}".format(decision_type))


def _parse_lightgbm(model: Any) -> ModelIR:
    """Parse a LightGBM model into an IR.

    Args:
        model: The LightGBM model object.

    Returns:
        ModelIR: The parsed IR.

    Raises:
        NotImplementedError: If the model is not a binary classifier.
    """
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
    category_maps = _build_lgb_category_maps(dump)
    trees = [
        _parse_lgb_tree_node(t["tree_structure"], feature_names, category_maps)
        for t in dump["tree_info"]
    ]

    return ModelIR(
        model_type="lightgbm",
        feature_names=feature_names,
        trees=trees,
        base_margin=0.0,
    )


def parse_model(model: Any) -> ModelIR:
    """Parse a binary classifier model into an intermediate representation.

    Args:
        model: The model object (XGBoost or LightGBM).

    Returns:
        ModelIR: The model in intermediate representation.

    Raises:
        TypeError: If the model object is not supported.
    """
    if hasattr(model, "get_booster") or (
        hasattr(model, "save_config") and hasattr(model, "get_dump")
    ):
        return _parse_xgboost(model)

    if (
        hasattr(model, "booster_")
        or hasattr(model, "_Booster")
        or hasattr(model, "dump_model")
    ):
        return _parse_lightgbm(model)

    raise TypeError(
        "Unsupported model object. Expected XGBoost or LightGBM binary model"
    )
