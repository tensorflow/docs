page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.metrics.mean_cosine_distance


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/metrics_impl.py#L914-L985">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the cosine distance between the labels and predictions.

``` python
tf.compat.v1.metrics.mean_cosine_distance(
    labels,
    predictions,
    dim,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The `mean_cosine_distance` function creates two local variables,
`total` and `count` that are used to compute the average cosine distance
between `predictions` and `labels`. This average is weighted by `weights`,
and it is ultimately returned as `mean_distance`, which is an idempotent
operation that simply divides `total` by `count`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`mean_distance`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`labels`</b>: A `Tensor` of arbitrary shape.
* <b>`predictions`</b>: A `Tensor` of the same shape as `labels`.
* <b>`dim`</b>: The dimension along which the cosine distance is computed.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `labels` dimension). Also,
  dimension `dim` must be `1`.
* <b>`metrics_collections`</b>: An optional list of collections that the metric
  value variable should be added to.
* <b>`updates_collections`</b>: An optional list of collections that the metric update
  ops should be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`mean_distance`</b>: A `Tensor` representing the current mean, the value of
  `total` divided by `count`.
* <b>`update_op`</b>: An operation that increments the `total` and `count` variables
  appropriately.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  either `metrics_collections` or `updates_collections` are not a list or
  tuple.
* <b>`RuntimeError`</b>: If eager execution is enabled.
