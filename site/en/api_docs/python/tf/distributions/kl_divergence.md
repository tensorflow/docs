page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distributions.kl_divergence

### Aliases:

* `tf.contrib.distributions.kl_divergence`
* `tf.distributions.kl_divergence`

``` python
tf.distributions.kl_divergence(
    distribution_a,
    distribution_b,
    allow_nan_stats=True,
    name=None
)
```



Defined in [`tensorflow/python/ops/distributions/kullback_leibler.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/distributions/kullback_leibler.py).

Get the KL-divergence KL(distribution_a || distribution_b).

If there is no KL method registered specifically for `type(distribution_a)`
and `type(distribution_b)`, then the class hierarchies of these types are
searched.

If one KL method is registered between any pairs of classes in these two
parent hierarchies, it is used.

If more than one such registered method exists, the method whose registered
classes have the shortest sum MRO paths to the input types is used.

If more than one such shortest path exists, the first method
identified in the search is used (favoring a shorter MRO distance to
`type(distribution_a)`).

#### Args:

* <b>`distribution_a`</b>: The first distribution.
* <b>`distribution_b`</b>: The second distribution.
* <b>`allow_nan_stats`</b>: Python `bool`, default `True`. When `True`,
    statistics (e.g., mean, mode, variance) use the value "`NaN`" to
    indicate the result is undefined. When `False`, an exception is raised
    if one or more of the statistic's batch members are undefined.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this class.


#### Returns:

A Tensor with the batchwise KL-divergence between `distribution_a`
and `distribution_b`.


#### Raises:

* <b>`NotImplementedError`</b>: If no KL method is defined for distribution types
    of `distribution_a` and `distribution_b`.