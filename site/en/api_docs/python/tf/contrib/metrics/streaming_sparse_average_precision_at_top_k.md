

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.metrics.streaming_sparse_average_precision_at_top_k

### `tf.contrib.metrics.streaming_sparse_average_precision_at_top_k`

``` python
streaming_sparse_average_precision_at_top_k(
    top_k_predictions,
    labels,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



Defined in [`tensorflow/contrib/metrics/python/ops/metric_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/metrics/python/ops/metric_ops.py).

Computes average precision@k of predictions with respect to sparse labels.

`streaming_sparse_average_precision_at_top_k` creates two local variables,
`average_precision_at_<k>/total` and `average_precision_at_<k>/max`, that
are used to compute the frequency. This frequency is ultimately returned as
`average_precision_at_<k>`: an idempotent operation that simply divides
`average_precision_at_<k>/total` by `average_precision_at_<k>/max`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`precision_at_<k>`. Set operations applied to `top_k` and `labels` calculate
the true positives and false positives weighted by `weights`. Then `update_op`
increments `true_positive_at_<k>` and `false_positive_at_<k>` using these
values.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:

* <b>`top_k_predictions`</b>: Integer `Tensor` with shape [D1, ... DN, k] where N >= 1.
    Commonly, N=1 and `predictions_idx` has shape [batch size, k]. The final
    dimension must be set and contains the top `k` predicted class indices.
    [D1, ... DN] must match `labels`. Values should be in range
    [0, num_classes).
* <b>`labels`</b>: `int64` `Tensor` or `SparseTensor` with shape
    [D1, ... DN, num_labels] or [D1, ... DN], where the latter implies
    num_labels=1. N >= 1 and num_labels is the number of target classes for
    the associated prediction. Commonly, N=1 and `labels` has shape
    [batch_size, num_labels]. [D1, ... DN] must match `top_k_predictions`.
    Values should be in range [0, num_classes).
* <b>`weights`</b>: `Tensor` whose rank is either 0, or n-1, where n is the rank of
    `labels`. If the latter, it must be broadcastable to `labels` (i.e., all
    dimensions must be either `1`, or the same as the corresponding `labels`
    dimension).
* <b>`metrics_collections`</b>: An optional list of collections that values should
    be added to.
* <b>`updates_collections`</b>: An optional list of collections that updates should
    be added to.
* <b>`name`</b>: Name of new update operation, and namespace for other dependent ops.


#### Returns:

* <b>`mean_average_precision`</b>: Scalar `float64` `Tensor` with the mean average
    precision values.
* <b>`update`</b>: `Operation` that increments  variables appropriately, and whose
    value matches `metric`.


#### Raises:

* <b>`ValueError`</b>: if the last dimension of top_k_predictions is not set.