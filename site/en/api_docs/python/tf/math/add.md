page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.add


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/add">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns x + y element-wise.

### Aliases:

* <a href="/api_docs/python/tf/RaggedTensor#__add__"><code>tf.RaggedTensor.__add__</code></a>
* <a href="/api_docs/python/tf/math/add"><code>tf.add</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__add__"><code>tf.compat.v1.RaggedTensor.__add__</code></a>
* <a href="/api_docs/python/tf/math/add"><code>tf.compat.v1.add</code></a>
* <a href="/api_docs/python/tf/math/add"><code>tf.compat.v1.math.add</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__add__"><code>tf.compat.v2.RaggedTensor.__add__</code></a>
* <a href="/api_docs/python/tf/math/add"><code>tf.compat.v2.add</code></a>
* <a href="/api_docs/python/tf/math/add"><code>tf.compat.v2.math.add</code></a>


``` python
tf.math.add(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/add"><code>math.add</code></a> supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `string`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
