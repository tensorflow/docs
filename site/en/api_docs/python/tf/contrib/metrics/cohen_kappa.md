page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.cohen_kappa

``` python
tf.contrib.metrics.cohen_kappa(
    labels,
    predictions_idx,
    num_classes,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



Defined in [`tensorflow/contrib/metrics/python/ops/metric_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/metrics/python/ops/metric_ops.py).

Calculates Cohen's kappa.

[Cohen's kappa](https://en.wikipedia.org/wiki/Cohen's_kappa) is a statistic
that measures inter-annotator agreement.

The `cohen_kappa` function calculates the confusion matrix, and creates three
local variables to compute the Cohen's kappa: `po`, `pe_row`, and `pe_col`,
which refer to the diagonal part, rows and columns totals of the confusion
matrix, respectively. This value is ultimately returned as `kappa`, an
idempotent operation that is calculated by

    pe = (pe_row * pe_col) / N
    k = (sum(po) - sum(pe)) / (N - sum(pe))

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`kappa`. `update_op` weights each prediction by the corresponding value in
`weights`.

Class labels are expected to start at 0. E.g., if `num_classes`
was three, then the possible labels would be [0, 1, 2].

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

NOTE: Equivalent to `sklearn.metrics.cohen_kappa_score`, but the method
doesn't support weighted matrix yet.

#### Args:

* <b>`labels`</b>: 1-D `Tensor` of real labels for the classification task. Must be
    one of the following types: int16, int32, int64.
* <b>`predictions_idx`</b>: 1-D `Tensor` of predicted class indices for a given
    classification. Must have the same type as `labels`.
* <b>`num_classes`</b>: The possible number of labels.
* <b>`weights`</b>: Optional `Tensor` whose shape matches `predictions`.
* <b>`metrics_collections`</b>: An optional list of collections that `kappa` should
    be added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
    be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:

* <b>`kappa`</b>: Scalar float `Tensor` representing the current Cohen's kappa.
* <b>`update_op`</b>: `Operation` that increments `po`, `pe_row` and `pe_col`
    variables appropriately and whose value matches `kappa`.


#### Raises:

* <b>`ValueError`</b>: If `num_classes` is less than 2, or `predictions` and `labels`
    have mismatched shapes, or if `weights` is not `None` and its shape
    doesn't match `predictions`, or if either `metrics_collections` or
    `updates_collections` are not a list or tuple.
* <b>`RuntimeError`</b>: If eager execution is enabled.