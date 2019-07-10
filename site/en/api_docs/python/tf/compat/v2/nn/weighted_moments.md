page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.nn.weighted_moments

Returns the frequency-weighted mean and variance of `x`.

``` python
tf.compat.v2.nn.weighted_moments(
    x,
    axes,
    frequency_weights,
    keepdims=False,
    name=None
)
```



Defined in [`python/ops/nn_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_impl.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A tensor.
* <b>`axes`</b>: 1-d tensor of int32 values; these are the axes along which
  to compute mean and variance.
* <b>`frequency_weights`</b>: A tensor of positive weights which can be
  broadcast with x.
* <b>`keepdims`</b>: Produce moments with the same dimensionality as the input.
* <b>`name`</b>: Name used to scope the operation.


#### Returns:

Two tensors: `weighted_mean` and `weighted_variance`.
