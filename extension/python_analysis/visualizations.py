"""Reusable plotting functions for the Streamlit dashboard."""

import matplotlib.pyplot as plt
import pandas as pd


def create_distribution_figure(dataframe, column, title):
    counts = dataframe[column].value_counts()
    fig, ax = plt.subplots(figsize=(10, 5))
    counts.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(column)
    ax.set_ylabel("Number of Papers")
    ax.tick_params(axis="x", labelrotation=35)
    fig.tight_layout()
    return fig


def create_topic_operation_heatmap(dataframe):
    cross_table = pd.crosstab(dataframe["Topic"], dataframe["Operation"])
    fig, ax = plt.subplots(figsize=(13, 7))
    image = ax.imshow(cross_table.values, aspect="auto")
    ax.set_title("Topic × Operation Relationship")
    ax.set_xticks(range(len(cross_table.columns)))
    ax.set_xticklabels(cross_table.columns, rotation=40, ha="right")
    ax.set_yticks(range(len(cross_table.index)))
    ax.set_yticklabels(cross_table.index)

    for row in range(len(cross_table.index)):
        for column in range(len(cross_table.columns)):
            value = cross_table.iloc[row, column]
            if value:
                ax.text(column, row, str(value), ha="center", va="center")

    fig.colorbar(image, ax=ax, label="Number of Papers")
    fig.tight_layout()
    return fig
