description: Generate bounding box proposals from encoded bounding boxes.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.generate_bounding_box_proposals" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.generate_bounding_box_proposals

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L5532-L5580">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generate bounding box proposals from encoded bounding boxes.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.generate_bounding_box_proposals`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.generate_bounding_box_proposals(
    scores, bbox_deltas, image_info, anchors, nms_threshold=0.7, pre_nms_topn=6000,
    min_size=16, post_nms_topn=300, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`scores`
</td>
<td>
A 4-D float `Tensor` of shape
`[num_images, height, width, num_achors]` containing scores of
the boxes for given anchors, can be unsorted.
</td>
</tr><tr>
<td>
`bbox_deltas`
</td>
<td>
A 4-D float `Tensor` of shape
`[num_images, height, width, 4 x num_anchors]` encoding boxes 
with respect to each anchor. Coordinates are given 
in the form `[dy, dx, dh, dw]`.
</td>
</tr><tr>
<td>
`image_info`
</td>
<td>
A 2-D float `Tensor` of shape `[num_images, 5]` 
containing image information Height, Width, Scale.
</td>
</tr><tr>
<td>
`anchors`
</td>
<td>
A 2-D float `Tensor` of shape `[num_anchors, 4]` 
describing the anchor boxes.
Boxes are formatted in the form `[y1, x1, y2, x2]`.
</td>
</tr><tr>
<td>
`nms_threshold`
</td>
<td>
A scalar float `Tensor` for non-maximal-suppression
threshold. Defaults to 0.7.
</td>
</tr><tr>
<td>
`pre_nms_topn`
</td>
<td>
A scalar int `Tensor` for the number of 
top scoring boxes to be used as input. Defaults to 6000.
</td>
</tr><tr>
<td>
`min_size`
</td>
<td>
A scalar float `Tensor`. Any box that has a smaller size
than min_size will be discarded. Defaults to 16.
</td>
</tr><tr>
<td>
`post_nms_topn`
</td>
<td>
An integer. Maximum number of rois in the output.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`rois`
</td>
<td>
Region of interest boxes sorted by their scores.
</td>
</tr><tr>
<td>
`roi_probabilities`
</td>
<td>
scores of the ROI boxes in the ROIs' `Tensor`.
</td>
</tr>
</table>

