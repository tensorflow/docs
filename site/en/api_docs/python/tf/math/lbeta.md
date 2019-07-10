page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.lbeta

Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

### Aliases:

* `tf.compat.v1.lbeta`
* `tf.compat.v1.math.lbeta`
* `tf.compat.v2.math.lbeta`
* `tf.lbeta`
* `tf.math.lbeta`

``` python
tf.math.lbeta(
    x,
    name=None
)
```



Defined in [`python/ops/special_math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/special_math_ops.py).

<!-- Placeholder for "Used in" -->

Given one-dimensional `z = [z_0,...,z_{K-1}]`, we define

<div> $$Beta(z) = \prod_j Gamma(z_j) / Gamma(\sum_j z_j)$$ </div>

And for `n + 1` dimensional `x` with shape `[N1, ..., Nn, K]`, we define
<div> $$lbeta(x)[i1, ..., in] = Log(|Beta(x[i1, ..., in, :])|)$$. </div>

In other words, the last dimension is treated as the `z` vector.

Note that if `z = [u, v]`, then
\\(Beta(z) = int_0^1 t^{u-1} (1 - t)^{v-1} dt\\), which defines the
traditional bivariate beta function.

If the last dimension is empty, we follow the convention that the sum over
the empty set is zero, and the product is one.

#### Args:


* <b>`x`</b>: A rank `n + 1` `Tensor`, `n >= 0` with type `float`, or `double`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The logarithm of \\(|Beta(x)|\\) reducing along the last dimension.
