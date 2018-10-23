

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.make_ndarray

### Aliases:

* `tf.contrib.util.make_ndarray`
* `tf.make_ndarray`

``` python
make_ndarray(tensor)
```



Defined in [`tensorflow/python/framework/tensor_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/framework/tensor_util.py).

See the guide: [Utilities (contrib) > Miscellaneous Utility Functions](../../../api_guides/python/contrib.util#Miscellaneous_Utility_Functions)

Create a numpy ndarray from a tensor.

Create a numpy ndarray with the same shape and data as the tensor.

#### Args:

* <b>`tensor`</b>: A TensorProto.


#### Returns:

A numpy array with the tensor contents.


#### Raises:

* <b>`TypeError`</b>: if tensor has unsupported type.