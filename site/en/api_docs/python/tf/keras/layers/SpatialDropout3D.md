page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.SpatialDropout3D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L284-L338">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SpatialDropout3D`

Spatial 3D version of Dropout.

Inherits From: [`Dropout`](../../../tf/keras/layers/Dropout)

### Aliases:

* Class `tf.compat.v1.keras.layers.SpatialDropout3D`
* Class `tf.compat.v2.keras.layers.SpatialDropout3D`


<!-- Placeholder for "Used in" -->

This version performs the same function as Dropout, however it drops
entire 3D feature maps instead of individual elements. If adjacent voxels
within feature maps are strongly correlated (as is normally the case in
early convolution layers) then regular dropout will not regularize the
activations and will otherwise just result in an effective learning rate
decrease. In this case, SpatialDropout3D will help promote independence
between feature maps and should be used instead.

#### Arguments:


* <b>`rate`</b>: Float between 0 and 1. Fraction of the input units to drop.
* <b>`data_format`</b>: 'channels_first' or 'channels_last'.
    In 'channels_first' mode, the channels dimension (the depth)
    is at index 1, in 'channels_last' mode is it at index 4.
    It defaults to the `image_data_format` value found in your
    Keras config file at `~/.keras/keras.json`.
    If you never set it, then it will be "channels_last".


#### Call arguments:


* <b>`inputs`</b>: A 5D tensor.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding dropout) or in inference mode (doing nothing).


#### Input shape:

5D tensor with shape:
`(samples, channels, dim1, dim2, dim3)` if data_format='channels_first'
or 5D tensor with shape:
`(samples, dim1, dim2, dim3, channels)` if data_format='channels_last'.



#### Output shape:

Same as input.



#### References:

- [Efficient Object Localization Using Convolutional
  Networks](https://arxiv.org/abs/1411.4280)


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L323-L331">View source</a>

``` python
__init__(
    rate,
    data_format=None,
    **kwargs
)
```
