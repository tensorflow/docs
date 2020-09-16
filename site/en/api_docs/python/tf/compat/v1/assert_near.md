description: Assert the condition x and y are close element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.assert_near" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.assert_near

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/check_ops.py#L762-L838">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Assert the condition `x` and `y` are close element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.assert_near`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.assert_near(
    x, y, rtol=None, atol=None, data=None, summarize=None, message=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_near(x, y)]):
  output = tf.reduce_sum(x)
```

This condition holds if for every pair of (possibly broadcast) elements
`x[i]`, `y[i]`, we have

```tf.abs(x[i] - y[i]) <= atol + rtol * tf.abs(y[i])```.

If both `x` and `y` are empty, this is trivially satisfied.

The default `atol` and `rtol` is `10 * eps`, where `eps` is the smallest
representable positive number such that `1 + eps != 1`.  This is about
`1.2e-6` in `32bit`, `2.22e-15` in `64bit`, and `0.00977` in `16bit`.
See `numpy.finfo`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Float or complex `Tensor`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Float or complex `Tensor`, same `dtype` as, and broadcastable to, `x`.
</td>
</tr><tr>
<td>
`rtol`
</td>
<td>
`Tensor`.  Same `dtype` as, and broadcastable to, `x`.
The relative tolerance.  Default is `10 * eps`.
</td>
</tr><tr>
<td>
`atol`
</td>
<td>
`Tensor`.  Same `dtype` as, and broadcastable to, `x`.
The absolute tolerance.  Default is `10 * eps`.
</td>
</tr><tr>
<td>
`data`
</td>
<td>
The tensors to print out if the condition is False.  Defaults to
error message and first few entries of `x`, `y`.
</td>
</tr><tr>
<td>
`summarize`
</td>
<td>
Print this many entries of each tensor.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
A string to prefix to the default message.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).  Defaults to "assert_near".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Op that raises `InvalidArgumentError` if `x` and `y` are not close enough.
</td>
</tr>

</table>




#### Numpy Compatibility
Similar to `numpy.assert_allclose`, except tolerance depends on data type.
This is due to the fact that `TensorFlow` is often used with `32bit`, `64bit`,
and even `16bit` data.

