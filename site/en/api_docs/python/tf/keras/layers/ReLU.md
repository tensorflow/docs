page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ReLU

## Class `ReLU`

Rectified Linear Unit activation function.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.ReLU`
* Class `tf.compat.v2.keras.layers.ReLU`
* Class `tf.keras.layers.ReLU`



Defined in [`python/keras/layers/advanced_activations.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/advanced_activations.py).

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

``` python
__init__(
    max_value=None,
    negative_slope=0,
    threshold=0,
    **kwargs
)
```






