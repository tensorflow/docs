

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.get_distribution_strategy

``` python
tf.contrib.distribute.get_distribution_strategy()
```



Defined in [`tensorflow/python/training/distribute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/training/distribute.py).

Returns the current `DistributionStrategy` object.

Prefer to use `get_tower_context()` or `get_cross_tower_context()`
instead when possible.

#### Returns:

A `DistributionStrategy` object. Inside a
`with distribution_strategy.scope()` block, it returns
`distribution_strategy`, otherwise it returns the default
(single-tower) `DistributionStrategy` object.