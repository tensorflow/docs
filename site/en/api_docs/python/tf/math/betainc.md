page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.betainc


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/betainc">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Compute the regularized incomplete beta integral \\(I_x(a, b)\\).

### Aliases:

* <a href="/api_docs/python/tf/math/betainc"><code>tf.betainc</code></a>
* <a href="/api_docs/python/tf/math/betainc"><code>tf.compat.v1.betainc</code></a>
* <a href="/api_docs/python/tf/math/betainc"><code>tf.compat.v1.math.betainc</code></a>
* <a href="/api_docs/python/tf/math/betainc"><code>tf.compat.v2.math.betainc</code></a>


``` python
tf.math.betainc(
    a,
    b,
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The regularized incomplete beta integral is defined as:


\\(I_x(a, b) = \frac{B(x; a, b)}{B(a, b)}\\)

where


\\(B(x; a, b) = \int_0^x t^{a-1} (1 - t)^{b-1} dt\\)


is the incomplete beta function and \\(B(a, b)\\) is the *complete*
beta function.

#### Args:


* <b>`a`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`b`</b>: A `Tensor`. Must have the same type as `a`.
* <b>`x`</b>: A `Tensor`. Must have the same type as `a`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `a`.
