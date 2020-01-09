page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.Sum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/Sum">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L376-L413">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Sum`

Computes the (weighted) sum of the given values.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/Sum"><code>tf.compat.v1.keras.metrics.Sum</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/Sum"><code>tf.compat.v2.keras.metrics.Sum</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/Sum"><code>tf.compat.v2.metrics.Sum</code></a>


<!-- Placeholder for "Used in" -->

For example, if values is [1, 3, 5, 7] then the sum is 16.
If the weights were specified as [1, 1, 0, 0] then the sum would be 4.

This metric creates one variable, `total`, that is used to compute the sum of
`values`. This is ultimately returned as `sum`.

If `sample_weight` is `None`, weights default to 1.  Use `sample_weight` of 0
to mask values.

#### Usage:



```python
m = tf.keras.metrics.Sum()
m.update_state([1, 3, 5, 7])
print('Final result: ', m.result().numpy())  # Final result: 16.0
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.add_metric(tf.keras.metrics.Sum(name='sum_1')(outputs))
model.compile('sgd', loss='mse')
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L405-L413">View source</a>

``` python
__init__(
    name='sum',
    dtype=None
)
```

Creates a `Sum` instance.


#### Args:


* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L300-L360">View source</a>

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
