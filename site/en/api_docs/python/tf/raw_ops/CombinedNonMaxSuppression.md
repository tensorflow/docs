description: Greedily selects a subset of bounding boxes in descending order of score,

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CombinedNonMaxSuppression" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CombinedNonMaxSuppression

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
<p>`tf.compat.v1.raw_ops.CombinedNonMaxSuppression`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CombinedNonMaxSuppression(
    boxes, scores, max_output_size_per_class, max_total_size, iou_threshold,
    score_threshold, pad_per_class=(False), clip_boxes=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation performs non_max_suppression on the inputs per batch, across
all classes.
Prunes away boxes that have high intersection-over-union (IOU) overlap
with previously selected boxes.  Bounding boxes are supplied as
[y1, x1, y2, x2], where (y1, x1) and (y2, x2) are the coordinates of any
diagonal pair of box corners and the coordinates can be provided as normalized
(i.e., lying in the interval [0, 1]) or absolute.  Note that this algorithm
is agnostic to where the origin is in the coordinate system. Also note that
this algorithm is invariant to orthogonal transformations and translations
of the coordinate system; thus translating or reflections of the coordinate
system result in the same boxes being selected by the algorithm.
The output of this operation is the final boxes, scores and classes tensor
returned after performing non_max_suppression.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`boxes`
</td>
<td>
A `Tensor` of type `float32`.
A 4-D float tensor of shape `[batch_size, num_boxes, q, 4]`. If `q` is 1 then
same boxes are used for all classes otherwise, if `q` is equal to number of
classes, class-specific boxes are used.
</td>
</tr><tr>
<td>
`scores`
</td>
<td>
A `Tensor` of type `float32`.
A 3-D float tensor of shape `[batch_size, num_boxes, num_classes]`
representing a single score corresponding to each box (each row of boxes).
</td>
</tr><tr>
<td>
`max_output_size_per_class`
</td>
<td>
A `Tensor` of type `int32`.
A scalar integer tensor representing the maximum number of
boxes to be selected by non max suppression per class
</td>
</tr><tr>
<td>
`max_total_size`
</td>
<td>
A `Tensor` of type `int32`.
A scalar representing maximum number of boxes retained over all classes.
</td>
</tr><tr>
<td>
`iou_threshold`
</td>
<td>
A `Tensor` of type `float32`.
A 0-D float tensor representing the threshold for deciding whether
boxes overlap too much with respect to IOU.
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
`pad_per_class`
</td>
<td>
An optional `bool`. Defaults to `False`.
If false, the output nmsed boxes, scores and classes
are padded/clipped to `max_total_size`. If true, the
output nmsed boxes, scores and classes are padded to be of length
`max_size_per_class`*`num_classes`, unless it exceeds `max_total_size` in
which case it is clipped to `max_total_size`. Defaults to false.
</td>
</tr><tr>
<td>
`clip_boxes`
</td>
<td>
An optional `bool`. Defaults to `True`.
If true, assume the box coordinates are between [0, 1] and clip the output boxes
if they fall beyond [0, 1]. If false, do not do clipping and output the box
coordinates as it is.
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
A tuple of `Tensor` objects (nmsed_boxes, nmsed_scores, nmsed_classes, valid_detections).
</td>
</tr>
<tr>
<td>
`nmsed_boxes`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`nmsed_scores`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`nmsed_classes`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`valid_detections`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr>
</table>

