from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional


@dataclass
class TreeNode:
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
        return self.leaf_value is not None


@dataclass
class ModelIR:
    model_type: str
    feature_names: List[str]
    trees: List[TreeNode]
    base_margin: float = 0.0


def _is_missing(value: Any, missing_type: str) -> bool:
    if value is None:
        return True
    if isinstance(value, float) and math.isnan(value):
        return True
    if missing_type == "zero" and value == 0:
        return True
    return False


def eval_tree(node: TreeNode, row: Dict[str, Any]) -> float:
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
    margin = float(ir.base_margin)
    for tree in ir.trees:
        margin += eval_tree(tree, row)
    return margin


def eval_probability(ir: ModelIR, row: Dict[str, Any]) -> float:
    margin = eval_margin(ir, row)
    return 1.0 / (1.0 + math.exp(-margin))


def collect_feature_names(nodes: Iterable[TreeNode]) -> List[str]:
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
