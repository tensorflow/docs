page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.make_ndarray

Create a numpy ndarray from a tensor.

### Aliases:

* `tf.compat.v1.make_ndarray`
* `tf.compat.v2.make_ndarray`
* `tf.contrib.util.make_ndarray`
* `tf.make_ndarray`

``` python
tf.make_ndarray(tensor)
```



Defined in [`python/framework/tensor_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/tensor_util.py).

<!-- Placeholder for "Used in" -->

Create a numpy ndarray with the same shape and data as the tensor.

#### Args:


* <b>`tensor`</b>: A TensorProto.


#### Returns:

A numpy array with the tensor contents.



#### Raises:


* <b>`TypeError`</b>: if tensor has unsupported type.