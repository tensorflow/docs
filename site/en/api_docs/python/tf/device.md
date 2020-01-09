page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.device

``` python
tf.device(device_name_or_function)
```



Defined in [`tensorflow/python/framework/ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/framework/ops.py).

Wrapper for `Graph.device()` using the default graph.

See
<a href="../tf/Graph#device"><code>tf.Graph.device</code></a>
for more details.

#### Args:

* <b>`device_name_or_function`</b>: The device name or function to use in
    the context.


#### Returns:

A context manager that specifies the default device to use for newly
created ops.


#### Raises:

* <b>`RuntimeError`</b>: If eager execution is enabled and a function is passed in.