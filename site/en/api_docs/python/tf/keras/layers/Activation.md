page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Activation


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/Activation">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/core.py#L342-L372">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Activation`

Applies an activation function to an output.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/Activation"><code>tf.compat.v1.keras.layers.Activation</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/Activation"><code>tf.compat.v2.keras.layers.Activation</code></a>


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`activation`</b>: Activation function, such as <a href="../../../tf/nn/relu"><code>tf.nn.relu</code></a>, or string name of
  built-in activation function, such as "relu".


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/core.py#L358-L361">View source</a>

``` python
__init__(
    activation,
    **kwargs
)
```
