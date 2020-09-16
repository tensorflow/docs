description: Lookup embedding results, accounting for invalid IDs and empty features.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.safe_embedding_lookup_sparse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.safe_embedding_lookup_sparse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/embedding_ops.py#L630-L691">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Lookup embedding results, accounting for invalid IDs and empty features.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.safe_embedding_lookup_sparse(
    embedding_weights, sparse_ids, sparse_weights=None, combiner='mean',
    default_id=None, max_norm=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The partitioned embedding in `embedding_weights` must all be the same shape
except for the first dimension. The first dimension is allowed to vary as the
vocabulary size is not necessarily a multiple of `P`.  `embedding_weights`
may be a `PartitionedVariable` as returned by using
<a href="../../tf/compat/v1/get_variable.md"><code>tf.compat.v1.get_variable()</code></a> with a
partitioner.

Invalid IDs (< 0) are pruned from input IDs and weights, as well as any IDs
with non-positive weight. For an entry with no features, the embedding vector
for `default_id` is returned, or the 0-vector if `default_id` is not supplied.

The ids and weights may be multi-dimensional. Embeddings are always aggregated
along the last dimension.

Note: when doing embedding lookup on `embedding_weights`, "div" partition
strategy will be used. Support for other partition strategy will be added
later.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`embedding_weights`
</td>
<td>
A list of `P` float `Tensor`s or values representing
partitioned embedding `Tensor`s.  Alternatively, a `PartitionedVariable`
created by partitioning along dimension 0.  The total unpartitioned shape
should be `[e_0, e_1, ..., e_m]`, where `e_0` represents the vocab size
and `e_1, ..., e_m` are the embedding dimensions.
</td>
</tr><tr>
<td>
`sparse_ids`
</td>
<td>
`SparseTensor` of shape `[d_0, d_1, ..., d_n]` containing the
ids. `d_0` is typically batch size.
</td>
</tr><tr>
<td>
`sparse_weights`
</td>
<td>
`SparseTensor` of same shape as `sparse_ids`, containing
float weights corresponding to `sparse_ids`, or `None` if all weights are
be assumed to be 1.0.
</td>
</tr><tr>
<td>
`combiner`
</td>
<td>
A string specifying how to combine embedding results for each
entry. Currently "mean", "sqrtn" and "sum" are supported, with "mean" the
default.
</td>
</tr><tr>
<td>
`default_id`
</td>
<td>
The id to use for an entry with no features.
</td>
</tr><tr>
<td>
`max_norm`
</td>
<td>
If not `None`, all embeddings are l2-normalized to max_norm before
combining.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Dense `Tensor` of shape `[d_0, d_1, ..., d_{n-1}, e_1, ..., e_m]`.
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
if `embedding_weights` is empty.
</td>
</tr>
</table>

