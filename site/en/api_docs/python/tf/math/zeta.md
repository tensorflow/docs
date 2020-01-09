page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.zeta


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/zeta">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Compute the Hurwitz zeta function \\(\zeta(x, q)\\).

### Aliases:

* <a href="/api_docs/python/tf/math/zeta"><code>tf.compat.v1.math.zeta</code></a>
* <a href="/api_docs/python/tf/math/zeta"><code>tf.compat.v1.zeta</code></a>
* <a href="/api_docs/python/tf/math/zeta"><code>tf.compat.v2.math.zeta</code></a>
* <a href="/api_docs/python/tf/math/zeta"><code>tf.zeta</code></a>


``` python
tf.math.zeta(
    x,
    q,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The Hurwitz zeta function is defined as:


\\(\zeta(x, q) = \sum_{n=0}^{\infty} (q + n)^{-x}\\)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`q`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
