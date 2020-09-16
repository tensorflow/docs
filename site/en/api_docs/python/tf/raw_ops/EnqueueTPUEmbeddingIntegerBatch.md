description: An op that enqueues a list of input batch tensors to TPUEmbedding.

robots: noindex

# tf.raw_ops.EnqueueTPUEmbeddingIntegerBatch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An op that enqueues a list of input batch tensors to TPUEmbedding.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.EnqueueTPUEmbeddingIntegerBatch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.EnqueueTPUEmbeddingIntegerBatch(
    batch, mode_override, device_ordinal=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`batch`
</td>
<td>
A list of at least 1 `Tensor` objects with type `int32`.
A list of 1D tensors, one for each embedding table, containing the
indices into the tables.
</td>
</tr><tr>
<td>
`mode_override`
</td>
<td>
A `Tensor` of type `string`.
A string input that overrides the mode specified in the
TPUEmbeddingConfiguration. Supported values are {'unspecified', 'inference',
'training', 'backward_pass_only'}. When set to 'unspecified', the mode set
in TPUEmbeddingConfiguration is used, otherwise mode_override is used.
</td>
</tr><tr>
<td>
`device_ordinal`
</td>
<td>
An optional `int`. Defaults to `-1`.
The TPU device to use. Should be >= 0 and less than the number
of TPU cores in the task on which the node is placed.
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
The created Operation.
</td>
</tr>

</table>

