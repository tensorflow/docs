page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.Mean


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L416-L454">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Mean`

Computes the (weighted) mean of the given values.



### Aliases:

* Class `tf.compat.v1.keras.metrics.Mean`
* Class `tf.compat.v2.keras.metrics.Mean`
* Class `tf.compat.v2.metrics.Mean`
* Class `tf.metrics.Mean`


### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)

### Used in the tutorials:

* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)
* [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)
* [TensorFlow 2.0 quickstart for experts](https://www.tensorflow.org/tutorials/quickstart/advanced)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



For example, if values is [1, 3, 5, 7] then the mean is 4.
If the weights were specified as [1, 1, 0, 0] then the mean would be 2.

This metric creates two variables, `total` and `count` that are used to
compute the average of `values`. This average is ultimately returned as `mean`
which is an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

#### Usage:



```python
m = tf.keras.metrics.Mean()
m.update_state([1, 3, 5, 7])
print('Final result: ', m.result().numpy())  # Final result: 4.0
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.add_metric(tf.keras.metrics.Mean(name='mean_1')(outputs))
model.compile('sgd', loss='mse')
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L446-L454">View source</a>

``` python
__init__(
    name='mean',
    dtype=None
)
```

Creates a `Mean` instance.


#### Args:


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/metrics.py#L299-L359">View source</a>

``` python
update_state(
    values,
    sample_weight=None
)
```

Accumulates statistics for computing the reduction metric.

For example, if `values` is [1, 3, 5, 7] and reduction=SUM_OVER_BATCH_SIZE,
then the value of `result()` is 4. If the `sample_weight` is specified as
[1, 1, 0, 0] then value of `result()` would be 2.

#### Args:


* <b>`values`</b>: Per-example value.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1.


#### Returns:

Update op.
