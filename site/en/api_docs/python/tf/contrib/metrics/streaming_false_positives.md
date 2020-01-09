page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.streaming_false_positives


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/metrics/python/ops/metric_ops.py#L138-L180">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sum the weights of false positives. (deprecated)

``` python
tf.contrib.metrics.streaming_false_positives(
    predictions,
    labels,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.metrics.false_positives. Note that the order of the labels and predictions arguments has been switched.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`predictions`</b>: The predicted values, a `Tensor` of arbitrary dimensions. Will
  be cast to `bool`.
* <b>`labels`</b>: The ground truth values, a `Tensor` whose dimensions must match
  `predictions`. Will be cast to `bool`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `labels` dimension).
* <b>`metrics_collections`</b>: An optional list of collections that the metric value
  variable should be added to.
* <b>`updates_collections`</b>: An optional list of collections that the metric update
  ops should be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`value_tensor`</b>: A `Tensor` representing the current value of the metric.
* <b>`update_op`</b>: An operation that accumulates the error from a batch of data.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  either `metrics_collections` or `updates_collections` are not a list or
  tuple.
