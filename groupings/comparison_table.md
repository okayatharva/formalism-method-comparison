# Formal vs. Topical Comparison

| Method | Topical Group | By Objects | By Assumptions | By Operation |
|---|---|---|---|---|
| GCN | Graph learning | Graph w/ features | Locality, fixed structure | Fixed-weight averaging |
| GraphSAGE | Graph learning | Graph w/ features | Explicit permutation invariance | Sample+aggregate+concat |
| GAT | Graph learning | Graph w/ features | Relaxed graph-access requirement | Learned attention |
| PointNet++ | Computer vision | Metric space of points | Permutation invariance (inherited) | Hierarchical local grouping |
| ViT | Computer vision | Set/sequence, no graph | Less inductive bias than CNN | Learned attention |
| Deep Sets | General ML | Set, no graph | Explicit permutation invariance | Sum-pooling |

## Together topically, apart formally
GCN and GAT are both labeled as papers on graph learning, but their mechanisms of operation differ greatly, as GCN relies on averaging of the neighbors using fixed weight values that are based on graph topology, while GAT learns the neighbor attention weights.

## Apart topically, together formally
The GAT and ViT are not at all related to each other topic-wise. However, in both cases, we calculate the learned weights of attention on some set of elements and fuse the two using their relevance to each other, where GAT only uses the neighbors of the graph, while ViT uses all the patches.

## Which axis disagrees most with topic
**Operation** shows the most divergence. It separates the three “graph learning” papers into two different categories (GCN and nothing; GAT and ViT), and combines one graph paper with one vision paper. Objects and assumptions are looser with regard to the topic but still somehow align with it (the three graph papers share “graph” as an object; the metric space of PointNet++ is close to a graph without being one).