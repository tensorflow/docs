page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.LeakyReLU

## Class `LeakyReLU`

Leaky version of a Rectified Linear Unit.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.LeakyReLU`
* Class `tf.compat.v2.keras.layers.LeakyReLU`
* Class `tf.keras.layers.LeakyReLU`



Defined in [`python/keras/layers/advanced_activations.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/advanced_activations.py).

<!-- Placeholder for "Used in" -->

It allows a small gradient when the unit is not active:
`f(x) = alpha * x for x < 0`,
`f(x) = x for x >= 0`.

#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as the input.



#### Arguments:


* <b>`alpha`</b>: Float >= 0. Negative slope coefficient.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    alpha=0.3,
    **kwargs
)
```






