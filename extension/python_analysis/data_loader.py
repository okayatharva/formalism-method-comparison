"""Load research records from JSON files."""

import json
from pathlib import Path


def load_records(records_dir):
    """Return (valid_records, warnings) from a directory of JSON files."""
    records = []
    warnings = []
    records_dir = Path(records_dir)

    if not records_dir.is_dir():
        return [], [f"Records directory not found: {records_dir}"]

    for file_path in sorted(records_dir.glob("*.json")):
        try:
            with file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, dict):
                records.append(data)
            else:
                warnings.append(
                    f"Could not read {file_path.name}: expected a JSON object"
                )
        except (OSError, json.JSONDecodeError) as error:
            warnings.append(f"Could not read {file_path.name}: {error}")

    return records, warnings
