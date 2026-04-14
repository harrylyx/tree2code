# testdata Parity Report

- generated_at: 2026-04-14 20:30:02
- data_source: `test_data/all_data.pq`
- dedupe_key: `idx` (keep first)
- raw_rows: 3999950
- dedup_rows: 79999
- acceptance_score_p: no row with abs error >= 1e-4
- acceptance_score: exact match at configured score scale

## XGB Parity
- rows: 79999
- features: 267

### Python vs Native (`score_p`)
- max_abs: 5.960464477539062e-08
- p99_abs: 1.490116119384766e-08
- mean_abs: 1.748271486631302e-09
- count_ge_1e_4: 0
- count_ge_1e_6: 0

### Python vs Native (`score`)
- max_abs: 0.001000000000203727
- p99_abs: 0
- mean_abs: 1.662520781493193e-06
- count_ge_1e_4: 133
- count_ge_1e_6: 133
- score_scale_mismatch: 133

### SQL vs Native (`score_p`)
- max_abs: 8.896255487833571e-08
- p99_abs: 1.842312316424622e-08
- mean_abs: 2.584327756070586e-09
- count_ge_1e_4: 0
- count_ge_1e_6: 0

### SQL vs Native (`score`)
- max_abs: 0.001000000000203727
- p99_abs: 0
- mean_abs: 1.662520781493193e-06
- count_ge_1e_4: 133
- count_ge_1e_6: 133
- score_scale_mismatch: 133

## LGB Parity
- rows: 79999
- features: 168

### Python vs Native (`score_p`)
- max_abs: 0
- p99_abs: 0
- mean_abs: 0
- count_ge_1e_4: 0
- count_ge_1e_6: 0

### Python vs Native (`score`)
- max_abs: 0
- p99_abs: 0
- mean_abs: 0
- count_ge_1e_4: 0
- count_ge_1e_6: 0
- score_scale_mismatch: 0

### SQL vs Native (`score_p`)
- max_abs: 5.551115123125783e-16
- p99_abs: 3.05311331771918e-16
- mean_abs: 7.240147580011967e-17
- count_ge_1e_4: 0
- count_ge_1e_6: 0

### SQL vs Native (`score`)
- max_abs: 0
- p99_abs: 0
- mean_abs: 0
- count_ge_1e_4: 0
- count_ge_1e_6: 0
- score_scale_mismatch: 0

## LGB Stress Check (500 Trees, 16 Leaves)
- n_estimators: 500
- num_leaves: 16
- rows: 3000

### SQL vs Native (`score_p`)
- max_abs: 6.106226635438361e-16
- p99_abs: 3.33066907387547e-16
- mean_abs: 6.165128628964067e-17
- count_ge_1e_4: 0
- count_ge_1e_6: 0

### SQL vs Native (`score`)
- max_abs: 0
- p99_abs: 0
- mean_abs: 0
- count_ge_1e_4: 0
- count_ge_1e_6: 0
- score_scale_mismatch: 0

### Python vs Native (`score_p`)
- max_abs: 0
- p99_abs: 0
- mean_abs: 0
- count_ge_1e_4: 0
- count_ge_1e_6: 0

## tree2code vs treemodel2sql SQL Comparison
| backend | tree2code_len | treemodel2sql_len | normalized_equal | has_and_is_null_pattern |
|---|---:|---:|---|---|
| xgb | 370066 | 170561 | False | True |
| lgb | 135983 | 72826 | False | True |

- `normalized_equal` compares SQL strings after lowercasing and whitespace normalization only.

## Acceptance Summary
- XGB score_p criterion: True
- XGB score criterion: False
- LGB score_p criterion: True
- LGB score criterion: True
- LGB stress score_p criterion: True
- LGB stress score criterion: True
