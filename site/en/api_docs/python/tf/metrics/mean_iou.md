page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.metrics.mean_iou

``` python
tf.metrics.mean_iou(
    labels,
    predictions,
    num_classes,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/metrics_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/metrics_impl.py).

Calculate per-step mean Intersection-Over-Union (mIOU).

Mean Intersection-Over-Union is a common evaluation metric for
semantic image segmentation, which first computes the IOU for each
semantic class and then computes the average over classes.
IOU is defined as follows:
  IOU = true_positive / (true_positive + false_positive + false_negative).
The predictions are accumulated in a confusion matrix, weighted by `weights`,
and mIOU is then calculated from it.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the `mean_iou`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:

* <b>`labels`</b>: A `Tensor` of ground truth labels with shape [batch size] and of
    type `int32` or `int64`. The tensor will be flattened if its rank > 1.
* <b>`predictions`</b>: A `Tensor` of prediction results for semantic labels, whose
    shape is [batch size] and type `int32` or `int64`. The tensor will be
    flattened if its rank > 1.
* <b>`num_classes`</b>: The possible number of labels the prediction task can
    have. This value must be provided, since a confusion matrix of
    dimension = [num_classes, num_classes] will be allocated.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `labels` dimension).
* <b>`metrics_collections`</b>: An optional list of collections that `mean_iou`
    should be added to.
* <b>`updates_collections`</b>: An optional list of collections `update_op` should be
    added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:

* <b>`mean_iou`</b>: A `Tensor` representing the mean intersection-over-union.
* <b>`update_op`</b>: An operation that increments the confusion matrix.


#### Raises:

* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
    `weights` is not `None` and its shape doesn't match `predictions`, or if
    either `metrics_collections` or `updates_collections` are not a list or
    tuple.
* <b>`RuntimeError`</b>: If eager execution is enabled.