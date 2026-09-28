# By Objects — 10 New Papers

I looked at what each paper actually works on, not what it's used for.

- A plain sequence of words with no fixed structure: Transformer
- A bag of items with no order between them: ABMIL
- A group of points plus a graph that gets rebuilt as the network learns: DGCNN
- A stored set of memory patterns and a query: Hopfield
- Just a raw set of 3D points: PointNet
- A group of objects, but looked at two at a time: Relation Networks
- A table with rows and columns (patches and channels): MLP-Mixer
- A graph, where each neighbor's info is treated as a group that can repeat: GIN
- A set of input-output pairs plus some new inputs to predict: CNP
- Atoms in 3D space, each with a position and a charge: SchNet

Most of these end up being "a plain unordered group of things" or "a group of
things with some extra structure attached, like a graph." MLP-Mixer is the
odd one out — it's the only one that isn't really a set at all, just a fixed
table.