page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.precision_at_recall

``` python
tf.contrib.metrics.precision_at_recall(
    labels,
    predictions,
    target_recall,
    weights=None,
    num_thresholds=200,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



Defined in [`tensorflow/contrib/metrics/python/ops/metric_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/metrics/python/ops/metric_ops.py).

Computes the precision at a given recall.

This function creates variables to track the true positives, false positives,
true negatives, and false negatives at a set of thresholds. Among those
thresholds where recall is at least `target_recall`, precision is computed
at the threshold where recall is closest to `target_recall`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
precision at `target_recall`. `update_op` increments the counts of true
positives, false positives, true negatives, and false negatives with the
weight of each case found in the `predictions` and `labels`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

For additional information about precision and recall, see
http://en.wikipedia.org/wiki/Precision_and_recall

#### Args:

* <b>`labels`</b>: The ground truth values, a `Tensor` whose dimensions must match
    `predictions`. Will be cast to `bool`.
* <b>`predictions`</b>: A floating point `Tensor` of arbitrary shape and whose values
    are in the range `[0, 1]`.
* <b>`target_recall`</b>: A scalar value in range `[0, 1]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `labels` dimension).
* <b>`num_thresholds`</b>: The number of thresholds to use for matching the given
    recall.
* <b>`metrics_collections`</b>: An optional list of collections to which `precision`
    should be added.
* <b>`updates_collections`</b>: An optional list of collections to which `update_op`
    should be added.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:

* <b>`precision`</b>: A scalar `Tensor` representing the precision at the given
    `target_recall` value.
* <b>`update_op`</b>: An operation that increments the variables for tracking the
    true positives, false positives, true negatives, and false negatives and
    whose value matches `precision`.


#### Raises:

* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, if
    `weights` is not `None` and its shape doesn't match `predictions`, or if
    `target_recall` is not between 0 and 1, or if either `metrics_collections`
    or `updates_collections` are not a list or tuple.
* <b>`RuntimeError`</b>: If eager execution is enabled.