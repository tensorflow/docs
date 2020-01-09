page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.digamma


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/digamma">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes Psi, the derivative of Lgamma (the log of the absolute value of

### Aliases:

* <a href="/api_docs/python/tf/math/digamma"><code>tf.compat.v1.digamma</code></a>
* <a href="/api_docs/python/tf/math/digamma"><code>tf.compat.v1.math.digamma</code></a>
* <a href="/api_docs/python/tf/math/digamma"><code>tf.compat.v2.math.digamma</code></a>
* <a href="/api_docs/python/tf/math/digamma"><code>tf.digamma</code></a>


``` python
tf.math.digamma(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

`Gamma(x)`), element-wise.

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
