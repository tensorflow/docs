description: This op produces Region of Interests from given bounding boxes(bbox_deltas) encoded wrt anchors according to eq.2 in arXiv:1506.01497

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.GenerateBoundingBoxProposals" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.GenerateBoundingBoxProposals

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



This op produces Region of Interests from given bounding boxes(bbox_deltas) encoded wrt anchors according to eq.2 in arXiv:1506.01497

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.GenerateBoundingBoxProposals`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.GenerateBoundingBoxProposals(
    scores, bbox_deltas, image_info, anchors, nms_threshold, pre_nms_topn, min_size,
    post_nms_topn=300, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

      The op selects top `pre_nms_topn` scoring boxes, decodes them with respect to anchors,
      applies non-maximal suppression on overlapping boxes with higher than
      `nms_threshold` intersection-over-union (iou) value, discarding boxes where shorter
      side is less than `min_size`.
      Inputs:
      `scores`: A 4D tensor of shape [Batch, Height, Width, Num Anchors] containing the scores per anchor at given postion
      `bbox_deltas`: is a tensor of shape [Batch, Height, Width, 4 x Num Anchors] boxes encoded to each anchor
      `anchors`: A 1D tensor of shape [4 x Num Anchors], representing the anchors.
      Outputs:
      `rois`: output RoIs, a 3D tensor of shape [Batch, post_nms_topn, 4], padded by 0 if less than post_nms_topn candidates found.
      `roi_probabilities`: probability scores of each roi in 'rois', a 2D tensor of shape [Batch,post_nms_topn], padded with 0 if needed, sorted by scores.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`scores`
</td>
<td>
A `Tensor` of type `float32`.
A 4-D float tensor of shape `[num_images, height, width, num_achors]` containing scores of the boxes for given anchors, can be unsorted.
</td>
</tr><tr>
<td>
`bbox_deltas`
</td>
<td>
A `Tensor` of type `float32`.
A 4-D float tensor of shape `[num_images, height, width, 4 x num_anchors]`. encoding boxes with respec to each anchor.
Coordinates are given in the form [dy, dx, dh, dw].
</td>
</tr><tr>
<td>
`image_info`
</td>
<td>
A `Tensor` of type `float32`.
A 2-D float tensor of shape `[num_images, 5]` containing image information Height, Width, Scale.
</td>
</tr><tr>
<td>
`anchors`
</td>
<td>
A `Tensor` of type `float32`.
A 2-D float tensor of shape `[num_anchors, 4]` describing the anchor boxes. Boxes are formatted in the form [y1, x1, y2, x2].
</td>
</tr><tr>
<td>
`nms_threshold`
</td>
<td>
A `Tensor` of type `float32`.
A scalar float tensor for non-maximal-suppression threshold.
</td>
</tr><tr>
<td>
`pre_nms_topn`
</td>
<td>
A `Tensor` of type `int32`.
A scalar int tensor for the number of top scoring boxes to be used as input.
</td>
</tr><tr>
<td>
`min_size`
</td>
<td>
A `Tensor` of type `float32`.
A scalar float tensor. Any box that has a smaller size than min_size will be discarded.
</td>
</tr><tr>
<td>
`post_nms_topn`
</td>
<td>
An optional `int`. Defaults to `300`.
An integer. Maximum number of rois in the output.
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
A tuple of `Tensor` objects (rois, roi_probabilities).
</td>
</tr>
<tr>
<td>
`rois`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`roi_probabilities`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

