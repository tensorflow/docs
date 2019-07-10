page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.SparseCategoricalAccuracy

## Class `SparseCategoricalAccuracy`

Calculates how often predictions matches integer labels.



### Aliases:

* Class `tf.compat.v1.keras.metrics.SparseCategoricalAccuracy`
* Class `tf.compat.v2.keras.metrics.SparseCategoricalAccuracy`
* Class `tf.compat.v2.metrics.SparseCategoricalAccuracy`
* Class `tf.keras.metrics.SparseCategoricalAccuracy`



Defined in [`python/keras/metrics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/metrics.py).

<!-- Placeholder for "Used in" -->

For example, if `y_true` is [[2], [1]] and `y_pred` is
[[0.1, 0.9, 0.8], [0.05, 0.95, 0]] then the categorical accuracy is 1/2 or .5.
If the weights were specified as [0.7, 0.3] then the categorical accuracy
would be .3. You can provide logits of classes as `y_pred`, since argmax of
logits and probabilities are same.

This metric creates two local variables, `total` and `count` that are used to
compute the frequency with which `y_pred` matches `y_true`. This frequency is
ultimately returned as `sparse categorical accuracy`: an idempotent operation
that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

#### Usage:



```python
m = tf.keras.metrics.SparseCategoricalAccuracy()
m.update_state([[2], [1]], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]])
print('Final result: ', m.result().numpy())  # Final result: 0.5
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
    'sgd',
    loss='mse',
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name='sparse_categorical_accuracy',
    dtype=None
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




