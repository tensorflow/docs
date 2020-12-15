description: Depthwise separable 2D convolution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.DepthwiseConv2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.DepthwiseConv2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/convolutional.py#L2240-L2453">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Depthwise separable 2D convolution.

Inherits From: [`Conv2D`](../../../tf/keras/layers/Conv2D.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.DepthwiseConv2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.DepthwiseConv2D(
    kernel_size, strides=(1, 1), padding='valid', depth_multiplier=1,
    data_format=None, dilation_rate=(1, 1), activation=None, use_bias=(True),
    depthwise_initializer='glorot_uniform', bias_initializer='zeros',
    depthwise_regularizer=None, bias_regularizer=None, activity_regularizer=None,
    depthwise_constraint=None, bias_constraint=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Depthwise Separable convolutions consist of performing
just the first step in a depthwise spatial convolution
(which acts on each input channel separately).
The `depth_multiplier` argument controls how many
output channels are generated per input channel in the depthwise step.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
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
one of `'valid'` or `'same'` (case-insensitive).
`"valid"` means no padding. `"same"` results in padding evenly to
the left/right or up/down of the input such that output has the same
height/width dimension as the input.
</td>
</tr><tr>
<td>
`depth_multiplier`
</td>
<td>
The number of depthwise convolution output channels
for each input channel.
The total number of depthwise convolution output
channels will be equal to `filters_in * depth_multiplier`.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string,
one of `channels_last` (default) or `channels_first`.
The ordering of the dimensions in the inputs.
`channels_last` corresponds to inputs with shape
`(batch_size, height, width, channels)` while `channels_first`
corresponds to inputs with shape
`(batch_size, channels, height, width)`.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be 'channels_last'.
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
An integer or tuple/list of 2 integers, specifying
the dilation rate to use for dilated convolution.
Currently, specifying any `dilation_rate` value != 1 is
incompatible with specifying any `strides` value != 1.
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
Boolean, whether the layer uses a bias vector.
</td>
</tr><tr>
<td>
`depthwise_initializer`
</td>
<td>
Initializer for the depthwise kernel matrix (
see <a href="../../../tf/keras/initializers.md"><code>keras.initializers</code></a>).
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
Initializer for the bias vector (
see <a href="../../../tf/keras/initializers.md"><code>keras.initializers</code></a>).
</td>
</tr><tr>
<td>
`depthwise_regularizer`
</td>
<td>
Regularizer function applied to
the depthwise kernel matrix (see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Regularizer function applied to the bias vector (
see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`activity_regularizer`
</td>
<td>
Regularizer function applied to
the output of the layer (its 'activation') (
see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`depthwise_constraint`
</td>
<td>
Constraint function applied to
the depthwise kernel matrix (
see <a href="../../../tf/keras/constraints.md"><code>keras.constraints</code></a>).
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
Constraint function applied to the bias vector (
see <a href="../../../tf/keras/constraints.md"><code>keras.constraints</code></a>).
</td>
</tr>
</table>



#### Input shape:

4D tensor with shape:
`[batch_size, channels, rows, cols]` if data_format='channels_first'
or 4D tensor with shape:
`[batch_size, rows, cols, channels]` if data_format='channels_last'.



#### Output shape:

4D tensor with shape:
`[batch_size, filters, new_rows, new_cols]` if data_format='channels_first'
or 4D tensor with shape:
`[batch_size, new_rows, new_cols, filters]` if data_format='channels_last'.
`rows` and `cols` values might have changed due to padding.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of rank 4 representing
`activation(depthwiseconv2d(inputs, kernel) + bias)`.
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
if `padding` is "causal".
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
when both `strides` > 1 and `dilation_rate` > 1.
</td>
</tr>
</table>



