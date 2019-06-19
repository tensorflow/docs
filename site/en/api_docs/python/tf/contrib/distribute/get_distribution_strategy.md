page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.get_distribution_strategy

``` python
tf.contrib.distribute.get_distribution_strategy()
```



Defined in [`tensorflow/python/training/distribute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/training/distribute.py).

Returns the current `DistributionStrategy` object.

Prefer to use `get_tower_context()` or `get_cross_tower_context()`
instead when possible.

#### Returns:

A `DistributionStrategy` object. Inside a
`with distribution_strategy.scope()` block, it returns
`distribution_strategy`, otherwise it returns the default
(single-tower) `DistributionStrategy` object.