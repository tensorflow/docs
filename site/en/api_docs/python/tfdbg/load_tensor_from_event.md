page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.load_tensor_from_event

``` python
tfdbg.load_tensor_from_event(event)
```



Defined in [`tensorflow/python/debug/lib/debug_data.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/debug/lib/debug_data.py).

Load a tensor from an Event proto.

#### Args:

* <b>`event`</b>: The Event proto, assumed to hold a tensor value in its
      summary.value[0] field.


#### Returns:

The tensor value loaded from the event file, as a `numpy.ndarray`, if
representation of the tensor value by a `numpy.ndarray` is possible.
For uninitialized Tensors, returns `None`. For Tensors of data types that
cannot be represented as `numpy.ndarray` (e.g., <a href="../tf/resource"><code>tf.resource</code></a>), return
the `TensorProto` protobuf object without converting it to a
`numpy.ndarray`.