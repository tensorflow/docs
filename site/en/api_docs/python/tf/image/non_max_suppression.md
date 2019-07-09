page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.non_max_suppression

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



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Working with Bounding Boxes](../../../../api_guides/python/image#Working_with_Bounding_Boxes)

Greedily selects a subset of bounding boxes in descending order of score.

Prunes away boxes that have high intersection-over-union (IOU) overlap
with previously selected boxes.  Bounding boxes are supplied as
[y1, x1, y2, x2], where (y1, x1) and (y2, x2) are the coordinates of any
diagonal pair of box corners and the coordinates can be provided as normalized
(i.e., lying in the interval [0, 1]) or absolute.  Note that this algorithm
is agnostic to where the origin is in the coordinate system.  Note that this
algorithm is invariant to orthogonal transformations and translations
of the coordinate system; thus translating or reflections of the coordinate
system result in the same boxes being selected by the algorithm.
The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes.  The bounding
box coordinates corresponding to the selected indices can then be obtained
using the `tf.gather operation`.  For example:
  selected_indices = tf.image.non_max_suppression(
      boxes, scores, max_output_size, iou_threshold)
  selected_boxes = tf.gather(boxes, selected_indices)

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