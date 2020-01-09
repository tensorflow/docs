page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.SpatialDropout1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L183-L221">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SpatialDropout1D`

Spatial 1D version of Dropout.

Inherits From: [`Dropout`](../../../tf/keras/layers/Dropout)

### Aliases:

* Class `tf.compat.v1.keras.layers.SpatialDropout1D`
* Class `tf.compat.v2.keras.layers.SpatialDropout1D`


<!-- Placeholder for "Used in" -->

This version performs the same function as Dropout, however it drops
entire 1D feature maps instead of individual elements. If adjacent frames
within feature maps are strongly correlated (as is normally the case in
early convolution layers) then regular dropout will not regularize the
activations and will otherwise just result in an effective learning rate
decrease. In this case, SpatialDropout1D will help promote independence
between feature maps and should be used instead.

#### Arguments:


* <b>`rate`</b>: Float between 0 and 1. Fraction of the input units to drop.


#### Call arguments:


* <b>`inputs`</b>: A 3D tensor.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding dropout) or in inference mode (doing nothing).


#### Input shape:

3D tensor with shape:
`(samples, timesteps, channels)`



#### Output shape:

Same as input.



#### References:

- [Efficient Object Localization Using Convolutional
  Networks](https://arxiv.org/abs/1411.4280)


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L214-L216">View source</a>

``` python
__init__(
    rate,
    **kwargs
)
```
