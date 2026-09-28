# Extension: Testing the Recommendation on 10 More Papers

## Why I did this

In my original write up, I recommended grouping methods by their operation because it helped me find something that topic based searching could miss. GAT, a graph paper, and ViT, a vision paper, looked very different, but they were doing a similar thing underneath.

But this was based on only one pair from six papers. So for this part, I picked 10 more papers to see if this pattern actually happens again or if it was just luck.

## What I picked and why

I did not pick these papers randomly. I picked:

More attention based papers from different fields, like the original Transformer paper from NLP, an attention based method for medical imaging, and a memory network paper, to see if the same pattern appears again.

More graph and point cloud papers, like PointNet, DGCNN, and GIN, to see if papers from the same topic can still use different operations.

A few papers that did not fit into my first five operation buckets, to see if my grouping system would still work with new papers.

## What I found

The attention pattern appeared again, and more than I expected. I found it in five different areas: graphs with GAT, vision with ViT, language with the Transformer, medical imaging with an attention based method for pathology slides, and a memory network paper.

The basic idea is the same in all of them. They give different importance to different pieces of information and then combine them based on that importance. The way they describe it changes depending on the field.

The most surprising part for me was the memory network paper. It does not just look similar to Transformer attention. It actually proves mathematically that its formula is the same as Transformer attention. So this was stronger than my original observation because the similarity is actually proven in the paper.

I also found something unexpected in GIN. It proves that summing neighbor information is better than averaging it, which is better than just taking the max. This helped explain why some of the papers I looked at earlier, such as PointNet and PointNet++, use an operation that can be weaker than sum based approaches.

Two of the new papers also did not fit my old buckets. I had to add a new bucket for distance based filtering in the molecule paper and another one for comparing pairs of things in the relational reasoning paper.

## A new pattern I noticed

While looking through all 16 papers, I noticed that papers using learned attention usually do not give a formal proof. They mainly show their results through experiments.

On the other hand, papers using max or sum based aggregation over a set are more likely to have a mathematical proof. This happened often enough that I think it is worth tracking separately from the operation bucket.

## My updated recommendation

I still think grouping by operation is the right choice. After looking at these 10 new papers, I am more confident about it.

I would also keep `has_formal_proof` as a separate field along with the operation bucket. These two things seem related, but they are not the same.

Two papers still do not fit neatly into the existing buckets: PointNet++ because of its step by step point grouping, and the molecule paper because of its distance based filtering. For now, I think this is a useful finding rather than a problem with the grouping. I would need more papers to know if these operations are actually rare or if I just have not found similar examples yet.
