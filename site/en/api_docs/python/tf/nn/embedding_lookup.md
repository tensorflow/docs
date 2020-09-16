description: Looks up ids in a list of embedding tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.embedding_lookup" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.embedding_lookup

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/embedding_ops.py#L329-L373">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Looks up `ids` in a list of embedding tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.embedding_lookup(
    params, ids, max_norm=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function is used to perform parallel lookups on the list of
tensors in `params`.  It is a generalization of
<a href="../../tf/gather.md"><code>tf.gather</code></a>, where `params` is
interpreted as a partitioning of a large embedding tensor.  `params` may be
a `PartitionedVariable` as returned by using <a href="../../tf/compat/v1/get_variable.md"><code>tf.compat.v1.get_variable()</code></a>
with a
partitioner.

If `len(params) > 1`, each element `id` of `ids` is partitioned between
the elements of `params` according to the `partition_strategy`.
In all strategies, if the id space does not evenly divide the number of
partitions, each of the first `(max_id + 1) % len(params)` partitions will
be assigned one more id.

The `partition_strategy` is always `"div"` currently. This means that we
assign ids to partitions in a contiguous manner. For instance, 13 ids are
split across 5 partitions as:
`[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`

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
element must be appropriately sized for the 'div' `partition_strategy`.
</td>
</tr><tr>
<td>
`ids`
</td>
<td>
A `Tensor` with type `int32` or `int64` containing the ids to be looked
up in `params`.
</td>
</tr><tr>
<td>
`max_norm`
</td>
<td>
If not `None`, each embedding is clipped if its l2-norm is larger
than this value.
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
A `Tensor` with the same type as the tensors in `params`.
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

