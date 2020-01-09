page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ThresholdedReLU


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/ThresholdedReLU">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/advanced_activations.py#L200-L235">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ThresholdedReLU`

Thresholded Rectified Linear Unit.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/ThresholdedReLU"><code>tf.compat.v1.keras.layers.ThresholdedReLU</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/ThresholdedReLU"><code>tf.compat.v2.keras.layers.ThresholdedReLU</code></a>


<!-- Placeholder for "Used in" -->


#### It follows:


`f(x) = x for x > theta`,
`f(x) = 0 otherwise`.

#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as the input.



#### Arguments:


* <b>`theta`</b>: Float >= 0. Threshold location of activation.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/advanced_activations.py#L219-L222">View source</a>

``` python
__init__(
    theta=1.0,
    **kwargs
)
```
