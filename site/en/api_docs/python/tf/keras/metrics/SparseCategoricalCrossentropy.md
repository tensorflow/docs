page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.SparseCategoricalCrossentropy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L2620-L2687">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SparseCategoricalCrossentropy`

Computes the crossentropy metric between the labels and predictions.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy"><code>tf.compat.v1.keras.metrics.SparseCategoricalCrossentropy</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy"><code>tf.compat.v2.keras.metrics.SparseCategoricalCrossentropy</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy"><code>tf.compat.v2.metrics.SparseCategoricalCrossentropy</code></a>


<!-- Placeholder for "Used in" -->

Use this crossentropy metric when there are two or more label classes.
We expect labels to be provided as integers. If you want to provide labels
using `one-hot` representation, please use `CategoricalCrossentropy` metric.
There should be `# classes` floating point values per feature for `y_pred`
and a single floating point value per feature for `y_true`.

In the snippet below, there is a single floating point value per example for
`y_true` and `# classes` floating pointing values per example for `y_pred`.
The shape of `y_true` is `[batch_size]` and the shape of `y_pred` is
`[batch_size, num_classes]`.

#### Usage:



```python
m = tf.keras.metrics.SparseCategoricalCrossentropy()
m.update_state(
  [1, 2],
  [[0.05, 0.95, 0], [0.1, 0.8, 0.1]])

# y_true = one_hot(y_true) = [[0, 1, 0], [0, 0, 1]]
# logits = log(y_pred)
# softmax = exp(logits) / sum(exp(logits), axis=-1)
# softmax = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]]

# xent = -sum(y * log(softmax), 1)
# log(softmax) = [[-2.9957, -0.0513, -16.1181], [-2.3026, -0.2231, -2.3026]]
# y_true * log(softmax) = [[0, -0.0513, 0], [0, 0, -2.3026]]

# xent = [0.0513, 2.3026]
# Reduced xent = (0.0513 + 2.3026) / 2

print('Final result: ', m.result().numpy())  # Final result: 1.176
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
  'sgd',
  loss='mse',
  metrics=[tf.keras.metrics.SparseCategoricalCrossentropy()])
```

#### Args:


* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.
* <b>`from_logits`</b>: (Optional ) Whether `y_pred` is expected to be a logits tensor.
  By default, we assume that `y_pred` encodes a probability distribution.
* <b>`axis`</b>: (Optional) Defaults to -1. The dimension along which the metric is
  computed.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L2676-L2687">View source</a>

``` python
__init__(
    name='sparse_categorical_crossentropy',
    dtype=None,
    from_logits=False,
    axis=-1
)
```

Creates a `MeanMetricWrapper` instance.


#### Args:


* <b>`fn`</b>: The metric function to wrap, with signature
  `fn(y_true, y_pred, **kwargs)`.
* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.
* <b>`**kwargs`</b>: The keyword arguments that are passed on to `fn`.

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
