# By Assumptions — 10 New Papers

Five out of these 10 papers say directly that their method has to give the
same answer no matter what order you feed the data in. That's ABMIL, DGCNN,
PointNet, GIN, and CNP.

The Transformer paper doesn't state anything like this at all — it just
describes the architecture.

Hopfield needs its patterns to be spread out enough from each other for its
proofs to actually work.

Relation Networks assumes it doesn't know ahead of time which pairs of
things are actually related — it has to figure that out on its own.

MLP-Mixer assumes the same weights get reused across positions, and it
skips position embeddings on purpose.

SchNet assumes basic physics facts — rotating or moving a molecule shouldn't
change its predicted energy.

Seeing that half these new papers repeat the same "order shouldn't matter"
assumption I found in my first six papers made me more confident this isn't
just something I noticed by chance.