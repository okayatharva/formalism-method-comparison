# Ten-Paper Research Extension

This folder contains a separate extension to the original formalism-method comparison research.

The original research examined six scientific papers. This extension examines ten additional papers to investigate whether similar formal operations appear across different research topics.

**Important:** The extension analyses only its ten additional papers. It does not merge its records or grouping results with those of the original six-paper research.

## Research Questions

- Do different research topics use similar underlying operations?
- Can methods within the same topic use different operations?
- What do objects, assumptions, and guarantees reveal about the structure of a method?
- What formal proof or theorem support is reported in the selected papers?

## Contents

- `records/` — JSON records for the ten additional papers, including the `has_formal_proof` field.
- `groupings/` — Grouping and comparison results for the ten-paper extension only.
- `extension_writeup.md` — The extension's research discussion, findings, and limitations.
- `python_analysis/` — The Python modules, Streamlit dashboard, and generated analysis outputs.

## Main Observations

In this ten-paper extension, Learned Attention appears in selected methods from Memory Networks, NLP, and Medical Imaging. Neighbor Aggregation appears in selected methods from 3D Vision and Graph Learning.

The extension also identifies different operations among the selected 3D Vision methods: Neighbor Aggregation and Max Aggregation.

These are exploratory observations from the selected ten papers. A shared label does not by itself establish that two methods are mathematically equivalent or that the patterns generalize to all research fields.

## Run the Dashboard

From the repository root:

```bash
python -m pip install -r requirements.txt
streamlit run extension/python_analysis/app.py
```

## Run the Tests

From the repository root:

```bash
python -m pip install pytest
PYTHONPATH=extension/python_analysis python -m pytest tests/ -v
```

## Data Integrity and Limitations

The dashboard reads JSON files from this extension's `records/` directory. The original six-paper records and their analysis remain separate and should not be modified by the extension workflow.

The ten papers form a limited, selected sample. Topic and operation labels should be interpreted in the context of the definitions and assumptions in the original papers. Formal proofs, mathematical properties, and empirical results are distinct kinds of evidence.
