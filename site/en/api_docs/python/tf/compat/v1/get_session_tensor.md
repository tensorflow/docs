page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.get_session_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/session_ops.py#L182-L220">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get the tensor of type `dtype` by feeding a tensor handle.

``` python
tf.compat.v1.get_session_tensor(
    handle,
    dtype,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This is EXPERIMENTAL and subject to change.

Get the value of the tensor from a tensor handle. The tensor
is produced in a previous run() and stored in the state of the
session.

#### Args:


* <b>`handle`</b>: The string representation of a persistent tensor handle.
* <b>`dtype`</b>: The type of the output tensor.
* <b>`name`</b>: Optional name prefix for the return tensor.


#### Returns:

A pair of tensors. The first is a placeholder for feeding a
tensor handle and the second is the tensor in the session state
keyed by the tensor handle.



#### Example:



```python
c = tf.multiply(a, b)
h = tf.compat.v1.get_session_handle(c)
h = sess.run(h)

p, a = tf.compat.v1.get_session_tensor(h.handle, tf.float32)
b = tf.multiply(a, 10)
c = sess.run(b, feed_dict={p: h.handle})
```
