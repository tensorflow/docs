page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.non_max_suppression


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/non_max_suppression">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L2604-L2653">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Greedily selects a subset of bounding boxes in descending order of score.

### Aliases:

* <a href="/api_docs/python/tf/image/non_max_suppression"><code>tf.compat.v1.image.non_max_suppression</code></a>
* <a href="/api_docs/python/tf/image/non_max_suppression"><code>tf.compat.v2.image.non_max_suppression</code></a>


``` python
tf.image.non_max_suppression(
    boxes,
    scores,
    max_output_size,
    iou_threshold=0.5,
    score_threshold=float('-inf'),
    name=None
)
```



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
using the <a href="../../tf/gather"><code>tf.gather</code></a> operation.  For example:

>     selected_indices = tf.image.non_max_suppression(
>         boxes, scores, max_output_size, iou_threshold)
>     selected_boxes = tf.gather(boxes, selected_indices)

#### Args:


* <b>`boxes`</b>: A 2-D float `Tensor` of shape `[num_boxes, 4]`.
* <b>`scores`</b>: A 1-D float `Tensor` of shape `[num_boxes]` representing a single
  score corresponding to each box (each row of boxes).
* <b>`max_output_size`</b>: A scalar integer `Tensor` representing the maximum number
  of boxes to be selected by non max suppression.
* <b>`iou_threshold`</b>: A float representing the threshold for deciding whether boxes
  overlap too much with respect to IOU.
* <b>`score_threshold`</b>: A float representing the threshold for deciding when to
  remove boxes based on score.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:


* <b>`selected_indices`</b>: A 1-D integer `Tensor` of shape `[M]` representing the
  selected indices from the boxes tensor, where `M <= max_output_size`.
