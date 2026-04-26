from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Union

from .parsers import parse_model
from .render_pmml import render_pmml
from .render_python import render_python
from .render_sql import render_sql
from .scoring import build_abnormal_spec, build_score_spec


def _normalize_to(to: Union[str, Sequence[str]]) -> List[str]:
    """Normalize the 'to' parameter into a list of lowercase strings.

    Args:
        to: Target conversion format(s). Can be 'sql', 'python', 'pmml',
            or a list of them.

    Returns:
        List[str]: Normalized target formats.

    Raises:
        ValueError: If an unsupported target format is provided.
    """
    if isinstance(to, str):
        values = [to]
    else:
        values = list(to)

    normalized: List[str] = []
    for item in values:
        value = str(item).lower().strip()
        if value not in {"sql", "python", "pmml"}:
            raise ValueError("to must contain only: 'sql', 'python', 'pmml'")
        if value not in normalized:
            normalized.append(value)
    return normalized


def convert(
    model: Any,
    to: Union[str, Sequence[str]] = "sql",
    *,
    dialect: str = "psql",
    sql_mode: str = "expression",
    literal_format: str = "standard",
    keep_columns: Optional[Sequence[str]] = None,
    table_name: str = "data_table",
    output_table: Optional[str] = None,
    base_score: Optional[float] = None,
    pdo: Optional[float] = None,
    base_odds: Optional[float] = None,
    score_scale: int = 3,
    abnormal_rule: Optional[str] = None,
    default_fill_value: Optional[float] = None,
    abnormal_value: Optional[float] = None,
    compatible_mode: bool = False,
    pmml_version: str = "4.4.1",
    pmml_model_name: str = "tree2code_model",
    pmml_target_name: str = "target",
    pmml_positive_class: str = "1",
    pmml_negative_class: str = "0",
) -> Dict[str, Any]:
    """Convert a binary XGBoost / LightGBM model into SQL, Python, and/or PMML.

    Args:
        model: The trained model object (XGBoost Booster/Classifier or LightGBM Booster/Classifier).
        to: Target format(s). One of 'sql', 'python', 'pmml', or a list of them.
            Defaults to "sql".
        dialect: SQL dialect. Either 'psql' (PostgreSQL) or 'hive'. Defaults to "psql".
        sql_mode: SQL output format. One of:
            - 'expression': Returns the raw score_p and score mathematical expressions.
            - 'select': Returns a SELECT statement.
            - 'ddl': Returns a full DROP + CREATE TABLE AS SELECT statement.
            Defaults to "expression".
        literal_format: Literal formatting mode. One of:
            - 'standard': Standard numeric formatting (e.g., 0.1).
            - 'scientific': Scientific notation (e.g., 1.0e-01), forcing DOUBLE parsing in Spark.
            Defaults to "standard".
        keep_columns: Columns to include in the SELECT/DDL statement.
        table_name: Source table name for SELECT/DDL. Defaults to "data_table".
        output_table: Target table name for DDL mode. Defaults to "output_table".
        base_score: Credit scorecard parameter: base score.
        pdo: Credit scorecard parameter: points to double the odds.
        base_odds: Credit scorecard parameter: base odds.
        score_scale: Number of decimal places for the score. Defaults to 3.
        abnormal_rule: Predefined check rule. One of 'all_null' or 'all_default'.
        default_fill_value: The value representing 'default/null' if rule is 'all_default'.
        abnormal_value: The value to output if the abnormal rule is triggered.
        compatible_mode: Whether to enable nan handling. Default is False.
        pmml_version: PMML version. One of '4.4.1', '4.3', or '4.2.1'.
        pmml_model_name: Model name to use in generated PMML.
        pmml_target_name: Synthetic binary target field name to use in PMML.
        pmml_positive_class: Positive class label to use in PMML.
        pmml_negative_class: Negative class label to use in PMML.

    Returns:
        Dict[str, Any]: A dictionary containing the generated code and metadata.
            Keys include 'meta', and optionally 'sql', 'python', and 'pmml'.

    Example:
        >>> out = convert(model, to="sql", dialect="hive", sql_mode="select")
        >>> print(out["sql"]["select_sql"])
    """

    outputs = _normalize_to(to)
    score_spec = build_score_spec(base_score, pdo, base_odds, score_scale)
    abnormal_spec = build_abnormal_spec(
        abnormal_rule, default_fill_value, abnormal_value
    )

    ir = parse_model(model)

    result: Dict[str, Any] = {
        "meta": {
            "model_type": ir.model_type,
            "feature_names": list(ir.feature_names),
        }
    }

    if "sql" in outputs:
        result["sql"] = render_sql(
            ir=ir,
            dialect=dialect,
            sql_mode=sql_mode,
            keep_columns=keep_columns,
            table_name=table_name,
            output_table=output_table,
            score_spec=score_spec,
            abnormal_spec=abnormal_spec,
            literal_format=literal_format,
            compatible_mode=compatible_mode,
        )

    if "python" in outputs:
        result["python"] = render_python(
            ir=ir,
            score_spec=score_spec,
            abnormal_spec=abnormal_spec,
            compatible_mode=compatible_mode,
        )

    if "pmml" in outputs:
        result["pmml"] = render_pmml(
            ir=ir,
            pmml_version=pmml_version,
            model_name=pmml_model_name,
            target_name=pmml_target_name,
            positive_class=pmml_positive_class,
            negative_class=pmml_negative_class,
        )

    return result
