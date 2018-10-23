


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.framework.assert_same_float_dtype

### `tf.contrib.framework.assert_same_float_dtype`

```
tf.contrib.framework.assert_same_float_dtype(tensors=None, dtype=None)
```


See the guide: [Framework (contrib)](../../../../../api_guides/python/contrib.framework)

Validate and return float type based on `tensors` and `dtype`.

For ops such as matrix multiplication, inputs and weights must be of the
same float type. This function validates that all `tensors` are the same type,
validates that type is `dtype` (if supplied), and returns the type. Type must
be `dtypes.float32` or `dtypes.float64`. If neither `tensors` nor
`dtype` is supplied, default to `dtypes.float32`.

#### Args:

* <b>`tensors`</b>: Tensors of input values. Can include `None` elements, which will be
      ignored.
* <b>`dtype`</b>: Expected type.
Returns:
  Validated type.
Raises:
* <b>`ValueError`</b>: if neither `tensors` nor `dtype` is supplied, or result is not
      float.

Defined in [`tensorflow/contrib/framework/python/framework/tensor_util.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/python/framework/tensor_util.py).

