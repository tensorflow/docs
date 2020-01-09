page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.device


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/ops.py#L5111-L5144">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Wrapper for `Graph.device()` using the default graph.

``` python
tf.compat.v1.device(device_name_or_function)
```



<!-- Placeholder for "Used in" -->

See <a href="../../../tf/Graph#device"><code>tf.Graph.device</code></a> for more details.

#### Args:


* <b>`device_name_or_function`</b>: The device name or function to use in the context.


#### Returns:

A context manager that specifies the default device to use for newly
created ops.



#### Raises:


* <b>`RuntimeError`</b>: If eager execution is enabled and a function is passed in.
