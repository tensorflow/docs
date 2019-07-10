page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.GlobalMaxPool3D

## Class `GlobalMaxPool3D`

Global Max pooling operation for 3D data.



### Aliases:

* Class `tf.compat.v1.keras.layers.GlobalMaxPool3D`
* Class `tf.compat.v1.keras.layers.GlobalMaxPooling3D`
* Class `tf.compat.v2.keras.layers.GlobalMaxPool3D`
* Class `tf.compat.v2.keras.layers.GlobalMaxPooling3D`
* Class `tf.keras.layers.GlobalMaxPool3D`
* Class `tf.keras.layers.GlobalMaxPooling3D`



Defined in [`python/keras/layers/pooling.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/pooling.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`data_format`</b>: A string,
  one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
  while `channels_first` corresponds to inputs with shape
  `(batch, channels, spatial_dim1, spatial_dim2, spatial_dim3)`.
  It defaults to the `image_data_format` value found in your
  Keras config file at `~/.keras/keras.json`.
  If you never set it, then it will be "channels_last".


#### Input shape:

- If `data_format='channels_last'`:
  5D tensor with shape:
  `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
- If `data_format='channels_first'`:
  5D tensor with shape:
  `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`



#### Output shape:

2D tensor with shape `(batch_size, channels)`.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    data_format=None,
    **kwargs
)
```






