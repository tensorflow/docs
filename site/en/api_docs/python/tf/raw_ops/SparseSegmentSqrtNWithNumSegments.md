description: Computes the sum along sparse segments of a tensor divided by the sqrt of N.

robots: noindex

# tf.raw_ops.SparseSegmentSqrtNWithNumSegments

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the sum along sparse segments of a tensor divided by the sqrt of N.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseSegmentSqrtNWithNumSegments`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseSegmentSqrtNWithNumSegments(
    data, indices, segment_ids, num_segments, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

N is the size of the segment being reduced.

Like `SparseSegmentSqrtN`, but allows missing ids in `segment_ids`. If an id is
missing, the `output` tensor at that position will be zeroed.

Read
[the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
for an explanation of segments.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A 1-D tensor. Has same rank as `segment_ids`.
</td>
</tr><tr>
<td>
`segment_ids`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A 1-D tensor. Values should be sorted and can be repeated.
</td>
</tr><tr>
<td>
`num_segments`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Should equal the number of distinct segment IDs.
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
A `Tensor`. Has the same type as `data`.
</td>
</tr>

</table>

