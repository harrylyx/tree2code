from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional, Sequence, Union

from .parsers import parse_model
from .render_python import render_python
from .render_sql import render_sql
from .scoring import build_abnormal_spec, build_score_spec


def _normalize_to(to: Union[str, Sequence[str]]) -> List[str]:
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
    base_score: Optional[float] = None,
    pdo: Optional[float] = None,
    base_odds: Optional[float] = None,
    score_scale: int = 3,
    abnormal_rule: Optional[str] = None,
    default_fill_value: Optional[float] = None,
    abnormal_value: Optional[float] = None,
) -> Dict[str, Any]:
    """Convert a binary XGBoost / LightGBM model into SQL and/or pure Python code."""

    outputs = _normalize_to(to)
    score_spec = build_score_spec(base_score, pdo, base_odds, score_scale)
    abnormal_spec = build_abnormal_spec(abnormal_rule, default_fill_value, abnormal_value)

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
