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

## 6. 测试与验证

### 6.1 SQL 执行型测试矩阵

树生成 SQL 的正确性统一通过“执行型测试”验证，不再依赖字符串断言：

| 模型 | 特征类型 | 执行引擎 | 测试文件 |
|---|---|---|---|
| LightGBM | 数值 + 类别 | PySpark (Hive SQL) | `tests/test_pyspark_parity.py` |
| XGBoost | 数值 + 类别 | PySpark (Hive SQL) | `tests/test_pyspark_parity.py` |
| LightGBM | 数值 + 类别 | PostgreSQL (psql SQL) | `tests/test_psql_integration.py` |
| XGBoost | 数值 + 类别 | PostgreSQL (psql SQL) | `tests/test_psql_integration.py` |

### 6.2 PySpark 一致性验证
重点验证 Hive SQL 在 Spark 环境下的数值一致性（含类别变量、缺失值）：

```bash
uv run pytest tests/test_pyspark_parity.py -q
```

该测试覆盖了：
- **Hive 兼容缺失值口径**：Hive 路径不依赖 `isnan`，通过字符串判定兼容 `NaN`/`NULL`。
- **双精度对齐**：验证科学计数法字面量是否能强制 Spark 使用 DOUBLE 路径，避免 10^-6 级的误差。
- **字面量格式覆盖**：同时覆盖 `literal_format="standard"` 和 `literal_format="scientific"`。
- **类别分裂对齐**：验证类别命中分支与类别缺失值分支的 SQL 执行结果。

### 6.3 PostgreSQL 集成测试
若本地有 PostgreSQL 环境，可通过环境变量或项目根目录 `.env` 跑真实数据库对齐（含类别变量）：

`.env` 示例：

```bash
TREE2CODE_PGHOST=127.0.0.1
TREE2CODE_PGPORT=5432
TREE2CODE_PGUSER=your_user
TREE2CODE_PGPASSWORD=your_password
TREE2CODE_PGDATABASE=postgres
```

或直接导出环境变量：

```bash
export TREE2CODE_PGHOST=127.0.0.1
export TREE2CODE_PGPORT=5432
export TREE2CODE_PGUSER=your_user
export TREE2CODE_PGPASSWORD=your_password
export TREE2CODE_PGDATABASE=postgres

uv run pytest tests/test_psql_integration.py -q
```

本地未配置 PostgreSQL 连接时，`tests/test_psql_integration.py` 会自动 `skip`，不影响其它测试收集和执行。
在 CI 中应配置 PostgreSQL 并强制执行该测试文件。

### 6.4 SQL 主链路回归
```bash
uv run pytest tests/test_pyspark_parity.py tests/test_psql_integration.py tests/test_sql_rendering.py -q
```

### 6.5 跨版本矩阵测试（3.8 ~ 3.14）
```bash
python3 scripts/run_version_matrix.py --output matrix_report.json
```
脚本会自动探测模型库的不同版本组合并运行烟测。
