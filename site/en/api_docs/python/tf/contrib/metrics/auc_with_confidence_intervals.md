page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.auc_with_confidence_intervals

``` python
tf.contrib.metrics.auc_with_confidence_intervals(
    labels,
    predictions,
    weights=None,
    alpha=0.95,
    logit_transformation=True,
    metrics_collections=(),
    updates_collections=(),
    name=None
)
```



Defined in [`tensorflow/contrib/metrics/python/ops/metric_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/metrics/python/ops/metric_ops.py).

Computes the AUC and asymptotic normally distributed confidence interval.

USAGE NOTE: this approach requires storing all of the predictions and labels
for a single evaluation in memory, so it may not be usable when the evaluation
batch size and/or the number of evaluation steps is very large.

Computes the area under the ROC curve and its confidence interval using
placement values. This has the advantage of being resilient to the
distribution of predictions by aggregating across batches, accumulating labels
and predictions and performing the final calculation using all of the
concatenated values.

#### Args:

* <b>`labels`</b>: A `Tensor` of ground truth labels with the same shape as `labels`
    and with values of 0 or 1 whose values are castable to `int64`.
* <b>`predictions`</b>: A `Tensor` of predictions whose values are castable to
    `float64`. Will be flattened into a 1-D `Tensor`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `labels`.
* <b>`alpha`</b>: Confidence interval level desired.
* <b>`logit_transformation`</b>: A boolean value indicating whether the estimate should
    be logit transformed prior to calculating the confidence interval. Doing
    so enforces the restriction that the AUC should never be outside the
    interval [0,1].
* <b>`metrics_collections`</b>: An optional iterable of collections that `auc` should
    be added to.
* <b>`updates_collections`</b>: An optional iterable of collections that `update_op`
    should be added to.
* <b>`name`</b>: An optional name for the variable_scope that contains the metric
    variables.


#### Returns:

* <b>`auc`</b>: A 1-D `Tensor` containing the current area-under-curve, lower, and
    upper confidence interval values.
* <b>`update_op`</b>: An operation that concatenates the input labels and predictions
    to the accumulated values.


#### Raises:

* <b>`ValueError`</b>: If `labels`, `predictions`, and `weights` have mismatched shapes
  or if `alpha` isn't in the range (0,1).