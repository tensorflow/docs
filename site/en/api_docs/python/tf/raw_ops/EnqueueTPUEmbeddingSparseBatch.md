description: An op that enqueues TPUEmbedding input indices from a SparseTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.EnqueueTPUEmbeddingSparseBatch" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.EnqueueTPUEmbeddingSparseBatch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An op that enqueues TPUEmbedding input indices from a SparseTensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.EnqueueTPUEmbeddingSparseBatch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.EnqueueTPUEmbeddingSparseBatch(
    sample_indices, embedding_indices, aggregation_weights, mode_override,
    device_ordinal=-1, combiners=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This Op eases the porting of code that uses embedding_lookup_sparse(),
although some Python preprocessing of the SparseTensor arguments to
embedding_lookup_sparse() is required to produce the arguments to this Op,
since only a single EnqueueTPUEmbeddingSparseBatch Op is allowed per training
step.

The tensors at corresponding positions in the three input lists
must have the same shape, i.e. rank 1 with dim_size() equal to the total
number of lookups into the table described by the corresponding table_id.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sample_indices`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
A list of rank 1 Tensors specifying the training example and
feature to which the corresponding embedding_indices and aggregation_weights
values belong. sample_indices[i] must equal b * nf + f, where nf is the
number of features from the corresponding table, f is in [0, nf), and
b is in [0, batch size).
</td>
</tr><tr>
<td>
`embedding_indices`
</td>
<td>
A list with the same length as `sample_indices` of `Tensor` objects with the same type in: `int32`, `int64`.
A list of rank 1 Tensors, indices into the embedding tables.
</td>
</tr><tr>
<td>
`aggregation_weights`
</td>
<td>
A list with the same length as `sample_indices` of `Tensor` objects with the same type in: `float32`, `float64`.
A list of rank 1 Tensors containing per sample -- i.e. per
(training example, feature) -- aggregation weights.
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
`combiners`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
A list of string scalars, one for each embedding table that specify
how to normalize the embedding activations after weighted summation.
Supported combiners are 'mean', 'sum', or 'sqrtn'. It is invalid to have
the sum of the weights be 0 for 'mean' or the sum of the squared weights be
0 for 'sqrtn'. If combiners isn't passed, the default is to use 'sum' for
all tables.
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

