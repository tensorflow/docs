page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.UpSampling2D

## Class `UpSampling2D`

Upsampling layer for 2D inputs.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.UpSampling2D`
* Class `tf.compat.v2.keras.layers.UpSampling2D`
* Class `tf.keras.layers.UpSampling2D`



Defined in [`python/keras/layers/convolutional.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/convolutional.py).

<!-- Placeholder for "Used in" -->

Repeats the rows and columns of the data
by `size[0]` and `size[1]` respectively.

#### Arguments:


* <b>`size`</b>: Int, or tuple of 2 integers.
  The upsampling factors for rows and columns.
* <b>`data_format`</b>: A string,
  one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, height, width, channels)` while `channels_first`
  corresponds to inputs with shape
  `(batch, channels, height, width)`.
  It defaults to the `image_data_format` value found in your
  Keras config file at `~/.keras/keras.json`.
  If you never set it, then it will be "channels_last".
* <b>`interpolation`</b>: A string, one of `nearest` or `bilinear`.


#### Input shape:

4D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch, rows, cols, channels)`
- If `data_format` is `"channels_first"`:
    `(batch, channels, rows, cols)`



#### Output shape:

4D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch, upsampled_rows, upsampled_cols, channels)`
- If `data_format` is `"channels_first"`:
    `(batch, channels, upsampled_rows, upsampled_cols)`


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    size=(2, 2),
    data_format=None,
    interpolation='nearest',
    **kwargs
)
```






