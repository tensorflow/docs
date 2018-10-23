

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.delete_session_tensor

``` python
delete_session_tensor(
    handle,
    name=None
)
```



Defined in [`tensorflow/python/ops/session_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/session_ops.py).

See the guide: [Tensor Handle Operations > Tensor Handle Operations](../../../api_guides/python/session_ops#Tensor_Handle_Operations)

Delete the tensor for the given tensor handle.

This is EXPERIMENTAL and subject to change.

Delete the tensor of a given tensor handle. The tensor is produced
in a previous run() and stored in the state of the session.

#### Args:

* <b>`handle`</b>: The string representation of a persistent tensor handle.
* <b>`name`</b>: Optional name prefix for the return tensor.


#### Returns:

A pair of graph elements. The first is a placeholder for feeding a
tensor handle and the second is a deletion operation.