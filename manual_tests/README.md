# Manual Tests

This directory contains checks that are useful locally but are not part of
the default CI suite. Tests here may expect local-only data files or optional
environment setup.

Run them explicitly, for example:

```bash
uv run pytest manual_tests/test_pmml_real_data_script.py -q
```
