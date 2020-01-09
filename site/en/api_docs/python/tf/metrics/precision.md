page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.metrics.precision


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/metrics_impl.py#L1947-L2039">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the precision of the predictions with respect to the labels.

### Aliases:

* <a href="/api_docs/python/tf/metrics/precision"><code>tf.compat.v1.metrics.precision</code></a>


``` python
tf.metrics.precision(
    labels,
    predictions,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The `precision` function creates two local variables,
`true_positives` and `false_positives`, that are used to compute the
precision. This value is ultimately returned as `precision`, an idempotent
operation that simply divides `true_positives` by the sum of `true_positives`
and `false_positives`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`precision`. `update_op` weights each prediction by the corresponding value in
`weights`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`labels`</b>: The ground truth values, a `Tensor` whose dimensions must match
  `predictions`. Will be cast to `bool`.
* <b>`predictions`</b>: The predicted values, a `Tensor` of arbitrary dimensions. Will
  be cast to `bool`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `labels` dimension).
* <b>`metrics_collections`</b>: An optional list of collections that `precision` should
  be added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
  be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`precision`</b>: Scalar float `Tensor` with the value of `true_positives`
  divided by the sum of `true_positives` and `false_positives`.
* <b>`update_op`</b>: `Operation` that increments `true_positives` and
  `false_positives` variables appropriately and whose value matches
  `precision`.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  either `metrics_collections` or `updates_collections` are not a list or
  tuple.
* <b>`RuntimeError`</b>: If eager execution is enabled.
