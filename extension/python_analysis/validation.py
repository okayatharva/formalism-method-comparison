"""Validate actual paper IDs against the expected dataset."""

def validate_dataset(dataframe, expected_ids):
    actual_ids = set(dataframe["Paper ID"].astype(str)) if "Paper ID" in dataframe else set()
    expected_ids = set(map(str, expected_ids))

    return {
        "missing_ids": expected_ids - actual_ids,
        "extra_ids": actual_ids - expected_ids,
        "record_count": len(dataframe),
    }
