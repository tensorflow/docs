page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.non_max_suppression_overlaps

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



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/image_ops_impl.py).

Greedily selects a subset of bounding boxes in descending order of score.

Prunes away boxes that have high overlap with previously selected boxes.
N-by-n overlap values are supplied as square matrix.
The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes.  The bounding
box coordinates corresponding to the selected indices can then be obtained
using the `tf.gather operation`.  For example:
  selected_indices = tf.image.non_max_suppression_overlaps(
      overlaps, scores, max_output_size, iou_threshold)
  selected_boxes = tf.gather(boxes, selected_indices)

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