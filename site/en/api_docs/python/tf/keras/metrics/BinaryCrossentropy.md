page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.BinaryCrossentropy

## Class `BinaryCrossentropy`

Computes the crossentropy metric between the labels and predictions.



### Aliases:

* Class `tf.compat.v1.keras.metrics.BinaryCrossentropy`
* Class `tf.compat.v2.keras.metrics.BinaryCrossentropy`
* Class `tf.compat.v2.metrics.BinaryCrossentropy`
* Class `tf.keras.metrics.BinaryCrossentropy`



Defined in [`python/keras/metrics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/metrics.py).

<!-- Placeholder for "Used in" -->

This is the crossentropy metric class to be used when there are only two
label classes (0 and 1).

#### Usage:



```python
m = tf.keras.metrics.BinaryCrossentropy()
m.update_state([1., 0., 1., 0.], [1., 1., 1., 0.])

# EPSILON = 1e-7, y = y_true, y` = y_pred, Y_MAX = 0.9999999
# y` = clip_ops.clip_by_value(output, EPSILON, 1. - EPSILON)
# y` = [Y_MAX, Y_MAX, Y_MAX, EPSILON]

# Metric = -(y log(y` + EPSILON) + (1 - y) log(1 - y` + EPSILON))
#        = [-log(Y_MAX + EPSILON), -log(1 - Y_MAX + EPSILON),
#           -log(Y_MAX + EPSILON), -log(1)]
#        = [(0 + 15.33) / 2, (0 + 0) / 2]
# Reduced metric = 7.665 / 2

print('Final result: ', m.result().numpy())  # Final result: 3.833
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
    'sgd',
    loss='mse',
    metrics=[tf.keras.metrics.BinaryCrossentropy()])
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name='binary_crossentropy',
    dtype=None,
    from_logits=False,
    label_smoothing=0
)
```

Creates a `BinaryCrossentropy` instance.


#### Args:


* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.
* <b>`from_logits`</b>: (Optional )Whether output is expected to be a logits tensor.
  By default, we consider that output encodes a probability distribution.
* <b>`label_smoothing`</b>: (Optional) Float in [0, 1]. When > 0, label values are
  smoothed, meaning the confidence on label values are relaxed.
  e.g. `label_smoothing=0.2` means that we will use a value of `0.1` for
  label `0` and `0.9` for label `1`"



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




