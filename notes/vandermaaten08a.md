---
tags: [paper]
title: vandermaaten08a
created: '2020-05-13T06:41:25.499Z'
modified: '2020-05-13T07:23:10.178Z'
---

# vandermaaten08a

- There have been plently of attempts at visualising high-dimensional data on a 2/3 dimensional map, including Sammon mapping, Isomap, Locally Linear Embedding, Stochastic Neighbour Embedding.
- Older implementations tended to cluster all data points towards the centre of the map and proved difficult to optimise.
- You basically set a summed probability between all points in the low-dimensional space to a summed probability between all points in the high-dimensional space. 
- t-SNE uses the student-t distribution (with a heavy tail) in the low-dimensional space to calculate the probability. This alleviates both the crowding problem and is easier to optimise.
- Optimisation uses a simple momentum term, plus two new ideas. "Early compression" which forces map points to stay close to each other at the start of optimisation, it is then easier for clusters to move through each other and explore all possible global organisations of the data, this is implemented as an L2-penalty term proportional to the sum of squared distances from the origin, this is then removed at an iteration given as input. Secondly, "Early exaggeration" which creates tight widely seperated clusters.
