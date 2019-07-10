page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.GaussianNoise

## Class `GaussianNoise`

Apply additive zero-centered Gaussian noise.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.GaussianNoise`
* Class `tf.compat.v2.keras.layers.GaussianNoise`
* Class `tf.keras.layers.GaussianNoise`



Defined in [`python/keras/layers/noise.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/noise.py).

<!-- Placeholder for "Used in" -->

This is useful to mitigate overfitting
(you could see it as a form of random data augmentation).
Gaussian Noise (GS) is a natural choice as corruption process
for real valued inputs.

As it is a regularization layer, it is only active at training time.

#### Arguments:


* <b>`stddev`</b>: Float, standard deviation of the noise distribution.


#### Call arguments:


* <b>`inputs`</b>: Input tensor (of any rank).
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding noise) or in inference mode (doing nothing).


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    stddev,
    **kwargs
)
```






