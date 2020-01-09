page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.atan2


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/atan2">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

### Aliases:

* <a href="/api_docs/python/tf/math/atan2"><code>tf.atan2</code></a>
* <a href="/api_docs/python/tf/math/atan2"><code>tf.compat.v1.atan2</code></a>
* <a href="/api_docs/python/tf/math/atan2"><code>tf.compat.v1.math.atan2</code></a>
* <a href="/api_docs/python/tf/math/atan2"><code>tf.compat.v2.atan2</code></a>
* <a href="/api_docs/python/tf/math/atan2"><code>tf.compat.v2.math.atan2</code></a>


``` python
tf.math.atan2(
    y,
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This is the angle \( \theta \in [-\pi, \pi] \) such that
\[ x = r \cos(\theta) \]
and
\[ y = r \sin(\theta) \]
where \(r = \sqrt(x^2 + y^2) \).

#### Args:


* <b>`y`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`x`</b>: A `Tensor`. Must have the same type as `y`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `y`.
