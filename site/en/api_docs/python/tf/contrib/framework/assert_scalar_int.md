

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.framework.assert_scalar_int

### `tf.contrib.framework.assert_scalar_int`

``` python
assert_scalar_int(
    tensor,
    name=None
)
```



Defined in [`tensorflow/contrib/framework/python/framework/tensor_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/framework/python/framework/tensor_util.py).

See the guide: [Framework (contrib)](../../../../../api_guides/python/contrib.framework)

Assert `tensor` is 0-D, of type `tf.int32` or `tf.int64`.

#### Args:

* <b>`tensor`</b>: `Tensor` to test.
* <b>`name`</b>: Name of the op and of the new `Tensor` if one is created.
Returns:
  `tensor`, for chaining.
Raises:
* <b>`ValueError`</b>: if `tensor` is not 0-D, of type `tf.int32` or `tf.int64`.