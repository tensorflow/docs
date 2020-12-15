description: Looks up embeddings for the given ids from a list of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.embedding_lookup" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.embedding_lookup

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/embedding_ops.py#L253-L328">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Looks up embeddings for the given `ids` from a list of tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.embedding_lookup(
    params, ids, partition_strategy='mod', name=None, validate_indices=(True),
    max_norm=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function is used to perform parallel lookups on the list of tensors in
`params`.  It is a generalization of <a href="../../../../tf/gather.md"><code>tf.gather</code></a>, where `params` is
interpreted as a partitioning of a large embedding tensor.  `params` may be
a `PartitionedVariable` as returned by using <a href="../../../../tf/compat/v1/get_variable.md"><code>tf.compat.v1.get_variable()</code></a>
with a partitioner.

If `len(params) > 1`, each element `id` of `ids` is partitioned between
the elements of `params` according to the `partition_strategy`.
In all strategies, if the id space does not evenly divide the number of
partitions, each of the first `(max_id + 1) % len(params)` partitions will
be assigned one more id.

If `partition_strategy` is `"mod"`, we assign each id to partition
`p = id % len(params)`. For instance,
13 ids are split across 5 partitions as:
`[[0, 5, 10], [1, 6, 11], [2, 7, 12], [3, 8], [4, 9]]`

If `partition_strategy` is `"div"`, we assign ids to partitions in a
contiguous manner. In this case, 13 ids are split across 5 partitions as:
`[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`

If the input ids are ragged tensors, partition variables are not supported and
the partition strategy and the max_norm are ignored.
The results of the lookup are concatenated into a dense
tensor. The returned tensor has shape `shape(ids) + shape(params)[1:]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`params`
</td>
<td>
A single tensor representing the complete embedding tensor, or a
list of P tensors all of same shape except for the first dimension,
representing sharded embedding tensors.  Alternatively, a
`PartitionedVariable`, created by partitioning along dimension 0. Each
element must be appropriately sized for the given `partition_strategy`.
</td>
</tr><tr>
<td>
`ids`
</td>
<td>
A `Tensor` or a 'RaggedTensor' with type `int32` or `int64` containing
the ids to be looked up in `params`.
</td>
</tr><tr>
<td>
`partition_strategy`
</td>
<td>
A string specifying the partitioning strategy, relevant
if `len(params) > 1`. Currently `"div"` and `"mod"` are supported. Default
is `"mod"`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`validate_indices`
</td>
<td>
DEPRECATED. If this operation is assigned to CPU, values
in `indices` are always validated to be within range.  If assigned to GPU,
out-of-bound indices result in safe but unspecified behavior, which may
include raising an error.
</td>
</tr><tr>
<td>
`max_norm`
</td>
<td>
If not `None`, each embedding is clipped if its l2-norm is larger
than this value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` or a 'RaggedTensor', depending on the input, with the same type
as the tensors in `params`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `params` is empty.
</td>
</tr>
</table>

