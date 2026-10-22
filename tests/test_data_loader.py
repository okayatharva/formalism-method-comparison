"""Tests for reading JSON paper records."""

import json

from data_loader import load_records


def test_load_records_reads_json_object(tmp_path):
    records_dir = tmp_path / "records"
    records_dir.mkdir()
    (records_dir / "paper.json").write_text(
        json.dumps({"paper_id": "example", "method_name": "Example"}),
        encoding="utf-8",
    )

    records, warnings = load_records(records_dir)

    assert len(records) == 1
    assert records[0]["paper_id"] == "example"
    assert warnings == []


def test_load_records_reports_missing_directory(tmp_path):
    records, warnings = load_records(tmp_path / "does-not-exist")

    assert records == []
    assert any("not found" in warning for warning in warnings)


def test_load_records_skips_invalid_json_and_keeps_valid_record(tmp_path):
    records_dir = tmp_path / "records"
    records_dir.mkdir()
    (records_dir / "good.json").write_text('{"paper_id": "good"}', encoding="utf-8")
    (records_dir / "bad.json").write_text("{not valid json", encoding="utf-8")

    records, warnings = load_records(records_dir)

    assert len(records) == 1
    assert records[0]["paper_id"] == "good"
    assert any("Could not read bad.json" in warning for warning in warnings)
