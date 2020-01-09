page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.log_sigmoid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/log_sigmoid">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L3124-L3142">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes log sigmoid of `x` element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/log_sigmoid"><code>tf.compat.v1.log_sigmoid</code></a>
* <a href="/api_docs/python/tf/math/log_sigmoid"><code>tf.compat.v1.math.log_sigmoid</code></a>
* <a href="/api_docs/python/tf/math/log_sigmoid"><code>tf.compat.v2.math.log_sigmoid</code></a>
* <a href="/api_docs/python/tf/math/log_sigmoid"><code>tf.log_sigmoid</code></a>


``` python
tf.math.log_sigmoid(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Specifically, `y = log(1 / (1 + exp(-x)))`.  For numerical stability,
we use `y = -tf.nn.softplus(-x)`.

#### Args:


* <b>`x`</b>: A Tensor with type `float32` or `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A Tensor with the same type as `x`.
