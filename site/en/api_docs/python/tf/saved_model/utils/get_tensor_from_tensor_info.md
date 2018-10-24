

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.utils.get_tensor_from_tensor_info

``` python
tf.saved_model.utils.get_tensor_from_tensor_info(
    tensor_info,
    graph=None,
    import_scope=None
)
```



Defined in [`tensorflow/python/saved_model/utils_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/saved_model/utils_impl.py).

Returns the Tensor or SparseTensor described by a TensorInfo proto.

#### Args:

* <b>`tensor_info`</b>: A TensorInfo proto describing a Tensor or SparseTensor.
* <b>`graph`</b>: The tf.Graph in which tensors are looked up. If None, the
      current default graph is used.
* <b>`import_scope`</b>: If not None, names in `tensor_info` are prefixed with this
      string before lookup.


#### Returns:

The Tensor or SparseTensor in `graph` described by `tensor_info`.


#### Raises:

* <b>`KeyError`</b>: If `tensor_info` does not correspond to a tensor in `graph`.
* <b>`ValueError`</b>: If `tensor_info` is malformed.