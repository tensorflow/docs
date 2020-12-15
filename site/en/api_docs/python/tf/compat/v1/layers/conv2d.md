description: Functional interface for the 2D convolution layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.conv2d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.layers.conv2d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/legacy_tf_layers/convolutional.py#L327-L437">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functional interface for the 2D convolution layer.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.conv2d(
    inputs, filters, kernel_size, strides=(1, 1), padding='valid',
    data_format='channels_last', dilation_rate=(1, 1), activation=None,
    use_bias=(True), kernel_initializer=None,
    bias_initializer=tf.zeros_initializer(), kernel_regularizer=None,
    bias_regularizer=None, activity_regularizer=None, kernel_constraint=None,
    bias_constraint=None, trainable=(True), name=None, reuse=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer creates a convolution kernel that is convolved
(actually cross-correlated) with the layer input to produce a tensor of
outputs. If `use_bias` is True (and a `bias_initializer` is provided),
a bias vector is created and added to the outputs. Finally, if
`activation` is not `None`, it is applied to the outputs as well.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
Tensor input.
</td>
</tr><tr>
<td>
`filters`
</td>
<td>
Integer, the dimensionality of the output space (i.e. the number
of filters in the convolution).
</td>
</tr><tr>
<td>
`kernel_size`
</td>
<td>
An integer or tuple/list of 2 integers, specifying the
height and width of the 2D convolution window.
Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of 2 integers,
specifying the strides of the convolution along the height and width.
Can be a single integer to specify the same value for
all spatial dimensions.
Specifying any stride value != 1 is incompatible with specifying
any `dilation_rate` value != 1.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
One of `"valid"` or `"same"` (case-insensitive).
`"valid"` means no padding. `"same"` results in padding evenly to 
the left/right or up/down of the input such that output has the same 
height/width dimension as the input.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string, one of `channels_last` (default) or `channels_first`.
The ordering of the dimensions in the inputs.
`channels_last` corresponds to inputs with shape
`(batch, height, width, channels)` while `channels_first` corresponds to
inputs with shape `(batch, channels, height, width)`.
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
An integer or tuple/list of 2 integers, specifying
the dilation rate to use for dilated convolution.
Can be a single integer to specify the same value for
all spatial dimensions.
Currently, specifying any `dilation_rate` value != 1 is
incompatible with specifying any stride value != 1.
</td>
</tr><tr>
<td>
`activation`
</td>
<td>
Activation function. Set it to None to maintain a
linear activation.
</td>
</tr><tr>
<td>
`use_bias`
</td>
<td>
Boolean, whether the layer uses a bias.
</td>
</tr><tr>
<td>
`kernel_initializer`
</td>
<td>
An initializer for the convolution kernel.
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
An initializer for the bias vector. If None, the default
initializer will be used.
</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>
Optional regularizer for the convolution kernel.
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Optional regularizer for the bias vector.
</td>
</tr><tr>
<td>
`activity_regularizer`
</td>
<td>
Optional regularizer function for the output.
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Optional projection function to be applied to the
kernel after being updated by an `Optimizer` (e.g. used to implement
norm constraints or value constraints for layer weights). The function
must take as input the unprojected variable and must return the
projected variable (which must have the same shape). Constraints are
not safe to use when doing asynchronous distributed training.
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
Optional projection function to be applied to the
bias after being updated by an `Optimizer`.
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, if `True` also add variables to the graph collection
`GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a>).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string, the name of the layer.
</td>
</tr><tr>
<td>
`reuse`
</td>
<td>
Boolean, whether to reuse the weights of a previous layer
by the same name.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Output tensor.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if eager execution is enabled.
</td>
</tr>
</table>

