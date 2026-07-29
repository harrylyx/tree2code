# Define base odds as negative-to-positive odds

`base_odds` means the negative-to-positive class odds `(1 - p) / p` at the base score, so a value of `100` represents 100:1. Every scoring output must apply this same public meaning and convert it consistently to the positive-to-negative odds used by the score formula; this avoids making callers reverse the value differently for Python and SQL.
