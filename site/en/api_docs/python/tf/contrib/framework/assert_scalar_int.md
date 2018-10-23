


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.framework.assert_scalar_int

### `tf.contrib.framework.assert_scalar_int`

```
tf.contrib.framework.assert_scalar_int(tensor, name=None)
```


See the guide: [Framework (contrib)](../../../../../api_guides/python/contrib.framework)

Assert `tensor` is 0-D, of type `tf.int32` or `tf.int64`.

#### Args:

* <b>`tensor`</b>: `Tensor` to test.
* <b>`name`</b>: Name of the op and of the new `Tensor` if one is created.
Returns:
  `tensor`, for chaining.
Raises:
* <b>`ValueError`</b>: if `tensor` is not 0-D, of type `tf.int32` or `tf.int64`.

Defined in [`tensorflow/contrib/framework/python/framework/tensor_util.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/python/framework/tensor_util.py).

