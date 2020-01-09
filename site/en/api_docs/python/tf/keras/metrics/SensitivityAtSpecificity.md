page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.SensitivityAtSpecificity


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L1426-L1503">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SensitivityAtSpecificity`

Computes the sensitivity at a given specificity.



### Aliases:

* Class `tf.compat.v1.keras.metrics.SensitivityAtSpecificity`
* Class `tf.compat.v2.keras.metrics.SensitivityAtSpecificity`
* Class `tf.compat.v2.metrics.SensitivityAtSpecificity`
* Class `tf.metrics.SensitivityAtSpecificity`


<!-- Placeholder for "Used in" -->

`Sensitivity` measures the proportion of actual positives that are correctly
identified as such (tp / (tp + fn)).
`Specificity` measures the proportion of actual negatives that are correctly
identified as such (tn / (tn + fp)).

This metric creates four local variables, `true_positives`, `true_negatives`,
`false_positives` and `false_negatives` that are used to compute the
sensitivity at the given specificity. The threshold for the given specificity
value is computed and used to evaluate the corresponding sensitivity.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

For additional information about specificity and sensitivity, see the
following: https://en.wikipedia.org/wiki/Sensitivity_and_specificity

#### Usage:



```python
m = tf.keras.metrics.SensitivityAtSpecificity(0.4, num_thresholds=1)
m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9])
print('Final result: ', m.result().numpy())  # Final result: 0.5
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
    'sgd',
    loss='mse',
    metrics=[tf.keras.metrics.SensitivityAtSpecificity()])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L1464-L1479">View source</a>

``` python
__init__(
    specificity,
    num_thresholds=200,
    name=None,
    dtype=None
)
```

Creates a `SensitivityAtSpecificity` instance.


#### Args:


* <b>`specificity`</b>: A scalar value in range `[0, 1]`.
* <b>`num_thresholds`</b>: (Optional) Defaults to 200. The number of thresholds to
  use for matching the given specificity.
* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L144-L160">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L1419-L1422">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L1481-L1495">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L1394-L1417">View source</a>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates confusion matrix statistics.


#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be a
  `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
  be broadcastable to `y_true`.


#### Returns:

Update op.
