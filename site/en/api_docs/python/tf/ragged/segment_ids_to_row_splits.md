description: Generates the RaggedTensor row_splits corresponding to a segmentation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.segment_ids_to_row_splits" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.segment_ids_to_row_splits

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ragged/segment_id_ops.py#L76-L132">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates the RaggedTensor `row_splits` corresponding to a segmentation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.segment_ids_to_row_splits`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.segment_ids_to_row_splits(
    segment_ids, num_segments=None, out_type=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns an integer vector `splits`, where `splits[0] = 0` and
`splits[i] = splits[i-1] + count(segment_ids==i)`.  Example:

```
>>> print(tf.ragged.segment_ids_to_row_splits([0, 0, 0, 2, 2, 3, 4, 4, 4]))
tf.Tensor([0 3 3 5 6 9], shape=(6,), dtype=int64)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`segment_ids`
</td>
<td>
A 1-D integer Tensor.
</td>
</tr><tr>
<td>
`num_segments`
</td>
<td>
A scalar integer indicating the number of segments.  Defaults
to `max(segment_ids) + 1` (or zero if `segment_ids` is empty).
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
The dtype for the return value.  Defaults to `segment_ids.dtype`,
or <a href="../../tf.md#int64"><code>tf.int64</code></a> if `segment_ids` does not have a dtype.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A sorted 1-D integer Tensor, with `shape=[num_segments + 1]`.
</td>
</tr>

</table>

