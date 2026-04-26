from __future__ import annotations

import math
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from .ir import ModelIR, TreeNode


@dataclass(frozen=True)
class PmmlVersionSpec:
    """PMML namespace and root version attributes for one supported version."""

    version_attr: str
    namespace: str
    supports_is_final_result: bool


SUPPORTED_PMML_VERSIONS: Dict[str, PmmlVersionSpec] = {
    "4.4.1": PmmlVersionSpec("4.4.1", "https://www.dmg.org/PMML-4_4", True),
    "4.3": PmmlVersionSpec("4.3", "https://www.dmg.org/PMML-4_3", True),
    "4.2.1": PmmlVersionSpec("4.2", "https://www.dmg.org/PMML-4_2", False),
}


def _fmt_num(value: float) -> str:
    """Format a finite float for PMML numeric attributes."""
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("PMML numeric values must be finite")
    return format(value, ".17g")


def _indent_xml(element: ET.Element, level: int = 0) -> None:
    """Indent an ElementTree in a Python 3.8 compatible way."""
    indent = "\n" + ("  " * level)
    child_indent = "\n" + ("  " * (level + 1))
    children = list(element)
    if children:
        if not element.text or not element.text.strip():
            element.text = child_indent
        for child in children:
            _indent_xml(child, level + 1)
        if not children[-1].tail or not children[-1].tail.strip():
            children[-1].tail = indent
    if level and (not element.tail or not element.tail.strip()):
        element.tail = indent


def _iter_split_nodes(nodes: Iterable[TreeNode]) -> Iterable[TreeNode]:
    """Yield all non-leaf nodes from the provided trees."""
    stack = list(nodes)
    while stack:
        node = stack.pop()
        if node.is_leaf:
            continue
        yield node
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)


def _collect_categorical_values(ir: ModelIR) -> Dict[str, List[Any]]:
    """Collect categorical split values by feature."""
    values_by_feature: Dict[str, List[Any]] = {}
    for node in _iter_split_nodes(ir.trees):
        if node.split_type != "categorical":
            continue
        assert node.feature is not None
        values = values_by_feature.setdefault(node.feature, [])
        for value in node.categories or []:
            if value not in values:
                values.append(value)
    return values_by_feature


def _is_numeric_category(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _pmml_array_type(values: Sequence[Any]) -> str:
    if values and all(isinstance(v, int) and not isinstance(v, bool) for v in values):
        return "int"
    if values and all(_is_numeric_category(v) for v in values):
        return "real"
    return "string"


def _format_array_token(value: Any, array_type: str) -> str:
    if array_type in {"int", "real"}:
        return _fmt_num(float(value))

    text = str(value)
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    if escaped == "" or any(ch.isspace() for ch in escaped):
        return f'"{escaped}"'
    return escaped


def _add_array(parent: ET.Element, values: Sequence[Any]) -> None:
    array_type = _pmml_array_type(values)
    array = ET.SubElement(
        parent,
        "Array",
        {
            "n": str(len(values)),
            "type": array_type,
        },
    )
    array.text = " ".join(_format_array_token(value, array_type) for value in values)


def _add_mining_schema(
    parent: ET.Element,
    feature_names: Sequence[str],
    *,
    target_name: Optional[str] = None,
) -> None:
    schema = ET.SubElement(parent, "MiningSchema")
    for feature_name in feature_names:
        ET.SubElement(
            schema,
            "MiningField",
            {
                "name": feature_name,
                "usageType": "active",
            },
        )
    if target_name is not None:
        ET.SubElement(
            schema,
            "MiningField",
            {
                "name": target_name,
                "usageType": "target",
            },
        )


def _add_output_score_p(
    parent: ET.Element,
    target_name: str,
    positive_class: str,
    *,
    final: bool = True,
) -> None:
    output = ET.SubElement(parent, "Output")
    attrs = {
        "name": "score_p",
        "optype": "continuous",
        "dataType": "double",
        "targetField": target_name,
        "feature": "probability",
        "value": positive_class,
    }
    if not final:
        attrs["isFinalResult"] = "false"
    ET.SubElement(output, "OutputField", attrs)


def _add_simple_predicate(
    parent: ET.Element, field: str, operator: str, value: Any
) -> None:
    ET.SubElement(
        parent,
        "SimplePredicate",
        {
            "field": field,
            "operator": operator,
            "value": _fmt_num(float(value))
            if isinstance(value, (int, float)) and not isinstance(value, bool)
            else str(value),
        },
    )


def _add_simple_set_predicate(
    parent: ET.Element, field: str, operator: str, values: Sequence[Any]
) -> None:
    predicate = ET.SubElement(
        parent,
        "SimpleSetPredicate",
        {
            "field": field,
            "booleanOperator": operator,
        },
    )
    _add_array(predicate, values)


def _zero_predicate(parent: ET.Element, field: str, *, equal: bool) -> None:
    _add_simple_predicate(parent, field, "equal" if equal else "notEqual", 0.0)


def _add_surrogate_predicate(
    parent: ET.Element,
    primary_builder: Tuple[str, Tuple[Any, ...]],
    missing_fallback: bool,
) -> None:
    compound = ET.SubElement(
        parent, "CompoundPredicate", {"booleanOperator": "surrogate"}
    )
    kind, args = primary_builder
    if kind == "simple":
        _add_simple_predicate(compound, *args)
    elif kind == "set":
        _add_simple_set_predicate(compound, *args)
    else:
        raise ValueError(f"Unsupported predicate builder kind: {kind}")
    ET.SubElement(compound, "True" if missing_fallback else "False")


def _add_numeric_predicate(
    parent: ET.Element, node: TreeNode, *, left_branch: bool
) -> None:
    assert node.feature is not None
    assert node.threshold is not None

    if left_branch:
        operator = "lessOrEqual" if node.operator == "<=" else "lessThan"
        zero_fallback = _numeric_zero_goes_left(node)
    else:
        operator = "greaterThan" if node.operator == "<=" else "greaterOrEqual"
        zero_fallback = not _numeric_zero_goes_left(node)

    builder: Tuple[str, Tuple[Any, ...]] = (
        "simple",
        (node.feature, operator, node.threshold),
    )

    if node.missing_type == "none":
        _add_surrogate_predicate(parent, builder, zero_fallback)
        return

    if node.missing_type == "zero":
        if left_branch == node.default_left:
            compound = ET.SubElement(
                parent, "CompoundPredicate", {"booleanOperator": "or"}
            )
            _zero_predicate(compound, node.feature, equal=True)
            _add_simple_predicate(compound, node.feature, operator, node.threshold)
        else:
            compound = ET.SubElement(
                parent, "CompoundPredicate", {"booleanOperator": "and"}
            )
            _zero_predicate(compound, node.feature, equal=False)
            _add_simple_predicate(compound, node.feature, operator, node.threshold)
        return

    _add_simple_predicate(parent, node.feature, operator, node.threshold)


def _numeric_zero_goes_left(node: TreeNode) -> bool:
    assert node.threshold is not None
    threshold = float(node.threshold)
    if node.operator == "<=":
        return 0.0 <= threshold
    return 0.0 < threshold


def _add_categorical_predicate(
    parent: ET.Element, node: TreeNode, *, left_branch: bool
) -> None:
    assert node.feature is not None
    categories = node.categories or []
    operator = "isIn" if left_branch else "isNotIn"
    builder: Tuple[str, Tuple[Any, ...]] = ("set", (node.feature, operator, categories))

    if node.missing_type == "none":
        _add_surrogate_predicate(parent, builder, missing_fallback=not left_branch)
        return

    if node.missing_type == "zero":
        if left_branch == node.default_left:
            compound = ET.SubElement(
                parent, "CompoundPredicate", {"booleanOperator": "or"}
            )
            _zero_predicate(compound, node.feature, equal=True)
            _add_simple_set_predicate(compound, node.feature, operator, categories)
        else:
            compound = ET.SubElement(
                parent, "CompoundPredicate", {"booleanOperator": "and"}
            )
            _zero_predicate(compound, node.feature, equal=False)
            _add_simple_set_predicate(compound, node.feature, operator, categories)
        return

    _add_simple_set_predicate(parent, node.feature, operator, categories)


def _add_branch_predicate(
    parent: ET.Element, node: TreeNode, *, left_branch: bool
) -> None:
    if node.split_type == "categorical":
        _add_categorical_predicate(parent, node, left_branch=left_branch)
    else:
        _add_numeric_predicate(parent, node, left_branch=left_branch)


def _render_node(
    node: TreeNode,
    *,
    node_id_prefix: str,
    next_id: List[int],
    predicate_parent: Optional[ET.Element] = None,
) -> ET.Element:
    current_id = f"{node_id_prefix}_{next_id[0]}"
    next_id[0] += 1

    attrs = {"id": current_id}
    if node.is_leaf:
        assert node.leaf_value is not None
        attrs["score"] = _fmt_num(node.leaf_value)
    else:
        attrs["score"] = "0"

    element = ET.Element("Node", attrs)
    if predicate_parent is None:
        ET.SubElement(element, "True")
    else:
        element.append(predicate_parent)

    if node.is_leaf:
        return element

    assert node.left is not None
    assert node.right is not None

    left_predicate = ET.Element("PredicateContainer")
    _add_branch_predicate(left_predicate, node, left_branch=True)
    right_predicate = ET.Element("PredicateContainer")
    _add_branch_predicate(right_predicate, node, left_branch=False)

    left_child = _render_node(
        node.left,
        node_id_prefix=node_id_prefix,
        next_id=next_id,
        predicate_parent=list(left_predicate)[0],
    )
    right_child = _render_node(
        node.right,
        node_id_prefix=node_id_prefix,
        next_id=next_id,
        predicate_parent=list(right_predicate)[0],
    )

    if node.missing_type != "none":
        element.attrib["defaultChild"] = (
            left_child.attrib["id"] if node.default_left else right_child.attrib["id"]
        )

    element.append(left_child)
    element.append(right_child)
    return element


def _add_tree_model(
    parent: ET.Element,
    tree: TreeNode,
    *,
    tree_index: int,
    feature_names: Sequence[str],
    model_name: str,
) -> None:
    tree_model = ET.SubElement(
        parent,
        "TreeModel",
        {
            "modelName": f"{model_name}_tree_{tree_index}",
            "functionName": "regression",
            "splitCharacteristic": "binarySplit",
            "missingValueStrategy": "defaultChild",
            "noTrueChildStrategy": "returnNullPrediction",
        },
    )
    _add_mining_schema(tree_model, feature_names)
    tree_model.append(
        _render_node(
            tree,
            node_id_prefix=f"tree_{tree_index}_node",
            next_id=[0],
        )
    )


def _add_data_dictionary(
    root: ET.Element,
    ir: ModelIR,
    target_name: str,
    positive_class: str,
    negative_class: str,
) -> None:
    categorical_values = _collect_categorical_values(ir)
    data_dictionary = ET.SubElement(
        root,
        "DataDictionary",
        {"numberOfFields": str(len(ir.feature_names) + 1)},
    )

    for feature_name in ir.feature_names:
        values = categorical_values.get(feature_name)
        if values is None:
            ET.SubElement(
                data_dictionary,
                "DataField",
                {
                    "name": feature_name,
                    "optype": "continuous",
                    "dataType": "double",
                },
            )
            continue

        array_type = _pmml_array_type(values)
        data_type = (
            "integer"
            if array_type == "int"
            else "double"
            if array_type == "real"
            else "string"
        )
        ET.SubElement(
            data_dictionary,
            "DataField",
            {
                "name": feature_name,
                "optype": "categorical",
                "dataType": data_type,
            },
        )

    target = ET.SubElement(
        data_dictionary,
        "DataField",
        {
            "name": target_name,
            "optype": "categorical",
            "dataType": "string",
        },
    )
    ET.SubElement(target, "Value", {"value": positive_class})
    ET.SubElement(target, "Value", {"value": negative_class})


def _add_ensemble_segment(
    segmentation: ET.Element,
    ir: ModelIR,
    model_name: str,
    margin_field: str,
    *,
    supports_is_final_result: bool,
) -> None:
    segment = ET.SubElement(segmentation, "Segment", {"id": "tree_ensemble"})
    ET.SubElement(segment, "True")
    ensemble = ET.SubElement(
        segment,
        "MiningModel",
        {
            "modelName": f"{model_name}_tree_ensemble",
            "functionName": "regression",
        },
    )
    _add_mining_schema(ensemble, ir.feature_names)

    output = ET.SubElement(ensemble, "Output")
    output_attrs = {
        "name": margin_field,
        "optype": "continuous",
        "dataType": "double",
        "feature": "predictedValue",
    }
    if supports_is_final_result:
        output_attrs["isFinalResult"] = "false"
    ET.SubElement(output, "OutputField", output_attrs)

    ensemble_segmentation = ET.SubElement(
        ensemble,
        "Segmentation",
        {"multipleModelMethod": "sum"},
    )
    for tree_index, tree in enumerate(ir.trees):
        tree_segment = ET.SubElement(
            ensemble_segmentation,
            "Segment",
            {"id": f"tree_{tree_index}"},
        )
        ET.SubElement(tree_segment, "True")
        _add_tree_model(
            tree_segment,
            tree,
            tree_index=tree_index,
            feature_names=ir.feature_names,
            model_name=model_name,
        )


def _add_probability_segment(
    segmentation: ET.Element,
    ir: ModelIR,
    *,
    model_name: str,
    margin_field: str,
    target_name: str,
    positive_class: str,
    negative_class: str,
) -> None:
    segment = ET.SubElement(segmentation, "Segment", {"id": "probability"})
    ET.SubElement(segment, "True")
    regression = ET.SubElement(
        segment,
        "RegressionModel",
        {
            "modelName": f"{model_name}_probability",
            "functionName": "classification",
            "normalizationMethod": "logit",
            "targetFieldName": target_name,
        },
    )
    _add_mining_schema(regression, [margin_field], target_name=target_name)
    _add_output_score_p(regression, target_name, positive_class)

    positive_table = ET.SubElement(
        regression,
        "RegressionTable",
        {
            "targetCategory": positive_class,
            "intercept": _fmt_num(ir.base_margin),
        },
    )
    ET.SubElement(
        positive_table,
        "NumericPredictor",
        {
            "name": margin_field,
            "coefficient": "1",
        },
    )
    ET.SubElement(
        regression,
        "RegressionTable",
        {
            "targetCategory": negative_class,
            "intercept": "0",
        },
    )


def render_pmml(
    ir: ModelIR,
    *,
    pmml_version: str = "4.4.1",
    model_name: str = "tree2code_model",
    target_name: str = "target",
    positive_class: str = "1",
    negative_class: str = "0",
) -> str:
    """Render the model IR into a PMML XML document.

    Args:
        ir: The model intermediate representation.
        pmml_version: PMML version key. Supports '4.4.1', '4.3', and '4.2.1'.
        model_name: Name for the top-level PMML model.
        target_name: Name for the synthetic binary target field.
        positive_class: Label for the positive class probability.
        negative_class: Label for the negative class.

    Returns:
        The PMML document as a string.

    Raises:
        ValueError: If the PMML version or field names are invalid.
    """
    if pmml_version not in SUPPORTED_PMML_VERSIONS:
        supported = "', '".join(SUPPORTED_PMML_VERSIONS)
        raise ValueError(f"pmml_version must be one of: '{supported}'")

    if target_name in ir.feature_names:
        raise ValueError("pmml_target_name must not duplicate a feature name")

    version_spec = SUPPORTED_PMML_VERSIONS[pmml_version]
    margin_field = f"{model_name}_margin"
    if margin_field in ir.feature_names or margin_field == target_name:
        margin_field = "__tree2code_margin"

    root = ET.Element(
        "PMML",
        {
            "xmlns": version_spec.namespace,
            "version": version_spec.version_attr,
        },
    )
    ET.SubElement(root, "Header", {"copyright": "tree2code"})
    _add_data_dictionary(root, ir, target_name, positive_class, negative_class)

    mining_model = ET.SubElement(
        root,
        "MiningModel",
        {
            "modelName": model_name,
            "functionName": "classification",
        },
    )
    _add_mining_schema(mining_model, ir.feature_names, target_name=target_name)
    _add_output_score_p(mining_model, target_name, positive_class)

    segmentation = ET.SubElement(
        mining_model,
        "Segmentation",
        {"multipleModelMethod": "modelChain"},
    )
    _add_ensemble_segment(
        segmentation,
        ir,
        model_name,
        margin_field,
        supports_is_final_result=version_spec.supports_is_final_result,
    )
    _add_probability_segment(
        segmentation,
        ir,
        model_name=model_name,
        margin_field=margin_field,
        target_name=target_name,
        positive_class=positive_class,
        negative_class=negative_class,
    )

    _indent_xml(root)
    body = ET.tostring(root, encoding="unicode", short_empty_elements=True)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + body
