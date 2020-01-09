page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.device


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/device">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L5108-L5141">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Wrapper for <a href="../tf/Graph#device"><code>Graph.device()</code></a> using the default graph.

### Aliases:

* <a href="/api_docs/python/tf/device"><code>tf.compat.v1.device</code></a>


``` python
tf.device(device_name_or_function)
```



<!-- Placeholder for "Used in" -->

See <a href="../tf/Graph#device"><code>tf.Graph.device</code></a> for more details.

#### Args:


* <b>`device_name_or_function`</b>: The device name or function to use in the context.


#### Returns:

A context manager that specifies the default device to use for newly
created ops.



#### Raises:


* <b>`RuntimeError`</b>: If eager execution is enabled and a function is passed in.
