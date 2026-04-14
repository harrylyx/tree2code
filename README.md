# tree2code

`tree2code` 是一个轻量工具：把 XGBoost / LightGBM 二分类树模型转换成 SQL 和纯 Python 打分代码。

当前能力：
- 支持模型：XGBoost、LightGBM（二分类，数值 + 类别特征）
- 支持输出：
  - SQL（PostgreSQL、Hive）
  - 纯 Python 评分函数
- 支持评分卡输出：输入 `base_score`、`pdo`、`base_odds` 后，输出 `score_p` + `score`
- 支持异常值规则：
  - `all_null`：入模变量全空触发
  - `all_default`：入模变量全等默认填充值触发
  - 触发后可把 `score_p` 和 `score` 同时置为异常值（例如 `-2`）

## 1. 环境与安装

- 环境管理：`uv`
- Python：`3.8 ~ 3.14`

本项目运行时依赖尽量保持为 0（核心转换逻辑不强绑模型库）。
测试时按需注入模型库依赖。

```bash
# 创建虚拟环境并进入
uv venv
source .venv/bin/activate

# 安装项目本体
uv pip install -e .
```

## 2. 最简 API

```python
from tree2code import convert

out = convert(
    model,
    to=["sql", "python"],
    dialect="psql",          # psql / hive
    sql_mode="select",       # expression / select
    keep_columns=["id"],
    table_name="input_table",
)
```

返回内容里包含：
- `out["sql"]["score_p_expr"]`
- `out["sql"]["score_expr"]`（仅当提供评分参数）
- `out["sql"]["select_sql"]`（`sql_mode="select"` 时）
- `out["python"]`（可 `exec` 的 `predict_row` 函数源码）

## 3. 评分卡参数

传入以下参数即可输出模型分：
- `base_score`
- `pdo`
- `base_odds`
- `score_scale`（默认 3）

```python
out = convert(
    model,
    to="python",
    base_score=600,
    pdo=50,
    base_odds=20,
    score_scale=3,
)
```

## 4. 异常值规则

```python
out = convert(
    model,
    to="python",
    base_score=600,
    pdo=50,
    base_odds=20,
    abnormal_rule="all_null",   # all_null / all_default / None
    default_fill_value=-999.0,    # 仅 all_default 时需要
    abnormal_value=-2,
)
```

说明：
- 只有当 `abnormal_value` 显式传入时，异常覆盖才会生效。
- 触发异常时，`score_p` 与 `score` 都输出异常值。

## 5. 一致性口径

- LightGBM：概率对齐阈值 `1e-12`
- XGBoost：概率对齐阈值 `1e-7`
  - 原因：XGBoost 原生预测链路是 float32，会有微小数值差异
- 模型分：按 `score_scale` 规则四舍五入后要求一致

## 6. 本地测试

### 6.1 常规测试

```bash
uv run --group dev \
  --with numpy --with pandas --with scikit-learn \
  --with xgboost==3.2.0 --with lightgbm==4.6.0 \
  --with 'psycopg[binary]' \
  pytest -q
```

### 6.2 PostgreSQL 集成测试

测试连接通过环境变量注入（不在仓库里写明文账号密码）：

```bash
export TREE2CODE_PGHOST=127.0.0.1
export TREE2CODE_PGPORT=5432
export TREE2CODE_PGUSER=your_user
export TREE2CODE_PGPASSWORD=your_password
export TREE2CODE_PGDATABASE=postgres
```

## 7. 跨版本矩阵测试（3.8 ~ 3.14）

```bash
python3 scripts/run_version_matrix.py --output matrix_report.json
```

脚本会自动：
- 为每个 Python 版本探测 XGB/LGB 的“最低可安装版本 + 最高可安装版本”
- 跑转换烟测
- 生成矩阵报告

## 8. GitHub CI/CD

已配置：
- `CI`：PR / push 自动测试（含 PostgreSQL 集成）
- `Release`：打 tag 后自动构建 wheel/sdist 并上传到 GitHub Release

详见：`docs/CI_CD.md`

## 9. test_data 全量对齐报告

按 `idx` 去重后，跑原模型 / 生成 Python / 生成 SQL 三方对齐，并输出报告：

```bash
python3 scripts/run_testdata_parity.py --output docs/testdata_parity_report.md
```

## 10. LGB SQL 一致性对比（tree2code vs treemodel2sql）

```bash
python3 scripts/compare_lgb_sql_consistency.py \
  --model-path test_data/lgb_model.pkl \
  --keep-columns idx \
  --table-name input_table
```

## 11. 两份 SQL 按树对比（逐棵树数值差异）

输入任意两份 SQL 文件，按树索引比较每棵树里的数值差异（哪些值只在 A 出现、只在 B 出现、近似相等但文本不一致）：

```bash
python3 scripts/compare_sql_tree_values.py \
  --sql-a docs/sql_compare/lgb_tree2code_hive.sql \
  --sql-b docs/sql_compare/lgb_treemodel2sql.sql \
  --name-a tree2code \
  --name-b treemodel2sql
```

默认输出：
- `docs/sql_compare/sql_tree_value_diff_report.md`
- `docs/sql_compare/sql_tree_value_diff_report.json`

## 12. PySpark 对齐测试（原模型为金标准）

使用 Spark 本地模式执行两份 SQL（`tree2code` 和 `treemodel2sql`），与原生 LightGBM 预测做逐行对齐：

```bash
python3 scripts/run_pyspark_parity.py \
  --data-path test_data/all_data.pq \
  --model-path test_data/lgb_model.pkl
```

默认输出：
- `docs/pyspark_parity_report.md`
- `docs/pyspark_parity_report.json`
