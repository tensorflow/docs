description: Greedily selects a subset of bounding boxes in descending order of score.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.non_max_suppression_overlaps" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.non_max_suppression_overlaps

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L3138-L3180">
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
<p>`tf.compat.v1.image.non_max_suppression_overlaps`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.non_max_suppression_overlaps(
    overlaps, scores, max_output_size, overlap_threshold=0.5,
    score_threshold=float('-inf'), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Prunes away boxes that have high overlap with previously selected boxes.
N-by-n overlap values are supplied as square matrix.
The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes.  The bounding
box coordinates corresponding to the selected indices can then be obtained
using the <a href="../../tf/gather.md"><code>tf.gather</code></a> operation.  For example:
  ```python
  selected_indices = tf.image.non_max_suppression_overlaps(
      overlaps, scores, max_output_size, iou_threshold)
  selected_boxes = tf.gather(boxes, selected_indices)
  ```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`overlaps`
</td>
<td>
A 2-D float `Tensor` of shape `[num_boxes, num_boxes]`.
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
`overlap_threshold`
</td>
<td>
A float representing the threshold for deciding whether
boxes overlap too much with respect to the provided overlap values.
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
selected indices from the overlaps tensor, where `M <= max_output_size`.
</td>
</tr>
</table>

