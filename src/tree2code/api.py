from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Union

from .parsers import parse_model
from .render_python import render_python
from .render_sql import render_sql
from .scoring import build_abnormal_spec, build_score_spec


def _normalize_to(to: Union[str, Sequence[str]]) -> List[str]:
    """Normalize the 'to' parameter into a list of lowercase strings.

    Args:
        to: Target conversion format(s). Can be 'sql', 'python', or a list of them.

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
        if value not in {"sql", "python"}:
            raise ValueError("to must contain only: 'sql', 'python'")
        if value not in normalized:
            normalized.append(value)
    return normalized


def convert(
    model: Any,
    to: Union[str, Sequence[str]] = "sql",
    *,
    dialect: str = "psql",
    sql_mode: str = "expression",
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
) -> Dict[str, Any]:
    """Convert a binary XGBoost / LightGBM model into SQL and/or pure Python code.

    Args:
        model: The trained model object (XGBoost Booster/Classifier or LightGBM Booster/Classifier).
        to: Target format(s). One of 'sql', 'python', or a list containing both. Defaults to "sql".
        dialect: SQL dialect. Either 'psql' (PostgreSQL) or 'hive'. Defaults to "psql".
        sql_mode: SQL output format. One of:
            - 'expression': Returns the raw score_p and score mathematical expressions.
            - 'select': Returns a SELECT statement.
            - 'ddl': Returns a full DROP + CREATE TABLE AS SELECT statement.
            Defaults to "expression".
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

    Returns:
        Dict[str, Any]: A dictionary containing the generated code and metadata.
            Keys include 'meta', and optionally 'sql' and 'python'.

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
        )

    if "python" in outputs:
        result["python"] = render_python(
            ir=ir,
            score_spec=score_spec,
            abnormal_spec=abnormal_spec,
        )

    return result
