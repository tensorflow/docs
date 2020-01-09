page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.streaming_percentage_less


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/metrics/python/ops/metric_ops.py#L3433-L3480">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the percentage of values less than the given threshold.

``` python
tf.contrib.metrics.streaming_percentage_less(
    values,
    threshold,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The `streaming_percentage_less` function creates two local variables,
`total` and `count` that are used to compute the percentage of `values` that
fall below `threshold`. This rate is weighted by `weights`, and it is
ultimately returned as `percentage` which is an idempotent operation that
simply divides `total` by `count`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`percentage`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`values`</b>: A numeric `Tensor` of arbitrary size.
* <b>`threshold`</b>: A scalar threshold.
* <b>`weights`</b>: An optional `Tensor` whose shape is broadcastable to `values`.
* <b>`metrics_collections`</b>: An optional list of collections that the metric value
  variable should be added to.
* <b>`updates_collections`</b>: An optional list of collections that the metric update
  ops should be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`percentage`</b>: A `Tensor` representing the current mean, the value of `total`
  divided by `count`.
* <b>`update_op`</b>: An operation that increments the `total` and `count` variables
  appropriately.


#### Raises:


* <b>`ValueError`</b>: If `weights` is not `None` and its shape doesn't match `values`,
  or if either `metrics_collections` or `updates_collections` are not a list
  or tuple.
