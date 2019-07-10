page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.streaming_curve_points

Computes curve (ROC or PR) values for a prespecified number of points.

``` python
tf.contrib.metrics.streaming_curve_points(
    labels=None,
    predictions=None,
    weights=None,
    num_thresholds=200,
    metrics_collections=None,
    updates_collections=None,
    curve='ROC',
    name=None
)
```



Defined in [`contrib/metrics/python/ops/metric_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/metrics/python/ops/metric_ops.py).

<!-- Placeholder for "Used in" -->

The `streaming_curve_points` function creates four local variables,
`true_positives`, `true_negatives`, `false_positives` and `false_negatives`
that are used to compute the curve values. To discretize the curve, a linearly
spaced set of thresholds is used to compute pairs of recall and precision
values.

For best results, `predictions` should be distributed approximately uniformly
in the range [0, 1] and not peaked around 0 or 1.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`labels`</b>: A `Tensor` whose shape matches `predictions`. Will be cast to
  `bool`.
* <b>`predictions`</b>: A floating point `Tensor` of arbitrary shape and whose values
  are in the range `[0, 1]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `labels` dimension).
* <b>`num_thresholds`</b>: The number of thresholds to use when discretizing the roc
  curve.
* <b>`metrics_collections`</b>: An optional list of collections that `auc` should be
  added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
  be added to.
* <b>`curve`</b>: Specifies the name of the curve to be computed, 'ROC' [default] or
  'PR' for the Precision-Recall-curve.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`points`</b>: A `Tensor` with shape [num_thresholds, 2] that contains points of
  the curve.
* <b>`update_op`</b>: An operation that increments the `true_positives`,
  `true_negatives`, `false_positives` and `false_negatives` variables.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  either `metrics_collections` or `updates_collections` are not a list or
  tuple.

TODO(chizeng): Consider rewriting this method to make use of logic within the
precision_recall_at_equal_thresholds method (to improve run time).