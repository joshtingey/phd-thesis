---
tags: [ref]
title: cacm12
created: '2020-05-13T06:37:38.813Z'
modified: '2020-05-14T14:05:42.417Z'
---

# cacm12

## [A few useful things to know about machine learning](https://dl.acm.org/doi/pdf/10.1145/2347736.2347755)

@article{domingos2012few,
  title={A few useful things to know about machine learning},
  author={Domingos, Pedro},
  journal={Communications of the ACM},
  volume={55},
  number={10},
  pages={78--87},
  year={2012},
  publisher={ACM New York, NY, USA}
}

- Using cleverer algorithms has a smaller pay-off than you might expect, as to first order they all do the same thing, essentially grouping nearby examples into the same class.
- A dumb algorithm with lots of data tends to beat a clever one with modest amounts of it.
- You should try the simplest learners first. Decision tress before neural network before Convolutional neural networks.
- Combining different models in an ensemble greatly reduces variance while only slightly increasing bias (bagging, boosting, stacking).
- Few learners search their hypothesis space fully. Therefore, a learner with a large hypothesis space that tries fewer hypotheses from it is less likely to overfit than one that tries more hypotheses from a smaller space.
