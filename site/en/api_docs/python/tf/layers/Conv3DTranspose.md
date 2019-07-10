page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.Conv3DTranspose

## Class `Conv3DTranspose`

Transposed 3D convolution layer (sometimes called 3D Deconvolution).

Inherits From: [`Conv3DTranspose`](../../tf/keras/layers/Conv3DTranspose), [`Layer`](../../tf/layers/Layer)

### Aliases:

* Class `tf.compat.v1.layers.Conv3DTranspose`
* Class `tf.layers.Conv3DTranspose`



Defined in [`python/layers/convolutional.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/layers/convolutional.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`filters`</b>: Integer, the dimensionality of the output space (i.e. the number
  of filters in the convolution).
* <b>`kernel_size`</b>: An integer or tuple/list of 3 integers, specifying the
  depth, height and width of the 3D convolution window.
  Can be a single integer to specify the same value for all spatial
  dimensions.
* <b>`strides`</b>: An integer or tuple/list of 3 integers, specifying the strides
  of the convolution along the depth, height and width.
  Can be a single integer to specify the same value for all spatial
  dimensions.
* <b>`padding`</b>: One of `"valid"` or `"same"` (case-insensitive).
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, depth, height, width, channels)` while `channels_first`
  corresponds to inputs with shape
  `(batch, channels, depth, height, width)`.
* <b>`activation`</b>: Activation function. Set it to `None` to maintain a
  linear activation.
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias.
* <b>`kernel_initializer`</b>: An initializer for the convolution kernel.
* <b>`bias_initializer`</b>: An initializer for the bias vector. If `None`, the default
  initializer will be used.
* <b>`kernel_regularizer`</b>: Optional regularizer for the convolution kernel.
* <b>`bias_regularizer`</b>: Optional regularizer for the bias vector.
* <b>`activity_regularizer`</b>: Optional regularizer function for the output.
* <b>`kernel_constraint`</b>: Optional projection function to be applied to the
    kernel after being updated by an `Optimizer` (e.g. used to implement
    norm constraints or value constraints for layer weights). The function
    must take as input the unprojected variable and must return the
    projected variable (which must have the same shape). Constraints are
    not safe to use when doing asynchronous distributed training.
* <b>`bias_constraint`</b>: Optional projection function to be applied to the
    bias after being updated by an `Optimizer`.
* <b>`trainable`</b>: Boolean, if `True` also add variables to the graph collection
  <a href="../../tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a> (see <a href="../../tf/Variable"><code>tf.Variable</code></a>).
* <b>`name`</b>: A string, the name of the layer.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    filters,
    kernel_size,
    strides=(1, 1, 1),
    padding='valid',
    data_format='channels_last',
    activation=None,
    use_bias=True,
    kernel_initializer=None,
    bias_initializer=tf.zeros_initializer(),
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    **kwargs
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="scope_name"><code>scope_name</code></h3>






