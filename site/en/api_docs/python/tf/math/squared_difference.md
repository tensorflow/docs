page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.squared_difference


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/squared_difference">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns (x - y)(x - y) element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/squared_difference"><code>tf.compat.v1.math.squared_difference</code></a>
* <a href="/api_docs/python/tf/math/squared_difference"><code>tf.compat.v1.squared_difference</code></a>
* <a href="/api_docs/python/tf/math/squared_difference"><code>tf.compat.v2.math.squared_difference</code></a>
* <a href="/api_docs/python/tf/math/squared_difference"><code>tf.squared_difference</code></a>


``` python
tf.math.squared_difference(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/squared_difference"><code>math.squared_difference</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
