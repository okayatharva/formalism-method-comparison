"""Tests for transforming paper records into analysis rows."""

from analysis import build_dataframe, get_operation, get_proof_status, get_topic


def test_researched_topic_and_operation_are_used():
    record = {
        "paper_id": "1706.03762",
        "method_name": "Transformer",
        "formalism": {"operation": "operation from JSON"},
    }
    assert get_topic(record) == "NLP"
    assert get_operation(record) == "Learned Attention"


def test_unknown_topic_falls_back_to_first_arxiv_category():
    record = {"paper_id": "custom-paper", "arxiv_categories": ["cs.AI", "cs.LG"]}
    assert get_topic(record) == "cs.AI"


def test_proof_status_does_not_guess_missing_value():
    assert get_proof_status({}) == "Not specified"
    assert get_proof_status({"has_formal_proof": True}) == "Formal proof / theorem"
    assert get_proof_status({"has_formal_proof": False}) == "No formal proof"


def test_dataframe_has_expected_columns_even_when_empty():
    dataframe = build_dataframe([])
    assert "Method" in dataframe.columns
    assert "Paper ID" in dataframe.columns
    assert dataframe.empty
