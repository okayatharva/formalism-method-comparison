# Formalism Structure & Grouping — Write-up

## 1. Extraction

I first read the abstract, introduction, and method section of each paper to understand the basic idea of the method. I then used AI to help create a first draft of the JSON fields and checked the important details and evidence against the original papers.

While checking the papers, I noticed that AI can sometimes give details that sound correct but are not exactly from the paper. For example, in the Deep Sets record, I had to correct the section and wording after checking the original paper.

I also noticed that not every paper has the same type of assumptions or guarantees. Some have theoretical results, while others mainly have experimental results. I kept these differences instead of forcing all the records to follow the same structure.

## 2. The Three Groupings

**By objects:**

* GCN, GraphSAGE, GAT → graphs with nodes, edges, and features.
* PointNet++ → metric space of points.
* ViT, Deep Sets → sets or sequences without a fixed graph structure.

**By assumptions:**

* GraphSAGE, PointNet++, Deep Sets → permutation invariance.
* GCN → locality and fixed graph structure.
* GAT → works with local neighborhoods and does not require the complete graph structure beforehand.
* ViT → has less built-in spatial structure than CNNs.

**By operation:**

* GCN → neighborhood aggregation using graph-based weights.
* GraphSAGE → sample, aggregate, and combine neighbor information.
* GAT, ViT → learned attention.
* PointNet++ → hierarchical local grouping.
* Deep Sets → sum-pooling.

The three groupings give different results because each one looks at a different part of the method.

## 3. Formal vs. Topical

| Method     | Topical Group   | By Objects             | By Assumptions               | By Operation             |
| ---------- | --------------- | ---------------------- | ---------------------------- | ------------------------ |
| GCN        | Graph learning  | Graph w/ features      | Locality, fixed structure    | Fixed-weight aggregation |
| GraphSAGE  | Graph learning  | Graph w/ features      | Permutation invariance       | Sample + aggregate       |
| GAT        | Graph learning  | Graph w/ features      | Local neighborhood attention | Learned attention        |
| PointNet++ | Computer vision | Metric space of points | Permutation invariance       | Hierarchical grouping    |
| ViT        | Computer vision | Sequence of patches    | Less inductive bias than CNN | Learned attention        |
| Deep Sets  | General ML      | Set of elements        | Permutation invariance       | Sum-pooling              |

**Together topically, apart formally:** GCN and GAT are both graph-learning methods, but they use different operations. GCN uses graph-based aggregation, while GAT learns attention weights.

**Apart topically, together formally:** GAT and ViT are from different areas, but both use learned attention to combine information from different elements. This was the most interesting similarity I found.

**Which axis disagrees most with topic:** I think **operation** disagrees the most with topic because it connects GAT with ViT even though they belong to different topical groups.

## 4. My Recommendation

I would choose **operation** as an important grouping axis for the database.

It helped me find the GAT–ViT connection, which would probably be missed if we only grouped papers by topic.

However, the operation grouping is not perfect. PointNet++ does not have a close match in these six papers. More papers would be needed to see whether it has similar methods.

## 5. What I Would Do With More Time

With more time, I would first like to understand the formalism concepts better, especially how objects, assumptions, guarantees, and operations can be used to compare different methods.

I would also like to explore more papers and see if the same patterns that I found in these six papers appear in other methods. For example, I would like to learn more about attention, aggregation, permutation invariance, and other types of operations.

After understanding these concepts better, I would try the grouping on more papers and see whether the same groups still make sense. I would also try to make the grouping rules clearer so that they are easier to apply to new papers.

For a larger number of papers, I think AI could help with the first extraction, while the important information should still be checked against the original papers.