page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.FalsePositives


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/FalsePositives">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L905-L951">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `FalsePositives`

Calculates the number of false positives.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/FalsePositives"><code>tf.compat.v1.keras.metrics.FalsePositives</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/FalsePositives"><code>tf.compat.v2.keras.metrics.FalsePositives</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/FalsePositives"><code>tf.compat.v2.metrics.FalsePositives</code></a>


<!-- Placeholder for "Used in" -->

For example, if `y_true` is [0, 1, 0, 0] and `y_pred` is [0, 0, 1, 1]
then the false positives value is 2.  If the weights were specified as
[0, 0, 1, 0] then the false positives value would be 1.

If `sample_weight` is given, calculates the sum of the weights of
false positives. This metric creates one local variable, `accumulator`
that is used to keep track of the number of false positives.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

#### Usage:



```python
m = tf.keras.metrics.FalsePositives()
m.update_state([0, 1, 0, 0], [0, 0, 1, 1])
print('Final result: ', m.result().numpy())  # Final result: 2
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', loss='mse', metrics=[tf.keras.metrics.FalsePositives()])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L935-L951">View source</a>

``` python
__init__(
    thresholds=None,
    name=None,
    dtype=None
)
```

Creates a `FalsePositives` instance.


#### Args:


* <b>`thresholds`</b>: (Optional) Defaults to 0.5. A float value or a python
  list/tuple of float threshold values in [0, 1]. A threshold is compared
  with prediction values to determine the truth value of predictions
  (i.e., above the threshold is `true`, below is `false`). One metric
  value is generated for each threshold value.
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L893-L896">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L886-L891">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L866-L884">View source</a>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates the given confusion matrix condition statistics.


#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be a
  `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
  be broadcastable to `y_true`.


#### Returns:

Update op.
