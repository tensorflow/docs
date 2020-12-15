description: Looks up embeddings for the given ids from a list of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.embedding_lookup" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.embedding_lookup

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/embedding_ops.py#L331-L394">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Looks up embeddings for the given `ids` from a list of tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.embedding_lookup(
    params, ids, max_norm=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function is used to perform parallel lookups on the list of tensors in
`params`.  It is a generalization of <a href="../../tf/gather.md"><code>tf.gather</code></a>, where `params` is
interpreted as a partitioning of a large embedding tensor.

If `len(params) > 1`, each element `id` of `ids` is partitioned between the
elements of `params` according to the "div" partition strategy, which means we
assign ids to partitions in a contiguous manner. For instance, 13 ids are
split across 5 partitions as:
`[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.

If the id space does not evenly divide the number of partitions, each of the
first `(max_id + 1) % len(params)` partitions will be assigned one more id.

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
list of tensors all of same shape except for the first dimension,
representing sharded embedding tensors following "div" partition strategy.
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

For instance, if `params` is a 5x2 matrix:

```python
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
```

or a list of matrices:

```python
params[0]: [[1, 2], [3, 4]]
params[1]: [[5, 6], [7, 8]]
params[2]: [[9, 10]]
```

and `ids` is:

```python
[0, 3, 4]
```

The output will be a 3x2 matrix:

```python
[[1, 2], [7, 8], [9, 10]]
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
If `params` is empty.
</td>
</tr>
</table>

