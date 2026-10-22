"""Export the analysis results to CSV and Markdown."""

from pathlib import Path


def export_csv(dataframe, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False, encoding="utf-8")
    return output_path


def export_markdown_report(
    dataframe,
    output_path,
    cross_topic_findings=None,
    same_topic_findings=None,
):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    topic_counts = dataframe["Topic"].value_counts()
    operation_counts = dataframe["Operation"].value_counts()

    with output_path.open("w", encoding="utf-8") as report:
        report.write("# Python-Based Analysis of the 10-Paper Extension\n\n")
        report.write(f"Number of papers analysed: {len(dataframe)}\n\n")

        report.write("## Topic Distribution\n\n")
        for topic, count in topic_counts.items():
            report.write(f"- {topic}: {count}\n")

        report.write("\n## Operation Distribution\n\n")
        for operation, count in operation_counts.items():
            report.write(f"- {operation}: {count}\n")

        report.write("\n## Different Topics Sharing the Same Operation\n\n")
        for operation, group in cross_topic_findings or []:
            report.write(f"### {operation}\n\n")
            for _, row in group.iterrows():
                report.write(f"- {row['Method']} ({row['Topic']})\n")
            report.write("\n")

        report.write("\n## Same Topic Using Different Operations\n\n")
        for topic, group in same_topic_findings or []:
            report.write(f"### {topic}\n\n")
            for _, row in group.iterrows():
                report.write(f"- {row['Method']} → {row['Operation']}\n")
            report.write("\n")

        report.write(
            "\n## Interpretation\n\n"
            "This analysis compares topic labels with operation-based "
            "classifications to identify shared operations across topics "
            "and differing operations within a topic.\n"
        )

    return output_path
