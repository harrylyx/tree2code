# tree2code

tree2code converts trained binary tree models into standalone scoring artifacts while preserving the model's probability and scorecard semantics.

## Language

**Positive-class probability**:
The model output `p` for the positive class.
_Avoid_: Score, model score

**Base odds**:
The negative-to-positive class odds `(1 - p) / p` at the base score. For example, `base_odds=100` means 100 negative outcomes for every positive outcome.
_Avoid_: Probability odds, `p / (1 - p)`

**Raw score**:
The scorecard value calculated from the positive-class probability before decimal-place rounding.
_Avoid_: Probability, `score_p`

**Rounded score**:
The raw score rounded to a specified number of decimal places.
_Avoid_: Raw score, probability

**Required scoring feature**:
A feature that appears in at least one model split and can therefore affect the prediction. Features present during training but unused by every split are not required scoring features.
_Avoid_: Training feature, input column

**Missing feature**:
A required scoring feature whose key is absent from a scoring input.
_Avoid_: Missing value, null value

**Missing value**:
An explicitly supplied raw missing marker, such as `None`, numeric `NaN`, or a recognized textual marker such as `"nan"` or `"null"`.
_Avoid_: Missing feature

**Raw missing marker**:
Any accepted input representation of a missing value before normalization, including object, numeric, and textual forms.
_Avoid_: Missing feature, normalized missing value

**Default filling**:
Replacement of every raw missing marker with a configured fill value before prediction. The filled value becomes the model input rather than retaining native missing-value behavior.
_Avoid_: Missing-value routing, input validation

**All-default input**:
An input whose required scoring features all equal the configured fill value after default filling. It produces the configured abnormal result instead of a model prediction.
_Avoid_: All-missing input, missing feature
