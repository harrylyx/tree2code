from __future__ import annotations

import ctypes
import ctypes.util
import math
import struct
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional


@dataclass
class TreeNode:
    """A node in a decision tree.

    Attributes:
        feature: The name of the feature to split on.
        split_type: The split kind ('numeric' or 'categorical').
        threshold: The threshold value for numeric split.
        categories: Accepted category values for categorical split.
        left: The left child node (typically the 'True' branch).
        right: The right child node (typically the 'False' branch).
        default_left: Whether to go left if the feature value is missing.
        operator: The comparison operator (e.g., '<', '<=').
        missing_type: How missing values are represented ('nan', 'zero', or 'none').
        float32_compare: Whether numeric comparison should use float32 alignment.
        leaf_value: The value to return if this is a leaf node.
    """

    feature: Optional[str] = None
    split_type: str = "numeric"
    threshold: Optional[float] = None
    categories: Optional[List[Any]] = None
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None
    default_left: bool = True
    operator: str = "<"
    missing_type: str = "nan"
    float32_compare: bool = False
    leaf_value: Optional[float] = None

    @property
    def is_leaf(self) -> bool:
        """Check if the node is a leaf node."""
        return self.leaf_value is not None


@dataclass
class ModelIR:
    """Intermediate Representation of a tree-based model.

    Attributes:
        model_type: The type of model (e.g., 'xgboost', 'lightgbm').
        feature_names: List of all feature names used in the model.
        trees: List of roots of the decision trees.
        base_margin: The initial score before adding tree scores.
    """

    model_type: str
    feature_names: List[str]
    trees: List[TreeNode]
    base_margin: float = 0.0


def _is_missing(value: Any, missing_type: str) -> bool:
    """Internal helper to check if a value is considered 'missing'.

    Args:
        value: The value to check.
        missing_type: The type of missingness to check for ('nan', 'zero', or 'none').

    Returns:
        bool: True if the value is missing.
    """
    if missing_type == "none":
        return False

    if value is None:
        return True

    try:
        if math.isnan(float(value)):
            return True
    except (TypeError, ValueError):
        pass

    if missing_type == "zero" and value == 0:
        return True

    return False


def _normalize_category_value(value: Any) -> Any:
    """Normalize category value for robust categorical membership matching."""
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
        if value.is_integer():
            return int(value)
        return value
    return value


def _float32(value: Any) -> float:
    """Convert value to float32 precision in pure Python."""
    return struct.unpack("!f", struct.pack("!f", float(value)))[0]


def _load_expf() -> Any:
    """Load the platform float32 exp function when available."""
    candidates = [None, ctypes.util.find_library("m"), "msvcrt"]
    for candidate in candidates:
        try:
            if candidate is None:
                library = ctypes.CDLL(None)
            else:
                library = ctypes.CDLL(candidate)
            expf = library.expf
            expf.argtypes = [ctypes.c_float]
            expf.restype = ctypes.c_float
            return expf
        except Exception:
            continue
    return None


_EXPF = _load_expf()


def _xgb_sigmoid(value: Any) -> float:
    """Evaluate XGBoost's float32 logistic transform."""
    value = _float32(value)
    if _EXPF is None:
        return _float32(1.0 / (1.0 + math.exp(-value)))

    exp_value = _EXPF(ctypes.c_float(-value))
    denom = _float32(_float32(1.0) + exp_value)
    return _float32(_float32(1.0) / denom)


def _eval_numeric_branch(node: TreeNode, value: Any) -> bool:
    """Evaluate numeric split condition for one non-missing value."""
    assert node.threshold is not None

    # LightGBM `missing_type=None` treats NaN/None like numeric zero
    # in branch comparison rather than routing through default_left.
    if node.missing_type == "none":
        if value is None:
            value = 0.0
        else:
            try:
                parsed = float(value)
            except (TypeError, ValueError):
                parsed = None
            if parsed is not None and math.isnan(parsed):
                value = 0.0

    try:
        if node.float32_compare:
            left_value = _float32(value)
            threshold = _float32(node.threshold)
        else:
            left_value = float(value)
            threshold = float(node.threshold)
    except (TypeError, ValueError):
        return False

    if math.isnan(left_value):
        return False

    if node.operator == "<=":
        return left_value <= threshold
    return left_value < threshold


def _eval_categorical_branch(node: TreeNode, value: Any) -> bool:
    """Evaluate categorical split condition for one non-missing value."""
    categories = node.categories or []
    normalized = _normalize_category_value(value)
    return normalized in categories


def eval_tree(node: TreeNode, row: Dict[str, Any]) -> float:
    """Recursively evaluate a decision tree for a single row of data.

    Args:
        node: The current node in the tree.
        row: A dictionary mapping feature names to values.

    Returns:
        float: The leaf value determined by the tree.
    """
    if node.is_leaf:
        return float(node.leaf_value)

    assert node.feature is not None
    assert node.left is not None
    assert node.right is not None

    value = row.get(node.feature)
    missing = _is_missing(value, node.missing_type)

    if missing:
        go_left = node.default_left
    elif node.split_type == "categorical":
        go_left = _eval_categorical_branch(node, value)
    else:
        go_left = _eval_numeric_branch(node, value)

    return eval_tree(node.left if go_left else node.right, row)


def eval_margin(ir: ModelIR, row: Dict[str, Any]) -> float:
    """Calculate the raw margin (sum of tree scores + base margin) for a row.

    Args:
        ir: The model intermediate representation.
        row: A dictionary mapping feature names to values.

    Returns:
        float: The raw margin score.
    """
    if ir.model_type == "xgboost":
        margin = _float32(ir.base_margin)
        for tree in ir.trees:
            margin = _float32(margin + _float32(eval_tree(tree, row)))
        return margin

    margin = float(ir.base_margin)
    for tree in ir.trees:
        margin += eval_tree(tree, row)
    return margin


def eval_probability(ir: ModelIR, row: Dict[str, Any]) -> float:
    """Calculate the probability (sigmoid of margin) for a row.

    Args:
        ir: The model intermediate representation.
        row: A dictionary mapping feature names to values.

    Returns:
        float: The predicted probability.
    """
    margin = eval_margin(ir, row)
    if ir.model_type == "xgboost":
        return _xgb_sigmoid(margin)
    return 1.0 / (1.0 + math.exp(-margin))


def collect_feature_names(nodes: Iterable[TreeNode]) -> List[str]:
    """Traverse trees to collect all feature names used in splits.

    Args:
        nodes: An iterable of tree root nodes.

    Returns:
        List[str]: A sorted list of unique feature names.
    """
    names: List[str] = []

    def _visit(node: TreeNode) -> None:
        if node.is_leaf:
            return
        if node.feature is not None:
            names.append(node.feature)
        if node.left is not None:
            _visit(node.left)
        if node.right is not None:
            _visit(node.right)

    for n in nodes:
        _visit(n)

    uniq = sorted(set(names))
    if all(name.startswith("f") and name[1:].isdigit() for name in uniq):
        uniq.sort(key=lambda x: int(x[1:]))
    return uniq
