

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.streaming_dynamic_auc

``` python
tf.contrib.metrics.streaming_dynamic_auc(
    labels,
    predictions,
    curve='ROC',
    metrics_collections=(),
    updates_collections=(),
    name=None,
    weights=None
)
```



Defined in [`tensorflow/contrib/metrics/python/ops/metric_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/metrics/python/ops/metric_ops.py).

Computes the apporixmate AUC by a Riemann sum with data-derived thresholds.

USAGE NOTE: this approach requires storing all of the predictions and labels
for a single evaluation in memory, so it may not be usable when the evaluation
batch size and/or the number of evaluation steps is very large.

Computes the area under the ROC or PR curve using each prediction as a
threshold. This has the advantage of being resilient to the distribution of
predictions by aggregating across batches, accumulating labels and predictions
and performing the final calculation using all of the concatenated values.

#### Args:

* <b>`labels`</b>: A `Tensor` of ground truth labels with the same shape as `labels`
    and with values of 0 or 1 whose values are castable to `int64`.
* <b>`predictions`</b>: A `Tensor` of predictions whose values are castable to
    `float64`. Will be flattened into a 1-D `Tensor`.
* <b>`curve`</b>: The name of the curve for which to compute AUC, 'ROC' for the
    Receiving Operating Characteristic or 'PR' for the Precision-Recall curve.
* <b>`metrics_collections`</b>: An optional iterable of collections that `auc` should
    be added to.
* <b>`updates_collections`</b>: An optional iterable of collections that `update_op`
    should be added to.
* <b>`name`</b>: An optional name for the variable_scope that contains the metric
    variables.
* <b>`weights`</b>: A 'Tensor' of non-negative weights whose values are castable to
    `float64`. Will be flattened into a 1-D `Tensor`.


#### Returns:

* <b>`auc`</b>: A scalar `Tensor` containing the current area-under-curve value.
* <b>`update_op`</b>: An operation that concatenates the input labels and predictions
    to the accumulated values.


#### Raises:

* <b>`ValueError`</b>: If `labels` and `predictions` have mismatched shapes or if
    `curve` isn't a recognized curve type.