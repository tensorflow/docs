page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.AlphaDropout

## Class `AlphaDropout`

Applies Alpha Dropout to the input.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.AlphaDropout`
* Class `tf.compat.v2.keras.layers.AlphaDropout`
* Class `tf.keras.layers.AlphaDropout`



Defined in [`python/keras/layers/noise.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/noise.py).

<!-- Placeholder for "Used in" -->

Alpha Dropout is a `Dropout` that keeps mean and variance of inputs
to their original values, in order to ensure the self-normalizing property
even after this dropout.
Alpha Dropout fits well to Scaled Exponential Linear Units
by randomly setting activations to the negative saturation value.

#### Arguments:


* <b>`rate`</b>: float, drop probability (as with `Dropout`).
  The multiplicative noise will have
  standard deviation `sqrt(rate / (1 - rate))`.
* <b>`seed`</b>: A Python integer to use as random seed.


#### Call arguments:


* <b>`inputs`</b>: Input tensor (of any rank).
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding dropout) or in inference mode (doing nothing).


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    rate,
    noise_shape=None,
    seed=None,
    **kwargs
)
```






