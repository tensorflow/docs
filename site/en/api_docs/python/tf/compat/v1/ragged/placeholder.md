description: Creates a placeholder for a <a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> that will always be fed.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.ragged.placeholder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.ragged.placeholder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_factory_ops.py#L316-L351">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a placeholder for a <a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> that will always be fed.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.ragged.placeholder(
    dtype, ragged_rank, value_shape=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

**Important**: This ragged tensor will produce an error if evaluated.
Its value must be fed using the `feed_dict` optional argument to
`Session.run()`, `Tensor.eval()`, or `Operation.run()`.

@compatibility{eager} Placeholders are not compatible with eager execution.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
The data type for the `RaggedTensor`.
</td>
</tr><tr>
<td>
`ragged_rank`
</td>
<td>
The ragged rank for the `RaggedTensor`
</td>
</tr><tr>
<td>
`value_shape`
</td>
<td>
The shape for individual flat values in the `RaggedTensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` that may be used as a handle for feeding a value, but
not evaluated directly.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
if eager execution is enabled
</td>
</tr>
</table>

