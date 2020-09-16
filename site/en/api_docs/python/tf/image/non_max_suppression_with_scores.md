description: Greedily selects a subset of bounding boxes in descending order of score.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.non_max_suppression_with_scores" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.non_max_suppression_with_scores

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L2996-L3079">
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
<p>`tf.compat.v1.image.non_max_suppression_with_scores`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.non_max_suppression_with_scores(
    boxes, scores, max_output_size, iou_threshold=0.5,
    score_threshold=float('-inf'), soft_nms_sigma=0.0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Prunes away boxes that have high intersection-over-union (IOU) overlap
with previously selected boxes.  Bounding boxes are supplied as
`[y1, x1, y2, x2]`, where `(y1, x1)` and `(y2, x2)` are the coordinates of any
diagonal pair of box corners and the coordinates can be provided as normalized
(i.e., lying in the interval `[0, 1]`) or absolute.  Note that this algorithm
is agnostic to where the origin is in the coordinate system.  Note that this
algorithm is invariant to orthogonal transformations and translations
of the coordinate system; thus translating or reflections of the coordinate
system result in the same boxes being selected by the algorithm.
The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes.  The bounding
box coordinates corresponding to the selected indices can then be obtained
using the <a href="../../tf/gather.md"><code>tf.gather</code></a> operation.  For example:
  ```python
  selected_indices, selected_scores = tf.image.non_max_suppression_v2(
      boxes, scores, max_output_size, iou_threshold=1.0, score_threshold=0.1,
      soft_nms_sigma=0.5)
  selected_boxes = tf.gather(boxes, selected_indices)
  ```

This function generalizes the <a href="../../tf/image/non_max_suppression.md"><code>tf.image.non_max_suppression</code></a> op by also
supporting a Soft-NMS (with Gaussian weighting) mode (c.f.
Bodla et al, https://arxiv.org/abs/1704.04503) where boxes reduce the score
of other overlapping boxes instead of directly causing them to be pruned.
Consequently, in contrast to <a href="../../tf/image/non_max_suppression.md"><code>tf.image.non_max_suppression</code></a>,
`tf.image.non_max_suppression_v2` returns the new scores of each input box in
the second output, `selected_scores`.

To enable this Soft-NMS mode, set the `soft_nms_sigma` parameter to be
larger than 0.  When `soft_nms_sigma` equals 0, the behavior of
`tf.image.non_max_suppression_v2` is identical to that of
<a href="../../tf/image/non_max_suppression.md"><code>tf.image.non_max_suppression</code></a> (except for the extra output) both in function
and in running time.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`boxes`
</td>
<td>
A 2-D float `Tensor` of shape `[num_boxes, 4]`.
</td>
</tr><tr>
<td>
`scores`
</td>
<td>
A 1-D float `Tensor` of shape `[num_boxes]` representing a single
score corresponding to each box (each row of boxes).
</td>
</tr><tr>
<td>
`max_output_size`
</td>
<td>
A scalar integer `Tensor` representing the maximum number
of boxes to be selected by non-max suppression.
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
`soft_nms_sigma`
</td>
<td>
A scalar float representing the Soft NMS sigma parameter;
See Bodla et al, https://arxiv.org/abs/1704.04503).  When
`soft_nms_sigma=0.0` (which is default), we fall back to standard (hard)
NMS.
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

<tr>
<td>
`selected_indices`
</td>
<td>
A 1-D integer `Tensor` of shape `[M]` representing the
selected indices from the boxes tensor, where `M <= max_output_size`.
</td>
</tr><tr>
<td>
`selected_scores`
</td>
<td>
A 1-D float tensor of shape `[M]` representing the
corresponding scores for each selected box, where `M <= max_output_size`.
Scores only differ from corresponding input scores when using Soft NMS
(i.e. when `soft_nms_sigma>0`)
</td>
</tr>
</table>

