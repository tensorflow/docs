

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.saved_model.utils.build_tensor_info

### `tf.saved_model.utils.build_tensor_info`

``` python
build_tensor_info(tensor)
```



Defined in [`tensorflow/python/saved_model/utils_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/saved_model/utils_impl.py).

Utility function to build TensorInfo proto.

#### Args:

* <b>`tensor`</b>: Tensor whose name, dtype and shape are used to build the TensorInfo.


#### Returns:

  A TensorInfo protocol buffer constructed based on the supplied argument.