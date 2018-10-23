

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.device

``` python
device(device_name_or_function)
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/framework/ops.py).

See the guide: [Building Graphs > Utility functions](../../../api_guides/python/framework#Utility_functions)

Wrapper for `Graph.device()` using the default graph.

See
[`tf.Graph.device`](../tf/Graph#device)
for more details.

#### Args:

* <b>`device_name_or_function`</b>: The device name or function to use in
    the context.


#### Returns:

  A context manager that specifies the default device to use for newly
  created ops.