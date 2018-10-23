

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.metrics.true_positives_at_thresholds

``` python
true_positives_at_thresholds(
    labels,
    predictions,
    thresholds,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/metrics_impl.py).

Computes true positives at provided threshold values.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:

* <b>`labels`</b>: A `Tensor` whose shape matches `predictions`. Will be cast to
    `bool`.
* <b>`predictions`</b>: A floating point `Tensor` of arbitrary shape and whose values
    are in the range `[0, 1]`.
* <b>`thresholds`</b>: A python list or tuple of float thresholds in `[0, 1]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `labels` dimension).
* <b>`metrics_collections`</b>: An optional list of collections that `true_positives`
    should be added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
    be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:

* <b>`true_positives`</b>:  A float `Tensor` of shape `[len(thresholds)]`.
* <b>`update_op`</b>: An operation that updates the `true_positives` variable and
    returns its current value.


#### Raises:

* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
    `weights` is not `None` and its shape doesn't match `predictions`, or if
    either `metrics_collections` or `updates_collections` are not a list or
    tuple.