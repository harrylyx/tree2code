# Require only features used by model splits

Generated Python requires every feature referenced by at least one model split, reports absent keys as input errors, and ignores extra fields. Features that existed during training but never affect a split are not required, while explicitly supplied `None` or `NaN` values remain valid inputs governed by the source model's missing-value behavior.
