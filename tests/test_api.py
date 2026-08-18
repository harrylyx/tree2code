import inspect

import pytest

from tree2code import __version__, convert


def test_package_exposes_current_version():
    assert __version__ == "0.3.0"


def test_pmml_is_no_longer_a_supported_target(lgb_model):
    with pytest.raises(ValueError, match="only: 'sql', 'python'"):
        convert(lgb_model, to="pmml")


def test_pmml_parameters_are_removed_from_convert_interface():
    parameter_names = set(inspect.signature(convert).parameters)

    assert not {
        "pmml_version",
        "pmml_model_name",
        "pmml_target_name",
        "pmml_positive_class",
        "pmml_negative_class",
    } & parameter_names


@pytest.mark.parametrize("target", ["sql", "python"])
def test_convert_supports_each_remaining_target(lgb_model, target):
    result = convert(lgb_model, to=target)

    assert target in result
    assert set(result) == {"meta", target}


def test_convert_supports_both_remaining_targets(lgb_model):
    result = convert(lgb_model, to=["sql", "python"])

    assert set(result) == {"meta", "sql", "python"}
