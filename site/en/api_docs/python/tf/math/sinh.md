page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.sinh


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/sinh">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes hyperbolic sine of x element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/sinh"><code>tf.compat.v1.math.sinh</code></a>
* <a href="/api_docs/python/tf/math/sinh"><code>tf.compat.v1.sinh</code></a>
* <a href="/api_docs/python/tf/math/sinh"><code>tf.compat.v2.math.sinh</code></a>
* <a href="/api_docs/python/tf/math/sinh"><code>tf.compat.v2.sinh</code></a>
* <a href="/api_docs/python/tf/math/sinh"><code>tf.sinh</code></a>


``` python
tf.math.sinh(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

  Given an input tensor, this function computes hyperbolic sine of every
  element in the tensor. Input range is `[-inf,inf]` and output range
  is `[-inf,inf]`.

>     x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 2, 10, float("inf")])
>     tf.math.sinh(x) ==> [-inf -4.0515420e+03 -5.2109528e-01 1.1752012e+00 1.5094614e+00 3.6268604e+00 1.1013232e+04 inf]

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
