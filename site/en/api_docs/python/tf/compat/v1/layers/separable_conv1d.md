description: Functional interface for the depthwise separable 1D convolution layer. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.separable_conv1d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.layers.separable_conv1d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/layers/convolutional.py#L854-L971">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functional interface for the depthwise separable 1D convolution layer. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.separable_conv1d(
    inputs, filters, kernel_size, strides=1, padding='valid',
    data_format='channels_last', dilation_rate=1, depth_multiplier=1,
    activation=None, use_bias=(True), depthwise_initializer=None,
    pointwise_initializer=None, bias_initializer=tf.zeros_initializer(),
    depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None,
    activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None,
    bias_constraint=None, trainable=(True), name=None, reuse=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../../tf/keras/layers/SeparableConv1D.md"><code>tf.keras.layers.SeparableConv1D</code></a> instead.

This layer performs a depthwise convolution that acts separately on
channels, followed by a pointwise convolution that mixes channels.
If `use_bias` is True and a bias initializer is provided,
it adds a bias vector to the output.
It then optionally applies an activation function to produce the final output.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
Input tensor.
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
A single integer specifying the spatial
dimensions of the filters.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A single integer specifying the strides
of the convolution.
Specifying any `stride` value != 1 is incompatible with specifying
any `dilation_rate` value != 1.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
One of `"valid"` or `"same"` (case-insensitive).
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string, one of `channels_last` (default) or `channels_first`.
The ordering of the dimensions in the inputs.
`channels_last` corresponds to inputs with shape
`(batch, length, channels)` while `channels_first` corresponds to
inputs with shape `(batch, channels, length)`.
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
A single integer, specifying
the dilation rate to use for dilated convolution.
Currently, specifying any `dilation_rate` value != 1 is
incompatible with specifying any stride value != 1.
</td>
</tr><tr>
<td>
`depth_multiplier`
</td>
<td>
The number of depthwise convolution output channels for
each input channel. The total number of depthwise convolution output
channels will be equal to `num_filters_in * depth_multiplier`.
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
`depthwise_initializer`
</td>
<td>
An initializer for the depthwise convolution kernel.
</td>
</tr><tr>
<td>
`pointwise_initializer`
</td>
<td>
An initializer for the pointwise convolution kernel.
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
`depthwise_regularizer`
</td>
<td>
Optional regularizer for the depthwise
convolution kernel.
</td>
</tr><tr>
<td>
`pointwise_regularizer`
</td>
<td>
Optional regularizer for the pointwise
convolution kernel.
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
`depthwise_constraint`
</td>
<td>
Optional projection function to be applied to the
depthwise kernel after being updated by an `Optimizer` (e.g. used for
norm constraints or value constraints for layer weights). The function
must take as input the unprojected variable and must return the
projected variable (which must have the same shape). Constraints are
not safe to use when doing asynchronous distributed training.
</td>
</tr><tr>
<td>
`pointwise_constraint`
</td>
<td>
Optional projection function to be applied to the
pointwise kernel after being updated by an `Optimizer`.
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

