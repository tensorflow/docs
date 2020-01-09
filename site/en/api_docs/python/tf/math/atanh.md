page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.atanh


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/atanh">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes inverse hyperbolic tangent of x element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/atanh"><code>tf.atanh</code></a>
* <a href="/api_docs/python/tf/math/atanh"><code>tf.compat.v1.atanh</code></a>
* <a href="/api_docs/python/tf/math/atanh"><code>tf.compat.v1.math.atanh</code></a>
* <a href="/api_docs/python/tf/math/atanh"><code>tf.compat.v2.atanh</code></a>
* <a href="/api_docs/python/tf/math/atanh"><code>tf.compat.v2.math.atanh</code></a>


``` python
tf.math.atanh(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

  Given an input tensor, this function computes inverse hyperbolic tangent
  for every element in the tensor. Input range is `[-1,1]` and output range is
  `[-inf, inf]`. If input is `-1`, output will be `-inf` and if the
  input is `1`, output will be `inf`. Values outside the range will have
  `nan` as output.

>     x = tf.constant([-float("inf"), -1, -0.5, 1, 0, 0.5, 10, float("inf")])
>     tf.math.atanh(x) ==> [nan -inf -0.54930615 inf  0. 0.54930615 nan nan]

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
