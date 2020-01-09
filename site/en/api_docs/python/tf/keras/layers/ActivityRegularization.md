page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ActivityRegularization


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/ActivityRegularization">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/core.py#L1085-L1114">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ActivityRegularization`

Layer that applies an update to the cost function based input activity.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/ActivityRegularization"><code>tf.compat.v1.keras.layers.ActivityRegularization</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/ActivityRegularization"><code>tf.compat.v2.keras.layers.ActivityRegularization</code></a>


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`l1`</b>: L1 regularization factor (positive float).
* <b>`l2`</b>: L2 regularization factor (positive float).


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/core.py#L1101-L1106">View source</a>

``` python
__init__(
    l1=0.0,
    l2=0.0,
    **kwargs
)
```
