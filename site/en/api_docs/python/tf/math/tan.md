page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.tan


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/tan">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes tan of x element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/tan"><code>tf.compat.v1.math.tan</code></a>
* <a href="/api_docs/python/tf/math/tan"><code>tf.compat.v1.tan</code></a>
* <a href="/api_docs/python/tf/math/tan"><code>tf.compat.v2.math.tan</code></a>
* <a href="/api_docs/python/tf/math/tan"><code>tf.compat.v2.tan</code></a>
* <a href="/api_docs/python/tf/math/tan"><code>tf.tan</code></a>


``` python
tf.math.tan(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

  Given an input tensor, this function computes tangent of every
  element in the tensor. Input range is `(-inf, inf)` and
  output range is `(-inf, inf)`. If input lies outside the boundary, `nan`
  is returned.

>     x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10000, float("inf")])
>     tf.math.tan(x) ==> [nan 0.45231566 -0.5463025 1.5574077 2.572152 -1.7925274 0.32097113 nan]

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
