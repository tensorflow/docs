page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.SpatialDropout2D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/SpatialDropout2D">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/core.py#L225-L280">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SpatialDropout2D`

Spatial 2D version of Dropout.

Inherits From: [`Dropout`](../../../tf/keras/layers/Dropout)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/SpatialDropout2D"><code>tf.compat.v1.keras.layers.SpatialDropout2D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/SpatialDropout2D"><code>tf.compat.v2.keras.layers.SpatialDropout2D</code></a>


<!-- Placeholder for "Used in" -->

This version performs the same function as Dropout, however it drops
entire 2D feature maps instead of individual elements. If adjacent pixels
within feature maps are strongly correlated (as is normally the case in
early convolution layers) then regular dropout will not regularize the
activations and will otherwise just result in an effective learning rate
decrease. In this case, SpatialDropout2D will help promote independence
between feature maps and should be used instead.

#### Arguments:


* <b>`rate`</b>: Float between 0 and 1. Fraction of the input units to drop.
* <b>`data_format`</b>: 'channels_first' or 'channels_last'.
  In 'channels_first' mode, the channels dimension
  (the depth) is at index 1,
  in 'channels_last' mode is it at index 3.
  It defaults to the `image_data_format` value found in your
  Keras config file at `~/.keras/keras.json`.
  If you never set it, then it will be "channels_last".


#### Call arguments:


* <b>`inputs`</b>: A 4D tensor.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding dropout) or in inference mode (doing nothing).


#### Input shape:

4D tensor with shape:
`(samples, channels, rows, cols)` if data_format='channels_first'
or 4D tensor with shape:
`(samples, rows, cols, channels)` if data_format='channels_last'.



#### Output shape:

Same as input.



#### References:

- [Efficient Object Localization Using Convolutional
  Networks](https://arxiv.org/abs/1411.4280)


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/core.py#L265-L273">View source</a>

``` python
__init__(
    rate,
    data_format=None,
    **kwargs
)
```
