

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.make_ndarray

### Aliases:

* `tf.contrib.util.make_ndarray`
* `tf.make_ndarray`

``` python
tf.make_ndarray(tensor)
```



Defined in [`tensorflow/python/framework/tensor_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/framework/tensor_util.py).

See the guide: [Utilities (contrib) > Miscellaneous Utility Functions](../../../api_guides/python/contrib.util#Miscellaneous_Utility_Functions)

Create a numpy ndarray from a tensor.

Create a numpy ndarray with the same shape and data as the tensor.

#### Args:

* <b>`tensor`</b>: A TensorProto.


#### Returns:

A numpy array with the tensor contents.


#### Raises:

* <b>`TypeError`</b>: if tensor has unsupported type.