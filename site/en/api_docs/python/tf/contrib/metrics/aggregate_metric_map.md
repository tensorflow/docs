page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.aggregate_metric_map


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/metrics/python/ops/metric_ops.py#L3691-L3720">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Aggregates the metric names to tuple dictionary.

``` python
tf.contrib.metrics.aggregate_metric_map(names_to_tuples)
```



<!-- Placeholder for "Used in" -->

This function is useful for pairing metric names with their associated value
and update ops when the list of metrics is long. For example:

```python
  metrics_to_values, metrics_to_updates = slim.metrics.aggregate_metric_map({
      'Mean Absolute Error': new_slim.metrics.streaming_mean_absolute_error(
          predictions, labels, weights),
      'Mean Relative Error': new_slim.metrics.streaming_mean_relative_error(
          predictions, labels, labels, weights),
      'RMSE Linear': new_slim.metrics.streaming_root_mean_squared_error(
          predictions, labels, weights),
      'RMSE Log': new_slim.metrics.streaming_root_mean_squared_error(
          predictions, labels, weights),
  })
```

#### Args:


* <b>`names_to_tuples`</b>: a map of metric names to tuples, each of which contain the
  pair of (value_tensor, update_op) from a streaming metric.


#### Returns:

A dictionary from metric names to value ops and a dictionary from metric
names to update ops.
