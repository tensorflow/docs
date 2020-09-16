description: Lookup embedding results, accounting for invalid IDs and empty features.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.safe_embedding_lookup_sparse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.safe_embedding_lookup_sparse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/embedding_ops.py#L671-L770">
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
vocabulary size is not necessarily a multiple of num of shards.

Invalid IDs (< 0) are pruned from input IDs and weights, as well as any IDs
with non-positive weight. For an entry with no features, the embedding vector
for `default_id` is returned, or the 0-vector if `default_id` is not supplied.

The ids and weights may be multi-dimensional. Embeddings are always aggregated
along the last dimension.

If `len(embedding_weights) > 1`, each element `id` of `ids` is partitioned
between the elements of `embedding_weights` according to the "div" partition
strategy, which means we assign ids to partitions in a contiguous manner. For
instance, 13 ids are split across 5 partitions as:
`[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.

If the id space does not evenly divide the number of partitions, each of the
first `(max_id + 1) % len(embedding_weights)` partitions will be assigned one
more id.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`embedding_weights`
</td>
<td>
A single tensor representing the complete embedding
tensor, or a list of tensors all of same shape except for the first
dimension, representing sharded embedding tensors following "div"
partition strategy.
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
The id to use for an entry with no features. Defaults to
0-vector.
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
A dense tensor representing the combined embeddings for the
sparse ids. For each row in the dense tensor represented by `sparse_ids`,
the op looks up the embeddings for all ids in that row, multiplies them by
the corresponding weight, and combines these embeddings as specified.

In other words, if

`shape(combined embedding_weights) = [p0, p1, ..., pm]`

and

`shape(sparse_ids) = shape(sparse_weights) = [d0, d1, ..., dn]`

then

`shape(output) = [d0, d1, ... dn-1, p1, ..., pm]`.

For instance, if params is a 10x20 matrix, and sp_ids / sp_weights are

```python
[0, 0]: id 1, weight 2.0
[0, 1]: id 3, weight 0.5
[1, 0]: id -1, weight 1.0
[2, 3]: id 1, weight 3.0
```

`default_id` is 0.

with `combiner`="mean", then the output will be a 3x20 matrix where

```python
output[0, :] = (params[1, :] * 2.0 + params[3, :] * 0.5) / (2.0 + 0.5)
output[1, :] = (params[0, :] * 1.0) / 1.0
output[2, :] = (params[1, :] * 3.0) / 3.0
```
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

