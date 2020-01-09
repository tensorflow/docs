page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ReLU


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/ReLU">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/advanced_activations.py#L273-L332">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ReLU`

Rectified Linear Unit activation function.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/ReLU"><code>tf.compat.v1.keras.layers.ReLU</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/ReLU"><code>tf.compat.v2.keras.layers.ReLU</code></a>


<!-- Placeholder for "Used in" -->

With default values, it returns element-wise `max(x, 0)`.

Otherwise, it follows:
`f(x) = max_value` for `x >= max_value`,
`f(x) = x` for `threshold <= x < max_value`,
`f(x) = negative_slope * (x - threshold)` otherwise.

#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as the input.



#### Arguments:


* <b>`max_value`</b>: Float >= 0. Maximum activation value.
* <b>`negative_slope`</b>: Float >= 0. Negative slope coefficient.
* <b>`threshold`</b>: Float. Threshold value for thresholded activation.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/advanced_activations.py#L297-L311">View source</a>

``` python
__init__(
    max_value=None,
    negative_slope=0,
    threshold=0,
    **kwargs
)
```
