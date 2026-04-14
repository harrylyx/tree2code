# PySpark Parity Report

- generated_at: 2026-04-14 20:25:03
- data_source: `test_data/all_data.pq`
- dedupe_key: `idx` (keep first)
- raw_rows: 3999950
- dedup_rows: 79999
- gold_standard: native LightGBM prediction
- spark_mode: `local[*]`
- score_params: base_score=600.0, pdo=50.0, base_odds=20.0, scale=3

## tree2code SQL vs Native (`score_p`)
- max_abs: 7.302870019265661e-07
- p99_abs: 3.384330379535562e-07
- mean_abs: 8.610898596096361e-08
- count_ge_1e_4: 0

## tree2code SQL vs Native (`score`)
- max_abs: 0.001000000000203727
- p99_abs: 0.00100000000009004
- mean_abs: 9.113863923294276e-05
- score_scale_mismatch: 7291

## treemodel2sql SQL vs Native (`score_p`)
- max_abs: 7.302870019265661e-07
- p99_abs: 3.384330379535562e-07
- mean_abs: 8.610898596096361e-08
- count_ge_1e_4: 0

## treemodel2sql SQL vs Native (`score`)
- max_abs: 0.001000000000203727
- p99_abs: 0.00100000000009004
- mean_abs: 9.113863923294276e-05
- score_scale_mismatch: 7291

## SQL Pair Comparison
- rows_treemodel2sql_worse_than_tree2code: 0
- rows_tree2code_worse_than_treemodel2sql: 0
- rows_equal_error: 79999

## Threshold Mismatch (0 vs 1e-13)
- common_trees: 200
- mismatch_tree_count: 90
- mismatch_total_count: 99
- mismatch_tree_indices: 0, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 16, 19, 20, 22, 24, 25, 26, 27, 28, 30, 31, 32, 33, 36, 37, 38, 40, 41, 42, 43, 47, 49, 53, 54, 56, 58, 60, 61, 63, 66, 68, 70, 75, 78, 79, 81, 82, 86, 88, 89, 90, 96, 97, 99, 105, 106, 108, 109, 111, 112, 116, 118, 119, 120, 121, 123, 128, 134, 135, 136, 140, 149, 150, 154, 159, 161, 162, 166, 170, 173, 174, 176, 177, 179, 182, 186, 187, 190

## Conclusion
- worse_sql_by_score_p_max_abs: tie
- worse_sql_by_score_scale_mismatch: tie
