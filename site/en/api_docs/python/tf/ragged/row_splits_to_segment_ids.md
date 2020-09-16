description: Generates the segmentation corresponding to a RaggedTensor row_splits.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.row_splits_to_segment_ids" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.row_splits_to_segment_ids

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ragged/segment_id_ops.py#L34-L73">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates the segmentation corresponding to a RaggedTensor `row_splits`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.row_splits_to_segment_ids`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.row_splits_to_segment_ids(
    splits, name=None, out_type=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns an integer vector `segment_ids`, where `segment_ids[i] == j` if
`splits[j] <= i < splits[j+1]`.  Example:

```
>>> print(tf.ragged.row_splits_to_segment_ids([0, 3, 3, 5, 6, 9]))
 tf.Tensor([0 0 0 2 2 3 4 4 4], shape=(9,), dtype=int64)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`splits`
</td>
<td>
A sorted 1-D integer Tensor.  `splits[0]` must be zero.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
The dtype for the return value.  Defaults to `splits.dtype`,
or <a href="../../tf.md#int64"><code>tf.int64</code></a> if `splits` does not have a dtype.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A sorted 1-D integer Tensor, with `shape=[splits[-1]]`
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
If `splits` is invalid.
</td>
</tr>
</table>

