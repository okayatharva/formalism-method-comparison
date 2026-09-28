# Comparing Topic vs. Operation — 10 New Papers

| Method | Topic | Operation |
|---|---|---|
| Transformer | NLP | Learned attention |
| ABMIL | Medical imaging | Learned attention |
| Hopfield | Memory networks | Learned attention |
| DGCNN | 3D vision | Neighbor aggregation |
| PointNet | 3D vision | Max pooling |
| GIN | Graph theory | Neighbor aggregation |
| Relation Networks | Visual/text/physics QA | Pairwise comparison |
| MLP-Mixer | Vision (images) | Axis mixing |
| CNP | Regression | Encode-average-decode |
| SchNet | Chemistry | Distance-based weighting |

**Same topic, different operation:** DGCNN and PointNet are both "3D vision"
papers, but PointNet just takes the max over everything at once, while DGCNN
builds and rebuilds a local neighborhood graph as it learns. Same subject,
different math.

**Different topic, same operation — the one I'd point to first:**
Transformer, ABMIL, and Hopfield have nothing to do with each other by
subject, but all three learn to weigh some inputs more than others instead
of treating everything equally. That's the strongest evidence I found that
my original observation about GAT and ViT wasn't just a lucky coincidence.

**Bottom line:** sorting by operation disagreed with sorting by topic more
than any other way I tried. Almost every paper had its own separate
subject, yet three of them still ended up in the same operation group —
exactly the kind of thing a normal topic search would never catch.