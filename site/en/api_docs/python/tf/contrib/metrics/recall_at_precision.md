page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.recall_at_precision


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/metrics/python/ops/metric_ops.py#L2560-L2645">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes `recall` at `precision`.

``` python
tf.contrib.metrics.recall_at_precision(
    labels,
    predictions,
    precision,
    weights=None,
    num_thresholds=200,
    metrics_collections=None,
    updates_collections=None,
    name=None,
    strict_mode=False
)
```



<!-- Placeholder for "Used in" -->

The `recall_at_precision` function creates four local variables,
`tp` (true positives), `fp` (false positives) and `fn` (false negatives)
that are used to compute the `recall` at the given `precision` value. The
threshold for the given `precision` value is computed and used to evaluate the
corresponding `recall`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`recall`. `update_op` increments the `tp`, `fp` and `fn` counts with the
weight of each case found in the `predictions` and `labels`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`labels`</b>: The ground truth values, a `Tensor` whose dimensions must match
  `predictions`. Will be cast to `bool`.
* <b>`predictions`</b>: A floating point `Tensor` of arbitrary shape and whose values
  are in the range `[0, 1]`.
* <b>`precision`</b>: A scalar value in range `[0, 1]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `labels` dimension).
* <b>`num_thresholds`</b>: The number of thresholds to use for matching the given
  `precision`.
* <b>`metrics_collections`</b>: An optional list of collections that `recall` should be
  added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
  be added to.
* <b>`name`</b>: An optional variable_scope name.
* <b>`strict_mode`</b>: If true and there exists a threshold where the precision is
  above the target precision, return the corresponding recall at the
  threshold. Otherwise, return 0. If false, find the threshold where the
  precision is closest to the target precision and return the recall at the
  threshold.


#### Returns:


* <b>`recall`</b>: A scalar `Tensor` representing the recall at the given
  `precision` value.
* <b>`update_op`</b>: An operation that increments the `tp`, `fp` and `fn`
  variables appropriately and whose value matches `recall`.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  `precision` is not between 0 and 1, or if either `metrics_collections`
  or `updates_collections` are not a list or tuple.
