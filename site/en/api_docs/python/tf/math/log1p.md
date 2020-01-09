page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.log1p


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/log1p">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes natural logarithm of (1 + x) element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/log1p"><code>tf.compat.v1.log1p</code></a>
* <a href="/api_docs/python/tf/math/log1p"><code>tf.compat.v1.math.log1p</code></a>
* <a href="/api_docs/python/tf/math/log1p"><code>tf.compat.v2.math.log1p</code></a>
* <a href="/api_docs/python/tf/math/log1p"><code>tf.log1p</code></a>


``` python
tf.math.log1p(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

I.e., \\(y = \log_e (1 + x)\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
