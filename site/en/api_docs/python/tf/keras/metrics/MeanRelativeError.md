page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.MeanRelativeError


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/MeanRelativeError">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L459-L539">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MeanRelativeError`

Computes the mean relative error by normalizing with the given values.

Inherits From: [`Mean`](../../../tf/keras/metrics/Mean)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/MeanRelativeError"><code>tf.compat.v1.keras.metrics.MeanRelativeError</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/MeanRelativeError"><code>tf.compat.v2.keras.metrics.MeanRelativeError</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/MeanRelativeError"><code>tf.compat.v2.metrics.MeanRelativeError</code></a>


<!-- Placeholder for "Used in" -->

This metric creates two local variables, `total` and `count` that are used to
compute the mean relative absolute error. This average is weighted by
`sample_weight`, and it is ultimately returned as `mean_relative_error`:
an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

#### Usage:



```python
m = tf.keras.metrics.MeanRelativeError(normalizer=[1, 3, 2, 3])
m.update_state([1, 3, 2, 3], [2, 4, 6, 8])

# metric = mean(|y_pred - y_true| / normalizer)
#        = mean([1, 1, 4, 5] / [1, 3, 2, 3]) = mean([1, 1/3, 2, 5/3])
#        = 5/4 = 1.25
print('Final result: ', m.result().numpy())  # Final result: 1.25
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
  'sgd',
  loss='mse',
  metrics=[tf.keras.metrics.MeanRelativeError(normalizer=[1, 3])])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L493-L503">View source</a>

``` python
__init__(
    normalizer,
    name=None,
    dtype=None
)
```

Creates a `MeanRelativeError` instance.


#### Args:


* <b>`normalizer`</b>: The normalizer values with same shape as predictions.
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L204-L210">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L362-L372">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L505-L533">View source</a>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates metric statistics.


#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be a
  `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
  be broadcastable to `y_true`.


#### Returns:

Update op.
