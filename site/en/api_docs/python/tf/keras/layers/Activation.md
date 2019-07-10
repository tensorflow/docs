page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Activation

## Class `Activation`

Applies an activation function to an output.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Activation`
* Class `tf.compat.v2.keras.layers.Activation`
* Class `tf.keras.layers.Activation`



Defined in [`python/keras/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/core.py).

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

``` python
__init__(
    activation,
    **kwargs
)
```






