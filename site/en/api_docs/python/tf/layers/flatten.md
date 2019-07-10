page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.flatten

``` python
tf.layers.flatten(
    inputs,
    name=None,
    data_format='channels_last'
)
```



Defined in [`tensorflow/python/layers/core.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/layers/core.py).

Flattens an input tensor while preserving the batch axis (axis 0). (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use keras.layers.flatten instead.

#### Arguments:

* <b>`inputs`</b>: Tensor input.
* <b>`name`</b>: The name of the layer (string).
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
    The ordering of the dimensions in the inputs.
    `channels_last` corresponds to inputs with shape
    `(batch, height, width, channels)` while `channels_first` corresponds to
    inputs with shape `(batch, channels, height, width)`.


#### Returns:

  Reshaped tensor.

Examples:

```
  x = tf.placeholder(shape=(None, 4, 4), dtype='float32')
  y = flatten(x)
  # now `y` has shape `(None, 16)`

  x = tf.placeholder(shape=(None, 3, None), dtype='float32')
  y = flatten(x)
  # now `y` has shape `(None, None)`
```