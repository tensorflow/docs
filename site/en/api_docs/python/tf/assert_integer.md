


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.assert_integer

### `tf.assert_integer`

```
tf.assert_integer(x, message=None, name=None)
```


See the guide: [Asserts and boolean checks](../../../api_guides/python/check_ops)

Assert that `x` is of integer dtype.

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.assert_integer(x)]):
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

Defined in [`tensorflow/python/ops/check_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/check_ops.py).

