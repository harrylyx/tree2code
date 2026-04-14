# tree2code for AI Agents

Welcome! `tree2code` is a lightweight tool designed to convert XGBoost and LightGBM binary classifier models into SQL or pure Python scoring code. It is built to be simple, robust, and highly performant for deployment in production systems where native model libraries might not be available.

## Core Architecture

The project follows a classic compiler design: **Parser -> Intermediate Representation (IR) -> Renderer**.

- **`ir.py`**: Defines the `ModelIR` and `TreeNode` dataclasses. All model types are first converted into this format before being rendered to SQL or Python.
- **`parsers.py`**: Handles the logic for converting model objects (XGBoost/LightGBM) into the `ModelIR`. It supports numeric splits and binary classification.
- **`render_sql.py`**: Renders the `ModelIR` into SQL. It supports multiple dialects (PSQL, Hive) and modes (expression, select, ddl).
- **`render_python.py`**: Renders the `ModelIR` into a self-contained Python function `predict_row`.
- **`scoring.py`**: Contains the logic for credit scorecard conversion (Probability to Score) and abnormal value rules.
- **`api.py`**: The main entry point `convert()` that orchestrates the entire process.

## Design Philosophy

- **Zero Runtime Dependencies**: The generated Python code and the core conversion logic do not require XGBoost or LightGBM at runtime. Users can deploy the output without installing heavy ML libraries.
- **Numerical Parity**: We strive for exact numerical alignment. 
    - For XGBoost, we use `float32` alignment because XGBoost's native prediction logic uses single-precision floats.
    - For credit scores, we use `decimal` rounding to ensure consistency.
- **Safe DDL**: The `ddl` mode generates a 3-layer subquery structure for readability and to prevent SQL length issues in some dialects.

## Coding Standards

- **Docstrings**: Use Google-style docstrings for all public modules and functions.
- **Linting**: Follow `black`, `isort`, and `flake8` standards. Pre-commit hooks are configured to enforce these.
- **Type Hints**: Use type hints throughout the codebase.

## Testing

Tests are located in the `tests/` directory. 
- Use `pytest` for running suites.
- For PostgreSQL integration tests, set up environment variables in a `.env` file (ignored by Git).
- Continuous Integration is configured via GitHub Actions.

## Key Constraints for Agents

1. **Do not add heavy runtime dependencies** to the `dependencies` list in `pyproject.toml`.
2. **Always verify numerical parity** when changing the scoring or probability calculation logic.
3. **Maintain multi-dialect support** in `render_sql.py`.

Happy coding!
