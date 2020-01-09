page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.is_non_decreasing


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/is_non_decreasing">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L1899-L1930">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns `True` if `x` is non-decreasing.

### Aliases:

* <a href="/api_docs/python/tf/math/is_non_decreasing"><code>tf.compat.v1.debugging.is_non_decreasing</code></a>
* <a href="/api_docs/python/tf/math/is_non_decreasing"><code>tf.compat.v1.is_non_decreasing</code></a>
* <a href="/api_docs/python/tf/math/is_non_decreasing"><code>tf.compat.v1.math.is_non_decreasing</code></a>
* <a href="/api_docs/python/tf/math/is_non_decreasing"><code>tf.compat.v2.math.is_non_decreasing</code></a>
* <a href="/api_docs/python/tf/math/is_non_decreasing"><code>tf.debugging.is_non_decreasing</code></a>
* <a href="/api_docs/python/tf/math/is_non_decreasing"><code>tf.is_non_decreasing</code></a>


``` python
tf.math.is_non_decreasing(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Elements of `x` are compared in row-major order.  The tensor `[x[0],...]`
is non-decreasing if for every adjacent pair we have `x[i] <= x[i+1]`.
If `x` has less than two elements, it is trivially non-decreasing.

See also:  `is_strictly_increasing`

#### Args:


* <b>`x`</b>: Numeric `Tensor`.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "is_non_decreasing"


#### Returns:

Boolean `Tensor`, equal to `True` iff `x` is non-decreasing.



#### Raises:


* <b>`TypeError`</b>: if `x` is not a numeric tensor.
