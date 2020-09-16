description: Depthwise separable 1D convolution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.SeparableConv1D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.SeparableConv1D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/convolutional.py#L1548-L1719">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Depthwise separable 1D convolution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.SeparableConvolution1D`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.SeparableConv1D`, `tf.compat.v1.keras.layers.SeparableConvolution1D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.SeparableConv1D(
    filters, kernel_size, strides=1, padding='valid', data_format=None,
    dilation_rate=1, depth_multiplier=1, activation=None, use_bias=(True),
    depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform',
    bias_initializer='zeros', depthwise_regularizer=None,
    pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None,
    depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

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
One of `"valid"`, `"same"`, or `"causal"` (case-insensitive).
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string, one of `channels_last` (default) or `channels_first`.
The ordering of the dimensions in the inputs.
`channels_last` corresponds to inputs with shape
`(batch_size, length, channels)` while `channels_first` corresponds to
inputs with shape `(batch_size, channels, length)`.
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
Activation function to use.
If you don't specify anything, no activation is applied (
see <a href="../../../tf/keras/activations.md"><code>keras.activations</code></a>).
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
An initializer for the depthwise convolution kernel (
see <a href="../../../tf/keras/initializers.md"><code>keras.initializers</code></a>).
</td>
</tr><tr>
<td>
`pointwise_initializer`
</td>
<td>
An initializer for the pointwise convolution kernel (
see <a href="../../../tf/keras/initializers.md"><code>keras.initializers</code></a>).
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
An initializer for the bias vector. If None, the default
initializer will be used (see <a href="../../../tf/keras/initializers.md"><code>keras.initializers</code></a>).
</td>
</tr><tr>
<td>
`depthwise_regularizer`
</td>
<td>
Optional regularizer for the depthwise
convolution kernel (see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`pointwise_regularizer`
</td>
<td>
Optional regularizer for the pointwise
convolution kernel (see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Optional regularizer for the bias vector (
see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`activity_regularizer`
</td>
<td>
Optional regularizer function for the output (
see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
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
not safe to use when doing asynchronous distributed training (
see <a href="../../../tf/keras/constraints.md"><code>keras.constraints</code></a>).
</td>
</tr><tr>
<td>
`pointwise_constraint`
</td>
<td>
Optional projection function to be applied to the
pointwise kernel after being updated by an `Optimizer` (
see <a href="../../../tf/keras/constraints.md"><code>keras.constraints</code></a>).
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
Optional projection function to be applied to the
bias after being updated by an `Optimizer` (
see <a href="../../../tf/keras/constraints.md"><code>keras.constraints</code></a>).
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, if `True` the weights of this layer will be marked as
trainable (and listed in `layer.trainable_weights`).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string, the name of the layer.
</td>
</tr>
</table>



#### Input shape:

3D tensor with shape:
`(batch_size, channels, steps)` if data_format='channels_first'
or 5D tensor with shape:
`(batch_size, steps, channels)` if data_format='channels_last'.



#### Output shape:

3D tensor with shape:
`(batch_size, filters, new_steps)` if data_format='channels_first'
or 3D tensor with shape:
`(batch_size,  new_steps, filters)` if data_format='channels_last'.
`new_steps` value might have changed due to padding or strides.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of rank 3 representing
`activation(separableconv1d(inputs, kernel) + bias)`.
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
when both `strides` > 1 and `dilation_rate` > 1.
</td>
</tr>
</table>



