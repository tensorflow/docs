page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.lbeta


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/lbeta">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/special_math_ops.py#L40-L86">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

### Aliases:

* <a href="/api_docs/python/tf/math/lbeta"><code>tf.compat.v1.lbeta</code></a>
* <a href="/api_docs/python/tf/math/lbeta"><code>tf.compat.v1.math.lbeta</code></a>
* <a href="/api_docs/python/tf/math/lbeta"><code>tf.compat.v2.math.lbeta</code></a>
* <a href="/api_docs/python/tf/math/lbeta"><code>tf.lbeta</code></a>


``` python
tf.math.lbeta(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given one-dimensional `z = [z_0,...,z_{K-1}]`, we define

<div> $$Beta(z) = \prod_j Gamma(z_j) / Gamma(\sum_j z_j)$$ </div>

And for `n + 1` dimensional `x` with shape `[N1, ..., Nn, K]`, we define
<div> $$lbeta(x)[i1, ..., in] = Log(|Beta(x[i1, ..., in, :])|)$$ </div>.

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
