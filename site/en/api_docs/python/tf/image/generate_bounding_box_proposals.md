description: Generate bounding box proposals from encoded bounding boxes.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.generate_bounding_box_proposals" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.generate_bounding_box_proposals

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/image_ops_impl.py#L5001-L5027">
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
scores of the ROI boxes in the ROIs' tensor.
</td>
</tr>
</table>

