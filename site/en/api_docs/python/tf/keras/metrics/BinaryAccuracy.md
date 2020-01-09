page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.BinaryAccuracy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L630-L671">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `BinaryAccuracy`

Calculates how often predictions matches labels.



### Aliases:

* Class `tf.compat.v1.keras.metrics.BinaryAccuracy`
* Class `tf.compat.v2.keras.metrics.BinaryAccuracy`
* Class `tf.compat.v2.metrics.BinaryAccuracy`
* Class `tf.metrics.BinaryAccuracy`


<!-- Placeholder for "Used in" -->

For example, if `y_true` is [1, 1, 0, 0] and `y_pred` is [0.98, 1, 0, 0.6]
then the binary accuracy is 3/4 or .75.  If the weights were specified as
[1, 0, 0, 1] then the binary accuracy would be 1/2 or .5.

This metric creates two local variables, `total` and `count` that are used to
compute the frequency with which `y_pred` matches `y_true`. This frequency is
ultimately returned as `binary accuracy`: an idempotent operation that simply
divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

#### Usage:



```python
m = tf.keras.metrics.BinaryAccuracy()
m.update_state([1, 1, 0, 0], [0.98, 1, 0, 0.6])
print('Final result: ', m.result().numpy())  # Final result: 0.75
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', loss='mse', metrics=[tf.keras.metrics.BinaryAccuracy()])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L661-L671">View source</a>

``` python
__init__(
    name='binary_accuracy',
    dtype=None,
    threshold=0.5
)
```

Creates a `BinaryAccuracy` instance.


#### Args:


* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.
* <b>`threshold`</b>: (Optional) Float representing the threshold for deciding
whether prediction values are 1 or 0.

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L203-L209">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L361-L371">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L558-L583">View source</a>

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
