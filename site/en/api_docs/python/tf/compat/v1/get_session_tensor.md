description: Get the tensor of type dtype by feeding a tensor handle.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.get_session_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.get_session_tensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/session_ops.py#L181-L219">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get the tensor of type `dtype` by feeding a tensor handle.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.get_session_tensor(
    handle, dtype, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is EXPERIMENTAL and subject to change.

Get the value of the tensor from a tensor handle. The tensor
is produced in a previous run() and stored in the state of the
session.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`handle`
</td>
<td>
The string representation of a persistent tensor handle.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output tensor.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the return tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A pair of tensors. The first is a placeholder for feeding a
tensor handle and the second is the tensor in the session state
keyed by the tensor handle.
</td>
</tr>

</table>



#### Example:



```python
c = tf.multiply(a, b)
h = tf.compat.v1.get_session_handle(c)
h = sess.run(h)

p, a = tf.compat.v1.get_session_tensor(h.handle, tf.float32)
b = tf.multiply(a, 10)
c = sess.run(b, feed_dict={p: h.handle})
```