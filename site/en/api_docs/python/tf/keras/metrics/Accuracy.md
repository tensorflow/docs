page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.Accuracy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L594-L626">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Accuracy`

Calculates how often predictions matches labels.



### Aliases:

* Class `tf.compat.v1.keras.metrics.Accuracy`
* Class `tf.compat.v2.keras.metrics.Accuracy`
* Class `tf.compat.v2.metrics.Accuracy`
* Class `tf.metrics.Accuracy`


### Used in the guide:

* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)

### Used in the tutorials:

* [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data)
* [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)



For example, if `y_true` is [1, 2, 3, 4] and `y_pred` is [0, 2, 3, 4]
then the accuracy is 3/4 or .75.  If the weights were specified as
[1, 1, 0, 0] then the accuracy would be 1/2 or .5.

This metric creates two local variables, `total` and `count` that are used to
compute the frequency with which `y_pred` matches `y_true`. This frequency is
ultimately returned as `binary accuracy`: an idempotent operation that simply
divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

#### Usage:



```python
m = tf.keras.metrics.Accuracy()
m.update_state([1, 2, 3, 4], [0, 2, 3, 4])
print('Final result: ', m.result().numpy())  # Final result: 0.75
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', loss='mse', metrics=[tf.keras.metrics.Accuracy()])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L625-L626">View source</a>

``` python
__init__(
    name='accuracy',
    dtype=None
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
