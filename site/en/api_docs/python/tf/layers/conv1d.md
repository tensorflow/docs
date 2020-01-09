page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.conv1d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/layers/convolutional.py#L118-L218">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Functional interface for 1D convolution layer (e.g. temporal convolution). (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/layers/conv1d"><code>tf.compat.v1.layers.conv1d</code></a>


``` python
tf.layers.conv1d(
    inputs,
    filters,
    kernel_size,
    strides=1,
    padding='valid',
    data_format='channels_last',
    dilation_rate=1,
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
    reuse=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/keras/layers/Conv1D"><code>tf.keras.layers.Conv1D</code></a> instead.

This layer creates a convolution kernel that is convolved
(actually cross-correlated) with the layer input to produce a tensor of
outputs. If `use_bias` is True (and a `bias_initializer` is provided),
a bias vector is created and added to the outputs. Finally, if
`activation` is not `None`, it is applied to the outputs as well.

#### Arguments:


* <b>`inputs`</b>: Tensor input.
* <b>`filters`</b>: Integer, the dimensionality of the output space (i.e. the number
  of filters in the convolution).
* <b>`kernel_size`</b>: An integer or tuple/list of a single integer, specifying the
  length of the 1D convolution window.
* <b>`strides`</b>: An integer or tuple/list of a single integer,
  specifying the stride length of the convolution.
  Specifying any stride value != 1 is incompatible with specifying
  any `dilation_rate` value != 1.
* <b>`padding`</b>: One of `"valid"` or `"same"` (case-insensitive).
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, length, channels)` while `channels_first` corresponds to
  inputs with shape `(batch, channels, length)`.
* <b>`dilation_rate`</b>: An integer or tuple/list of a single integer, specifying
  the dilation rate to use for dilated convolution.
  Currently, specifying any `dilation_rate` value != 1 is
  incompatible with specifying any `strides` value != 1.
* <b>`activation`</b>: Activation function. Set it to None to maintain a
  linear activation.
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias.
* <b>`kernel_initializer`</b>: An initializer for the convolution kernel.
* <b>`bias_initializer`</b>: An initializer for the bias vector. If None, the default
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
* <b>`reuse`</b>: Boolean, whether to reuse the weights of a previous layer
  by the same name.


#### Returns:

Output tensor.



#### Raises:


* <b>`ValueError`</b>: if eager execution is enabled.
