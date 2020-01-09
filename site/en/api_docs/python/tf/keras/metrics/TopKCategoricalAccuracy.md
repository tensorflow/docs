page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.TopKCategoricalAccuracy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/TopKCategoricalAccuracy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L769-L798">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TopKCategoricalAccuracy`

Computes how often targets are in the top `K` predictions.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/TopKCategoricalAccuracy"><code>tf.compat.v1.keras.metrics.TopKCategoricalAccuracy</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/TopKCategoricalAccuracy"><code>tf.compat.v2.keras.metrics.TopKCategoricalAccuracy</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/TopKCategoricalAccuracy"><code>tf.compat.v2.metrics.TopKCategoricalAccuracy</code></a>


<!-- Placeholder for "Used in" -->


#### Usage:



```python
m = tf.keras.metrics.TopKCategoricalAccuracy()
m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]])
print('Final result: ', m.result().numpy())  # Final result: 1.0
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', metrics=[tf.keras.metrics.TopKCategoricalAccuracy()])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L788-L798">View source</a>

``` python
__init__(
    k=5,
    name='top_k_categorical_accuracy',
    dtype=None
)
```

Creates a `TopKCategoricalAccuracy` instance.


#### Args:


* <b>`k`</b>: (Optional) Number of top elements to look at for computing accuracy.
  Defaults to 5.
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L559-L584">View source</a>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates metric statistics.

`y_true` and `y_pred` should have the same shape.

#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be
  a `Tensor` whose rank is either 0, or the same rank as `y_true`,
  and must be broadcastable to `y_true`.


#### Returns:

Update op.
