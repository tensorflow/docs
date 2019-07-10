page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Conv2D

## Class `Conv2D`

2D convolution layer (e.g. spatial convolution over images).



### Aliases:

* Class `tf.compat.v1.keras.layers.Conv2D`
* Class `tf.compat.v1.keras.layers.Convolution2D`
* Class `tf.compat.v2.keras.layers.Conv2D`
* Class `tf.compat.v2.keras.layers.Convolution2D`
* Class `tf.keras.layers.Conv2D`
* Class `tf.keras.layers.Convolution2D`



Defined in [`python/keras/layers/convolutional.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/convolutional.py).

<!-- Placeholder for "Used in" -->

This layer creates a convolution kernel that is convolved
with the layer input to produce a tensor of
outputs. If `use_bias` is True,
a bias vector is created and added to the outputs. Finally, if
`activation` is not `None`, it is applied to the outputs as well.

When using this layer as the first layer in a model,
provide the keyword argument `input_shape`
(tuple of integers, does not include the sample axis),
e.g. `input_shape=(128, 128, 3)` for 128x128 RGB pictures
in `data_format="channels_last"`.

#### Arguments:


* <b>`filters`</b>: Integer, the dimensionality of the output space
  (i.e. the number of output filters in the convolution).
* <b>`kernel_size`</b>: An integer or tuple/list of 2 integers, specifying the
  height and width of the 2D convolution window.
  Can be a single integer to specify the same value for
  all spatial dimensions.
* <b>`strides`</b>: An integer or tuple/list of 2 integers,
  specifying the strides of the convolution along the height and width.
  Can be a single integer to specify the same value for
  all spatial dimensions.
  Specifying any stride value != 1 is incompatible with specifying
  any `dilation_rate` value != 1.
* <b>`padding`</b>: one of `"valid"` or `"same"` (case-insensitive).
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
* <b>`dilation_rate`</b>: an integer or tuple/list of 2 integers, specifying
  the dilation rate to use for dilated convolution.
  Can be a single integer to specify the same value for
  all spatial dimensions.
  Currently, specifying any `dilation_rate` value != 1 is
  incompatible with specifying any stride value != 1.
* <b>`activation`</b>: Activation function to use.
  If you don't specify anything, no activation is applied
  (ie. "linear" activation: `a(x) = x`).
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias vector.
* <b>`kernel_initializer`</b>: Initializer for the `kernel` weights matrix.
* <b>`bias_initializer`</b>: Initializer for the bias vector.
* <b>`kernel_regularizer`</b>: Regularizer function applied to
  the `kernel` weights matrix.
* <b>`bias_regularizer`</b>: Regularizer function applied to the bias vector.
* <b>`activity_regularizer`</b>: Regularizer function applied to
  the output of the layer (its "activation")..
* <b>`kernel_constraint`</b>: Constraint function applied to the kernel matrix.
* <b>`bias_constraint`</b>: Constraint function applied to the bias vector.


#### Input shape:

4D tensor with shape:
`(samples, channels, rows, cols)` if data_format='channels_first'
or 4D tensor with shape:
`(samples, rows, cols, channels)` if data_format='channels_last'.



#### Output shape:

4D tensor with shape:
`(samples, filters, new_rows, new_cols)` if data_format='channels_first'
or 4D tensor with shape:
`(samples, new_rows, new_cols, filters)` if data_format='channels_last'.
`rows` and `cols` values might have changed due to padding.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    filters,
    kernel_size,
    strides=(1, 1),
    padding='valid',
    data_format=None,
    dilation_rate=(1, 1),
    activation=None,
    use_bias=True,
    kernel_initializer='glorot_uniform',
    bias_initializer='zeros',
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs
)
```






