


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.layers.conv1d, kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, trainable=True, name=None, reuse=None)

### `tf.layers.conv1d`

```
tf.layers.conv1d(inputs, filters, kernel_size, strides=1, padding='valid', data_format='channels_last', dilation_rate=1, activation=None, use_bias=True, kernel_initializer=None, bias_initializer=tf.zeros_initializer(), kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, trainable=True, name=None, reuse=None)
```


Functional interface for 1D convolution layer (e.g. temporal convolution).

This layer creates a convolution kernel that is convolved
(actually cross-correlated) with the layer input to produce a tensor of
outputs. If `use_bias` is True (and a `bias_initializer` is provided),
a bias vector is created and added to the outputs. Finally, if
`activation` is not `None`, it is applied to the outputs as well.

#### Arguments:

* <b>`inputs`</b>: Tensor input.
* <b>`filters`</b>: integer, the dimensionality of the output space (i.e. the number
    output of filters in the convolution).
* <b>`kernel_size`</b>: An integer or tuple/list of a single integer, specifying the
    length of the 1D convolution window.
* <b>`strides`</b>: an integer or tuple/list of a single integer,
    specifying the stride length of the convolution.
    Specifying any stride value != 1 is incompatible with specifying
    any `dilation_rate` value != 1.
* <b>`padding`</b>: one of `"valid"` or `"same"` (case-insensitive).
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
    The ordering of the dimensions in the inputs.
    `channels_last` corresponds to inputs with shape
    `(batch, length, channels)` while `channels_first` corresponds to
    inputs with shape `(batch, channels, length)`.
* <b>`dilation_rate`</b>: an integer or tuple/list of a single integer, specifying
    the dilation rate to use for dilated convolution.
    Currently, specifying any `dilation_rate` value != 1 is
    incompatible with specifying any `strides` value != 1.
* <b>`activation`</b>: Activation function. Set it to None to maintain a
    linear activation.
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias.
* <b>`kernel_initializer`</b>: An initializer for the convolution kernel.
* <b>`bias_initializer`</b>: An initializer for the bias vector. If None, no bias will
    be applied.
* <b>`kernel_regularizer`</b>: Optional regularizer for the convolution kernel.
* <b>`bias_regularizer`</b>: Optional regularizer for the bias vector.
* <b>`activity_regularizer`</b>: Regularizer function for the output.
* <b>`trainable`</b>: Boolean, if `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
* <b>`name`</b>: A string, the name of the layer.
* <b>`reuse`</b>: Boolean, whether to reuse the weights of a previous layer
    by the same name.


#### Returns:

  Output tensor.

Defined in [`tensorflow/python/layers/convolutional.py`](https://www.tensorflow.org/code/tensorflow/python/layers/convolutional.py).

