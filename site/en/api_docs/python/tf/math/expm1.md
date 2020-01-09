page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.expm1


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/expm1">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes `exp(x) - 1` element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/expm1"><code>tf.compat.v1.expm1</code></a>
* <a href="/api_docs/python/tf/math/expm1"><code>tf.compat.v1.math.expm1</code></a>
* <a href="/api_docs/python/tf/math/expm1"><code>tf.compat.v2.math.expm1</code></a>
* <a href="/api_docs/python/tf/math/expm1"><code>tf.expm1</code></a>


``` python
tf.math.expm1(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

  i.e. `exp(x) - 1` or `e^(x) - 1`, where `x` is the input tensor.
  `e` denotes Euler's number and is approximately equal to 2.718281.

>     x = tf.constant(2.0)
>     tf.math.expm1(x) ==> 6.389056
>     
>     x = tf.constant([2.0, 8.0])
>     tf.math.expm1(x) ==> array([6.389056, 2979.958], dtype=float32)
>     
>     x = tf.constant(1 + 1j)
>     tf.math.expm1(x) ==> (0.46869393991588515+2.2873552871788423j)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
