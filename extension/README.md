# Extension Folder

This folder is a follow up to my main write up. My original analysis was based on just six papers, and I found one interesting pair, GAT and ViT, that looked completely unrelated by subject but turned out to do the same thing underneath. Since this was based on only one example, I wanted to check if it was actually a pattern or just luck.

For this part, I picked 10 more papers on purpose. Some were chosen to check if the same attention pattern appears again in completely different fields, and some were chosen to see if my grouping system works for papers that do not fit into my original categories.

## What's in here

`records/` contains the JSON records for the 10 new papers, using the same format as my original six, with one extra field called `has_formal_proof` because the professor specifically asked me to check if this mattered.

`groupings/` contains the same type of grouping I did before, by objects, assumptions, operation, topic, and a comparison table. I did this only on the 10 new papers so that I could test the pattern separately instead of mixing the old and new papers together.

`extension_writeup.md` contains my full write up of what I found, what surprised me, and what I would still want to check.

## Short version of what I found

Three of the 10 new papers, one about translating language, one about reading medical scans, and one about modeling memory, all turned out to use the same basic idea: learning how much to trust each piece of information instead of treating everything equally.

These three fields are very different from each other. For me, this is the strongest evidence so far that my original GAT and ViT finding was not just a coincidence.
