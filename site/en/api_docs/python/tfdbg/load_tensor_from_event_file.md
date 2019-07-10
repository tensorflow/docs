page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.load_tensor_from_event_file

``` python
tfdbg.load_tensor_from_event_file(event_file_path)
```



Defined in [`tensorflow/python/debug/lib/debug_data.py`](https://github.com/tensorflow/tensorflow/blob/r1.14/tensorflow/python/debug/lib/debug_data.py).

Load a tensor from an event file.

Assumes that the event file contains a `Event` protobuf and the `Event`
protobuf contains a `Tensor` value.

#### Args:

* <b>`event_file_path`</b>: (`str`) path to the event file.


#### Returns:

The tensor value loaded from the event file, as a `numpy.ndarray`. For
uninitialized Tensors, returns `None`. For Tensors of data types that
cannot be converted to `numpy.ndarray` (e.g., <a href="../tf/dtypes#resource"><code>tf.resource</code></a>), return
`None`.