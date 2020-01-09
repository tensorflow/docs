page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.non_max_suppression_padded


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/non_max_suppression_padded">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L2742-L2803">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Greedily selects a subset of bounding boxes in descending order of score.

### Aliases:

* <a href="/api_docs/python/tf/image/non_max_suppression_padded"><code>tf.compat.v1.image.non_max_suppression_padded</code></a>
* <a href="/api_docs/python/tf/image/non_max_suppression_padded"><code>tf.compat.v2.image.non_max_suppression_padded</code></a>


``` python
tf.image.non_max_suppression_padded(
    boxes,
    scores,
    max_output_size,
    iou_threshold=0.5,
    score_threshold=float('-inf'),
    pad_to_max_output_size=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Performs algorithmically equivalent operation to tf.image.non_max_suppression,
with the addition of an optional parameter which zero-pads the output to
be of size `max_output_size`.
The output of this operation is a tuple containing the set of integers
indexing into the input collection of bounding boxes representing the selected
boxes and the number of valid indices in the index set.  The bounding box
coordinates corresponding to the selected indices can then be obtained using
the <a href="../../tf/slice"><code>tf.slice</code></a> and <a href="../../tf/gather"><code>tf.gather</code></a> operations.  For example:

>     selected_indices_padded, num_valid = tf.image.non_max_suppression_padded(
>         boxes, scores, max_output_size, iou_threshold,
>         score_threshold, pad_to_max_output_size=True)
>     selected_indices = tf.slice(
>         selected_indices_padded, tf.constant([0]), num_valid)
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
* <b>`pad_to_max_output_size`</b>: bool.  If True, size of `selected_indices` output is
  padded to `max_output_size`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:


* <b>`selected_indices`</b>: A 1-D integer `Tensor` of shape `[M]` representing the
  selected indices from the boxes tensor, where `M <= max_output_size`.
* <b>`valid_outputs`</b>: A scalar integer `Tensor` denoting how many elements in
`selected_indices` are valid.  Valid elements occur first, then padding.
