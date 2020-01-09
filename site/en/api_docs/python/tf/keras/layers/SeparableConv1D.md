page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.SeparableConv1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional.py#L1387-L1530">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SeparableConv1D`

Depthwise separable 1D convolution.



### Aliases:

* Class `tf.compat.v1.keras.layers.SeparableConv1D`
* Class `tf.compat.v1.keras.layers.SeparableConvolution1D`
* Class `tf.compat.v2.keras.layers.SeparableConv1D`
* Class `tf.compat.v2.keras.layers.SeparableConvolution1D`
* Class `tf.keras.layers.SeparableConvolution1D`


<!-- Placeholder for "Used in" -->

This layer performs a depthwise convolution that acts separately on
channels, followed by a pointwise convolution that mixes channels.
If `use_bias` is True and a bias initializer is provided,
it adds a bias vector to the output.
It then optionally applies an activation function to produce the final output.

#### Arguments:


* <b>`filters`</b>: Integer, the dimensionality of the output space (i.e. the number
  of filters in the convolution).
* <b>`kernel_size`</b>: A single integer specifying the spatial
  dimensions of the filters.
* <b>`strides`</b>: A single integer specifying the strides
  of the convolution.
  Specifying any `stride` value != 1 is incompatible with specifying
  any `dilation_rate` value != 1.
* <b>`padding`</b>: One of `"valid"`, `"same"`, or `"causal"` (case-insensitive).
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, length, channels)` while `channels_first` corresponds to
  inputs with shape `(batch, channels, length)`.
* <b>`dilation_rate`</b>: A single integer, specifying
  the dilation rate to use for dilated convolution.
  Currently, specifying any `dilation_rate` value != 1 is
  incompatible with specifying any stride value != 1.
* <b>`depth_multiplier`</b>: The number of depthwise convolution output channels for
  each input channel. The total number of depthwise convolution output
  channels will be equal to `num_filters_in * depth_multiplier`.
* <b>`activation`</b>: Activation function. Set it to None to maintain a
  linear activation.
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias.
* <b>`depthwise_initializer`</b>: An initializer for the depthwise convolution kernel.
* <b>`pointwise_initializer`</b>: An initializer for the pointwise convolution kernel.
* <b>`bias_initializer`</b>: An initializer for the bias vector. If None, the default
  initializer will be used.
* <b>`depthwise_regularizer`</b>: Optional regularizer for the depthwise
  convolution kernel.
* <b>`pointwise_regularizer`</b>: Optional regularizer for the pointwise
  convolution kernel.
* <b>`bias_regularizer`</b>: Optional regularizer for the bias vector.
* <b>`activity_regularizer`</b>: Optional regularizer function for the output.
* <b>`depthwise_constraint`</b>: Optional projection function to be applied to the
  depthwise kernel after being updated by an `Optimizer` (e.g. used for
  norm constraints or value constraints for layer weights). The function
  must take as input the unprojected variable and must return the
  projected variable (which must have the same shape). Constraints are
  not safe to use when doing asynchronous distributed training.
* <b>`pointwise_constraint`</b>: Optional projection function to be applied to the
  pointwise kernel after being updated by an `Optimizer`.
* <b>`bias_constraint`</b>: Optional projection function to be applied to the
  bias after being updated by an `Optimizer`.
* <b>`trainable`</b>: Boolean, if `True` the weights of this layer will be marked as
  trainable (and listed in `layer.trainable_weights`).
* <b>`name`</b>: A string, the name of the layer.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional.py#L1446-L1488">View source</a>

``` python
__init__(
    filters,
    kernel_size,
    strides=1,
    padding='valid',
    data_format=None,
    dilation_rate=1,
    depth_multiplier=1,
    activation=None,
    use_bias=True,
    depthwise_initializer='glorot_uniform',
    pointwise_initializer='glorot_uniform',
    bias_initializer='zeros',
    depthwise_regularizer=None,
    pointwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    pointwise_constraint=None,
    bias_constraint=None,
    **kwargs
)
```
