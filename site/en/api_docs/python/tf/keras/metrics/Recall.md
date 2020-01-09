page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.Recall


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/Recall">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1232-L1354">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Recall`

Computes the recall of the predictions with respect to the labels.

Inherits From: [`Metric`](../../../tf/keras/metrics/Metric)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/Recall"><code>tf.compat.v1.keras.metrics.Recall</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/Recall"><code>tf.compat.v2.keras.metrics.Recall</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/Recall"><code>tf.compat.v2.metrics.Recall</code></a>


<!-- Placeholder for "Used in" -->

For example, if `y_true` is [0, 1, 1, 1] and `y_pred` is [1, 0, 1, 1]
then the recall value is 2/(2+1) ie. 0.66. If the weights were specified as
[0, 0, 1, 0] then the recall value would be 1.

This metric creates two local variables, `true_positives` and
`false_negatives`, that are used to compute the recall. This value is
ultimately returned as `recall`, an idempotent operation that simply divides
`true_positives` by the sum of `true_positives` and `false_negatives`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

If `top_k` is set, recall will be computed as how often on average a class
among the labels of a batch entry is in the top-k predictions.

If `class_id` is specified, we calculate recall by considering only the
entries in the batch for which `class_id` is in the label, and computing the
fraction of them for which `class_id` is above the threshold and/or in the
top-k predictions.

#### Usage:



```python
m = tf.keras.metrics.Recall()
m.update_state([0, 1, 1, 1], [1, 0, 1, 1])
print('Final result: ', m.result().numpy())  # Final result: 0.66
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', loss='mse', metrics=[tf.keras.metrics.Recall()])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1271-L1309">View source</a>

``` python
__init__(
    thresholds=None,
    top_k=None,
    class_id=None,
    name=None,
    dtype=None
)
```

Creates a `Recall` instance.


#### Args:


* <b>`thresholds`</b>: (Optional) A float value or a python list/tuple of float
  threshold values in [0, 1]. A threshold is compared with prediction
  values to determine the truth value of predictions (i.e., above the
  threshold is `true`, below is `false`). One metric value is generated
  for each threshold value. If neither thresholds nor top_k are set, the
  default is to calculate recall with `thresholds=0.5`.
* <b>`top_k`</b>: (Optional) Unset by default. An int value specifying the top-k
  predictions to consider when calculating recall.
* <b>`class_id`</b>: (Optional) Integer class ID for which we want binary metrics.
  This must be in the half-open interval `[0, num_classes)`, where
  `num_classes` is the last dimension of predictions.
* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L145-L161">View source</a>

``` python
__new__(
    cls,
    *args,
    **kwargs
)
```

Create and return a new object.  See help(type) for accurate signature.




## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1342-L1345">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1337-L1340">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1311-L1335">View source</a>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates true positive and false negative statistics.


#### Args:


* <b>`y_true`</b>: The ground truth values, with the same dimensions as `y_pred`.
  Will be cast to `bool`.
* <b>`y_pred`</b>: The predicted values. Each element must be in the range `[0, 1]`.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be a
  `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
  be broadcastable to `y_true`.


#### Returns:

Update op.
