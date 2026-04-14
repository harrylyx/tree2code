# SQL Tree Value Diff Report

- sql_a: `docs/sql_compare/lgb_tree2code_hive.sql`
- sql_b: `docs/sql_compare/lgb_treemodel2sql.sql`
- name_a: `tree2code`
- name_b: `treemodel2sql`
- extract_mode_a: `margin`
- extract_mode_b: `alias`
- trees_a: `200`
- trees_b: `200`
- tokenizer_identifier_digit_guard_passed: `True`
- tokenizer_guard_tokens: `['3.5', '-0.1', '0']`
- threshold_mismatch_trees(0_vs_1e-13): `90`
- threshold_mismatch_total_count(0_vs_1e-13): `99`

## Tree Summary
| tree_index | status | a_tokens | b_tokens | a_only | b_only | approx_shared | threshold_mismatch |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 1 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 2 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 3 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 4 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 5 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 6 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 7 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 8 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 9 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 10 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 11 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 12 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 13 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 14 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 15 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 16 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 17 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 18 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 19 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 20 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 21 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 22 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 23 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 24 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 25 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 26 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 27 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 28 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 29 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 30 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 31 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 32 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 33 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 34 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 35 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 36 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 37 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 38 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 39 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 40 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 41 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 42 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 43 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 44 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 45 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 46 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 47 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 48 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 49 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 50 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 51 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 52 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 53 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 54 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 55 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 56 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 57 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 58 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 59 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 60 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 61 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 62 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 63 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 64 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 65 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 66 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 67 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 68 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 69 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 70 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 71 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 72 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 73 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 74 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 75 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 76 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 77 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 78 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 79 | present_in_both | 5 | 5 | 4 | 4 | 3 | 2 |
| 80 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 81 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 82 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 83 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 84 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 85 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 86 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 87 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 88 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 89 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 90 | present_in_both | 5 | 5 | 4 | 4 | 3 | 2 |
| 91 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 92 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 93 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 94 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 95 | present_in_both | 5 | 5 | 4 | 4 | 5 | 0 |
| 96 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 97 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 98 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 99 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 100 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 101 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 102 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 103 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 104 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 105 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 106 | present_in_both | 5 | 5 | 2 | 2 | 3 | 2 |
| 107 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 108 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 109 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 110 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 111 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 112 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 113 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 114 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 115 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 116 | present_in_both | 5 | 5 | 3 | 3 | 3 | 2 |
| 117 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 118 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 119 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 120 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 121 | present_in_both | 5 | 5 | 4 | 4 | 3 | 2 |
| 122 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 123 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 124 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 125 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 126 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 127 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 128 | present_in_both | 5 | 5 | 4 | 4 | 3 | 2 |
| 129 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 130 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 131 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 132 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 133 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 134 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 135 | present_in_both | 5 | 5 | 2 | 2 | 3 | 2 |
| 136 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 137 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 138 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 139 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 140 | present_in_both | 5 | 5 | 4 | 4 | 3 | 2 |
| 141 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 142 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 143 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 144 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 145 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 146 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 147 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 148 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 149 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 150 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 151 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 152 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 153 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 154 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 155 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 156 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 157 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 158 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 159 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 160 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 161 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 162 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 163 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 164 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 165 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 166 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 167 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 168 | present_in_both | 5 | 5 | 3 | 3 | 5 | 0 |
| 169 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 170 | present_in_both | 5 | 5 | 4 | 4 | 4 | 1 |
| 171 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 172 | present_in_both | 5 | 5 | 4 | 4 | 5 | 0 |
| 173 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 174 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 175 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 176 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 177 | present_in_both | 5 | 5 | 1 | 1 | 4 | 1 |
| 178 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 179 | present_in_both | 5 | 5 | 3 | 3 | 3 | 2 |
| 180 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 181 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 182 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 183 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 184 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 185 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 186 | present_in_both | 5 | 5 | 2 | 2 | 4 | 1 |
| 187 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 188 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 189 | present_in_both | 5 | 5 | 0 | 0 | 5 | 0 |
| 190 | present_in_both | 5 | 5 | 3 | 3 | 4 | 1 |
| 191 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 192 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 193 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 194 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |
| 195 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 196 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 197 | present_in_both | 5 | 5 | 1 | 1 | 5 | 0 |
| 198 | present_in_both | 5 | 5 | 4 | 4 | 5 | 0 |
| 199 | present_in_both | 5 | 5 | 2 | 2 | 5 | 0 |

## Threshold Mismatch Trees
- tree_indices: 0, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 16, 19, 20, 22, 24, 25, 26, 27, 28, 30, 31, 32, 33, 36, 37, 38, 40, 41, 42, 43, 47, 49, 53, 54, 56, 58, 60, 61, 63, 66, 68, 70, 75, 78, 79, 81, 82, 86, 88, 89, 90, 96, 97, 99, 105, 106, 108, 109, 111, 112, 116, 118, 119, 120, 121, 123, 128, 134, 135, 136, 140, 149, 150, 154, 159, 161, 162, 166, 170, 173, 174, 176, 177, 179, 182, 186, 187, 190

## Tree Details

### Tree 0 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-2.4628822481842358` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-2.462882248184236` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-2.4628822481842358` vs `-2.462882248184236` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 1 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0073109151833848987` x 1
- top_only_treemodel2sql:
  - `0.007310915183384899` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0073109151833848987` vs `0.007310915183384899` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 2 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.038499405054906399` x 1
- top_only_treemodel2sql:
  - `0.0384994050549064` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.038499405054906399` vs `0.0384994050549064` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 3 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.034415959832898392` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.03441595983289839` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.034415959832898392` vs `0.03441595983289839` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 4 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.054706905369382289` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.05470690536938229` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.054706905369382289` vs `0.05470690536938229` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 5 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.023666342845193498` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.0236663428451935` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.023666342845193498` vs `0.0236663428451935` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 6 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0056295611338307242` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.005629561133830724` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0056295611338307242` vs `0.005629561133830724` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 7 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 8 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 9 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 10 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `34.500000000000007` x 1
  - `0.0087501655617911664` x 1
- top_only_treemodel2sql:
  - `34.50000000000001` x 1
  - `0.008750165561791166` x 1
- close_pairs(abs_diff <= tolerance):
  - `34.500000000000007` vs `34.50000000000001` (diff=0, a=1, b=1)
  - `0.0087501655617911664` vs `0.008750165561791166` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 11 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.037058036909436987` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.03705803690943699` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.037058036909436987` vs `0.03705803690943699` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 12 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `9.5000000000000018` x 1
  - `-0.00048790121227694142` x 1
  - `0.027267082181530761` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `9.500000000000002` x 1
  - `-0.0004879012122769414` x 1
  - `0.02726708218153076` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `9.5000000000000018` vs `9.500000000000002` (diff=0, a=1, b=1)
  - `-0.00048790121227694142` vs `-0.0004879012122769414` (diff=0, a=1, b=1)
  - `0.027267082181530761` vs `0.02726708218153076` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 13 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `45.500000000000007` x 1
  - `1E-13` x 1
  - `0.0062776272833541761` x 1
- top_only_treemodel2sql:
  - `45.50000000000001` x 1
  - `0` x 1
  - `0.006277627283354176` x 1
- close_pairs(abs_diff <= tolerance):
  - `45.500000000000007` vs `45.50000000000001` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0062776272833541761` vs `0.006277627283354176` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 14 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.018931765659086799` x 1
  - `0.0060731731243174568` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.0189317656590868` x 1
  - `0.006073173124317457` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.018931765659086799` vs `-0.0189317656590868` (diff=0, a=1, b=1)
  - `0.0060731731243174568` vs `0.006073173124317457` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 15 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `-0.0088697465654303288` x 1
  - `1E-13` x 1
  - `0.033594426296331643` x 1
- top_only_treemodel2sql:
  - `-0.008869746565430329` x 1
  - `0` x 1
  - `0.03359442629633164` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0088697465654303288` vs `-0.008869746565430329` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.033594426296331643` vs `0.03359442629633164` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 16 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.016096192149103419` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.01609619214910342` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.016096192149103419` vs `-0.01609619214910342` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 17 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 18 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0075759086470408247` x 1
  - `0.0082561785275601547` x 1
  - `0.051749477183743411` x 1
- top_only_treemodel2sql:
  - `-0.007575908647040825` x 1
  - `0.008256178527560155` x 1
  - `0.05174947718374341` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0075759086470408247` vs `-0.007575908647040825` (diff=0, a=1, b=1)
  - `0.0082561785275601547` vs `0.008256178527560155` (diff=0, a=1, b=1)
  - `0.051749477183743411` vs `0.05174947718374341` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 19 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 20 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `-0.0087889265190990665` x 1
  - `1E-13` x 1
  - `0.027228186180819292` x 1
- top_only_treemodel2sql:
  - `-0.008788926519099067` x 1
  - `0` x 1
  - `0.02722818618081929` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0087889265190990665` vs `-0.008788926519099067` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.027228186180819292` vs `0.02722818618081929` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 21 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0090140018601388965` x 1
  - `-0.0024957638217521011` x 1
- top_only_treemodel2sql:
  - `-0.009014001860138897` x 1
  - `-0.002495763821752101` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0090140018601388965` vs `-0.009014001860138897` (diff=0, a=1, b=1)
  - `-0.0024957638217521011` vs `-0.002495763821752101` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 22 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 23 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.013748785406705131` x 1
  - `-0.0086646748833850411` x 1
- top_only_treemodel2sql:
  - `0.01374878540670513` x 1
  - `-0.008664674883385041` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.013748785406705131` vs `0.01374878540670513` (diff=0, a=1, b=1)
  - `-0.0086646748833850411` vs `-0.008664674883385041` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 24 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 25 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `7.5000000000000009` x 1
  - `-0.0051713018907514783` x 1
  - `0.015894101564951659` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `7.500000000000001` x 1
  - `-0.005171301890751478` x 1
  - `0.01589410156495166` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `7.5000000000000009` vs `7.500000000000001` (diff=0, a=1, b=1)
  - `-0.0051713018907514783` vs `-0.005171301890751478` (diff=0, a=1, b=1)
  - `0.015894101564951659` vs `0.01589410156495166` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 26 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0050753504748189109` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.005075350474818911` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0050753504748189109` vs `0.005075350474818911` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 27 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 28 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `6.5000000000000009` x 1
  - `-0.0048557271896470158` x 1
  - `-0.014014976044327219` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `6.500000000000001` x 1
  - `-0.004855727189647016` x 1
  - `-0.01401497604432722` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `6.5000000000000009` vs `6.500000000000001` (diff=0, a=1, b=1)
  - `-0.0048557271896470158` vs `-0.004855727189647016` (diff=0, a=1, b=1)
  - `-0.014014976044327219` vs `-0.01401497604432722` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 29 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `32.500000000000007` x 1
  - `0.0099557344618717708` x 1
- top_only_treemodel2sql:
  - `32.50000000000001` x 1
  - `0.00995573446187177` x 1
- close_pairs(abs_diff <= tolerance):
  - `32.500000000000007` vs `32.50000000000001` (diff=0, a=1, b=1)
  - `0.0099557344618717708` vs `0.00995573446187177` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 30 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.015014600325827561` x 1
  - `-0.0071724524063081817` x 1
  - `-0.011831776837191801` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.01501460032582756` x 1
  - `-0.007172452406308182` x 1
  - `-0.0118317768371918` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.015014600325827561` vs `0.01501460032582756` (diff=0, a=1, b=1)
  - `-0.0071724524063081817` vs `-0.007172452406308182` (diff=0, a=1, b=1)
  - `-0.011831776837191801` vs `-0.0118317768371918` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 31 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0076435929469874852` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.007643592946987485` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0076435929469874852` vs `0.007643592946987485` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 32 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0096593385794973789` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.009659338579497379` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0096593385794973789` vs `0.009659338579497379` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 33 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0088475114618395256` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.008847511461839526` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0088475114618395256` vs `0.008847511461839526` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 34 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 35 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0074288607748409889` x 1
  - `5.5000000000000009` x 1
- top_only_treemodel2sql:
  - `-0.007428860774840989` x 1
  - `5.500000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0074288607748409889` vs `-0.007428860774840989` (diff=0, a=1, b=1)
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 36 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.0093567938079617257` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.009356793807961726` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.0093567938079617257` vs `-0.009356793807961726` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 37 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.0067703400520713669` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.006770340052071367` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.0067703400520713669` vs `-0.006770340052071367` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 38 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `7.5000000000000009` x 1
  - `-0.016676400807535061` x 1
  - `0.0027027831704477799` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `7.500000000000001` x 1
  - `-0.01667640080753506` x 1
  - `0.00270278317044778` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `7.5000000000000009` vs `7.500000000000001` (diff=0, a=1, b=1)
  - `-0.016676400807535061` vs `-0.01667640080753506` (diff=0, a=1, b=1)
  - `0.0027027831704477799` vs `0.00270278317044778` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 39 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0088372764802229185` x 1
- top_only_treemodel2sql:
  - `0.008837276480222919` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0088372764802229185` vs `0.008837276480222919` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 40 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.019070801097472521` x 1
  - `0.00082462580167543638` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.01907080109747252` x 1
  - `0.0008246258016754364` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.019070801097472521` vs `-0.01907080109747252` (diff=0, a=1, b=1)
  - `0.00082462580167543638` vs `0.0008246258016754364` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 41 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0079515873563552903` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.00795158735635529` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0079515873563552903` vs `0.00795158735635529` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 42 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0083854609255509839` x 1
  - `-0.030256358886643148` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.008385460925550984` x 1
  - `-0.03025635888664315` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0083854609255509839` vs `0.008385460925550984` (diff=0, a=1, b=1)
  - `-0.030256358886643148` vs `-0.03025635888664315` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 43 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `5.5000000000000009` x 1
  - `1E-13` x 1
  - `0.0044956900812135187` x 1
  - `0.031550880606673173` x 1
- top_only_treemodel2sql:
  - `5.500000000000001` x 1
  - `0` x 1
  - `0.004495690081213519` x 1
  - `0.03155088060667317` x 1
- close_pairs(abs_diff <= tolerance):
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0044956900812135187` vs `0.004495690081213519` (diff=0, a=1, b=1)
  - `0.031550880606673173` vs `0.03155088060667317` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 44 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.020230109965988358` x 1
- top_only_treemodel2sql:
  - `-0.02023010996598836` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.020230109965988358` vs `-0.02023010996598836` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 45 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `45.500000000000007` x 1
  - `0.0055541929743736229` x 1
- top_only_treemodel2sql:
  - `45.50000000000001` x 1
  - `0.005554192974373623` x 1
- close_pairs(abs_diff <= tolerance):
  - `45.500000000000007` vs `45.50000000000001` (diff=0, a=1, b=1)
  - `0.0055541929743736229` vs `0.005554192974373623` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 46 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0091301662121777288` x 1
  - `-0.0078249543168390553` x 1
- top_only_treemodel2sql:
  - `0.009130166212177729` x 1
  - `-0.007824954316839055` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0091301662121777288` vs `0.009130166212177729` (diff=0, a=1, b=1)
  - `-0.0078249543168390553` vs `-0.007824954316839055` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 47 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.019539005440341518` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.01953900544034152` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.019539005440341518` vs `-0.01953900544034152` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 48 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.021469775568127791` x 1
  - `-0.00025789681689403161` x 1
- top_only_treemodel2sql:
  - `-0.02146977556812779` x 1
  - `-0.0002578968168940316` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.021469775568127791` vs `-0.02146977556812779` (diff=0, a=1, b=1)
  - `-0.00025789681689403161` vs `-0.0002578968168940316` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 49 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0098416305390266259` x 1
  - `0.00066208709781991114` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.009841630539026626` x 1
  - `0.0006620870978199111` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0098416305390266259` vs `0.009841630539026626` (diff=0, a=1, b=1)
  - `0.00066208709781991114` vs `0.0006620870978199111` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 50 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 51 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0085637261217881341` x 1
- top_only_treemodel2sql:
  - `0.008563726121788134` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0085637261217881341` vs `0.008563726121788134` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 52 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0087333344532606796` x 1
- top_only_treemodel2sql:
  - `0.00873333445326068` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0087333344532606796` vs `0.00873333445326068` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 53 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.0088373386688814209` x 1
  - `0.0084727734914154442` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.008837338668881421` x 1
  - `0.008472773491415444` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.0088373386688814209` vs `-0.008837338668881421` (diff=0, a=1, b=1)
  - `0.0084727734914154442` vs `0.008472773491415444` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 54 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.0026563788068411438` x 1
  - `-0.018744238813878641` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.002656378806841144` x 1
  - `-0.01874423881387864` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.0026563788068411438` vs `-0.002656378806841144` (diff=0, a=1, b=1)
  - `-0.018744238813878641` vs `-0.01874423881387864` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 55 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `65.500000000000014` x 1
- top_only_treemodel2sql:
  - `65.50000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `65.500000000000014` vs `65.50000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 56 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 57 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0079557729415166405` x 1
  - `-0.0070039651686499603` x 1
- top_only_treemodel2sql:
  - `0.00795577294151664` x 1
  - `-0.00700396516864996` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0079557729415166405` vs `0.00795577294151664` (diff=0, a=1, b=1)
  - `-0.0070039651686499603` vs `-0.00700396516864996` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 58 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0083536624850551675` x 1
  - `-0.0064573759889835231` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.008353662485055167` x 1
  - `-0.006457375988983523` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0083536624850551675` vs `0.008353662485055167` (diff=0, a=1, b=1)
  - `-0.0064573759889835231` vs `-0.006457375988983523` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 59 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.019975652151133921` x 1
- top_only_treemodel2sql:
  - `-0.01997565215113392` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.019975652151133921` vs `-0.01997565215113392` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 60 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0076774065818251414` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.007677406581825141` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0076774065818251414` vs `0.007677406581825141` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 61 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0088159391541196164` x 1
  - `7.5000000000000009` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.008815939154119616` x 1
  - `7.500000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0088159391541196164` vs `0.008815939154119616` (diff=0, a=1, b=1)
  - `7.5000000000000009` vs `7.500000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 62 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0076755064526000524` x 1
  - `-0.0068997720510901696` x 1
- top_only_treemodel2sql:
  - `0.007675506452600052` x 1
  - `-0.00689977205109017` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0076755064526000524` vs `0.007675506452600052` (diff=0, a=1, b=1)
  - `-0.0068997720510901696` vs `-0.00689977205109017` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 63 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0067658180770385342` x 1
  - `-0.0076426847520855079` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.006765818077038534` x 1
  - `-0.007642684752085508` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0067658180770385342` vs `0.006765818077038534` (diff=0, a=1, b=1)
  - `-0.0076426847520855079` vs `-0.007642684752085508` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 64 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 65 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.017463820905455351` x 1
- top_only_treemodel2sql:
  - `-0.01746382090545535` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.017463820905455351` vs `-0.01746382090545535` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 66 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `5.5000000000000009` x 1
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `5.500000000000001` x 1
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 67 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0024410072650946418` x 1
- top_only_treemodel2sql:
  - `-0.002441007265094642` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0024410072650946418` vs `-0.002441007265094642` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 68 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0064462434683737763` x 1
  - `-0.0070955724637126634` x 1
  - `-0.029249166727213879` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.006446243468373776` x 1
  - `-0.007095572463712663` x 1
  - `-0.02924916672721388` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0064462434683737763` vs `0.006446243468373776` (diff=0, a=1, b=1)
  - `-0.0070955724637126634` vs `-0.007095572463712663` (diff=0, a=1, b=1)
  - `-0.029249166727213879` vs `-0.02924916672721388` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 69 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.025692281766151029` x 1
- top_only_treemodel2sql:
  - `0.02569228176615103` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.025692281766151029` vs `0.02569228176615103` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 70 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0089395624764591029` x 1
  - `0.00062923804046889241` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.008939562476459103` x 1
  - `0.0006292380404688924` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0089395624764591029` vs `0.008939562476459103` (diff=0, a=1, b=1)
  - `0.00062923804046889241` vs `0.0006292380404688924` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 71 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0058301358232116032` x 1
  - `0.0076012770616142658` x 1
- top_only_treemodel2sql:
  - `-0.005830135823211603` x 1
  - `0.007601277061614266` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0058301358232116032` vs `-0.005830135823211603` (diff=0, a=1, b=1)
  - `0.0076012770616142658` vs `0.007601277061614266` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 72 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0041516056357307589` x 1
  - `0.0090369802908066964` x 1
  - `-0.017714935763963689` x 1
- top_only_treemodel2sql:
  - `-0.004151605635730759` x 1
  - `0.009036980290806696` x 1
  - `-0.01771493576396369` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0041516056357307589` vs `-0.004151605635730759` (diff=0, a=1, b=1)
  - `0.0090369802908066964` vs `0.009036980290806696` (diff=0, a=1, b=1)
  - `-0.017714935763963689` vs `-0.01771493576396369` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 73 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 74 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0058446572066255956` x 1
  - `-0.0093022531698549061` x 1
- top_only_treemodel2sql:
  - `0.005844657206625596` x 1
  - `-0.009302253169854906` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0058446572066255956` vs `0.005844657206625596` (diff=0, a=1, b=1)
  - `-0.0093022531698549061` vs `-0.009302253169854906` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 75 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0072732431879966881` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.007273243187996688` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0072732431879966881` vs `0.007273243187996688` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 76 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0081112431267463311` x 1
- top_only_treemodel2sql:
  - `0.008111243126746331` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0081112431267463311` vs `0.008111243126746331` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 77 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `5.5000000000000009` x 1
  - `0.0015488657127521179` x 1
- top_only_treemodel2sql:
  - `5.500000000000001` x 1
  - `0.001548865712752118` x 1
- close_pairs(abs_diff <= tolerance):
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `0.0015488657127521179` vs `0.001548865712752118` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 78 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0065400537862560773` x 1
  - `-0.0059009293359204278` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.006540053786256077` x 1
  - `-0.005900929335920428` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0065400537862560773` vs `0.006540053786256077` (diff=0, a=1, b=1)
  - `-0.0059009293359204278` vs `-0.005900929335920428` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 79 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
  - `0.0091791684346042204` x 1
  - `-0.0032213993876063331` x 1
- top_only_treemodel2sql:
  - `0` x 2
  - `0.00917916843460422` x 1
  - `-0.003221399387606333` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
  - `0.0091791684346042204` vs `0.00917916843460422` (diff=0, a=1, b=1)
  - `-0.0032213993876063331` vs `-0.003221399387606333` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 80 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0026419751242369831` x 1
  - `0.023611306684714461` x 1
- top_only_treemodel2sql:
  - `-0.002641975124236983` x 1
  - `0.02361130668471446` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0026419751242369831` vs `-0.002641975124236983` (diff=0, a=1, b=1)
  - `0.023611306684714461` vs `0.02361130668471446` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 81 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 82 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.0018516216784246261` x 1
  - `0.0081009938816987651` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.001851621678424626` x 1
  - `0.008100993881698765` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.0018516216784246261` vs `-0.001851621678424626` (diff=0, a=1, b=1)
  - `0.0081009938816987651` vs `0.008100993881698765` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 83 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0077876880179024227` x 1
  - `-0.0081253659919799572` x 1
- top_only_treemodel2sql:
  - `0.007787688017902423` x 1
  - `-0.008125365991979957` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0077876880179024227` vs `0.007787688017902423` (diff=0, a=1, b=1)
  - `-0.0081253659919799572` vs `-0.008125365991979957` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 84 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0059842166591075469` x 1
  - `82.500000000000014` x 1
- top_only_treemodel2sql:
  - `-0.005984216659107547` x 1
  - `82.50000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0059842166591075469` vs `-0.005984216659107547` (diff=0, a=1, b=1)
  - `82.500000000000014` vs `82.50000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 85 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `46.500000000000007` x 1
  - `0.0052218252693657522` x 1
  - `-0.0078922559035768305` x 1
- top_only_treemodel2sql:
  - `46.50000000000001` x 1
  - `0.005221825269365752` x 1
  - `-0.00789225590357683` x 1
- close_pairs(abs_diff <= tolerance):
  - `46.500000000000007` vs `46.50000000000001` (diff=0, a=1, b=1)
  - `0.0052218252693657522` vs `0.005221825269365752` (diff=0, a=1, b=1)
  - `-0.0078922559035768305` vs `-0.00789225590357683` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 86 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0071935442714035043` x 1
  - `39.500000000000007` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.007193544271403504` x 1
  - `39.50000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0071935442714035043` vs `0.007193544271403504` (diff=0, a=1, b=1)
  - `39.500000000000007` vs `39.50000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 87 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 88 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.032991998242846231` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.03299199824284623` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.032991998242846231` vs `-0.03299199824284623` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 89 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `5.5000000000000009` x 1
  - `-0.00036919539318756687` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `5.500000000000001` x 1
  - `-0.0003691953931875669` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `-0.00036919539318756687` vs `-0.0003691953931875669` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 90 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
  - `0.0035987120758263409` x 1
  - `-0.031267159733482451` x 1
- top_only_treemodel2sql:
  - `0` x 2
  - `0.003598712075826341` x 1
  - `-0.03126715973348245` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
  - `0.0035987120758263409` vs `0.003598712075826341` (diff=0, a=1, b=1)
  - `-0.031267159733482451` vs `-0.03126715973348245` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 91 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 92 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0091378291836960168` x 1
  - `0.0068694101508815497` x 1
  - `-0.0080076753132772068` x 1
- top_only_treemodel2sql:
  - `-0.009137829183696017` x 1
  - `0.00686941015088155` x 1
  - `-0.008007675313277207` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0091378291836960168` vs `-0.009137829183696017` (diff=0, a=1, b=1)
  - `0.0068694101508815497` vs `0.00686941015088155` (diff=0, a=1, b=1)
  - `-0.0080076753132772068` vs `-0.008007675313277207` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 93 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0071928856752750264` x 1
- top_only_treemodel2sql:
  - `-0.007192885675275026` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0071928856752750264` vs `-0.007192885675275026` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 94 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `96.500000000000014` x 1
  - `0.035368349466279127` x 1
- top_only_treemodel2sql:
  - `96.50000000000001` x 1
  - `0.03536834946627913` x 1
- close_pairs(abs_diff <= tolerance):
  - `96.500000000000014` vs `96.50000000000001` (diff=0, a=1, b=1)
  - `0.035368349466279127` vs `0.03536834946627913` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 95 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0055812060701325144` x 1
  - `87.500000000000014` x 1
  - `0.013490717635320729` x 1
  - `-0.0045648555476758583` x 1
- top_only_treemodel2sql:
  - `-0.005581206070132514` x 1
  - `87.50000000000001` x 1
  - `0.01349071763532073` x 1
  - `-0.004564855547675858` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0055812060701325144` vs `-0.005581206070132514` (diff=0, a=1, b=1)
  - `87.500000000000014` vs `87.50000000000001` (diff=0, a=1, b=1)
  - `0.013490717635320729` vs `0.01349071763532073` (diff=0, a=1, b=1)
  - `-0.0045648555476758583` vs `-0.004564855547675858` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 96 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.0062361209862123604` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.00623612098621236` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.0062361209862123604` vs `-0.00623612098621236` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 97 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0097764639293613839` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.009776463929361384` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0097764639293613839` vs `0.009776463929361384` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 98 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.00036073772913034152` x 1
- top_only_treemodel2sql:
  - `0.0003607377291303415` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.00036073772913034152` vs `0.0003607377291303415` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 99 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0065817256383438579` x 1
  - `0.00062215626769995412` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.006581725638343858` x 1
  - `0.0006221562676999541` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0065817256383438579` vs `0.006581725638343858` (diff=0, a=1, b=1)
  - `0.00062215626769995412` vs `0.0006221562676999541` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 100 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.011921103204623071` x 1
  - `0.0050863612845005179` x 1
  - `-0.0082268888809492891` x 1
- top_only_treemodel2sql:
  - `-0.01192110320462307` x 1
  - `0.005086361284500518` x 1
  - `-0.008226888880949289` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.011921103204623071` vs `-0.01192110320462307` (diff=0, a=1, b=1)
  - `0.0050863612845005179` vs `0.005086361284500518` (diff=0, a=1, b=1)
  - `-0.0082268888809492891` vs `-0.008226888880949289` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 101 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `65.500000000000014` x 1
  - `0.0090408201715821337` x 1
- top_only_treemodel2sql:
  - `65.50000000000001` x 1
  - `0.009040820171582134` x 1
- close_pairs(abs_diff <= tolerance):
  - `65.500000000000014` vs `65.50000000000001` (diff=0, a=1, b=1)
  - `0.0090408201715821337` vs `0.009040820171582134` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 102 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.017865119595041581` x 1
- top_only_treemodel2sql:
  - `0.01786511959504158` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.017865119595041581` vs `0.01786511959504158` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 103 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0032741767425172371` x 1
  - `-0.0076982372682245261` x 1
  - `0.033184163684634727` x 1
- top_only_treemodel2sql:
  - `0.003274176742517237` x 1
  - `-0.007698237268224526` x 1
  - `0.03318416368463473` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0032741767425172371` vs `0.003274176742517237` (diff=0, a=1, b=1)
  - `-0.0076982372682245261` vs `-0.007698237268224526` (diff=0, a=1, b=1)
  - `0.033184163684634727` vs `0.03318416368463473` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 104 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0067845930587170644` x 1
- top_only_treemodel2sql:
  - `0.006784593058717064` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0067845930587170644` vs `0.006784593058717064` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 105 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0026010922654924919` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.002601092265492492` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0026010922654924919` vs `0.002601092265492492` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 106 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
- top_only_treemodel2sql:
  - `0` x 2
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 107 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0063241196962790002` x 1
  - `-0.015789830898154569` x 1
- top_only_treemodel2sql:
  - `-0.006324119696279` x 1
  - `-0.01578983089815457` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0063241196962790002` vs `-0.006324119696279` (diff=0, a=1, b=1)
  - `-0.015789830898154569` vs `-0.01578983089815457` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 108 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0062917444325520716` x 1
  - `0.00051046088803626281` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.006291744432552072` x 1
  - `0.0005104608880362628` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0062917444325520716` vs `0.006291744432552072` (diff=0, a=1, b=1)
  - `0.00051046088803626281` vs `0.0005104608880362628` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 109 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0047485458976660247` x 1
  - `-0.0063380930518059488` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.004748545897666025` x 1
  - `-0.006338093051805949` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0047485458976660247` vs `0.004748545897666025` (diff=0, a=1, b=1)
  - `-0.0063380930518059488` vs `-0.006338093051805949` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 110 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.000094326104411988066` x 1
- top_only_treemodel2sql:
  - `-0.00009432610441198807` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.000094326104411988066` vs `-0.00009432610441198807` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 111 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `34.500000000000007` x 1
  - `-0.0064517115270028283` x 1
  - `0.0073490035914934833` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `34.50000000000001` x 1
  - `-0.006451711527002828` x 1
  - `0.007349003591493483` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `34.500000000000007` vs `34.50000000000001` (diff=0, a=1, b=1)
  - `-0.0064517115270028283` vs `-0.006451711527002828` (diff=0, a=1, b=1)
  - `0.0073490035914934833` vs `0.007349003591493483` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 112 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `5.5000000000000009` x 1
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `5.500000000000001` x 1
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 113 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `75.500000000000014` x 1
  - `0.0045942511385497174` x 1
  - `-0.0061444072001339417` x 1
- top_only_treemodel2sql:
  - `75.50000000000001` x 1
  - `0.004594251138549717` x 1
  - `-0.006144407200133942` x 1
- close_pairs(abs_diff <= tolerance):
  - `75.500000000000014` vs `75.50000000000001` (diff=0, a=1, b=1)
  - `0.0045942511385497174` vs `0.004594251138549717` (diff=0, a=1, b=1)
  - `-0.0061444072001339417` vs `-0.006144407200133942` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 114 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0068081548467824023` x 1
  - `0.0045723950327347411` x 1
- top_only_treemodel2sql:
  - `-0.006808154846782402` x 1
  - `0.004572395032734741` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0068081548467824023` vs `-0.006808154846782402` (diff=0, a=1, b=1)
  - `0.0045723950327347411` vs `0.004572395032734741` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 115 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4.5000000000000009` x 1
  - `40.500000000000007` x 1
  - `-0.023858550925708211` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
  - `40.50000000000001` x 1
  - `-0.02385855092570821` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `40.500000000000007` vs `40.50000000000001` (diff=0, a=1, b=1)
  - `-0.023858550925708211` vs `-0.02385855092570821` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 116 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
  - `-0.00050713573413819991` x 1
- top_only_treemodel2sql:
  - `0` x 2
  - `-0.0005071357341381999` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
  - `-0.00050713573413819991` vs `-0.0005071357341381999` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 117 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `44.500000000000007` x 1
  - `0.0059577034485222167` x 1
- top_only_treemodel2sql:
  - `44.50000000000001` x 1
  - `0.005957703448522217` x 1
- close_pairs(abs_diff <= tolerance):
  - `44.500000000000007` vs `44.50000000000001` (diff=0, a=1, b=1)
  - `0.0059577034485222167` vs `0.005957703448522217` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 118 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `4.5000000000000009` x 1
  - `0.00071456118504376813` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `4.500000000000001` x 1
  - `0.0007145611850437681` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `0.00071456118504376813` vs `0.0007145611850437681` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 119 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `4.5000000000000009` x 1
  - `1E-13` x 1
  - `-0.023757918256384718` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
  - `0` x 1
  - `-0.02375791825638472` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.023757918256384718` vs `-0.02375791825638472` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 120 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `8.5000000000000018` x 1
  - `0.0020258916904842559` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `8.500000000000002` x 1
  - `0.002025891690484256` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `8.5000000000000018` vs `8.500000000000002` (diff=0, a=1, b=1)
  - `0.0020258916904842559` vs `0.002025891690484256` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 121 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
  - `0.0046464508274316101` x 1
  - `-0.0055377765116291864` x 1
- top_only_treemodel2sql:
  - `0` x 2
  - `0.00464645082743161` x 1
  - `-0.005537776511629186` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
  - `0.0046464508274316101` vs `0.00464645082743161` (diff=0, a=1, b=1)
  - `-0.0055377765116291864` vs `-0.005537776511629186` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 122 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.00022618999187618349` x 1
  - `0.021106220837556679` x 1
  - `-0.013466562625759499` x 1
- top_only_treemodel2sql:
  - `0.0002261899918761835` x 1
  - `0.02110622083755668` x 1
  - `-0.0134665626257595` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.00022618999187618349` vs `0.0002261899918761835` (diff=0, a=1, b=1)
  - `0.021106220837556679` vs `0.02110622083755668` (diff=0, a=1, b=1)
  - `-0.013466562625759499` vs `-0.0134665626257595` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 123 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.0054136881714771526` x 1
  - `-0.022589815344294391` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.005413688171477153` x 1
  - `-0.02258981534429439` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.0054136881714771526` vs `-0.005413688171477153` (diff=0, a=1, b=1)
  - `-0.022589815344294391` vs `-0.02258981534429439` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 124 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0099032819963762939` x 1
- top_only_treemodel2sql:
  - `0.009903281996376294` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0099032819963762939` vs `0.009903281996376294` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 125 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0062948049697502638` x 1
  - `0.044555787144565678` x 1
  - `0.0041493855572431954` x 1
- top_only_treemodel2sql:
  - `-0.006294804969750264` x 1
  - `0.04455578714456568` x 1
  - `0.004149385557243195` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0062948049697502638` vs `-0.006294804969750264` (diff=0, a=1, b=1)
  - `0.044555787144565678` vs `0.04455578714456568` (diff=0, a=1, b=1)
  - `0.0041493855572431954` vs `0.004149385557243195` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 126 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `44.500000000000007` x 1
  - `0.0057914500722230861` x 1
- top_only_treemodel2sql:
  - `44.50000000000001` x 1
  - `0.005791450072223086` x 1
- close_pairs(abs_diff <= tolerance):
  - `44.500000000000007` vs `44.50000000000001` (diff=0, a=1, b=1)
  - `0.0057914500722230861` vs `0.005791450072223086` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 127 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `83.500000000000014` x 1
  - `-0.0071016514253969473` x 1
  - `-0.0087458931610403367` x 1
- top_only_treemodel2sql:
  - `83.50000000000001` x 1
  - `-0.007101651425396947` x 1
  - `-0.008745893161040337` x 1
- close_pairs(abs_diff <= tolerance):
  - `83.500000000000014` vs `83.50000000000001` (diff=0, a=1, b=1)
  - `-0.0071016514253969473` vs `-0.007101651425396947` (diff=0, a=1, b=1)
  - `-0.0087458931610403367` vs `-0.008745893161040337` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 128 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
  - `-0.015928615310698651` x 1
  - `0.0062171465686190232` x 1
- top_only_treemodel2sql:
  - `0` x 2
  - `-0.01592861531069865` x 1
  - `0.006217146568619023` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
  - `-0.015928615310698651` vs `-0.01592861531069865` (diff=0, a=1, b=1)
  - `0.0062171465686190232` vs `0.006217146568619023` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 129 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 130 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `46.500000000000007` x 1
  - `0.0051625787378938711` x 1
  - `-0.0046384979171851751` x 1
- top_only_treemodel2sql:
  - `46.50000000000001` x 1
  - `0.005162578737893871` x 1
  - `-0.004638497917185175` x 1
- close_pairs(abs_diff <= tolerance):
  - `46.500000000000007` vs `46.50000000000001` (diff=0, a=1, b=1)
  - `0.0051625787378938711` vs `0.005162578737893871` (diff=0, a=1, b=1)
  - `-0.0046384979171851751` vs `-0.004638497917185175` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 131 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `528.50000000000011` x 1
  - `53.500000000000007` x 1
  - `0.0045191934514959677` x 1
- top_only_treemodel2sql:
  - `528.5000000000001` x 1
  - `53.50000000000001` x 1
  - `0.004519193451495968` x 1
- close_pairs(abs_diff <= tolerance):
  - `528.50000000000011` vs `528.5000000000001` (diff=0, a=1, b=1)
  - `53.500000000000007` vs `53.50000000000001` (diff=0, a=1, b=1)
  - `0.0045191934514959677` vs `0.004519193451495968` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 132 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 133 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4.5000000000000009` x 1
  - `-0.0042492021976995708` x 1
  - `0.0045941917009074927` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
  - `-0.004249202197699571` x 1
  - `0.004594191700907493` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `-0.0042492021976995708` vs `-0.004249202197699571` (diff=0, a=1, b=1)
  - `0.0045941917009074927` vs `0.004594191700907493` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 134 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `4.5000000000000009` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `4.500000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 135 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
- top_only_treemodel2sql:
  - `0` x 2
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 136 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `8.5000000000000018` x 1
  - `0.0020543344721166258` x 1
  - `-0.0028432735702687431` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `8.500000000000002` x 1
  - `0.002054334472116626` x 1
  - `-0.002843273570268743` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `8.5000000000000018` vs `8.500000000000002` (diff=0, a=1, b=1)
  - `0.0020543344721166258` vs `0.002054334472116626` (diff=0, a=1, b=1)
  - `-0.0028432735702687431` vs `-0.002843273570268743` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 137 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0021630491332428662` x 1
- top_only_treemodel2sql:
  - `0.002163049133242866` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0021630491332428662` vs `0.002163049133242866` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 138 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4.5000000000000009` x 1
  - `-0.022451707849546199` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
  - `-0.0224517078495462` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `-0.022451707849546199` vs `-0.0224517078495462` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 139 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 140 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
  - `-0.00063649844233996467` x 1
  - `0.0057162122803048002` x 1
- top_only_treemodel2sql:
  - `0` x 2
  - `-0.0006364984423399647` x 1
  - `0.0057162122803048` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
  - `-0.00063649844233996467` vs `-0.0006364984423399647` (diff=0, a=1, b=1)
  - `0.0057162122803048002` vs `0.0057162122803048` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 141 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0062399476316512686` x 1
  - `0.038118578677572089` x 1
- top_only_treemodel2sql:
  - `-0.006239947631651269` x 1
  - `0.03811857867757209` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0062399476316512686` vs `-0.006239947631651269` (diff=0, a=1, b=1)
  - `0.038118578677572089` vs `0.03811857867757209` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 142 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `5.5000000000000009` x 1
  - `-0.0056297965770866227` x 1
  - `0.031523777166612227` x 1
- top_only_treemodel2sql:
  - `5.500000000000001` x 1
  - `-0.005629796577086623` x 1
  - `0.03152377716661223` x 1
- close_pairs(abs_diff <= tolerance):
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `-0.0056297965770866227` vs `-0.005629796577086623` (diff=0, a=1, b=1)
  - `0.031523777166612227` vs `0.03152377716661223` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 143 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `5.5000000000000009` x 1
  - `-0.0012766497571899519` x 1
  - `33.500000000000007` x 1
- top_only_treemodel2sql:
  - `5.500000000000001` x 1
  - `-0.001276649757189952` x 1
  - `33.50000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `-0.0012766497571899519` vs `-0.001276649757189952` (diff=0, a=1, b=1)
  - `33.500000000000007` vs `33.50000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 144 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4409.5000000000009` x 1
  - `0.0077359041129074577` x 1
- top_only_treemodel2sql:
  - `4409.500000000001` x 1
  - `0.007735904112907458` x 1
- close_pairs(abs_diff <= tolerance):
  - `4409.5000000000009` vs `4409.500000000001` (diff=0, a=1, b=1)
  - `0.0077359041129074577` vs `0.007735904112907458` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 145 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0012836480479917489` x 1
- top_only_treemodel2sql:
  - `0.001283648047991749` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0012836480479917489` vs `0.001283648047991749` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 146 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `57.500000000000007` x 1
- top_only_treemodel2sql:
  - `57.50000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `57.500000000000007` vs `57.50000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 147 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0025734802661918931` x 1
- top_only_treemodel2sql:
  - `0.002573480266191893` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0025734802661918931` vs `0.002573480266191893` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 148 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0043782225086474212` x 1
- top_only_treemodel2sql:
  - `-0.004378222508647421` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0043782225086474212` vs `-0.004378222508647421` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 149 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 150 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 151 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.080396157135723026` x 1
- top_only_treemodel2sql:
  - `0.08039615713572303` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.080396157135723026` vs `0.08039615713572303` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 152 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4.5000000000000009` x 1
  - `-0.0049623153195366282` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
  - `-0.004962315319536628` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `-0.0049623153195366282` vs `-0.004962315319536628` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 153 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0063110675631637969` x 1
- top_only_treemodel2sql:
  - `-0.006311067563163797` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0063110675631637969` vs `-0.006311067563163797` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 154 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 155 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `57.500000000000007` x 1
  - `-0.0091650330279537465` x 1
- top_only_treemodel2sql:
  - `57.50000000000001` x 1
  - `-0.009165033027953746` x 1
- close_pairs(abs_diff <= tolerance):
  - `57.500000000000007` vs `57.50000000000001` (diff=0, a=1, b=1)
  - `-0.0091650330279537465` vs `-0.009165033027953746` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 156 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0093438263394334392` x 1
- top_only_treemodel2sql:
  - `-0.00934382633943344` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0093438263394334392` vs `-0.00934382633943344` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 157 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4.5000000000000009` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 158 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0096134482666225887` x 1
- top_only_treemodel2sql:
  - `-0.009613448266622589` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0096134482666225887` vs `-0.009613448266622589` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 159 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `6.5000000000000009` x 1
  - `0.0072410570640366913` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `6.500000000000001` x 1
  - `0.007241057064036691` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `6.5000000000000009` vs `6.500000000000001` (diff=0, a=1, b=1)
  - `0.0072410570640366913` vs `0.007241057064036691` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 160 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0026172873523970701` x 1
  - `-0.0015279116896172839` x 1
- top_only_treemodel2sql:
  - `-0.00261728735239707` x 1
  - `-0.001527911689617284` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0026172873523970701` vs `-0.00261728735239707` (diff=0, a=1, b=1)
  - `-0.0015279116896172839` vs `-0.001527911689617284` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 161 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `4.5000000000000009` x 1
  - `1E-13` x 1
  - `0.0061577217998026387` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
  - `0` x 1
  - `0.006157721799802639` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0061577217998026387` vs `0.006157721799802639` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 162 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.020327933625446559` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.02032793362544656` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.020327933625446559` vs `-0.02032793362544656` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 163 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 164 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0094828698888913265` x 1
- top_only_treemodel2sql:
  - `0.009482869888891327` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0094828698888913265` vs `0.009482869888891327` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 165 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0067975429395147257` x 1
  - `0.036922603767843697` x 1
- top_only_treemodel2sql:
  - `-0.006797542939514726` x 1
  - `0.0369226037678437` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0067975429395147257` vs `-0.006797542939514726` (diff=0, a=1, b=1)
  - `0.036922603767843697` vs `0.0369226037678437` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 166 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `5.5000000000000009` x 1
  - `0.018412327014905971` x 1
  - `-0.0023812035540704221` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `5.500000000000001` x 1
  - `0.01841232701490597` x 1
  - `-0.002381203554070422` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `0.018412327014905971` vs `0.01841232701490597` (diff=0, a=1, b=1)
  - `-0.0023812035540704221` vs `-0.002381203554070422` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 167 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.014804709501878611` x 1
- top_only_treemodel2sql:
  - `-0.01480470950187861` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.014804709501878611` vs `-0.01480470950187861` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 168 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `81.500000000000014` x 1
  - `0.0030875004591237338` x 1
  - `-0.0064805465637732627` x 1
- top_only_treemodel2sql:
  - `81.50000000000001` x 1
  - `0.003087500459123734` x 1
  - `-0.006480546563773263` x 1
- close_pairs(abs_diff <= tolerance):
  - `81.500000000000014` vs `81.50000000000001` (diff=0, a=1, b=1)
  - `0.0030875004591237338` vs `0.003087500459123734` (diff=0, a=1, b=1)
  - `-0.0064805465637732627` vs `-0.006480546563773263` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 169 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.050866459338786411` x 1
  - `0.0027321223768814948` x 1
- top_only_treemodel2sql:
  - `0.05086645933878641` x 1
  - `0.002732122376881495` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.050866459338786411` vs `0.05086645933878641` (diff=0, a=1, b=1)
  - `0.0027321223768814948` vs `0.002732122376881495` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 170 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `37733.500000000007` x 1
  - `-0.0085018632238527021` x 1
  - `0.0055867644825081126` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `37733.50000000001` x 1
  - `-0.008501863223852702` x 1
  - `0.005586764482508113` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `37733.500000000007` vs `37733.50000000001` (diff=0, a=1, b=1)
  - `-0.0085018632238527021` vs `-0.008501863223852702` (diff=0, a=1, b=1)
  - `0.0055867644825081126` vs `0.005586764482508113` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 171 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0052788681262849208` x 1
- top_only_treemodel2sql:
  - `-0.005278868126284921` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0052788681262849208` vs `-0.005278868126284921` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 172 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4.5000000000000009` x 1
  - `0.00075315945816512627` x 1
  - `942.50000000000011` x 1
  - `0.072660117152298087` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
  - `0.0007531594581651263` x 1
  - `942.5000000000001` x 1
  - `0.07266011715229809` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `0.00075315945816512627` vs `0.0007531594581651263` (diff=0, a=1, b=1)
  - `942.50000000000011` vs `942.5000000000001` (diff=0, a=1, b=1)
  - `0.072660117152298087` vs `0.07266011715229809` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 173 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `-0.0042170014016568343` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `-0.004217001401656834` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `-0.0042170014016568343` vs `-0.004217001401656834` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 174 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `5.5000000000000009` x 1
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `5.500000000000001` x 1
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 175 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `6.5000000000000009` x 1
  - `0.021175407944136859` x 1
- top_only_treemodel2sql:
  - `6.500000000000001` x 1
  - `0.02117540794413686` x 1
- close_pairs(abs_diff <= tolerance):
  - `6.5000000000000009` vs `6.500000000000001` (diff=0, a=1, b=1)
  - `0.021175407944136859` vs `0.02117540794413686` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 176 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `4.5000000000000009` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `4.500000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 177 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
- top_only_treemodel2sql:
  - `0` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 178 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4.5000000000000009` x 1
  - `-0.014643317832996239` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
  - `-0.01464331783299624` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
  - `-0.014643317832996239` vs `-0.01464331783299624` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 179 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `2`
- top_only_tree2code:
  - `1E-13` x 2
  - `0.0062763032216488534` x 1
- top_only_treemodel2sql:
  - `0` x 2
  - `0.006276303221648853` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=2, b=2)
  - `0.0062763032216488534` vs `0.006276303221648853` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=2, b=2)

### Tree 180 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0091116915597920702` x 1
- top_only_treemodel2sql:
  - `-0.00911169155979207` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0091116915597920702` vs `-0.00911169155979207` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 181 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0019853380267240892` x 1
  - `-0.0048909705232652598` x 1
- top_only_treemodel2sql:
  - `0.001985338026724089` x 1
  - `-0.00489097052326526` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0019853380267240892` vs `0.001985338026724089` (diff=0, a=1, b=1)
  - `-0.0048909705232652598` vs `-0.00489097052326526` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 182 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0057524936930564638` x 1
  - `-0.0075727769460489022` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.005752493693056464` x 1
  - `-0.007572776946048902` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0057524936930564638` vs `0.005752493693056464` (diff=0, a=1, b=1)
  - `-0.0075727769460489022` vs `-0.007572776946048902` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 183 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0041131420056215477` x 1
- top_only_treemodel2sql:
  - `-0.004113142005621548` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0041131420056215477` vs `-0.004113142005621548` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 184 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `6.5000000000000009` x 1
  - `0.0068930056172013202` x 1
- top_only_treemodel2sql:
  - `6.500000000000001` x 1
  - `0.00689300561720132` x 1
- close_pairs(abs_diff <= tolerance):
  - `6.5000000000000009` vs `6.500000000000001` (diff=0, a=1, b=1)
  - `0.0068930056172013202` vs `0.00689300561720132` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 185 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `96.500000000000014` x 1
  - `-0.0073638733892642571` x 1
- top_only_treemodel2sql:
  - `96.50000000000001` x 1
  - `-0.007363873389264257` x 1
- close_pairs(abs_diff <= tolerance):
  - `96.500000000000014` vs `96.50000000000001` (diff=0, a=1, b=1)
  - `-0.0073638733892642571` vs `-0.007363873389264257` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 186 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `0.0083424875143002578` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `0.008342487514300258` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `0.0083424875143002578` vs `0.008342487514300258` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 187 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `57.500000000000007` x 1
  - `0.0047929446121774766` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `57.50000000000001` x 1
  - `0.004792944612177477` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `57.500000000000007` vs `57.50000000000001` (diff=0, a=1, b=1)
  - `0.0047929446121774766` vs `0.004792944612177477` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 188 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0022236564427530739` x 1
- top_only_treemodel2sql:
  - `0.002223656442753074` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0022236564427530739` vs `0.002223656442753074` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 189 (present_in_both)
- exact_only_tree2code_count: `0`
- exact_only_treemodel2sql_count: `0`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - (empty)
- top_only_treemodel2sql:
  - (empty)
- close_pairs(abs_diff <= tolerance):
  - (empty)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 190 (present_in_both)
- exact_only_tree2code_count: `3`
- exact_only_treemodel2sql_count: `3`
- threshold_mismatch_count(0_vs_1e-13): `1`
- top_only_tree2code:
  - `1E-13` x 1
  - `44.500000000000007` x 1
  - `0.0050268468747568266` x 1
- top_only_treemodel2sql:
  - `0` x 1
  - `44.50000000000001` x 1
  - `0.005026846874756827` x 1
- close_pairs(abs_diff <= tolerance):
  - `1E-13` vs `0` (diff=1e-13, a=1, b=1)
  - `44.500000000000007` vs `44.50000000000001` (diff=0, a=1, b=1)
  - `0.0050268468747568266` vs `0.005026846874756827` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - `1E-13` vs `0` (a=1, b=1)

### Tree 191 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `0.0058975451536968137` x 1
  - `-0.0089261868382999651` x 1
- top_only_treemodel2sql:
  - `0.005897545153696814` x 1
  - `-0.008926186838299965` x 1
- close_pairs(abs_diff <= tolerance):
  - `0.0058975451536968137` vs `0.005897545153696814` (diff=0, a=1, b=1)
  - `-0.0089261868382999651` vs `-0.008926186838299965` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 192 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `6.5000000000000009` x 1
- top_only_treemodel2sql:
  - `6.500000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `6.5000000000000009` vs `6.500000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 193 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.0090851956929146865` x 1
- top_only_treemodel2sql:
  - `-0.009085195692914686` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.0090851956929146865` vs `-0.009085195692914686` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 194 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `516.50000000000011` x 1
  - `-0.0088305669278055682` x 1
- top_only_treemodel2sql:
  - `516.5000000000001` x 1
  - `-0.008830566927805568` x 1
- close_pairs(abs_diff <= tolerance):
  - `516.50000000000011` vs `516.5000000000001` (diff=0, a=1, b=1)
  - `-0.0088305669278055682` vs `-0.008830566927805568` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 195 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `-0.00077137587800663152` x 1
- top_only_treemodel2sql:
  - `-0.0007713758780066315` x 1
- close_pairs(abs_diff <= tolerance):
  - `-0.00077137587800663152` vs `-0.0007713758780066315` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 196 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `4.5000000000000009` x 1
- top_only_treemodel2sql:
  - `4.500000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `4.5000000000000009` vs `4.500000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 197 (present_in_both)
- exact_only_tree2code_count: `1`
- exact_only_treemodel2sql_count: `1`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `5.5000000000000009` x 1
- top_only_treemodel2sql:
  - `5.500000000000001` x 1
- close_pairs(abs_diff <= tolerance):
  - `5.5000000000000009` vs `5.500000000000001` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 198 (present_in_both)
- exact_only_tree2code_count: `4`
- exact_only_treemodel2sql_count: `4`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `32962.500000000007` x 1
  - `0.00019881615420357741` x 1
  - `-0.023263491012767881` x 1
  - `0.0055995933317429941` x 1
- top_only_treemodel2sql:
  - `32962.50000000001` x 1
  - `0.0001988161542035774` x 1
  - `-0.02326349101276788` x 1
  - `0.005599593331742994` x 1
- close_pairs(abs_diff <= tolerance):
  - `32962.500000000007` vs `32962.50000000001` (diff=0, a=1, b=1)
  - `0.00019881615420357741` vs `0.0001988161542035774` (diff=0, a=1, b=1)
  - `-0.023263491012767881` vs `-0.02326349101276788` (diff=0, a=1, b=1)
  - `0.0055995933317429941` vs `0.005599593331742994` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)

### Tree 199 (present_in_both)
- exact_only_tree2code_count: `2`
- exact_only_treemodel2sql_count: `2`
- threshold_mismatch_count(0_vs_1e-13): `0`
- top_only_tree2code:
  - `96.500000000000014` x 1
  - `-0.0087525443744678796` x 1
- top_only_treemodel2sql:
  - `96.50000000000001` x 1
  - `-0.00875254437446788` x 1
- close_pairs(abs_diff <= tolerance):
  - `96.500000000000014` vs `96.50000000000001` (diff=0, a=1, b=1)
  - `-0.0087525443744678796` vs `-0.00875254437446788` (diff=0, a=1, b=1)
- threshold_mismatch_pairs(0_vs_1e-13):
  - (empty)
