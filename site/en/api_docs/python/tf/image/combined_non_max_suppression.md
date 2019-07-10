page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.combined_non_max_suppression

Greedily selects a subset of bounding boxes in descending order of score.

### Aliases:

* `tf.compat.v1.image.combined_non_max_suppression`
* `tf.compat.v2.image.combined_non_max_suppression`
* `tf.image.combined_non_max_suppression`

``` python
tf.image.combined_non_max_suppression(
    boxes,
    scores,
    max_output_size_per_class,
    max_total_size,
    iou_threshold=0.5,
    score_threshold=float('-inf'),
    pad_per_class=False,
    clip_boxes=True,
    name=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

This operation performs non_max_suppression on the inputs per batch, across
all classes.
Prunes away boxes that have high intersection-over-union (IOU) overlap
with previously selected boxes.  Bounding boxes are supplied as
[y1, x1, y2, x2], where (y1, x1) and (y2, x2) are the coordinates of any
diagonal pair of box corners and the coordinates can be provided as normalized
(i.e., lying in the interval [0, 1]) or absolute.  Note that this algorithm
is agnostic to where the origin is in the coordinate system. Also note that
this algorithm is invariant to orthogonal transformations and translations
of the coordinate system; thus translating or reflections of the coordinate
system result in the same boxes being selected by the algorithm.
The output of this operation is the final boxes, scores and classes tensor
returned after performing non_max_suppression.

#### Args:


* <b>`boxes`</b>: A 4-D float `Tensor` of shape `[batch_size, num_boxes, q, 4]`. If `q`
  is 1 then same boxes are used for all classes otherwise, if `q` is equal
  to number of classes, class-specific boxes are used.
* <b>`scores`</b>: A 3-D float `Tensor` of shape `[batch_size, num_boxes, num_classes]`
  representing a single score corresponding to each box (each row of boxes).
* <b>`max_output_size_per_class`</b>: A scalar integer `Tensor` representing the
  maximum number of boxes to be selected by non max suppression per class
* <b>`max_total_size`</b>: A scalar representing maximum number of boxes retained over
  all classes.
* <b>`iou_threshold`</b>: A float representing the threshold for deciding whether boxes
  overlap too much with respect to IOU.
* <b>`score_threshold`</b>: A float representing the threshold for deciding when to
  remove boxes based on score.
* <b>`pad_per_class`</b>: If false, the output nmsed boxes, scores and classes are
  padded/clipped to `max_total_size`. If true, the output nmsed boxes,
  scores and classes are padded to be of length
  `max_size_per_class`*`num_classes`, unless it exceeds `max_total_size` in
  which case it is clipped to `max_total_size`. Defaults to false.
* <b>`clip_boxes`</b>: If true, the coordinates of output nmsed boxes will be clipped
  to [0, 1]. If false, output the box coordinates as it is. Defaults to
  true.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

'nmsed_boxes': A [batch_size, max_detections, 4] float32 tensor
  containing the non-max suppressed boxes.
'nmsed_scores': A [batch_size, max_detections] float32 tensor containing
  the scores for the boxes.
'nmsed_classes': A [batch_size, max_detections] float32 tensor
  containing the class for boxes.
'valid_detections': A [batch_size] int32 tensor indicating the number of
  valid detections per batch item. Only the top valid_detections[i] entries
  in nms_boxes[i], nms_scores[i] and nms_class[i] are valid. The rest of the
  entries are zero paddings.
