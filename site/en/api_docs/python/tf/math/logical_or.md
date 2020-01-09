page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.logical_or


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/logical_or">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns the truth value of x OR y element-wise.

### Aliases:

* <a href="/api_docs/python/tf/RaggedTensor#__or__"><code>tf.RaggedTensor.__or__</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__or__"><code>tf.compat.v1.RaggedTensor.__or__</code></a>
* <a href="/api_docs/python/tf/math/logical_or"><code>tf.compat.v1.logical_or</code></a>
* <a href="/api_docs/python/tf/math/logical_or"><code>tf.compat.v1.math.logical_or</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__or__"><code>tf.compat.v2.RaggedTensor.__or__</code></a>
* <a href="/api_docs/python/tf/math/logical_or"><code>tf.compat.v2.logical_or</code></a>
* <a href="/api_docs/python/tf/math/logical_or"><code>tf.compat.v2.math.logical_or</code></a>
* <a href="/api_docs/python/tf/math/logical_or"><code>tf.logical_or</code></a>


``` python
tf.math.logical_or(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/logical_or"><code>math.logical_or</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` of type `bool`.
* <b>`y`</b>: A `Tensor` of type `bool`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.
