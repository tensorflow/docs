description: Assert the condition x > y holds element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.assert_greater" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.assert_greater

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/check_ops.py#L987-L992">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Assert the condition `x > y` holds element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.assert_greater`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.assert_greater(
    x, y, data=None, summarize=None, message=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This condition holds if for every pair of (possibly broadcast) elements
`x[i]`, `y[i]`, we have `x[i] > y[i]`.
If both `x` and `y` are empty, this is trivially satisfied.

When running in graph mode, you should add a dependency on this operation
to ensure that it runs. Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_greater(x, y)]):
  output = tf.reduce_sum(x)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Numeric `Tensor`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Numeric `Tensor`, same dtype as and broadcastable to `x`.
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
A name for this operation (optional).  Defaults to "assert_greater".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Op that raises `InvalidArgumentError` if `x > y` is False.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`InvalidArgumentError`
</td>
<td>
if the check can be performed immediately and
`x > y` is False. The check can be performed immediately during
eager execution or if `x` and `y` are statically known.
</td>
</tr>
</table>



#### Eager Compatibility
returns None

