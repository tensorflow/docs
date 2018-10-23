

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.metrics.recall

``` python
recall(
    labels,
    predictions,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/metrics_impl.py).

Computes the recall of the predictions with respect to the labels.

The `recall` function creates two local variables, `true_positives`
and `false_negatives`, that are used to compute the recall. This value is
ultimately returned as `recall`, an idempotent operation that simply divides
`true_positives` by the sum of `true_positives`  and `false_negatives`.

For estimation of the metric  over a stream of data, the function creates an
`update_op` that updates these variables and returns the `recall`. `update_op`
weights each prediction by the corresponding value in `weights`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:

* <b>`labels`</b>: The ground truth values, a `Tensor` whose dimensions must match
    `predictions`. Will be cast to `bool`.
* <b>`predictions`</b>: The predicted values, a `Tensor` of arbitrary dimensions. Will
    be cast to `bool`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
    be either `1`, or the same as the corresponding `labels` dimension).
* <b>`metrics_collections`</b>: An optional list of collections that `recall` should
    be added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
    be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:

* <b>`recall`</b>: Scalar float `Tensor` with the value of `true_positives` divided
    by the sum of `true_positives` and `false_negatives`.
* <b>`update_op`</b>: `Operation` that increments `true_positives` and
    `false_negatives` variables appropriately and whose value matches
    `recall`.


#### Raises:

* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
    `weights` is not `None` and its shape doesn't match `predictions`, or if
    either `metrics_collections` or `updates_collections` are not a list or
    tuple.