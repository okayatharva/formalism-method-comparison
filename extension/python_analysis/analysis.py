"""Transform paper records into analysis-ready rows."""

import pandas as pd

from config import TOPIC_MAP, OPERATION_MAP

DATAFRAME_COLUMNS = [
    "Method",
    "Paper ID",
    "Topic",
    "Operation",
    "Formal Support",
    "Objects",
    "Assumptions",
    "Guarantees",
    "arXiv Categories",
]


def get_paper_id(record):
    return str(record.get("paper_id", "Unknown"))


def get_method_name(record):
    return record.get("method_name", "Unknown Method")


def get_categories(record):
    categories = record.get("arxiv_categories", [])
    return categories if isinstance(categories, list) else [str(categories)]


def get_topic(record):
    paper_id = get_paper_id(record)
    if paper_id in TOPIC_MAP:
        return TOPIC_MAP[paper_id]

    categories = get_categories(record)
    return categories[0] if categories else "Unknown"


def get_operation(record):
    paper_id = get_paper_id(record)
    if paper_id in OPERATION_MAP:
        return OPERATION_MAP[paper_id]

    formalism = record.get("formalism", {})
    if not isinstance(formalism, dict):
        return "Unknown"

    return formalism.get("operation", "Unknown")


def get_proof_status(record):
    value = record.get("has_formal_proof")
    if value is True:
        return "Formal proof / theorem"
    if value is False:
        return "No formal proof"
    return "Not specified"


def get_list_text(value):
    if isinstance(value, list):
        return "; ".join(str(item) for item in value)
    return "" if value is None else str(value)


def _formalism_value(record, key):
    formalism = record.get("formalism", {})
    if not isinstance(formalism, dict):
        return ""
    return get_list_text(formalism.get(key, []))


def get_objects(record):
    return _formalism_value(record, "objects")


def get_assumptions(record):
    return _formalism_value(record, "assumptions")


def get_guarantees(record):
    return _formalism_value(record, "guarantees")


def build_dataframe(records):
    rows = []

    for record in records:
        rows.append({
            "Method": get_method_name(record),
            "Paper ID": get_paper_id(record),
            "Topic": get_topic(record),
            "Operation": get_operation(record),
            "Formal Support": get_proof_status(record),
            "Objects": get_objects(record),
            "Assumptions": get_assumptions(record),
            "Guarantees": get_guarantees(record),
            "arXiv Categories": ", ".join(get_categories(record)),
        })

    return pd.DataFrame(rows, columns=DATAFRAME_COLUMNS)
