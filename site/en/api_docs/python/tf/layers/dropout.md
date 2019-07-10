page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.dropout

Applies Dropout to the input. (deprecated)

### Aliases:

* `tf.compat.v1.layers.dropout`
* `tf.layers.dropout`

``` python
tf.layers.dropout(
    inputs,
    rate=0.5,
    noise_shape=None,
    seed=None,
    training=False,
    name=None
)
```



Defined in [`python/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/layers/core.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use keras.layers.dropout instead.

Dropout consists in randomly setting a fraction `rate` of input units to 0
at each update during training time, which helps prevent overfitting.
The units that are kept are scaled by `1 / (1 - rate)`, so that their
sum is unchanged at training time and inference time.

#### Arguments:


* <b>`inputs`</b>: Tensor input.
* <b>`rate`</b>: The dropout rate, between 0 and 1. E.g. "rate=0.1" would drop out
  10% of input units.
* <b>`noise_shape`</b>: 1D tensor of type `int32` representing the shape of the
  binary dropout mask that will be multiplied with the input.
  For instance, if your inputs have shape
  `(batch_size, timesteps, features)`, and you want the dropout mask
  to be the same for all timesteps, you can use
  `noise_shape=[batch_size, 1, features]`.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`training`</b>: Either a Python boolean, or a TensorFlow boolean scalar tensor
  (e.g. a placeholder). Whether to return the output in training mode
  (apply dropout) or in inference mode (return the input untouched).
* <b>`name`</b>: The name of the layer (string).


#### Returns:

Output tensor.



#### Raises:


* <b>`ValueError`</b>: if eager execution is enabled.