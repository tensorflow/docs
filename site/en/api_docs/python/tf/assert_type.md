


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.assert_type

### `tf.assert_type`

```
tf.assert_type(tensor, tf_type, message=None, name=None)
```


See the guide: [Asserts and boolean checks](../../../api_guides/python/check_ops)

Statically asserts that the given `Tensor` is of the specified type.

#### Args:

* <b>`tensor`</b>: A tensorflow `Tensor`.
* <b>`tf_type`</b>: A tensorflow type (`dtypes.float32`, `tf.int64`, `dtypes.bool`,
    etc).
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>:  A name to give this `Op`.  Defaults to "assert_type"


#### Raises:

* <b>`TypeError`</b>: If the tensors data type doesn't match `tf_type`.


#### Returns:

  A `no_op` that does nothing.  Type can be determined statically.

Defined in [`tensorflow/python/ops/check_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/check_ops.py).

