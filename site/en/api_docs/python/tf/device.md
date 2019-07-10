page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.device

Wrapper for <a href="../tf/Graph#device"><code>Graph.device()</code></a> using the default graph.

### Aliases:

* `tf.compat.v1.device`
* `tf.device`

``` python
tf.device(device_name_or_function)
```



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->

See <a href="../tf/Graph#device"><code>tf.Graph.device</code></a> for more details.

#### Args:


* <b>`device_name_or_function`</b>: The device name or function to use in the context.


#### Returns:

A context manager that specifies the default device to use for newly
created ops.



#### Raises:


* <b>`RuntimeError`</b>: If eager execution is enabled and a function is passed in.