page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.dropout

``` python
tf.nn.dropout(
    x,
    keep_prob=None,
    noise_shape=None,
    seed=None,
    name=None,
    rate=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/nn_ops.py).

Computes dropout. (deprecated arguments)

Warning: SOME ARGUMENTS ARE DEPRECATED: `(keep_prob)`. They will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.

For each element of `x`, with probability `rate`, outputs `0`, and otherwise
scales up the input by `1 / (1-rate)`. The scaling is such that the expected
sum is unchanged.

By default, each element is kept or dropped independently.  If `noise_shape`
is specified, it must be
[broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]`
will make independent decisions.  For example, if `shape(x) = [k, l, m, n]`
and `noise_shape = [k, 1, 1, n]`, each batch and channel component will be
kept independently and each row and column will be kept or not kept together.

#### Args:

* <b>`x`</b>: A floating point tensor.
* <b>`keep_prob`</b>: (deprecated) A deprecated alias for `(1-rate)`.
* <b>`noise_shape`</b>: A 1-D `Tensor` of type `int32`, representing the
    shape for randomly generated keep/drop flags.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    <a href="../../tf/random/set_random_seed"><code>tf.set_random_seed</code></a> for behavior.
* <b>`name`</b>: A name for this operation (optional).
* <b>`rate`</b>: A scalar `Tensor` with the same type as `x`. The probability that each
    element of `x` is discarded.


#### Returns:

A Tensor of the same shape of `x`.


#### Raises:

* <b>`ValueError`</b>: If `rate` is not in `[0, 1)` or if `x` is not a floating
    point tensor.