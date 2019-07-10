page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.debugging.assert_type

Asserts that the given `Tensor` is of the specified type.

``` python
tf.compat.v2.debugging.assert_type(
    tensor,
    tf_type,
    message=None,
    name=None
)
```



Defined in [`python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/check_ops.py).

<!-- Placeholder for "Used in" -->

This can always be checked statically, so this method returns nothing.

#### Args:


* <b>`tensor`</b>: A `Tensor`.
* <b>`tf_type`</b>: A tensorflow type (`dtypes.float32`, <a href="../../../../tf#int64"><code>tf.int64</code></a>, `dtypes.bool`,
  etc).
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>:  A name for this operation. Defaults to "assert_type"


#### Raises:


* <b>`TypeError`</b>: If the tensor's data type doesn't match `tf_type`.