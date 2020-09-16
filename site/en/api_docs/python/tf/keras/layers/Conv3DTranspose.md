description: Transposed convolution layer (sometimes called Deconvolution).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Conv3DTranspose" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Conv3DTranspose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/convolutional.py#L1037-L1338">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Transposed convolution layer (sometimes called Deconvolution).

Inherits From: [`Conv3D`](../../../tf/keras/layers/Conv3D.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.Convolution3DTranspose`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Conv3DTranspose`, `tf.compat.v1.keras.layers.Convolution3DTranspose`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Conv3DTranspose(
    filters, kernel_size, strides=(1, 1, 1), padding='valid', output_padding=None,
    data_format=None, activation=None, use_bias=(True),
    kernel_initializer='glorot_uniform', bias_initializer='zeros',
    kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None,
    kernel_constraint=None, bias_constraint=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The need for transposed convolutions generally arises
from the desire to use a transformation going in the opposite direction
of a normal convolution, i.e., from something that has the shape of the
output of some convolution to something that has the shape of its input
while maintaining a connectivity pattern that is compatible with
said convolution.

When using this layer as the first layer in a model,
provide the keyword argument `input_shape`
(tuple of integers, does not include the sample axis),
e.g. `input_shape=(128, 128, 128, 3)` for a 128x128x128 volume with 3 channels
if `data_format="channels_last"`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`filters`
</td>
<td>
Integer, the dimensionality of the output space
(i.e. the number of output filters in the convolution).
</td>
</tr><tr>
<td>
`kernel_size`
</td>
<td>
An integer or tuple/list of 3 integers, specifying the
depth, height and width of the 3D convolution window.
Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of 3 integers,
specifying the strides of the convolution along the depth, height
and width.
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
one of `"valid"` or `"same"` (case-insensitive).
</td>
</tr><tr>
<td>
`output_padding`
</td>
<td>
An integer or tuple/list of 3 integers,
specifying the amount of padding along the depth, height, and
width.
Can be a single integer to specify the same value for all
spatial dimensions.
The amount of output padding along a given dimension must be
lower than the stride along that same dimension.
If set to `None` (default), the output shape is inferred.
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
`(batch_size, depth, height, width, channels)` while `channels_first`
corresponds to inputs with shape
`(batch_size, channels, depth, height, width)`.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be "channels_last".
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
an integer or tuple/list of 3 integers, specifying
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
`kernel_initializer`
</td>
<td>
Initializer for the `kernel` weights matrix.
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
Initializer for the bias vector.
</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>
Regularizer function applied to
the `kernel` weights matrix (
see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
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
the output of the layer (its "activation") (
see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Constraint function applied to the kernel matrix (
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

5D tensor with shape:
`(batch_size, channels, depth, rows, cols)` if data_format='channels_first'
or 5D tensor with shape:
`(batch_size, depth, rows, cols, channels)` if data_format='channels_last'.



#### Output shape:

5D tensor with shape:
`(batch_size, filters, new_depth, new_rows, new_cols)` if
  data_format='channels_first'
or 5D tensor with shape:
`(batch_size, new_depth, new_rows, new_cols, filters)` if
  data_format='channels_last'.
`depth` and `rows` and `cols` values might have changed due to padding.
If `output_padding` is specified::
```
new_depth = ((depth - 1) * strides[0] + kernel_size[0] - 2 * padding[0] +
output_padding[0])
new_rows = ((rows - 1) * strides[1] + kernel_size[1] - 2 * padding[1] +
output_padding[1])
new_cols = ((cols - 1) * strides[2] + kernel_size[2] - 2 * padding[2] +
output_padding[2])
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of rank 5 representing
`activation(conv3dtranspose(inputs, kernel) + bias)`.
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



#### References:

- [A guide to convolution arithmetic for deep
  learning](https://arxiv.org/abs/1603.07285v1)
- [Deconvolutional
  Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)


