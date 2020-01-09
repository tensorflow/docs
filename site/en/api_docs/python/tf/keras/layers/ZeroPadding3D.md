page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ZeroPadding3D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/ZeroPadding3D">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/convolutional.py#L2216-L2330">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ZeroPadding3D`

Zero-padding layer for 3D data (spatial or spatio-temporal).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/ZeroPadding3D"><code>tf.compat.v1.keras.layers.ZeroPadding3D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/ZeroPadding3D"><code>tf.compat.v2.keras.layers.ZeroPadding3D</code></a>


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`padding`</b>: Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints.
  - If int: the same symmetric padding
    is applied to height and width.
  - If tuple of 3 ints:
    interpreted as two different
    symmetric padding values for height and width:
    `(symmetric_dim1_pad, symmetric_dim2_pad, symmetric_dim3_pad)`.
  - If tuple of 3 tuples of 2 ints:
    interpreted as
    `((left_dim1_pad, right_dim1_pad), (left_dim2_pad,
      right_dim2_pad), (left_dim3_pad, right_dim3_pad))`
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

5D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch, first_axis_to_pad, second_axis_to_pad, third_axis_to_pad,
      depth)`
- If `data_format` is `"channels_first"`:
    `(batch, depth, first_axis_to_pad, second_axis_to_pad,
      third_axis_to_pad)`



#### Output shape:

5D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch, first_padded_axis, second_padded_axis, third_axis_to_pad,
      depth)`
- If `data_format` is `"channels_first"`:
    `(batch, depth, first_padded_axis, second_padded_axis,
      third_axis_to_pad)`


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/convolutional.py#L2261-L2288">View source</a>

``` python
__init__(
    padding=(1, 1, 1),
    data_format=None,
    **kwargs
)
```
