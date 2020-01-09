page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_type


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/check_ops.py#L1589-L1605">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Asserts that the given `Tensor` is of the specified type.

### Aliases:

* `tf.compat.v2.debugging.assert_type`


``` python
tf.debugging.assert_type(
    tensor,
    tf_type,
    message=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This can always be checked statically, so this method returns nothing.

#### Args:


* <b>`tensor`</b>: A `Tensor`.
* <b>`tf_type`</b>: A tensorflow type (<a href="../../tf/dtypes#float32"><code>dtypes.float32</code></a>, <a href="../../tf#int64"><code>tf.int64</code></a>, <a href="../../tf/dtypes#bool"><code>dtypes.bool</code></a>,
  etc).
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>:  A name for this operation. Defaults to "assert_type"


#### Raises:


* <b>`TypeError`</b>: If the tensor's data type doesn't match `tf_type`.
