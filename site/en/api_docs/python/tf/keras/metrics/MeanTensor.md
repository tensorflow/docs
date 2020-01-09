page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.MeanTensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/MeanTensor">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L2383-L2490">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MeanTensor`

Computes the element-wise (weighted) mean of the given tensors.

Inherits From: [`Metric`](../../../tf/keras/metrics/Metric)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/MeanTensor"><code>tf.compat.v1.keras.metrics.MeanTensor</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/MeanTensor"><code>tf.compat.v2.keras.metrics.MeanTensor</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/MeanTensor"><code>tf.compat.v2.metrics.MeanTensor</code></a>


<!-- Placeholder for "Used in" -->

`MeanTensor` returns a tensor with the same shape of the input tensors. The
mean value is updated by keeping local variables `total` and `count`. The
`total` tracks the sum of the weighted values, and `count` stores the sum of
the weighted counts.

#### Usage:



```python
m = tf.keras.metrics.MeanTensor()
m.update_state([0, 1, 2, 3])
m.update_state([4, 5, 6, 7])
print('Result: ', m.result().numpy())  # Result: [2, 3, 4, 5]
m.update_state([12, 10, 8, 6], sample_weights= [0, 0.2, 0.5, 1])
print('Result: ', m.result().numpy())  # Result: [2, 3.636, 4.8, 5.333]
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L2403-L2414">View source</a>

``` python
__init__(
    name='mean_tensor',
    dtype=None
)
```

Creates a `MeanTensor` instance.


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




## Properties

<h3 id="count"><code>count</code></h3>




<h3 id="total"><code>total</code></h3>






## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L2487-L2490">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L2479-L2485">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L2436-L2477">View source</a>

``` python
update_state(
    values,
    sample_weight=None
)
```

Accumulates statistics for computing the element-wise mean.


#### Args:


* <b>`values`</b>: Per-example value.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1.


#### Returns:

Update op.
