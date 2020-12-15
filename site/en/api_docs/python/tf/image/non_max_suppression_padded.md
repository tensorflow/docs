description: Greedily selects a subset of bounding boxes in descending order of score.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.non_max_suppression_padded" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.non_max_suppression_padded

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L5028-L5125">
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
<p>`tf.compat.v1.image.non_max_suppression_padded`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.non_max_suppression_padded(
    boxes, scores, max_output_size, iou_threshold=0.5,
    score_threshold=float('-inf'), pad_to_max_output_size=(False), name=None,
    sorted_input=(False), canonicalized_coordinates=(False), tile_size=512
)
</code></pre>



<!-- Placeholder for "Used in" -->

Performs algorithmically equivalent operation to tf.image.non_max_suppression,
with the addition of an optional parameter which zero-pads the output to
be of size `max_output_size`.
The output of this operation is a tuple containing the set of integers
indexing into the input collection of bounding boxes representing the selected
boxes and the number of valid indices in the index set.  The bounding box
coordinates corresponding to the selected indices can then be obtained using
the <a href="../../tf/slice.md"><code>tf.slice</code></a> and <a href="../../tf/gather.md"><code>tf.gather</code></a> operations.  For example:
  ```python
  selected_indices_padded, num_valid = tf.image.non_max_suppression_padded(
      boxes, scores, max_output_size, iou_threshold,
      score_threshold, pad_to_max_output_size=True)
  selected_indices = tf.slice(
      selected_indices_padded, tf.constant([0]), num_valid)
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
a tensor of rank 2 or higher with a shape of [..., num_boxes, 4].
Dimensions except the last two are batch dimensions.
</td>
</tr><tr>
<td>
`scores`
</td>
<td>
a tensor of rank 1 or higher with a shape of [..., num_boxes].
</td>
</tr><tr>
<td>
`max_output_size`
</td>
<td>
a scalar integer `Tensor` representing the maximum number
of boxes to be selected by non max suppression.
</td>
</tr><tr>
<td>
`iou_threshold`
</td>
<td>
a float representing the threshold for deciding whether boxes
overlap too much with respect to IoU (intersection over union).
</td>
</tr><tr>
<td>
`score_threshold`
</td>
<td>
a float representing the threshold for box scores. Boxes
with a score that is not larger than this threshold will be suppressed.
</td>
</tr><tr>
<td>
`pad_to_max_output_size`
</td>
<td>
whether to pad the output idx to max_output_size.
Must be set to True when the input is a batch of images.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
name of operation.
</td>
</tr><tr>
<td>
`sorted_input`
</td>
<td>
a boolean indicating whether the input boxes and scores
are sorted in descending order by the score.
</td>
</tr><tr>
<td>
`canonicalized_coordinates`
</td>
<td>
if box coordinates are given as
`[y_min, x_min, y_max, x_max]`, setting to True eliminate redundant
computation to canonicalize box coordinates.
</td>
</tr><tr>
<td>
`tile_size`
</td>
<td>
an integer representing the number of boxes in a tile, i.e.,
the maximum number of boxes per image that can be used to suppress other
boxes in parallel; larger tile_size means larger parallelism and
potentially more redundant work.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
idx: a tensor with a shape of [..., num_boxes] representing the
indices selected by non-max suppression. The leading dimensions
are the batch dimensions of the input boxes. All numbers are within
[0, num_boxes). For each image (i.e., idx[i]), only the first num_valid[i]
indices (i.e., idx[i][:num_valid[i]]) are valid.
num_valid: a tensor of rank 0 or higher with a shape of [...]
representing the number of valid indices in idx. Its dimensions are the
batch dimensions of the input boxes.
</td>
</tr>
<tr>
<td>
`Raises`
</td>
<td>
ValueError: When set pad_to_max_output_size to False for batched input.
</td>
</tr>
</table>

