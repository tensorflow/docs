page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_type


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_type">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L1496-L1524">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Statically asserts that the given `Tensor` is of the specified type.

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_type"><code>tf.assert_type</code></a>
* <a href="/api_docs/python/tf/debugging/assert_type"><code>tf.compat.v1.assert_type</code></a>
* <a href="/api_docs/python/tf/debugging/assert_type"><code>tf.compat.v1.debugging.assert_type</code></a>


``` python
tf.debugging.assert_type(
    tensor,
    tf_type,
    message=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`tensor`</b>: A `Tensor`.
* <b>`tf_type`</b>: A tensorflow type (<a href="../../tf/dtypes#float32"><code>dtypes.float32</code></a>, <a href="../../tf#int64"><code>tf.int64</code></a>, <a href="../../tf/dtypes#bool"><code>dtypes.bool</code></a>,
  etc).
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>:  A name to give this `Op`.  Defaults to "assert_type"


#### Raises:


* <b>`TypeError`</b>: If the tensors data type doesn't match `tf_type`.


#### Returns:

A `no_op` that does nothing.  Type can be determined statically.
