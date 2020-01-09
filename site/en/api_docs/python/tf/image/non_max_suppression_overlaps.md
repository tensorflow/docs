page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.non_max_suppression_overlaps


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/non_max_suppression_overlaps">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L2806-L2848">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Greedily selects a subset of bounding boxes in descending order of score.

### Aliases:

* <a href="/api_docs/python/tf/image/non_max_suppression_overlaps"><code>tf.compat.v1.image.non_max_suppression_overlaps</code></a>
* <a href="/api_docs/python/tf/image/non_max_suppression_overlaps"><code>tf.compat.v2.image.non_max_suppression_overlaps</code></a>


``` python
tf.image.non_max_suppression_overlaps(
    overlaps,
    scores,
    max_output_size,
    overlap_threshold=0.5,
    score_threshold=float('-inf'),
    name=None
)
```



<!-- Placeholder for "Used in" -->

Prunes away boxes that have high overlap with previously selected boxes.
N-by-n overlap values are supplied as square matrix.
The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes.  The bounding
box coordinates corresponding to the selected indices can then be obtained
using the <a href="../../tf/gather"><code>tf.gather</code></a> operation.  For example:

>     selected_indices = tf.image.non_max_suppression_overlaps(
>         overlaps, scores, max_output_size, iou_threshold)
>     selected_boxes = tf.gather(boxes, selected_indices)

#### Args:


* <b>`overlaps`</b>: A 2-D float `Tensor` of shape `[num_boxes, num_boxes]`.
* <b>`scores`</b>: A 1-D float `Tensor` of shape `[num_boxes]` representing a single
  score corresponding to each box (each row of boxes).
* <b>`max_output_size`</b>: A scalar integer `Tensor` representing the maximum number
  of boxes to be selected by non max suppression.
* <b>`overlap_threshold`</b>: A float representing the threshold for deciding whether
  boxes overlap too much with respect to the provided overlap values.
* <b>`score_threshold`</b>: A float representing the threshold for deciding when to
  remove boxes based on score.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:


* <b>`selected_indices`</b>: A 1-D integer `Tensor` of shape `[M]` representing the
  selected indices from the overlaps tensor, where `M <= max_output_size`.
