


<!-- DO NOT EDIT! Automatically generated file. -->
# tfdbg.load_tensor_from_event_file

### `tfdbg.load_tensor_from_event_file`

```
tfdbg.load_tensor_from_event_file(event_file_path)
```


See the guide: [TensorFlow Debugger > Functions for loading debug-dump data](../../../api_guides/python/tfdbg#Functions_for_loading_debug_dump_data)

Load a tensor from an event file.

Assumes that the event file contains a `Event` protobuf and the `Event`
protobuf contains a `Tensor` value.

#### Args:

* <b>`event_file_path`</b>: (`str`) path to the event file.


#### Returns:

  The tensor value loaded from the event file, as a `numpy.ndarray`. For
  uninitialized tensors, returns None.

Defined in [`tensorflow/python/debug/lib/debug_data.py`](https://www.tensorflow.org/code/tensorflow/python/debug/lib/debug_data.py).

