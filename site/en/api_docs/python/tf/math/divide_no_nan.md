page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.divide_no_nan


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/divide_no_nan">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L1095-L1118">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes an unsafe divide which returns 0 if the y is zero.

### Aliases:

* <a href="/api_docs/python/tf/math/divide_no_nan"><code>tf.compat.v1.div_no_nan</code></a>
* <a href="/api_docs/python/tf/math/divide_no_nan"><code>tf.compat.v1.math.divide_no_nan</code></a>
* <a href="/api_docs/python/tf/math/divide_no_nan"><code>tf.compat.v2.math.divide_no_nan</code></a>
* <a href="/api_docs/python/tf/math/divide_no_nan"><code>tf.div_no_nan</code></a>


``` python
tf.math.divide_no_nan(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`y`</b>: A `Tensor` whose dtype is compatible with `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The element-wise value of the x divided by y.
