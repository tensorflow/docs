description: Eases the porting of code that uses tf.nn.embedding_lookup_sparse().

robots: noindex

# tf.raw_ops.EnqueueTPUEmbeddingSparseTensorBatch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Eases the porting of code that uses tf.nn.embedding_lookup_sparse().

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.EnqueueTPUEmbeddingSparseTensorBatch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.EnqueueTPUEmbeddingSparseTensorBatch(
    sample_indices, embedding_indices, aggregation_weights, mode_override,
    table_ids, device_ordinal=-1, combiners=[], max_sequence_lengths=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

sample_indices[i], embedding_indices[i] and aggregation_weights[i] correspond
to the ith feature. table_ids[i] indicates which embedding table to look up ith
feature.

The tensors at corresponding positions in the three input lists (sample_indices,
embedding_indices and aggregation_weights) must have the same shape, i.e. rank 1
with dim_size() equal to the total number of lookups into the table described by
the corresponding feature.

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
A list of rank 1 Tensors specifying the training example to
which the corresponding embedding_indices and aggregation_weights values
belong. It corresponds to sp_ids.indices[:,0] in  embedding_lookup_sparse().
</td>
</tr><tr>
<td>
`embedding_indices`
</td>
<td>
A list with the same length as `sample_indices` of `Tensor` objects with the same type in: `int32`, `int64`.
A list of rank 1 Tensors, indices into the embedding tables.
It corresponds to sp_ids.values in embedding_lookup_sparse().
</td>
</tr><tr>
<td>
`aggregation_weights`
</td>
<td>
A list with the same length as `sample_indices` of `Tensor` objects with the same type in: `float32`, `float64`.
A list of rank 1 Tensors containing per training example
aggregation weights. It corresponds to sp_weights.values in
embedding_lookup_sparse().
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
`table_ids`
</td>
<td>
A list of `ints`.
A list of integers specifying the identifier of the embedding table
(offset of TableDescriptor in the TPUEmbeddingConfiguration) to lookup the
corresponding input. The ith input is looked up using table_ids[i]. The size
of the table_ids list must be equal to that of sample_indices,
embedding_indices and aggregation_weights.
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
`max_sequence_lengths`
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
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

