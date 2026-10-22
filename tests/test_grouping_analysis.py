"""Tests for descriptive topic/operation grouping findings."""

import pandas as pd

from grouping_analysis import (
    find_cross_topic_operations,
    find_same_topic_different_operations,
)


def test_finds_one_operation_used_in_multiple_topics():
    dataframe = pd.DataFrame(
        [
            {"Method": "A", "Topic": "Vision", "Operation": "Attention"},
            {"Method": "B", "Topic": "Language", "Operation": "Attention"},
        ]
    )

    findings = find_cross_topic_operations(dataframe)

    assert len(findings) == 1
    assert findings[0][0] == "Attention"


def test_finds_one_topic_with_multiple_operations():
    dataframe = pd.DataFrame(
        [
            {"Method": "A", "Topic": "Vision", "Operation": "Attention"},
            {"Method": "B", "Topic": "Vision", "Operation": "Aggregation"},
        ]
    )

    findings = find_same_topic_different_operations(dataframe)

    assert len(findings) == 1
    assert findings[0][0] == "Vision"
