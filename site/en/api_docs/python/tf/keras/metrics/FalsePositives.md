page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.FalsePositives

## Class `FalsePositives`

Calculates the number of false positives.



### Aliases:

* Class `tf.compat.v1.keras.metrics.FalsePositives`
* Class `tf.compat.v2.keras.metrics.FalsePositives`
* Class `tf.compat.v2.metrics.FalsePositives`
* Class `tf.keras.metrics.FalsePositives`



Defined in [`python/keras/metrics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/metrics.py).

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



## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

``` python
reset_states()
```




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

Accumulates the given confusion matrix condition statistics.


#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be a
  `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
  be broadcastable to `y_true`.


#### Returns:

Update op.




