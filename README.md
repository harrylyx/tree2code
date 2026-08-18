# tree2code

`tree2code` 是一个轻量工具：把 XGBoost / LightGBM 二分类树模型转换成 SQL 或纯 Python 打分代码。

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
    sql_mode="select",       # expression / select / ddl
    keep_columns=["id"],
    table_name="input_table",
)
```

返回内容里包含：

- `out["meta"]["model_type"]`
- `out["meta"]["feature_names"]`（真正出现在模型分裂中的特征）
- `out["sql"]["score_p_expr"]`
- `out["sql"]["score_expr"]`（仅当提供评分参数）
- `out["sql"]["select_sql"]`（`sql_mode="select"` 时）
- `out["sql"]["ddl_sql"]`（`sql_mode="ddl"` 时）
- `out["python"]`（可 `exec` 的 `predict` 函数源码）

### 2.1 使用生成的 Python 函数

`out["python"]` 是一段不依赖 XGBoost 或 LightGBM 的完整 Python 源码。加载后调用 `predict(row)`：

```python
namespace = {}
exec(out["python"], namespace)
predict = namespace["predict"]

result = predict({"age": 42, "income": "12000.5"})
print(result["score_p"])
```

`row` 可以是字典或其他按键取值的映射对象。如果转换时提供了评分卡参数，返回值还会包含 `result["score"]`。

### 2.2 SQL 输出模式

| `sql_mode` | 用途 | 主要返回值 |
|---|---|---|
| `expression` | 嵌入现有 SQL | `score_p_expr`、`score_expr` |
| `select` | 生成完整查询 | `select_sql` |
| `ddl` | 生成删表并重建结果表的语句 | `ddl_sql` |

`compatible_mode=True` 时，SQL 会把 `NaN` 和 `NULL` 一起按模型的缺失值规则处理。该参数不影响生成的 Python。

## 3. 评分卡参数

传入以下参数即可输出模型分：

- `base_score`
- `pdo`
- `base_odds`：基准分对应的“负类 : 正类”赔率，即 `(1 - p) / p`
- `score_scale`（默认 3）

`base_score`、`pdo` 和 `base_odds` 必须一起提供。例如 `base_score=600, base_odds=20` 表示：当负类与正类的赔率为 20:1 时，分数是 600。负类与正类的赔率每翻一倍，分数增加一个 `pdo`。

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

评分公式为：

```text
factor = pdo / ln(2)
offset = base_score - factor * ln(base_odds)
score  = offset - factor * ln(p / (1 - p))
```

其中 `p` 是正类概率 `score_p`。最终分数使用十进制的四舍五入规则保留 `score_scale` 位小数。

## 4. Python 输入与缺失值

生成的 `predict(row)` 会在计算任何树之前统一处理输入：

- 只要求模型分裂实际使用的特征；训练时存在但未被任何分裂使用的列不需要传入。
- 缺少必需特征键时抛出 `KeyError`，并一次列出所有缺少项；多余键会被忽略。
- 数值特征统一转换为 `float`，因此 `"12.3"` 这类数字字符串可以直接使用。无法转换时抛出 `ValueError`，并列出无效特征及原始值。
- `None`、浮点 `NaN`，以及忽略大小写和首尾空格后的 `""`、`"nan"`、`"null"`、`"none"` 会被识别为缺失值。
- 生成代码顶部的 `MISSING_TEXT_VALUES` 是可编辑集合，可按业务需要增加 `"na"` 等文本标记。
- 缺失值最终按原 XGBoost / LightGBM 的分支规则走向；Python 端始终保持该行为，不受 `compatible_mode` 影响。

“缺少特征键”与“值为缺失值”是两种不同情况：前者是输入错误，后者是可以正常评分的模型输入。

## 5. 异常值规则

```python
out = convert(
    model,
    to="python",
    base_score=600,
    pdo=50,
    base_odds=20,
    abnormal_rule="all_null",   # all_null / all_default / None
    default_fill_value=-999.0,   # 仅 all_default 时需要
    abnormal_value=-2,
)
```

说明：

- 只有当 `abnormal_value` 显式传入时，异常覆盖才会生效。
- `all_null` 在所有必需评分特征都是缺失值时触发。
- `all_default` 必须同时提供 `default_fill_value`。对生成的 Python，缺失值会先被填成该默认值，再判断是否全为默认值；未触发时，填充后的值会继续参与模型计算。SQL 仅对表中的现有列值进行判断，不会执行这一填充步骤。
- 触发异常时，`score_p` 输出异常值；如果配置了评分卡参数，`score` 也输出同一异常值。

## 6. 一致性口径

- LightGBM：概率对齐阈值 `1e-12`
- XGBoost：
  - 纯 Python 输出与内部 IR 评估按 float32 累加和 float32 sigmoid 对齐，目标是逐值一致
  - SQL 受执行引擎的 `exp` 实现影响，验收阈值按实际引擎能力设置
- 模型分：按 `score_scale` 规则四舍五入后要求一致

## 7. 测试与验证

### 7.1 SQL 执行型测试矩阵

树生成 SQL 的正确性统一通过“执行型测试”验证，不再依赖字符串断言：

| 模型 | 特征类型 | 执行引擎 | 测试文件 |
|---|---|---|---|
| LightGBM | 数值 + 类别 | PySpark (Hive SQL) | `tests/test_pyspark_parity.py` |
| XGBoost | 数值 + 类别 | PySpark (Hive SQL) | `tests/test_pyspark_parity.py` |
| LightGBM | 数值 + 类别 | PostgreSQL (psql SQL) | `tests/test_psql_integration.py` |
| XGBoost | 数值 + 类别 | PostgreSQL (psql SQL) | `tests/test_psql_integration.py` |

### 7.2 PySpark 一致性验证

重点验证 Hive SQL 在 Spark 环境下的数值一致性（含类别变量、缺失值）：

```bash
uv run pytest tests/test_pyspark_parity.py -q
```

该测试覆盖了：

- **Hive 兼容缺失值口径**：Hive 路径不依赖 `isnan`，通过字符串判定兼容 `NaN`/`NULL`。
- **双精度对齐**：验证科学计数法字面量是否能强制 Spark 使用 DOUBLE 路径，避免 10^-6 级的误差。
- **字面量格式覆盖**：同时覆盖 `literal_format="standard"` 和 `literal_format="scientific"`。
- **类别分裂对齐**：验证类别命中分支与类别缺失值分支的 SQL 执行结果。

### 7.3 PostgreSQL 集成测试

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

### 7.4 SQL 主链路回归

```bash
uv run pytest tests/test_pyspark_parity.py tests/test_psql_integration.py tests/test_sql_rendering.py -q
```

### 7.5 跨版本矩阵测试（3.8 ~ 3.14）

```bash
python3 scripts/run_version_matrix.py --output matrix_report.json
```
脚本会自动探测模型库的不同版本组合并运行烟测。
