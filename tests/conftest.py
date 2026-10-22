"""Make the dashboard modules importable during tests from the repository root."""
from pathlib import Path
import sys

# The application modules intentionally live together in this folder rather
# than being installed as a package. Add that folder to pytest's import path.
PYTHON_ANALYSIS_DIR = Path(__file__).resolve().parents[1] / "extension" / "python_analysis"
if str(PYTHON_ANALYSIS_DIR) not in sys.path:
    sys.path.insert(0, str(PYTHON_ANALYSIS_DIR))
