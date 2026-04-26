import subprocess
import sys
import importlib.util
from pathlib import Path


def _load_script_module():
    path = Path("scripts/pmml_real_data_check.py")
    spec = importlib.util.spec_from_file_location("pmml_real_data_check", path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_pmml_real_data_script_has_cli_help():
    script = Path("scripts/pmml_real_data_check.py")

    result = subprocess.run(
        [sys.executable, str(script), "--help"],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    assert "--rows" in result.stdout
    assert "--pmml-version" in result.stdout


def test_pmml_real_data_script_model_arg_replaces_default():
    module = _load_script_module()

    args = module.build_parser().parse_args(["--model", "lgb"])

    assert module._parse_models(args.model) == ["lgb"]


def test_pmml_real_data_script_accepts_custom_tolerances():
    module = _load_script_module()

    args = module.build_parser().parse_args(
        ["--xgb-tolerance", "1e-5", "--lgb-tolerance", "1e-10"]
    )

    assert module._model_tolerance("xgb", args) == 1e-5
    assert module._model_tolerance("lgb", args) == 1e-10
    assert module._model_tolerance("all", args) == 1e-10
