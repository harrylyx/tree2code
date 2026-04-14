import importlib.util
import sys
from pathlib import Path


def _load_module():
    root = Path(__file__).resolve().parents[1]
    module_path = root / "scripts" / "compare_sql_tree_values.py"
    spec = importlib.util.spec_from_file_location("compare_sql_tree_values", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_tokenizer_ignores_identifier_digits():
    module = _load_module()
    text = "case when userinfo_14 <= 3.5 then -0.1 else 0 end"
    tokens = module._extract_number_tokens(text)
    assert tokens == ["3.5", "-0.1", "0"]


def test_threshold_mismatch_0_vs_1e_13_is_flagged():
    module = _load_module()
    tree_a = "case when (`f0` <= 1e-13) then -1 else 2 end"
    tree_b = "case when (f0 <= 0) then -1 else 2 end"
    result = module._compare_tree_values(
        tree_a,
        tree_b,
        max_values=20,
        close_tolerance=1e-12,
    )

    assert result["threshold_mismatch_count"] == 1
    assert len(result["threshold_mismatch_pairs"]) == 1
    pair = result["threshold_mismatch_pairs"][0]
    values = {str(pair["value_a"]), str(pair["value_b"])}
    assert values == {"0", "1E-13"}


def test_extract_trees_alias_and_margin_modes():
    module = _load_module()

    sql_alias = """
    select idx
    from (
      select
        case when f0 <= 1 then 0 else 1 end as tree_0_score,
        case when f1 <= 2 then 0 else 1 end as tree_1_score
      from t
    ) s
    """
    trees_alias, mode_alias = module._extract_trees(sql_alias, "alias")
    assert mode_alias == "alias"
    assert len(trees_alias) == 2
    assert 0 in trees_alias and 1 in trees_alias

    sql_margin = """
    select idx,
    1 / (1 + exp(-((case when f0 <= 1 then 0 else 1 end)
    + (case when f1 <= 2 then 0 else 1 end))))
    as score_p
    from t
    """
    trees_margin, mode_margin = module._extract_trees(sql_margin, "margin")
    assert mode_margin == "margin"
    assert len(trees_margin) == 2
    assert 0 in trees_margin and 1 in trees_margin
