page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distributions.kl_divergence

Get the KL-divergence KL(distribution_a || distribution_b). (deprecated)

### Aliases:

* `tf.compat.v1.distributions.kl_divergence`
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



Defined in [`python/ops/distributions/kullback_leibler.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/distributions/kullback_leibler.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2019-01-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of <a href="../../tf/distributions"><code>tf.distributions</code></a>.

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