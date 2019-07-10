page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.weighted_moments

Returns the frequency-weighted mean and variance of `x`.

### Aliases:

* `tf.compat.v1.nn.weighted_moments`
* `tf.nn.weighted_moments`

``` python
tf.nn.weighted_moments(
    x,
    axes,
    frequency_weights,
    name=None,
    keep_dims=None,
    keepdims=None
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
* <b>`name`</b>: Name used to scope the operation.
* <b>`keep_dims`</b>: Produce moments with the same dimensionality as the input.
* <b>`keepdims`</b>: Alias of keep_dims.


#### Returns:

Two tensors: `weighted_mean` and `weighted_variance`.
