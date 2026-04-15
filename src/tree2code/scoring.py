from __future__ import annotations

import math
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Optional

DEFAULT_SCORE_EPSILON = 1e-15


@dataclass
class ScoreSpec:
    """Specification for credit scorecard conversion.

    Attributes:
        base_score: The base score at base odds.
        pdo: Points to Double the Odds.
        base_odds: The odds at the base score.
        score_scale: Number of decimal places to round the final score.
        epsilon: Small value to clamp probability to avoid log(0).
    """

    base_score: float
    pdo: float
    base_odds: float
    score_scale: int = 3
    epsilon: float = DEFAULT_SCORE_EPSILON

    @property
    def factor(self) -> float:
        """Calculate the multiplier factor for the score formula."""
        return self.pdo / math.log(2.0)

    @property
    def offset(self) -> float:
        """Calculate the offset for the score formula."""
        return self.base_score + self.factor * math.log(self.base_odds)


def build_score_spec(
    base_score: Optional[float],
    pdo: Optional[float],
    base_odds: Optional[float],
    score_scale: int,
) -> Optional[ScoreSpec]:
    """Validate and build a ScoreSpec from optional parameters.

    Args:
        base_score: Optional base score.
        pdo: Optional PDO.
        base_odds: Optional base odds.
        score_scale: Precision for rounding.

    Returns:
        Optional[ScoreSpec]: The validated spec, or None if no parameters were provided.

    Raises:
        ValueError: If parameters are incomplete or invalid.
    """
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
    """Round a value to a given precision using ROUND_HALF_UP logic.

    Args:
        value: The number to round.
        scale: The number of decimal places.

    Returns:
        float: Rounded value.
    """
    quant = Decimal("1").scaleb(-scale)
    rounded = Decimal(str(value)).quantize(quant, rounding=ROUND_HALF_UP)
    return float(rounded)


def probability_to_score(probability: float, spec: ScoreSpec) -> float:
    """Convert a probability into a scorecard score.

    Args:
        probability: Predicted probability.
        spec: The scorecard specification.

    Returns:
        float: Calculated score.
    """
    odds = probability / (1.0 - probability)
    raw_score = spec.offset - spec.factor * math.log(odds)
    return round_half_up(raw_score, spec.score_scale)


@dataclass
class AbnormalSpec:
    """Specification for abnormal value handling.

    Attributes:
        rule: Type of rule ('all_null', 'all_default', or None).
        default_fill_value: The value representing 'default' if rule is 'all_default'.
        abnormal_value: The value to output if the rule is triggered.
    """

    rule: Optional[str] = None
    default_fill_value: Optional[float] = None
    abnormal_value: Optional[float] = None

    @property
    def active(self) -> bool:
        """Check if any abnormal rule is active and complete."""
        return (
            self.rule in {"all_null", "all_default"} and self.abnormal_value is not None
        )


def build_abnormal_spec(
    rule: Optional[str],
    default_fill_value: Optional[float],
    abnormal_value: Optional[float],
) -> AbnormalSpec:
    """Validate and build an AbnormalSpec.

    Args:
        rule: The rule name.
        default_fill_value: Optional default fill value.
        abnormal_value: Optional abnormal value output.

    Returns:
        AbnormalSpec: The validated spec.

    Raises:
        ValueError: If rule is unsupported or parameters are missing.
    """
    if rule not in {None, "all_null", "all_default"}:
        raise ValueError(
            "abnormal_rule must be one of: None, 'all_null', 'all_default'"
        )

    if (
        rule == "all_default"
        and abnormal_value is not None
        and default_fill_value is None
    ):
        raise ValueError(
            "default_fill_value is required when abnormal_rule='all_default'"
        )

    return AbnormalSpec(
        rule=rule, default_fill_value=default_fill_value, abnormal_value=abnormal_value
    )
