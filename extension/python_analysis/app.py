import json
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Formalism Analysis - 10 Paper Extension",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# PROJECT PATHS
# ============================================================

# app.py is inside:
# extension/python_analysis/
#
# Therefore:
# parent.parent = extension/

PROJECT_DIR = Path(__file__).resolve().parents[2]

EXTENSION_DIR = PROJECT_DIR / "extension"

RECORDS_DIR = EXTENSION_DIR / "records"

OUTPUT_DIR = Path(__file__).resolve().parent / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# EXPECTED 10 EXTENSION PAPERS
# ============================================================

EXPECTED_PAPERS = {
    "1706.08566": "SchNet",
    "1706.03762": "Transformer",
    "1802.04712": "ABMIL",
    "1801.07829": "DGCNN / EdgeConv",
    "2008.02217": "Continuous Modern Hopfield Network",
    "1612.00593": "PointNet",
    "1706.01427": "Relation Network",
    "2105.01601": "MLP-Mixer",
    "1810.00826": "GIN",
    "1807.01613": "CNP"
}


# ============================================================
# RESEARCHED TOPIC LABELS
# ============================================================

TOPIC_MAP = {

    "1706.08566":
        "Computational Chemistry",

    "1706.03762":
        "NLP",

    "1802.04712":
        "Medical Imaging",

    "1801.07829":
        "3D Vision",

    "2008.02217":
        "Memory Networks",

    "1612.00593":
        "3D Vision",

    "1706.01427":
        "Visual / Text / Physics QA",

    "2105.01601":
        "Computer Vision",

    "1810.00826":
        "Graph Learning",

    "1807.01613":
        "Regression / Meta-Learning"
}


# ============================================================
# RESEARCHED OPERATION LABELS
# ============================================================

OPERATION_MAP = {

    "1706.08566":
        "Distance-Based Weighting",

    "1706.03762":
        "Learned Attention",

    "1802.04712":
        "Learned Attention",

    "1801.07829":
        "Neighbor Aggregation",

    "2008.02217":
        "Learned Attention",

    "1612.00593":
        "Max Aggregation",

    "1706.01427":
        "Pairwise Comparison",

    "2105.01601":
        "Axis Mixing",

    "1810.00826":
        "Neighbor Aggregation",

    "1807.01613":
        "Encode-Average-Decode"
}


# ============================================================
# LOAD JSON RECORDS
# ============================================================

def load_records():

    records = []

    if not RECORDS_DIR.exists():

        st.error(
            f"Records folder was not found:\n\n{RECORDS_DIR}"
        )

        st.stop()

    json_files = sorted(
        RECORDS_DIR.glob("*.json")
    )

    for file_path in json_files:

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            if isinstance(data, dict):

                records.append(data)

        except Exception as error:

            st.warning(
                f"Could not read {file_path.name}: {error}"
            )

    return records


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_paper_id(record):

    return str(
        record.get(
            "paper_id",
            "Unknown"
        )
    )


def get_method_name(record):

    return record.get(
        "method_name",
        "Unknown Method"
    )


def get_categories(record):

    categories = record.get(
        "arxiv_categories",
        []
    )

    if isinstance(categories, list):

        return categories

    return [str(categories)]


def get_topic(record):

    paper_id = get_paper_id(record)

    if paper_id in TOPIC_MAP:

        return TOPIC_MAP[paper_id]

    categories = get_categories(record)

    if categories:

        return categories[0]

    return "Unknown"


def get_operation(record):

    paper_id = get_paper_id(record)

    if paper_id in OPERATION_MAP:

        return OPERATION_MAP[paper_id]

    formalism = record.get(
        "formalism",
        {}
    )

    return formalism.get(
        "operation",
        "Unknown"
    )


def get_proof_status(record):

    value = record.get(
        "has_formal_proof",
        None
    )

    if value is True:

        return "Formal proof / theorem"

    if value is False:

        return "No formal proof"

    return "Not specified"


def get_list_text(value):

    if isinstance(value, list):

        return "; ".join(
            str(item)
            for item in value
        )

    if value is None:

        return ""

    return str(value)


def get_objects(record):

    formalism = record.get(
        "formalism",
        {}
    )

    return get_list_text(
        formalism.get(
            "objects",
            []
        )
    )


def get_assumptions(record):

    formalism = record.get(
        "formalism",
        {}
    )

    return get_list_text(
        formalism.get(
            "assumptions",
            []
        )
    )


def get_guarantees(record):

    formalism = record.get(
        "formalism",
        {}
    )

    return get_list_text(
        formalism.get(
            "guarantees",
            []
        )
    )


# ============================================================
# BUILD DATAFRAME
# ============================================================

def build_dataframe(records):

    rows = []

    for record in records:

        paper_id = get_paper_id(record)

        rows.append({

            "Method":
                get_method_name(record),

            "Paper ID":
                paper_id,

            "Topic":
                get_topic(record),

            "Operation":
                get_operation(record),

            "Formal Support":
                get_proof_status(record),

            "Objects":
                get_objects(record),

            "Assumptions":
                get_assumptions(record),

            "Guarantees":
                get_guarantees(record),

            "arXiv Categories":
                ", ".join(
                    get_categories(record)
                )
        })

    return pd.DataFrame(rows)


# ============================================================
# VALIDATE THE DATASET
# ============================================================

records = load_records()

df = build_dataframe(records)

actual_ids = set(
    df["Paper ID"].astype(str)
)

expected_ids = set(
    EXPECTED_PAPERS.keys()
)

missing_ids = expected_ids - actual_ids

extra_ids = actual_ids - expected_ids


# ============================================================
# HEADER
# ============================================================

st.title(
    "📚 Formalism-Based Analysis"
)

st.subheader(
    "10-Paper Extension — Knowledge Discovery"
)

st.markdown(
    """
This dashboard provides a Python-based analysis of the
**10 additional scientific papers** researched as part of
the extension of the formalism-method comparison.

The existing research records are used as the input.
No changes are made to the original JSON records.
"""
)


# ============================================================
# DATASET INFORMATION
# ============================================================

st.info(
    f"Input folder: `{RECORDS_DIR}`"
)

if missing_ids:

    st.warning(
        "Some expected extension papers were not found: "
        + ", ".join(sorted(missing_ids))
    )

if extra_ids:

    st.info(
        "Additional JSON files were found in the folder: "
        + ", ".join(sorted(extra_ids))
    )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title(
    "Dashboard Filters"
)

topic_options = sorted(
    df["Topic"].unique()
)

operation_options = sorted(
    df["Operation"].unique()
)

selected_topics = st.sidebar.multiselect(
    "Topics",
    topic_options,
    default=topic_options
)

selected_operations = st.sidebar.multiselect(
    "Operations",
    operation_options,
    default=operation_options
)


filtered_df = df[
    df["Topic"].isin(selected_topics)
    &
    df["Operation"].isin(selected_operations)
]


# ============================================================
# KEY METRICS
# ============================================================

st.header(
    "1. Dataset Overview"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Papers",
        len(filtered_df)
    )

with col2:

    st.metric(
        "Topics",
        filtered_df["Topic"].nunique()
    )

with col3:

    st.metric(
        "Operations",
        filtered_df["Operation"].nunique()
    )

with col4:

    proof_count = (
        filtered_df["Formal Support"]
        ==
        "Formal proof / theorem"
    ).sum()

    st.metric(
        "Formal Proofs",
        proof_count
    )


# ============================================================
# PAPER TABLE
# ============================================================

st.header(
    "2. Researched Papers"
)

display_columns = [
    "Method",
    "Paper ID",
    "Topic",
    "Operation",
    "Formal Support"
]

st.dataframe(
    filtered_df[display_columns],
    width="stretch",
    hide_index=True
)


# ============================================================
# TOPIC DISTRIBUTION
# ============================================================

st.header(
    "3. Topic Distribution"
)

topic_counts = (
    filtered_df["Topic"]
    .value_counts()
)

fig_topic, ax_topic = plt.subplots(
    figsize=(10, 5)
)

topic_counts.plot(
    kind="bar",
    ax=ax_topic
)

ax_topic.set_title(
    "Distribution of Papers by Topic"
)

ax_topic.set_xlabel(
    "Topic"
)

ax_topic.set_ylabel(
    "Number of Papers"
)

plt.xticks(
    rotation=35,
    ha="right"
)

plt.tight_layout()

st.pyplot(
    fig_topic
)

fig_topic.savefig(
    OUTPUT_DIR / "topic_distribution.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close(fig_topic)


# ============================================================
# OPERATION DISTRIBUTION
# ============================================================

st.header(
    "4. Operation Distribution"
)

operation_counts = (
    filtered_df["Operation"]
    .value_counts()
)

fig_operation, ax_operation = plt.subplots(
    figsize=(10, 5)
)

operation_counts.plot(
    kind="bar",
    ax=ax_operation
)

ax_operation.set_title(
    "Distribution of Papers by Underlying Operation"
)

ax_operation.set_xlabel(
    "Operation"
)

ax_operation.set_ylabel(
    "Number of Papers"
)

plt.xticks(
    rotation=35,
    ha="right"
)

plt.tight_layout()

st.pyplot(
    fig_operation
)

fig_operation.savefig(
    OUTPUT_DIR / "operation_distribution.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close(fig_operation)


# ============================================================
# TOPIC × OPERATION HEATMAP
# ============================================================

st.header(
    "5. Topic × Operation Relationship"
)

st.markdown(
    """
This comparison is the main purpose of the analysis.

It helps identify:

- different topics sharing the same operation
- the same topic using different operations
"""
)

cross_table = pd.crosstab(
    filtered_df["Topic"],
    filtered_df["Operation"]
)

fig_heatmap, ax_heatmap = plt.subplots(
    figsize=(13, 7)
)

image = ax_heatmap.imshow(
    cross_table.values,
    aspect="auto"
)

ax_heatmap.set_title(
    "Topic × Operation Relationship"
)

ax_heatmap.set_xticks(
    range(len(cross_table.columns))
)

ax_heatmap.set_xticklabels(
    cross_table.columns,
    rotation=40,
    ha="right"
)

ax_heatmap.set_yticks(
    range(len(cross_table.index))
)

ax_heatmap.set_yticklabels(
    cross_table.index
)

for row in range(
    len(cross_table.index)
):

    for column in range(
        len(cross_table.columns)
    ):

        value = cross_table.iloc[
            row,
            column
        ]

        if value > 0:

            ax_heatmap.text(
                column,
                row,
                str(value),
                ha="center",
                va="center"
            )

fig_heatmap.colorbar(
    image,
    ax=ax_heatmap,
    label="Number of Papers"
)

plt.tight_layout()

st.pyplot(
    fig_heatmap
)

fig_heatmap.savefig(
    OUTPUT_DIR / "topic_vs_operation.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close(fig_heatmap)


# ============================================================
# DIFFERENT TOPICS — SAME OPERATION
# ============================================================

st.header(
    "6. Different Topics → Same Operation"
)

cross_topic_findings = []

for operation, group in filtered_df.groupby(
    "Operation"
):

    topics = group["Topic"].unique()

    if len(topics) > 1:

        cross_topic_findings.append(
            (
                operation,
                group
            )
        )


if cross_topic_findings:

    for operation, group in cross_topic_findings:

        st.subheader(
            f"🔗 {operation}"
        )

        st.write(
            "This operation appears across "
            "multiple research topics:"
        )

        for _, row in group.iterrows():

            st.write(
                f"• **{row['Method']}** "
                f"— {row['Topic']}"
            )

else:

    st.info(
        "No cross-topic shared operation was found "
        "under the current filters."
    )


# ============================================================
# SAME TOPIC — DIFFERENT OPERATIONS
# ============================================================

st.header(
    "7. Same Topic → Different Operations"
)

same_topic_findings = []

for topic, group in filtered_df.groupby(
    "Topic"
):

    operations = group["Operation"].unique()

    if len(operations) > 1:

        same_topic_findings.append(
            (
                topic,
                group
            )
        )


if same_topic_findings:

    for topic, group in same_topic_findings:

        st.subheader(
            f"🔀 {topic}"
        )

        st.write(
            "This topic contains methods "
            "with different operations:"
        )

        for _, row in group.iterrows():

            st.write(
                f"• **{row['Method']}** "
                f"→ {row['Operation']}"
            )

else:

    st.info(
        "No same-topic operation differences "
        "were found under the current filters."
    )


# ============================================================
# FORMAL SUPPORT
# ============================================================

st.header(
    "8. Formal Proof / Theorem Support"
)

proof_counts = (
    filtered_df["Formal Support"]
    .value_counts()
)

fig_proof, ax_proof = plt.subplots(
    figsize=(9, 5)
)

proof_counts.plot(
    kind="bar",
    ax=ax_proof
)

ax_proof.set_title(
    "Formal Support Across the 10 Papers"
)

ax_proof.set_xlabel(
    "Formal Support"
)

ax_proof.set_ylabel(
    "Number of Papers"
)

plt.xticks(
    rotation=25,
    ha="right"
)

plt.tight_layout()

st.pyplot(
    fig_proof
)

fig_proof.savefig(
    OUTPUT_DIR / "formal_support.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close(fig_proof)


# ============================================================
# INDIVIDUAL PAPER EXPLORER
# ============================================================

st.header(
    "9. Individual Paper Explorer"
)

selected_method = st.selectbox(
    "Select a method",
    filtered_df["Method"].tolist()
)

selected = filtered_df[
    filtered_df["Method"]
    ==
    selected_method
].iloc[0]


col1, col2 = st.columns(2)

with col1:

    st.write(
        f"**Method:** {selected['Method']}"
    )

    st.write(
        f"**Paper ID:** {selected['Paper ID']}"
    )

    st.write(
        f"**Topic:** {selected['Topic']}"
    )

with col2:

    st.write(
        f"**Operation:** {selected['Operation']}"
    )

    st.write(
        f"**Formal Support:** "
        f"{selected['Formal Support']}"
    )

    st.write(
        f"**arXiv Categories:** "
        f"{selected['arXiv Categories']}"
    )


st.subheader(
    "Objects"
)

st.write(
    selected["Objects"]
)


st.subheader(
    "Assumptions"
)

st.write(
    selected["Assumptions"]
)


st.subheader(
    "Guarantees"
)

st.write(
    selected["Guarantees"]
)


# ============================================================
# FULL DATA TABLE
# ============================================================

st.header(
    "10. Full Research Dataset"
)

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True
)


# ============================================================
# SAVE CSV
# ============================================================

csv_path = (
    OUTPUT_DIR /
    "paper_summary.csv"
)

filtered_df.to_csv(
    csv_path,
    index=False,
    encoding="utf-8"
)


# ============================================================
# GENERATE MARKDOWN REPORT
# ============================================================

report_path = (
    OUTPUT_DIR /
    "analysis_report.md"
)

with open(
    report_path,
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "# Python-Based Analysis of the 10-Paper Extension\n\n"
    )

    report.write(
        "## Dataset\n\n"
    )

    report.write(
        f"Number of papers analysed: "
        f"{len(filtered_df)}\n\n"
    )

    report.write(
        "## Topic Distribution\n\n"
    )

    for topic, count in topic_counts.items():

        report.write(
            f"- {topic}: {count}\n"
        )

    report.write(
        "\n## Operation Distribution\n\n"
    )

    for operation, count in operation_counts.items():

        report.write(
            f"- {operation}: {count}\n"
        )

    report.write(
        "\n## Different Topics Sharing the Same Operation\n\n"
    )

    if cross_topic_findings:

        for operation, group in cross_topic_findings:

            report.write(
                f"### {operation}\n\n"
            )

            for _, row in group.iterrows():

                report.write(
                    f"- {row['Method']} "
                    f"({row['Topic']})\n"
                )

            report.write("\n")

    else:

        report.write(
            "No cross-topic shared operation found.\n"
        )

    report.write(
        "\n## Same Topic Using Different Operations\n\n"
    )

    if same_topic_findings:

        for topic, group in same_topic_findings:

            report.write(
                f"### {topic}\n\n"
            )

            for _, row in group.iterrows():

                report.write(
                    f"- {row['Method']} "
                    f"→ {row['Operation']}\n"
                )

            report.write("\n")

    else:

        report.write(
            "No same-topic operation difference found.\n"
        )

    report.write(
        "\n## Interpretation\n\n"
    )

    report.write(
        "The Python analysis provides a reproducible "
        "comparison between topical classification and "
        "formal operation-based classification. The "
        "results can reveal cases where methods from "
        "different research areas share similar underlying "
        "operations, as well as cases where methods within "
        "the same topic use different operations.\n"
    )


# ============================================================
# DOWNLOAD SECTION
# ============================================================

st.header(
    "11. Download Analysis Results"
)

with open(
    csv_path,
    "rb"
) as file:

    st.download_button(
        label="⬇️ Download CSV",
        data=file,
        file_name="paper_summary.csv",
        mime="text/csv"
    )


with open(
    report_path,
    "rb"
) as file:

    st.download_button(
        label="⬇️ Download Markdown Report",
        data=file,
        file_name="analysis_report.md",
        mime="text/markdown"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Python + Streamlit analysis | "
    "Knowledge Discovery | 10-paper extension"
)
