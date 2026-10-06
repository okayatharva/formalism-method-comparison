# Python-Based Analysis of the 10-Paper Extension

## Dataset

Number of papers analysed: 10

## Topic Distribution

- 3D Vision: 2
- Memory Networks: 1
- Visual / Text / Physics QA: 1
- Computer Vision: 1
- Graph Learning: 1
- Regression / Meta-Learning: 1
- Computational Chemistry: 1
- NLP: 1
- Medical Imaging: 1

## Operation Distribution

- Learned Attention: 3
- Neighbor Aggregation: 2
- Max Aggregation: 1
- Pairwise Comparison: 1
- Axis Mixing: 1
- Encode-Average-Decode: 1
- Distance-Based Weighting: 1

## Different Topics Sharing the Same Operation

### Learned Attention

- Continuous Modern Hopfield Network (Memory Networks)
- Transformer (Attention Is All You Need) (NLP)
- Attention-based (Gated-)Attention MIL Pooling (Medical Imaging)

### Neighbor Aggregation

- EdgeConv (Dynamic Graph CNN / DGCNN) (3D Vision)
- Graph Isomorphism Network (GIN) (Graph Learning)


## Same Topic Using Different Operations

### 3D Vision

- EdgeConv (Dynamic Graph CNN / DGCNN) → Neighbor Aggregation
- PointNet → Max Aggregation


## Interpretation

The Python analysis provides a reproducible comparison between topical classification and formal operation-based classification. The results can reveal cases where methods from different research areas share similar underlying operations, as well as cases where methods within the same topic use different operations.
