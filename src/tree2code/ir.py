from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional


@dataclass
class TreeNode:
    """A node in a decision tree.

    Attributes:
        feature: The name of the feature to split on.
        threshold: The threshold value for the split.
        left: The left child node (typically the 'True' branch).
        right: The right child node (typically the 'False' branch).
        default_left: Whether to go left if the feature value is missing.
        operator: The comparison operator (e.g., '<', '<=').
        missing_type: How missing values are represented ('nan' or 'zero').
        leaf_value: The value to return if this is a leaf node.
    """

    feature: Optional[str] = None
    threshold: Optional[float] = None
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None
    default_left: bool = True
    operator: str = "<"
    missing_type: str = "nan"
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
        missing_type: The type of missingness to check for ('nan' or 'zero').

    Returns:
        bool: True if the value is missing.
    """
    if value is None:
        return True
    if isinstance(value, float) and math.isnan(value):
        return True
    if missing_type == "zero" and value == 0:
        return True
    return False


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
    assert node.threshold is not None

    value = row.get(node.feature)
    missing = _is_missing(value, node.missing_type)

    if missing:
        go_left = node.default_left
    else:
        if node.operator == "<=":
            go_left = value <= node.threshold
        else:
            go_left = value < node.threshold

    return eval_tree(node.left if go_left else node.right, row)


def eval_margin(ir: ModelIR, row: Dict[str, Any]) -> float:
    """Calculate the raw margin (sum of tree scores + base margin) for a row.

    Args:
        ir: The model intermediate representation.
        row: A dictionary mapping feature names to values.

    Returns:
        float: The raw margin score.
    """
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
