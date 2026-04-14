from tree2code.ir import TreeNode, eval_tree


def test_eval_tree_numeric_missing_type_none_routes_nan_and_none_right():
    tree = TreeNode(
        feature="f0",
        split_type="numeric",
        threshold=0.5,
        left=TreeNode(leaf_value=1.0),
        right=TreeNode(leaf_value=0.0),
        default_left=True,
        operator="<=",
        missing_type="none",
    )

    assert eval_tree(tree, {"f0": -1.0}) == 1.0
    assert eval_tree(tree, {"f0": 1.0}) == 0.0
    assert eval_tree(tree, {"f0": float("nan")}) == 0.0
    assert eval_tree(tree, {"f0": None}) == 0.0


def test_eval_tree_categorical_missing_type_none_routes_non_hits_right():
    tree = TreeNode(
        feature="cat",
        split_type="categorical",
        categories=["a", "b"],
        left=TreeNode(leaf_value=1.0),
        right=TreeNode(leaf_value=0.0),
        default_left=True,
        missing_type="none",
    )

    assert eval_tree(tree, {"cat": "a"}) == 1.0
    assert eval_tree(tree, {"cat": "z"}) == 0.0
    assert eval_tree(tree, {"cat": None}) == 0.0
    assert eval_tree(tree, {"cat": float("nan")}) == 0.0
