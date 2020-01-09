page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.delete_session_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/session_ops.py#L223-L244">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Delete the tensor for the given tensor handle.

### Aliases:

* <a href="/api_docs/python/tf/delete_session_tensor"><code>tf.compat.v1.delete_session_tensor</code></a>


``` python
tf.delete_session_tensor(
    handle,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This is EXPERIMENTAL and subject to change.

Delete the tensor of a given tensor handle. The tensor is produced
in a previous run() and stored in the state of the session.

#### Args:


* <b>`handle`</b>: The string representation of a persistent tensor handle.
* <b>`name`</b>: Optional name prefix for the return tensor.


#### Returns:

A pair of graph elements. The first is a placeholder for feeding a
tensor handle and the second is a deletion operation.
