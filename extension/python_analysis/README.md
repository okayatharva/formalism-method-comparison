# Python-Based Formalism Analysis

This folder contains the Python and Streamlit analysis of the **ten additional papers** in the research extension.

The application reads the JSON records from `extension/records/`. It analyses this extension dataset only; it does not combine the ten papers with the original six-paper research dataset.

## Run the Dashboard

From the repository root:

```bash
python -m pip install -r requirements.txt
streamlit run extension/python_analysis/app.py
```

Alternatively, from this directory:

```bash
streamlit run app.py
```

Streamlit prints the local URL when the server starts.

## Module Structure

- `app.py` — Streamlit interface and dashboard workflow.
- `config.py` — Expected paper IDs, category mappings, and project paths.
- `data_loader.py` — Loads JSON records and reports loading problems.
- `analysis.py` — Converts records into a tabular dataset and prepares analysis fields.
- `validation.py` — Checks record counts and expected paper IDs.
- `grouping_analysis.py` — Identifies operations shared across topics and topics with different operations.
- `visualizations.py` — Creates distribution charts and the topic-operation heatmap.
- `exports.py` — Writes analysis results and Markdown reports.

The modules separate interface, configuration, data loading, analysis, validation, grouping, visualization, and export responsibilities. This modular structure makes the implementation easier to inspect and maintain.

## Input Data

The application reads the ten additional JSON records from:

```text
extension/records/
```

The original six-paper records and their grouping results remain separate.

## Dashboard Sections

1. Dataset overview.
2. Researched papers.
3. Topic distribution.
4. Operation distribution.
5. Topic-operation relationship.
6. Different topics sharing an operation.
7. Different operations within the same topic.
8. Formal proof or theorem support.
9. Individual paper explorer.
10. Full research dataset.
11. Analysis downloads.

## Run Automated Tests

From the repository root:

```bash
python -m pip install pytest
PYTHONPATH=extension/python_analysis python -m pytest tests/ -v
```

The tests cover data loading, analysis fields, grouping findings, and dataset validation.

## Interpretation Notes

This dashboard explores ten selected papers. Topic and operation labels are research classifications and must be interpreted in the context of each paper's formal definitions.

A formal proof or theorem should not be inferred solely from empirical results or from a mathematical property described without an explicit proof. The dashboard's findings are exploratory and should not be treated as universal conclusions.
