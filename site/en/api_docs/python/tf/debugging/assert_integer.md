page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_integer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_integer">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L1438-L1474">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert that `x` is of integer dtype.

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_integer"><code>tf.assert_integer</code></a>
* <a href="/api_docs/python/tf/debugging/assert_integer"><code>tf.compat.v1.assert_integer</code></a>
* <a href="/api_docs/python/tf/debugging/assert_integer"><code>tf.compat.v1.debugging.assert_integer</code></a>


``` python
tf.debugging.assert_integer(
    x,
    message=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_integer(x)]):
  output = tf.reduce_sum(x)
```

#### Args:


* <b>`x`</b>: `Tensor` whose basetype is integer and is not quantized.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_integer".


#### Raises:


* <b>`TypeError`</b>:  If `x.dtype` is anything other than non-quantized integer.


#### Returns:

A `no_op` that does nothing.  Type can be determined statically.
