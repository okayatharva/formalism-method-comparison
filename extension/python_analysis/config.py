"""Central configuration for the formalism analysis project."""

from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = MODULE_DIR.parents[1]
EXTENSION_DIR = PROJECT_DIR / "extension"
RECORDS_DIR = EXTENSION_DIR / "records"
OUTPUT_DIR = MODULE_DIR / "output"

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
    "1807.01613": "CNP",
}

TOPIC_MAP = {
    "1706.08566": "Computational Chemistry",
    "1706.03762": "NLP",
    "1802.04712": "Medical Imaging",
    "1801.07829": "3D Vision",
    "2008.02217": "Memory Networks",
    "1612.00593": "3D Vision",
    "1706.01427": "Visual / Text / Physics QA",
    "2105.01601": "Computer Vision",
    "1810.00826": "Graph Learning",
    "1807.01613": "Regression / Meta-Learning",
}

OPERATION_MAP = {
    "1706.08566": "Distance-Based Weighting",
    "1706.03762": "Learned Attention",
    "1802.04712": "Learned Attention",
    "1801.07829": "Neighbor Aggregation",
    "2008.02217": "Learned Attention",
    "1612.00593": "Max Aggregation",
    "1706.01427": "Pairwise Comparison",
    "2105.01601": "Axis Mixing",
    "1810.00826": "Neighbor Aggregation",
    "1807.01613": "Encode-Average-Decode",
}
