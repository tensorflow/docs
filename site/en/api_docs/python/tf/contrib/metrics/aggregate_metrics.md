page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.aggregate_metrics

Aggregates the metric value tensors and update ops into two lists.

``` python
tf.contrib.metrics.aggregate_metrics(*value_update_tuples)
```



Defined in [`contrib/metrics/python/ops/metric_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/metrics/python/ops/metric_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`*value_update_tuples`</b>: a variable number of tuples, each of which contain the
  pair of (value_tensor, update_op) from a streaming metric.


#### Returns:

A list of value `Tensor` objects and a list of update ops.



#### Raises:


* <b>`ValueError`</b>: if `value_update_tuples` is empty.