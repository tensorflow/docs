page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_type

Statically asserts that the given `Tensor` is of the specified type.

### Aliases:

* `tf.assert_type`
* `tf.compat.v1.assert_type`
* `tf.compat.v1.debugging.assert_type`
* `tf.debugging.assert_type`

``` python
tf.debugging.assert_type(
    tensor,
    tf_type,
    message=None,
    name=None
)
```



Defined in [`python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/check_ops.py).

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
