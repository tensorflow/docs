page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.separable_conv2d

Adds a depth-separable 2D convolution with optional batch_norm layer.

### Aliases:

* `tf.contrib.layers.separable_conv2d`
* `tf.contrib.layers.separable_convolution2d`

``` python
tf.contrib.layers.separable_conv2d(
    inputs,
    num_outputs,
    kernel_size,
    depth_multiplier=1,
    stride=1,
    padding='SAME',
    data_format=DATA_FORMAT_NHWC,
    rate=1,
    activation_fn=tf.nn.relu,
    normalizer_fn=None,
    normalizer_params=None,
    weights_initializer=initializers.xavier_initializer(),
    pointwise_initializer=None,
    weights_regularizer=None,
    biases_initializer=tf.zeros_initializer(),
    biases_regularizer=None,
    reuse=None,
    variables_collections=None,
    outputs_collections=None,
    trainable=True,
    scope=None
)
```



Defined in [`contrib/layers/python/layers/layers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/layers.py).

<!-- Placeholder for "Used in" -->

This op first performs a depthwise convolution that acts separately on
channels, creating a variable called `depthwise_weights`. If `num_outputs`
is not None, it adds a pointwise convolution that mixes channels, creating a
variable called `pointwise_weights`. Then, if `normalizer_fn` is None,
it adds bias to the result, creating a variable called 'biases', otherwise,
the `normalizer_fn` is applied. It finally applies an activation function
to produce the end result.

#### Args:


* <b>`inputs`</b>: A tensor of size [batch_size, height, width, channels].
* <b>`num_outputs`</b>: The number of pointwise convolution output filters. If is None,
  then we skip the pointwise convolution stage.
* <b>`kernel_size`</b>: A list of length 2: [kernel_height, kernel_width] of of the
  filters. Can be an int if both values are the same.
* <b>`depth_multiplier`</b>: The number of depthwise convolution output channels for
  each input channel. The total number of depthwise convolution output
  channels will be equal to `num_filters_in * depth_multiplier`.
* <b>`stride`</b>: A list of length 2: [stride_height, stride_width], specifying the
  depthwise convolution stride. Can be an int if both strides are the same.
* <b>`padding`</b>: One of 'VALID' or 'SAME'.
* <b>`data_format`</b>: A string. `NHWC` (default) and `NCHW` are supported.
* <b>`rate`</b>: A list of length 2: [rate_height, rate_width], specifying the dilation
  rates for atrous convolution. Can be an int if both rates are the same. If
  any value is larger than one, then both stride values need to be one.
* <b>`activation_fn`</b>: Activation function. The default value is a ReLU function.
  Explicitly set it to None to skip it and maintain a linear activation.
* <b>`normalizer_fn`</b>: Normalization function to use instead of `biases`. If
  `normalizer_fn` is provided then `biases_initializer` and
  `biases_regularizer` are ignored and `biases` are not created nor added.
  default set to None for no normalizer function
* <b>`normalizer_params`</b>: Normalization function parameters.
* <b>`weights_initializer`</b>: An initializer for the depthwise weights.
* <b>`pointwise_initializer`</b>: An initializer for the pointwise weights. default set
  to None, means use weights_initializer.
* <b>`weights_regularizer`</b>: Optional regularizer for the weights.
* <b>`biases_initializer`</b>: An initializer for the biases. If None skip biases.
* <b>`biases_regularizer`</b>: Optional regularizer for the biases.
* <b>`reuse`</b>: Whether or not the layer and its variables should be reused. To be
  able to reuse the layer scope must be given.
* <b>`variables_collections`</b>: Optional list of collections for all the variables or
  a dictionary containing a different list of collection per variable.
* <b>`outputs_collections`</b>: Collection to add the outputs.
* <b>`trainable`</b>: Whether or not the variables should be trainable or not.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

A `Tensor` representing the output of the operation.


#### Raises:


* <b>`ValueError`</b>: If `data_format` is invalid.