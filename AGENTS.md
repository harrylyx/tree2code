# tree2code for AI Agents

Welcome! `tree2code` is a lightweight tool designed to convert XGBoost and LightGBM binary classifier models into SQL, pure Python scoring code, or PMML. It is built to be simple, robust, and highly performant for deployment in production systems where native model libraries might not be available.

## Core Architecture

The project follows a classic compiler design: **Parser -> Intermediate Representation (IR) -> Renderer**.

- **`ir.py`**: Defines the `ModelIR` and `TreeNode` dataclasses. All model types are first converted into this format before being rendered to SQL or Python.
- **`parsers.py`**: Handles the logic for converting model objects (XGBoost/LightGBM) into the `ModelIR`. It supports numeric splits and binary classification.
- **`render_sql.py`**: Renders the `ModelIR` into SQL. It supports multiple dialects (PSQL, Hive) and modes (expression, select, ddl).
- **`render_python.py`**: Renders the `ModelIR` into a self-contained Python function `predict_row`.
- **`render_pmml.py`**: Renders the `ModelIR` into PMML XML using only the Python standard library. Supported PMML versions are `4.4.1`, `4.3`, and `4.2.1`.
- **`scoring.py`**: Contains the logic for credit scorecard conversion (Probability to Score) and abnormal value rules.
- **`api.py`**: The main entry point `convert()` that orchestrates the entire process.

## Design Philosophy

- **Zero Runtime Dependencies**: The generated Python code, generated PMML text, and the core conversion logic do not require XGBoost, LightGBM, Java, or other heavy runtime libraries. PyPMML is only a development/test dependency for validation.
- **Numerical Parity**: We strive for exact numerical alignment. 
    - For XGBoost, Python output and internal IR evaluation use `float32` accumulation and a platform `expf` sigmoid path to align with native prediction.
    - For XGBoost SQL and PMML output, expect small differences from the execution engine's `exp` implementation. Current acceptance is `1e-7` scale, not LightGBM's `1e-12`.
    - For LightGBM, probability parity should remain at `1e-12` scale.
    - For credit scores, we use `decimal` rounding to ensure consistency.
- **Safe DDL**: The `ddl` mode generates a 3-layer subquery structure for readability and to prevent SQL length issues in some dialects.

## Coding Standards

- **Docstrings**: Use Google-style docstrings for all public modules and functions.
- **Linting**: Follow `black`, `isort`, and `flake8` standards. Pre-commit hooks are configured to enforce these.
- **Type Hints**: Use type hints throughout the codebase.

## Testing

Tests are located in the `tests/` directory. 
- Use `pytest` for running suites.
- Default CI only runs tests under `tests/`. Do not add tests there that require local-only `test_data` files.
- Tests that depend on local real data should live under `manual_tests/` or be exposed as scripts under `scripts/`.
- Real-data PMML validation is available via `uv run python scripts/pmml_real_data_check.py`.
- PMML tests use PyPMML to load generated PMML and run predictions. PyPMML requires Java, but this is a validation dependency only.
- For PostgreSQL integration tests, set up environment variables in a `.env` file (ignored by Git).
- Continuous Integration is configured via GitHub Actions.

## Key Constraints for Agents

1. **Do not add heavy runtime dependencies** to the `dependencies` list in `pyproject.toml`.
2. **Always verify numerical parity** when changing the scoring or probability calculation logic.
3. **Maintain multi-dialect support** in `render_sql.py`.
4. **Keep real `test_data` checks out of default CI**; use `manual_tests/` or `scripts/` for local-only validation.
5. **Do not expand PMML scope silently**; PMML currently guarantees binary model probability `score_p`, while scorecard `score` and abnormal-value overrides are not part of the PMML output.
6. **When releasing**, update the project version, run local tests, build the package, push `main`, and tag the release as `v<version>` so the GitHub Release workflow can publish artifacts.

Happy coding!
