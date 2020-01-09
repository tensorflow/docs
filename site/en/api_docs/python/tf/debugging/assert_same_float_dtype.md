page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_same_float_dtype


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_same_float_dtype">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L2015-L2046">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Validate and return float type based on `tensors` and `dtype`.

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_same_float_dtype"><code>tf.assert_same_float_dtype</code></a>
* <a href="/api_docs/python/tf/debugging/assert_same_float_dtype"><code>tf.compat.v1.assert_same_float_dtype</code></a>
* <a href="/api_docs/python/tf/debugging/assert_same_float_dtype"><code>tf.compat.v1.debugging.assert_same_float_dtype</code></a>
* <a href="/api_docs/python/tf/debugging/assert_same_float_dtype"><code>tf.compat.v2.debugging.assert_same_float_dtype</code></a>
* <a href="/api_docs/python/tf/debugging/assert_same_float_dtype"><code>tf.contrib.framework.assert_same_float_dtype</code></a>


``` python
tf.debugging.assert_same_float_dtype(
    tensors=None,
    dtype=None
)
```



<!-- Placeholder for "Used in" -->

For ops such as matrix multiplication, inputs and weights must be of the
same float type. This function validates that all `tensors` are the same type,
validates that type is `dtype` (if supplied), and returns the type. Type must
be a floating point type. If neither `tensors` nor `dtype` is supplied,
the function will return <a href="../../tf/dtypes#float32"><code>dtypes.float32</code></a>.

#### Args:


* <b>`tensors`</b>: Tensors of input values. Can include `None` elements, which will be
    ignored.
* <b>`dtype`</b>: Expected type.


#### Returns:

Validated type.



#### Raises:


* <b>`ValueError`</b>: if neither `tensors` nor `dtype` is supplied, or result is not
    float, or the common type of the inputs is not a floating point type.
