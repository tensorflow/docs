page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.floormod


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/floormod">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

### Aliases:

* <a href="/api_docs/python/tf/RaggedTensor#__mod__"><code>tf.RaggedTensor.__mod__</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__mod__"><code>tf.compat.v1.RaggedTensor.__mod__</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.compat.v1.floormod</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.compat.v1.math.floormod</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.compat.v1.math.mod</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.compat.v1.mod</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__mod__"><code>tf.compat.v2.RaggedTensor.__mod__</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.compat.v2.math.floormod</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.compat.v2.math.mod</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.floormod</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.math.mod</code></a>
* <a href="/api_docs/python/tf/math/floormod"><code>tf.mod</code></a>


``` python
tf.math.floormod(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

true, this follows Python semantics in that the result here is consistent
with a flooring divide. E.g. `floor(x / y) * y + mod(x, y) = x`.

*NOTE*: <a href="../../tf/math/floormod"><code>math.floormod</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`, `bfloat16`, `half`, `float32`, `float64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
