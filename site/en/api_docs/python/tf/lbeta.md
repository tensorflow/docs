

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.lbeta

### `tf.lbeta`

``` python
lbeta(
    x,
    name='lbeta'
)
```



Defined in [`tensorflow/python/ops/special_math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/special_math_ops.py).

See the guide: [Math > Basic Math Functions](../../../api_guides/python/math_ops#Basic_Math_Functions)

Computes `ln(|Beta(x)|)`, reducing along the last dimension.

Given one-dimensional `z = [z_0,...,z_{K-1}]`, we define

```Beta(z) = \prod_j Gamma(z_j) / Gamma(\sum_j z_j)```

And for `n + 1` dimensional `x` with shape `[N1, ..., Nn, K]`, we define
`lbeta(x)[i1, ..., in] = Log(|Beta(x[i1, ..., in, :])|)`.  In other words,
the last dimension is treated as the `z` vector.

Note that if `z = [u, v]`, then
`Beta(z) = int_0^1 t^{u-1} (1 - t)^{v-1} dt`, which defines the traditional
bivariate beta function.

If the last dimension is empty, we follow the convention that the sum over
the empty set is zero, and the product is one.

#### Args:

* <b>`x`</b>: A rank `n + 1` `Tensor`, `n >= 0` with type `float`, or `double`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  The logarithm of `|Beta(x)|` reducing along the last dimension.