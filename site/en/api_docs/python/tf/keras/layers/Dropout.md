page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Dropout

## Class `Dropout`

Applies Dropout to the input.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Dropout`
* Class `tf.compat.v2.keras.layers.Dropout`
* Class `tf.keras.layers.Dropout`



Defined in [`python/keras/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/core.py).

<!-- Placeholder for "Used in" -->

Dropout consists in randomly setting
a fraction `rate` of input units to 0 at each update during training time,
which helps prevent overfitting.

#### Arguments:


* <b>`rate`</b>: Float between 0 and 1. Fraction of the input units to drop.
* <b>`noise_shape`</b>: 1D integer tensor representing the shape of the
  binary dropout mask that will be multiplied with the input.
  For instance, if your inputs have shape
  `(batch_size, timesteps, features)` and
  you want the dropout mask to be the same for all timesteps,
  you can use `noise_shape=(batch_size, 1, features)`.
* <b>`seed`</b>: A Python integer to use as random seed.


#### Call arguments:


* <b>`inputs`</b>: Input tensor (of any rank).
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding dropout) or in inference mode (doing nothing).

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    rate,
    noise_shape=None,
    seed=None,
    **kwargs
)
```






