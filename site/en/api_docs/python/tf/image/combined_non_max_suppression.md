description: Greedily selects a subset of bounding boxes in descending order of score.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.combined_non_max_suppression" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.combined_non_max_suppression

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L4233-L4302">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Greedily selects a subset of bounding boxes in descending order of score.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.combined_non_max_suppression`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.combined_non_max_suppression(
    boxes, scores, max_output_size_per_class, max_total_size, iou_threshold=0.5,
    score_threshold=float('-inf'), pad_per_class=(False), clip_boxes=(True),
    name=None
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
A 4-D float `Tensor` of shape `[batch_size, num_boxes, q, 4]`. If `q`
is 1 then same boxes are used for all classes otherwise, if `q` is equal
to number of classes, class-specific boxes are used.
</td>
</tr><tr>
<td>
`scores`
</td>
<td>
A 3-D float `Tensor` of shape `[batch_size, num_boxes, num_classes]`
representing a single score corresponding to each box (each row of boxes).
</td>
</tr><tr>
<td>
`max_output_size_per_class`
</td>
<td>
A scalar integer `Tensor` representing the
maximum number of boxes to be selected by non-max suppression per class
</td>
</tr><tr>
<td>
`max_total_size`
</td>
<td>
A scalar representing the maximum number of boxes retained
over all classes.
</td>
</tr><tr>
<td>
`iou_threshold`
</td>
<td>
A float representing the threshold for deciding whether boxes
overlap too much with respect to IOU.
</td>
</tr><tr>
<td>
`score_threshold`
</td>
<td>
A float representing the threshold for deciding when to
remove boxes based on score.
</td>
</tr><tr>
<td>
`pad_per_class`
</td>
<td>
If false, the output nmsed boxes, scores and classes are
padded/clipped to `max_total_size`. If true, the output nmsed boxes,
scores and classes are padded to be of length
`max_size_per_class`*`num_classes`, unless it exceeds `max_total_size` in
which case it is clipped to `max_total_size`. Defaults to false.
</td>
</tr><tr>
<td>
`clip_boxes`
</td>
<td>
If true, the coordinates of output nmsed boxes will be clipped
to [0, 1]. If false, output the box coordinates as it is. Defaults to
true.
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
'nmsed_boxes': A [batch_size, max_detections, 4] float32 tensor
containing the non-max suppressed boxes.
'nmsed_scores': A [batch_size, max_detections] float32 tensor containing
the scores for the boxes.
'nmsed_classes': A [batch_size, max_detections] float32 tensor
containing the class for boxes.
'valid_detections': A [batch_size] int32 tensor indicating the number of
valid detections per batch item. Only the top valid_detections[i] entries
in nms_boxes[i], nms_scores[i] and nms_class[i] are valid. The rest of the
entries are zero paddings.
</td>
</tr>

</table>

