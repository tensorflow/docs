page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.timestamp


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/timestamp">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_logging_ops.py`



Provides the time since epoch in seconds.

### Aliases:

* <a href="/api_docs/python/tf/timestamp"><code>tf.compat.v1.timestamp</code></a>
* <a href="/api_docs/python/tf/timestamp"><code>tf.compat.v2.timestamp</code></a>


``` python
tf.timestamp(name=None)
```



<!-- Placeholder for "Used in" -->

Returns the timestamp as a `float64` for seconds since the Unix epoch.

Note: the timestamp is computed when the op is executed, not when it is added
to the graph.

#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float64`.
