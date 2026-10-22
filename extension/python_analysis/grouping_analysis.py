"""Find shared operations and within-topic operation differences."""

def find_cross_topic_operations(dataframe):
    findings = []

    for operation, group in dataframe.groupby("Operation", dropna=False):
        if group["Topic"].nunique(dropna=False) > 1:
            findings.append((operation, group))

    return findings


def find_same_topic_different_operations(dataframe):
    findings = []

    for topic, group in dataframe.groupby("Topic", dropna=False):
        if group["Operation"].nunique(dropna=False) > 1:
            findings.append((topic, group))

    return findings
