page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.KLDivergence

## Class `KLDivergence`

Computes Kullback-Leibler divergence metric between `y_true` and `y_pred`.



### Aliases:

* Class `tf.compat.v1.keras.metrics.KLDivergence`
* Class `tf.compat.v2.keras.metrics.KLDivergence`
* Class `tf.compat.v2.metrics.KLDivergence`
* Class `tf.keras.metrics.KLDivergence`



Defined in [`python/keras/metrics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/metrics.py).

<!-- Placeholder for "Used in" -->

`metric = y_true * log(y_true / y_pred)`

#### Usage:



```python
m = tf.keras.metrics.KLDivergence()
m.update_state([.4, .9, .2], [.5, .8, .12])
print('Final result: ', m.result().numpy())  # Final result: -0.043
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', metrics=[tf.keras.metrics.KLDivergence()])
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name='kullback_leibler_divergence',
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




