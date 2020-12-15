description: Greedily selects a subset of bounding boxes in descending order of score,

robots: noindex

# tf.raw_ops.NonMaxSuppressionV3

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
<p>`tf.compat.v1.raw_ops.NonMaxSuppressionV3`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.NonMaxSuppressionV3(
    boxes, scores, max_output_size, iou_threshold, score_threshold, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

pruning away boxes that have high intersection-over-union (IOU) overlap
with previously selected boxes.  Bounding boxes with score less than
`score_threshold` are removed.  Bounding boxes are supplied as
[y1, x1, y2, x2], where (y1, x1) and (y2, x2) are the coordinates of any
diagonal pair of box corners and the coordinates can be provided as normalized
(i.e., lying in the interval [0, 1]) or absolute.  Note that this algorithm
is agnostic to where the origin is in the coordinate system and more
generally is invariant to orthogonal transformations and translations
of the coordinate system; thus translating or reflections of the coordinate
system result in the same boxes being selected by the algorithm.
The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes.  The bounding
box coordinates corresponding to the selected indices can then be obtained
using the `tf.gather operation`.  For example:
  selected_indices = tf.image.non_max_suppression_v2(
      boxes, scores, max_output_size, iou_threshold, score_threshold)
  selected_boxes = tf.gather(boxes, selected_indices)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`boxes`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`.
A 2-D float tensor of shape `[num_boxes, 4]`.
</td>
</tr><tr>
<td>
`scores`
</td>
<td>
A `Tensor`. Must have the same type as `boxes`.
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
`iou_threshold`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`.
A 0-D float tensor representing the threshold for deciding whether
boxes overlap too much with respect to IOU.
</td>
</tr><tr>
<td>
`score_threshold`
</td>
<td>
A `Tensor`. Must have the same type as `iou_threshold`.
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

