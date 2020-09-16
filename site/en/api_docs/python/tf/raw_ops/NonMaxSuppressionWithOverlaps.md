description: Greedily selects a subset of bounding boxes in descending order of score,

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.NonMaxSuppressionWithOverlaps" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.NonMaxSuppressionWithOverlaps

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Greedily selects a subset of bounding boxes in descending order of score,

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.NonMaxSuppressionWithOverlaps`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.NonMaxSuppressionWithOverlaps(
    overlaps, scores, max_output_size, overlap_threshold, score_threshold, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

pruning away boxes that have high overlaps
with previously selected boxes.  Bounding boxes with score less than
`score_threshold` are removed. N-by-n overlap values are supplied as square matrix,
which allows for defining a custom overlap criterium (eg. intersection over union,
intersection over area, etc.).

The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes.  The bounding
box coordinates corresponding to the selected indices can then be obtained
using the `tf.gather operation`.  For example:

  selected_indices = tf.image.non_max_suppression_with_overlaps(
      overlaps, scores, max_output_size, overlap_threshold, score_threshold)
  selected_boxes = tf.gather(boxes, selected_indices)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`overlaps`
</td>
<td>
A `Tensor` of type `float32`.
A 2-D float tensor of shape `[num_boxes, num_boxes]` representing
the n-by-n box overlap values.
</td>
</tr><tr>
<td>
`scores`
</td>
<td>
A `Tensor` of type `float32`.
A 1-D float tensor of shape `[num_boxes]` representing a single
score corresponding to each box (each row of boxes).
</td>
</tr><tr>
<td>
`max_output_size`
</td>
<td>
A `Tensor` of type `int32`.
A scalar integer tensor representing the maximum number of
boxes to be selected by non max suppression.
</td>
</tr><tr>
<td>
`overlap_threshold`
</td>
<td>
A `Tensor` of type `float32`.
A 0-D float tensor representing the threshold for deciding whether
boxes overlap too.
</td>
</tr><tr>
<td>
`score_threshold`
</td>
<td>
A `Tensor` of type `float32`.
A 0-D float tensor representing the threshold for deciding when to remove
boxes based on score.
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
A `Tensor` of type `int32`.
</td>
</tr>

</table>

