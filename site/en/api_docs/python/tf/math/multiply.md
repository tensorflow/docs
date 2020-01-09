page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.multiply


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/multiply">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L328-L331">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns x * y element-wise.

### Aliases:

* <a href="/api_docs/python/tf/RaggedTensor#__mul__"><code>tf.RaggedTensor.__mul__</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__mul__"><code>tf.compat.v1.RaggedTensor.__mul__</code></a>
* <a href="/api_docs/python/tf/math/multiply"><code>tf.compat.v1.math.multiply</code></a>
* <a href="/api_docs/python/tf/math/multiply"><code>tf.compat.v1.multiply</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__mul__"><code>tf.compat.v2.RaggedTensor.__mul__</code></a>
* <a href="/api_docs/python/tf/math/multiply"><code>tf.compat.v2.math.multiply</code></a>
* <a href="/api_docs/python/tf/math/multiply"><code>tf.compat.v2.multiply</code></a>
* <a href="/api_docs/python/tf/math/multiply"><code>tf.multiply</code></a>


``` python
tf.math.multiply(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/multiply"><code>tf.multiply</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
