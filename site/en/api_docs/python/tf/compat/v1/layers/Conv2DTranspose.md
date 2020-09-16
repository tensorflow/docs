description: Transposed 2D convolution layer (sometimes called 2D Deconvolution).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.Conv2DTranspose" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.compat.v1.layers.Conv2DTranspose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/layers/convolutional.py#L1100-L1181">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Transposed 2D convolution layer (sometimes called 2D Deconvolution).

Inherits From: [`Conv2DTranspose`](../../../../tf/keras/layers/Conv2DTranspose.md), [`Layer`](../../../../tf/compat/v1/layers/Layer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.Conv2DTranspose(
    filters, kernel_size, strides=(1, 1), padding='valid',
    data_format='channels_last', activation=None, use_bias=(True),
    kernel_initializer=None, bias_initializer=tf.zeros_initializer(),
    kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None,
    kernel_constraint=None, bias_constraint=None, trainable=(True), name=None,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The need for transposed convolutions generally arises
from the desire to use a transformation going in the opposite direction
of a normal convolution, i.e., from something that has the shape of the
output of some convolution to something that has the shape of its input
while maintaining a connectivity pattern that is compatible with
said convolution.

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
A tuple or list of 2 positive integers specifying the spatial
dimensions of the filters. Can be a single integer to specify the same
value for all spatial dimensions.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A tuple or list of 2 positive integers specifying the strides
of the convolution. Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
one of `"valid"` or `"same"` (case-insensitive).
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
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.
</td>
</tr><tr>
<td>
`scope_name`
</td>
<td>

</td>
</tr>
</table>



