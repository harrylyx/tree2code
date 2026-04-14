from __future__ import annotations

import math
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional


DEFAULT_SCORE_EPSILON = 1e-15


@dataclass
class ScoreSpec:
    base_score: float
    pdo: float
    base_odds: float
    score_scale: int = 3
    epsilon: float = DEFAULT_SCORE_EPSILON

    @property
    def factor(self) -> float:
        return self.pdo / math.log(2.0)

    @property
    def offset(self) -> float:
        return self.base_score + self.factor * math.log(self.base_odds)


def build_score_spec(
    base_score: Optional[float],
    pdo: Optional[float],
    base_odds: Optional[float],
    score_scale: int,
) -> Optional[ScoreSpec]:
    values = [base_score, pdo, base_odds]
    has_any = any(v is not None for v in values)
    has_all = all(v is not None for v in values)

    if has_any and not has_all:
        raise ValueError("base_score, pdo, base_odds must be provided together")

    if not has_any:
        return None

    assert base_score is not None
    assert pdo is not None
    assert base_odds is not None

    if pdo <= 0:
        raise ValueError("pdo must be positive")
    if base_odds <= 0:
        raise ValueError("base_odds must be positive")
    if score_scale < 0:
        raise ValueError("score_scale must be >= 0")

    return ScoreSpec(
        base_score=float(base_score),
        pdo=float(pdo),
        base_odds=float(base_odds),
        score_scale=int(score_scale),
    )


def round_half_up(value: float, scale: int) -> float:
    quant = Decimal("1").scaleb(-scale)
    rounded = Decimal(str(value)).quantize(quant, rounding=ROUND_HALF_UP)
    return float(rounded)


def probability_to_score(probability: float, spec: ScoreSpec) -> float:
    p = min(max(float(probability), spec.epsilon), 1.0 - spec.epsilon)
    odds = p / (1.0 - p)
    raw_score = spec.offset - spec.factor * math.log(odds)
    return round_half_up(raw_score, spec.score_scale)


@dataclass
class AbnormalSpec:
    rule: Optional[str] = None
    default_fill_value: Optional[float] = None
    abnormal_value: Optional[float] = None

    @property
    def active(self) -> bool:
        return self.rule in {"all_null", "all_default"} and self.abnormal_value is not None


def build_abnormal_spec(
    rule: Optional[str],
    default_fill_value: Optional[float],
    abnormal_value: Optional[float],
) -> AbnormalSpec:
    if rule not in {None, "all_null", "all_default"}:
        raise ValueError("abnormal_rule must be one of: None, 'all_null', 'all_default'")

    if rule == "all_default" and abnormal_value is not None and default_fill_value is None:
        raise ValueError("default_fill_value is required when abnormal_rule='all_default'")

    return AbnormalSpec(rule=rule, default_fill_value=default_fill_value, abnormal_value=abnormal_value)
