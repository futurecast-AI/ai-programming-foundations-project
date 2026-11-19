"""Check the notebook's real functions and recorded outputs."""
import hashlib
from pathlib import Path

import nbformat
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def functions():
    """Load the actual notebook function definitions without running plotting cells."""
    scope = {"np": np, "pd": pd}
    nb = nbformat.read(ROOT / "data_workflow.ipynb", as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code" and cell.source.lstrip().startswith("def "):
            exec(cell.source, scope)
    return scope


def test_source_shape_and_integrity():
    """Verify the frozen input snapshot and rubric dataset minimum."""
    path = ROOT / "titanic.csv"
    assert pd.read_csv(path).shape == (891, 15)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == (
        "81787d320d7f7b03df935e91de8bd19e11d45c5bbcab86ef4d4a76dc91b7d4f2"
    )


def test_column_cleaning_is_nonmutating(functions):
    """Check normalization and preservation of caller-owned data."""
    source = pd.DataFrame({" Passenger Class ": [1]})
    result = functions["standardize_columns"](source)
    assert list(result) == ["passenger_class"]
    assert list(source) == [" Passenger Class "]


def test_category_cleaning_labels_missing_values(functions):
    """Verify text normalization and an explicit unknown embarkation label."""
    source = pd.DataFrame({"sex": [" Female ", "MALE"], "embarked": [" S ", None]})
    result = functions["clean_categories"](source)
    assert result["sex"].tolist() == ["female", "male"]
    assert result["embarked"].tolist() == ["s", "unknown"]
    assert pd.isna(source.loc[1, "embarked"])


def test_all_records_and_missing_ages_retained(functions):
    """Verify the documented cleaning policy on the actual dataset."""
    raw = pd.read_csv(ROOT / "titanic.csv")
    data = functions["prepare_analysis_data"](
        functions["clean_categories"](functions["standardize_columns"](raw))
    )
    assert data.shape == (891, 9)
    assert data["age"].isna().sum() == 177
    assert data["age_missing"].sum() == 177
    assert (data["embarked"] == "unknown").sum() == 2
    assert raw.duplicated().sum() == 107


def test_eda_matches_independent_calculations(functions):
    """Check group denominators, survivors, and rates independently."""
    raw = pd.read_csv(ROOT / "titanic.csv")
    clean = functions["prepare_analysis_data"](functions["clean_categories"](raw))
    result = functions["summarize_passengers"](clean)
    assert result["by_class"]["passengers"].tolist() == [216, 184, 491]
    assert result["by_class"]["survivors"].sum() == 342
    assert np.isclose(result["by_class"].loc[1, "survival_rate"], 136 / 216)
    assert result["by_sex_class"]["passengers"].sum() == 891


def test_bad_numeric_value_is_not_silently_lost(functions):
    """Ensure unexpected input corruption is reported, not silently dropped."""
    raw = pd.read_csv(ROOT / "titanic.csv").astype({"age": "object"})
    raw.loc[0, "age"] = "bad-number"
    with pytest.raises(ValueError, match="Invalid numeric"):
        functions["prepare_analysis_data"](functions["clean_categories"](raw))


def test_notebook_has_no_execution_errors():
    """Require a fully executed notebook ending in the requested narrative summary."""
    nb = nbformat.read(ROOT / "data_workflow.ipynb", as_version=4)
    code = [cell for cell in nb.cells if cell.cell_type == "code"]
    assert all(cell.execution_count is not None for cell in code)
    assert not any(output.output_type == "error" for cell in code for output in cell.outputs)
    assert nb.cells[-1].cell_type == "markdown"
    assert "Summary and interpretation" in nb.cells[-1].source


def test_three_nonempty_figures_exist():
    """Require all three labeled-figure artifacts from the executed workflow."""
    for name in ["figure_1_age_distribution.png", "figure_2_survival_by_class.png",
                 "figure_3_survival_by_sex_class.png"]:
        assert (ROOT / "outputs" / name).stat().st_size > 1000
