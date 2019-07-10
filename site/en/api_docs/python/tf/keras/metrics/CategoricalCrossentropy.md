page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.CategoricalCrossentropy

## Class `CategoricalCrossentropy`

Computes the crossentropy metric between the labels and predictions.



### Aliases:

* Class `tf.compat.v1.keras.metrics.CategoricalCrossentropy`
* Class `tf.compat.v2.keras.metrics.CategoricalCrossentropy`
* Class `tf.compat.v2.metrics.CategoricalCrossentropy`
* Class `tf.keras.metrics.CategoricalCrossentropy`



Defined in [`python/keras/metrics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/metrics.py).

<!-- Placeholder for "Used in" -->

This is the crossentropy metric class to be used when there are multiple
label classes (2 or more). Here we assume that labels are given as a `one_hot`
representation. eg., When labels values are [2, 0, 1],
 `y_true` = [[0, 0, 1], [1, 0, 0], [0, 1, 0]].

#### Usage:



```python
m = tf.keras.metrics.CategoricalCrossentropy()
m.update_state([[0, 1, 0], [0, 0, 1]],
               [[0.05, 0.95, 0], [0.1, 0.8, 0.1]])

# EPSILON = 1e-7, y = y_true, y` = y_pred
# y` = clip_ops.clip_by_value(output, EPSILON, 1. - EPSILON)
# y` = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]]

# xent = -sum(y * log(y'), axis = -1)
#      = -((log 0.95), (log 0.1))
#      = [0.051, 2.302]
# Reduced xent = (0.051 + 2.302) / 2

print('Final result: ', m.result().numpy())  # Final result: 1.176
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
  'sgd',
  loss='mse',
  metrics=[tf.keras.metrics.CategoricalCrossentropy()])
```

#### Args:


* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.
* <b>`from_logits`</b>: (Optional ) Whether `y_pred` is expected to be a logits tensor.
  By default, we assume that `y_pred` encodes a probability distribution.
* <b>`label_smoothing`</b>: Float in [0, 1]. When > 0, label values are smoothed,
  meaning the confidence on label values are relaxed. e.g.
  `label_smoothing=0.2` means that we will use a value of `0.1` for label
  `0` and `0.9` for label `1`"

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name='categorical_crossentropy',
    dtype=None,
    from_logits=False,
    label_smoothing=0
)
```






## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

``` python
result()
```




<h3 id="update_state"><code>update_state</code></h3>

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




