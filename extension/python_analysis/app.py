"""Streamlit dashboard for the formalism-method comparison extension."""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from analysis import build_dataframe
from config import EXPECTED_PAPERS, OUTPUT_DIR, RECORDS_DIR
from data_loader import load_records
from exports import export_csv, export_markdown_report
from grouping_analysis import (
    find_cross_topic_operations,
    find_same_topic_different_operations,
)
from validation import validate_dataset
from visualizations import (
    create_distribution_figure,
    create_topic_operation_heatmap,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Formalism Analysis - 10 Paper Extension",
    page_icon="📚",
    layout="wide",
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# LOAD AND PREPARE DATA
# ============================================================

records, warnings = load_records(RECORDS_DIR)
df = build_dataframe(records)

st.title("📚 Formalism-Based Analysis")
st.subheader("10-Paper Extension — Knowledge Discovery")

st.markdown(
    """
This dashboard analyses the ten additional scientific papers
researched for the formalism-method comparison extension.

It uses the existing JSON records as input and does not modify
the original research data.
"""
)

st.info(f"Input folder: `{RECORDS_DIR}`")

for warning in warnings:
    st.warning(warning)

if not RECORDS_DIR.is_dir():
    st.error("The research records directory is missing.")
    st.stop()

if df.empty:
    st.error("No valid research records were loaded. Check the JSON files.")
    st.stop()


# ============================================================
# DATASET VALIDATION
# ============================================================

validation = validate_dataset(df, set(EXPECTED_PAPERS))

if validation["missing_ids"]:
    st.warning(
        "Expected paper IDs not found: "
        + ", ".join(sorted(validation["missing_ids"]))
    )

if validation["extra_ids"]:
    st.info(
        "Additional paper IDs found: "
        + ", ".join(sorted(validation["extra_ids"]))
    )


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.title("Dashboard Filters")

topic_options = sorted(df["Topic"].dropna().unique().tolist())
operation_options = sorted(df["Operation"].dropna().unique().tolist())

selected_topics = st.sidebar.multiselect(
    "Topics",
    topic_options,
    default=topic_options,
)

selected_operations = st.sidebar.multiselect(
    "Operations",
    operation_options,
    default=operation_options,
)

filtered_df = df[
    df["Topic"].isin(selected_topics)
    & df["Operation"].isin(selected_operations)
].copy()


# ============================================================
# KEY METRICS
# ============================================================

st.header("1. Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Papers", len(filtered_df))

with col2:
    st.metric("Topics", filtered_df["Topic"].nunique())

with col3:
    st.metric("Operations", filtered_df["Operation"].nunique())

with col4:
    proof_count = (
        filtered_df["Formal Support"] == "Formal proof / theorem"
    ).sum()
    st.metric("Formal Proofs", int(proof_count))

if filtered_df.empty:
    st.warning("No papers match the selected filters.")
    st.info("Select one or more topics and operations in the sidebar.")


# ============================================================
# RESEARCHED PAPERS
# ============================================================

st.header("2. Researched Papers")

display_columns = [
    "Method",
    "Paper ID",
    "Topic",
    "Operation",
    "Formal Support",
]

st.dataframe(
    filtered_df[display_columns],
    width="stretch",
    hide_index=True,
)


# ============================================================
# TOPIC DISTRIBUTION
# ============================================================

st.header("3. Topic Distribution")

if not filtered_df.empty:
    fig_topic = create_distribution_figure(
        filtered_df,
        "Topic",
        "Distribution of Papers by Topic",
    )

    st.pyplot(fig_topic)
    fig_topic.savefig(
        OUTPUT_DIR / "topic_distribution.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close(fig_topic)
else:
    st.info("Topic distribution is unavailable for an empty selection.")


# ============================================================
# OPERATION DISTRIBUTION
# ============================================================

st.header("4. Operation Distribution")

if not filtered_df.empty:
    fig_operation = create_distribution_figure(
        filtered_df,
        "Operation",
        "Distribution of Papers by Underlying Operation",
    )

    st.pyplot(fig_operation)
    fig_operation.savefig(
        OUTPUT_DIR / "operation_distribution.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close(fig_operation)
else:
    st.info("Operation distribution is unavailable for an empty selection.")


# ============================================================
# TOPIC × OPERATION HEATMAP
# ============================================================

st.header("5. Topic × Operation Relationship")

st.markdown(
    """
This comparison helps identify:

- Different topics that share the same operation.
- The same topic using different operations.
"""
)

if not filtered_df.empty:
    fig_heatmap = create_topic_operation_heatmap(filtered_df)
    st.pyplot(fig_heatmap)
    fig_heatmap.savefig(
        OUTPUT_DIR / "topic_vs_operation.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close(fig_heatmap)
else:
    st.info("The heatmap is unavailable for an empty selection.")


# ============================================================
# DIFFERENT TOPICS — SAME OPERATION
# ============================================================

st.header("6. Different Topics → Same Operation")

cross_topic_findings = find_cross_topic_operations(filtered_df)

if cross_topic_findings:
    for operation, group in cross_topic_findings:
        st.subheader(f"🔗 {operation}")
        st.write("This operation appears across multiple research topics:")

        for _, row in group.iterrows():
            st.write(f"• **{row['Method']}** — {row['Topic']}")
else:
    st.info(
        "No cross-topic shared operation was found under the current filters."
    )


# ============================================================
# SAME TOPIC — DIFFERENT OPERATIONS
# ============================================================

st.header("7. Same Topic → Different Operations")

same_topic_findings = find_same_topic_different_operations(filtered_df)

if same_topic_findings:
    for topic, group in same_topic_findings:
        st.subheader(f"🔀 {topic}")
        st.write("This topic contains methods with different operations:")

        for _, row in group.iterrows():
            st.write(f"• **{row['Method']}** → {row['Operation']}")
else:
    st.info(
        "No same-topic operation differences were found under the current filters."
    )


# ============================================================
# FORMAL SUPPORT
# ============================================================

st.header("8. Formal Proof / Theorem Support")

if not filtered_df.empty:
    fig_proof = create_distribution_figure(
        filtered_df,
        "Formal Support",
        "Formal Support Across the Selected Papers",
    )

    st.pyplot(fig_proof)
    fig_proof.savefig(
        OUTPUT_DIR / "formal_support.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close(fig_proof)
else:
    st.info("Formal-support analysis is unavailable for an empty selection.")


# ============================================================
# INDIVIDUAL PAPER EXPLORER
# ============================================================

st.header("9. Individual Paper Explorer")

if not filtered_df.empty:
    selected_method = st.selectbox(
        "Select a method",
        filtered_df["Method"].tolist(),
    )

    selected = filtered_df[
        filtered_df["Method"] == selected_method
    ].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Method:** {selected['Method']}")
        st.write(f"**Paper ID:** {selected['Paper ID']}")
        st.write(f"**Topic:** {selected['Topic']}")

    with col2:
        st.write(f"**Operation:** {selected['Operation']}")
        st.write(f"**Formal Support:** {selected['Formal Support']}")
        st.write(f"**arXiv Categories:** {selected['arXiv Categories']}")

    st.subheader("Objects")
    st.write(selected["Objects"] or "Not specified")

    st.subheader("Assumptions")
    st.write(selected["Assumptions"] or "Not specified")

    st.subheader("Guarantees")
    st.write(selected["Guarantees"] or "Not specified")
else:
    st.info("Select papers in the sidebar to use the paper explorer.")


# ============================================================
# FULL RESEARCH DATASET
# ============================================================

st.header("10. Full Research Dataset")

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True,
)


# ============================================================
# EXPORT CSV AND MARKDOWN REPORT
# ============================================================

csv_path = export_csv(
    filtered_df,
    OUTPUT_DIR / "paper_summary.csv",
)

report_path = export_markdown_report(
    filtered_df,
    OUTPUT_DIR / "analysis_report.md",
    cross_topic_findings,
    same_topic_findings,
)


# ============================================================
# DOWNLOAD ANALYSIS RESULTS
# ============================================================

st.header("11. Download Analysis Results")

with csv_path.open("rb") as file:
    st.download_button(
        label="⬇️ Download CSV",
        data=file.read(),
        file_name="paper_summary.csv",
        mime="text/csv",
    )

with report_path.open("rb") as file:
    st.download_button(
        label="⬇️ Download Markdown Report",
        data=file.read(),
        file_name="analysis_report.md",
        mime="text/markdown",
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.caption(
    "Python + Streamlit analysis | "
    "Knowledge Discovery | 10-paper extension"
)
