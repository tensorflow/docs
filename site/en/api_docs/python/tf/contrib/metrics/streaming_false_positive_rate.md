

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.streaming_false_positive_rate

``` python
tf.contrib.metrics.streaming_false_positive_rate(
    predictions,
    labels,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



Defined in [`tensorflow/contrib/metrics/python/ops/metric_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/metrics/python/ops/metric_ops.py).

Computes the false positive rate of predictions with respect to labels.

The `false_positive_rate` function creates two local variables,
`false_positives` and `true_negatives`, that are used to compute the
false positive rate. This value is ultimately returned as
`false_positive_rate`, an idempotent operation that simply divides
`false_positives` by the sum of `false_positives` and `true_negatives`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`false_positive_rate`. `update_op` weights each prediction by the
corresponding value in `weights`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:

* <b>`predictions`</b>: The predicted values, a `Tensor` of arbitrary dimensions. Will
    be cast to `bool`.
* <b>`labels`</b>: The ground truth values, a `Tensor` whose dimensions must match
    `predictions`. Will be cast to `bool`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `labels` dimension).
* <b>`metrics_collections`</b>: An optional list of collections that
   `false_positive_rate` should be added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
    be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:

* <b>`false_positive_rate`</b>: Scalar float `Tensor` with the value of
    `false_positives` divided by the sum of `false_positives` and
    `true_negatives`.
* <b>`update_op`</b>: `Operation` that increments `false_positives` and
    `true_negatives` variables appropriately and whose value matches
    `false_positive_rate`.


#### Raises:

* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
    `weights` is not `None` and its shape doesn't match `predictions`, or if
    either `metrics_collections` or `updates_collections` are not a list or
    tuple.