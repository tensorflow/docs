page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.sigmoid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/sigmoid">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L3101-L3121">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes sigmoid of `x` element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/sigmoid"><code>tf.compat.v1.math.sigmoid</code></a>
* <a href="/api_docs/python/tf/math/sigmoid"><code>tf.compat.v1.nn.sigmoid</code></a>
* <a href="/api_docs/python/tf/math/sigmoid"><code>tf.compat.v1.sigmoid</code></a>
* <a href="/api_docs/python/tf/math/sigmoid"><code>tf.compat.v2.math.sigmoid</code></a>
* <a href="/api_docs/python/tf/math/sigmoid"><code>tf.compat.v2.nn.sigmoid</code></a>
* <a href="/api_docs/python/tf/math/sigmoid"><code>tf.compat.v2.sigmoid</code></a>
* <a href="/api_docs/python/tf/math/sigmoid"><code>tf.nn.sigmoid</code></a>
* <a href="/api_docs/python/tf/math/sigmoid"><code>tf.sigmoid</code></a>


``` python
tf.math.sigmoid(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Specifically, `y = 1 / (1 + exp(-x))`.

#### Args:


* <b>`x`</b>: A Tensor with type `float16`, `float32`, `float64`, `complex64`, or
  `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A Tensor with the same type as `x`.




#### Scipy Compatibility
Equivalent to scipy.special.expit
