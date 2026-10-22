"""Tests for comparing actual record IDs with expected IDs."""

import pandas as pd

from validation import validate_dataset


def test_validation_finds_missing_and_extra_ids():
    dataframe = pd.DataFrame({"Paper ID": ["paper-a", "paper-c"]})

    result = validate_dataset(dataframe, {"paper-a", "paper-b"})

    assert result["missing_ids"] == {"paper-b"}
    assert result["extra_ids"] == {"paper-c"}
    assert result["record_count"] == 2
