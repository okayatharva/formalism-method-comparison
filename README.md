# Formalism Structure & Grouping

This project explores whether scientific methods can be compared and grouped by their underlying formal structure rather than only by their research topic.

The project has two distinct parts:

1. **Original research:** An analysis of six scientific papers.
2. **Research extension:** A separate analysis of ten additional scientific papers.

The original six-paper research and the ten-paper extension are maintained separately. Their research records, groupings, and findings should not be treated as one combined dataset.

## Original Research — Six Papers

The original research examines four aspects of formalism:

- Objects
- Assumptions
- Guarantees
- Operations

Methods are compared by objects, assumptions, and operations to investigate similarities across research topics.

The original research records and grouping results remain in their existing locations.

## Research Extension — Ten Additional Papers

The extension investigates whether patterns identified in the original research also appear in ten additional papers.

The extension includes:
- Ten additional JSON research records
- Separate grouping and comparison results
- An extension research write-up
- A Python and Streamlit dashboard
- Automated tests for the Python analysis modules

The extension dashboard reads only the ten records in `extension/records/`. It does not combine them with the original six-paper dataset.

## Repository Structure

```text
formalism-method-comparison/
├── records/                       # Original six-paper records
├── groupings/                     # Original research groupings
├── extension/
│   ├── records/                   # Ten additional paper records
│   ├── groupings/                 # Extension-only groupings
│   ├── extension_writeup.md       # Ten-paper extension write-up
│   ├── README.md                  # Extension documentation
│   └── python_analysis/
│       ├── app.py                 # Streamlit dashboard
│       ├── config.py              # Configuration and paths
│       ├── data_loader.py         # JSON record loading
│       ├── analysis.py            # Analysis and DataFrame creation
│       ├── validation.py          # Dataset validation
│       ├── grouping_analysis.py   # Grouping comparisons
│       ├── visualizations.py      # Charts and heatmap
│       ├── exports.py             # Analysis exports
│       └── output/                # Generated dashboard outputs
└── tests/                         # Automated tests
```

## Run the Ten-Paper Extension Dashboard

From the repository root, create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Start the dashboard:

```bash
streamlit run extension/python_analysis/app.py
```

Streamlit will print the local URL to open in your browser.

## Run the Automated Tests

From the repository root:

```bash
python -m pip install pytest
PYTHONPATH=extension/python_analysis python -m pytest tests/ -v
```

The tests cover data loading, analysis fields, grouping findings, and dataset validation.

## Scope and Limitations

Both parts of the project investigate formal structures in selected scientific papers. The extension is a separate exploratory analysis of ten additional papers, not a merged reanalysis of all sixteen papers.

Topic and operation labels depend on interpreting each paper's formalism. Similar operation labels do not necessarily mean that two methods are mathematically identical. Formal proof or theorem support should also be distinguished from mathematical properties and empirical performance claims.
