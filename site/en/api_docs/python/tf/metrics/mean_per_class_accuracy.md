page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.metrics.mean_per_class_accuracy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/metrics_impl.py#L988-L1090">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Calculates the mean of the per-class accuracies.

### Aliases:

* <a href="/api_docs/python/tf/metrics/mean_per_class_accuracy"><code>tf.compat.v1.metrics.mean_per_class_accuracy</code></a>


``` python
tf.metrics.mean_per_class_accuracy(
    labels,
    predictions,
    num_classes,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Calculates the accuracy for each class, then takes the mean of that.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates the accuracy of each class and returns
them.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`labels`</b>: A `Tensor` of ground truth labels with shape [batch size] and of
  type `int32` or `int64`. The tensor will be flattened if its rank > 1.
* <b>`predictions`</b>: A `Tensor` of prediction results for semantic labels, whose
  shape is [batch size] and type `int32` or `int64`. The tensor will be
  flattened if its rank > 1.
* <b>`num_classes`</b>: The possible number of labels the prediction task can
  have. This value must be provided, since two variables with shape =
  [num_classes] will be allocated.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `labels` dimension).
* <b>`metrics_collections`</b>: An optional list of collections that
  `mean_per_class_accuracy'
  should be added to.
* <b>`updates_collections`</b>: An optional list of collections `update_op` should be
  added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`mean_accuracy`</b>: A `Tensor` representing the mean per class accuracy.
* <b>`update_op`</b>: An operation that updates the accuracy tensor.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  either `metrics_collections` or `updates_collections` are not a list or
  tuple.
* <b>`RuntimeError`</b>: If eager execution is enabled.
