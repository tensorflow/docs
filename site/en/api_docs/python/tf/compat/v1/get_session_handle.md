page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.get_session_handle


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/session_ops.py#L139-L179">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return the handle of `data`.

``` python
tf.compat.v1.get_session_handle(
    data,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This is EXPERIMENTAL and subject to change.

Keep `data` "in-place" in the runtime and create a handle that can be
used to retrieve `data` in a subsequent run().

Combined with `get_session_tensor`, we can keep a tensor produced in
one run call in place, and use it as the input in a future run call.

#### Args:


* <b>`data`</b>: A tensor to be stored in the session.
* <b>`name`</b>: Optional name prefix for the return tensor.


#### Returns:

A scalar string tensor representing a unique handle for `data`.



#### Raises:


* <b>`TypeError`</b>: if `data` is not a Tensor.


#### Example:



```python
c = tf.multiply(a, b)
h = tf.compat.v1.get_session_handle(c)
h = sess.run(h)

p, a = tf.compat.v1.get_session_tensor(h.handle, tf.float32)
b = tf.multiply(a, 10)
c = sess.run(b, feed_dict={p: h.handle})
```
