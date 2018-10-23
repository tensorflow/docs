


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.layers.conv2d_transpose, padding='valid', data_format='channels_last', activation=None, use_bias=True, kernel_initializer=None, bias_initializer=tf.zeros_initializer(), kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, trainable=True, name=None, reuse=None)

### `tf.layers.conv2d_transpose`

```
tf.layers.conv2d_transpose(inputs, filters, kernel_size, strides=(1, 1), padding='valid', data_format='channels_last', activation=None, use_bias=True, kernel_initializer=None, bias_initializer=tf.zeros_initializer(), kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, trainable=True, name=None, reuse=None)
```


Transposed convolution layer (sometimes called Deconvolution).

The need for transposed convolutions generally arises
from the desire to use a transformation going in the opposite direction
of a normal convolution, i.e., from something that has the shape of the
output of some convolution to something that has the shape of its input
while maintaining a connectivity pattern that is compatible with
said convolution.

#### Arguments:

* <b>`inputs`</b>: Input tensor.
* <b>`filters`</b>: integer, the dimensionality of the output space (i.e. the number
    output of filters in the convolution).
* <b>`kernel_size`</b>: a tuple or list of 2 positive integers specifying the spatial
    dimensions of of the filters. Can be a single integer to specify the same
    value for all spatial dimensions.
* <b>`strides`</b>: a tuple or list of 2 positive integers specifying the strides
    of the convolution. Can be a single integer to specify the same value for
    all spatial dimensions.
* <b>`padding`</b>: one of `"valid"` or `"same"` (case-insensitive).
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
    The ordering of the dimensions in the inputs.
    `channels_last` corresponds to inputs with shape
    `(batch, width, height, channels)` while `channels_first` corresponds to
    inputs with shape `(batch, channels, width, height)`.
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

