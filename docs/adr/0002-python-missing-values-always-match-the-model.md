# Make Python missing-value behavior independent of compatibility mode

Generated Python must always reproduce the source model's handling of `None` and `NaN`. `compatible_mode` may remain available for SQL engines with different NaN capabilities, but it must not make Python probability parity optional.
