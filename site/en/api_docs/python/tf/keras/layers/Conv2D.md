description: 2D convolution layer (e.g. spatial convolution over images).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Conv2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Conv2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/convolutional.py#L516-L671">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



2D convolution layer (e.g. spatial convolution over images).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.Convolution2D`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Conv2D`, `tf.compat.v1.keras.layers.Convolution2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Conv2D(
    filters, kernel_size, strides=(1, 1), padding='valid', data_format=None,
    dilation_rate=(1, 1), groups=1, activation=None, use_bias=(True),
    kernel_initializer='glorot_uniform', bias_initializer='zeros',
    kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None,
    kernel_constraint=None, bias_constraint=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer creates a convolution kernel that is convolved
with the layer input to produce a tensor of
outputs. If `use_bias` is True,
a bias vector is created and added to the outputs. Finally, if
`activation` is not `None`, it is applied to the outputs as well.

When using this layer as the first layer in a model,
provide the keyword argument `input_shape`
(tuple of integers, does not include the sample axis),
e.g. `input_shape=(128, 128, 3)` for 128x128 RGB pictures
in `data_format="channels_last"`.

#### Examples:



```
>>> # The inputs are 28x28 RGB images with `channels_last` and the batch
>>> # size is 4.
>>> input_shape = (4, 28, 28, 3)
>>> x = tf.random.normal(input_shape)
>>> y = tf.keras.layers.Conv2D(
... 2, 3, activation='relu', input_shape=input_shape[1:])(x)
>>> print(y.shape)
(4, 26, 26, 2)
```

```
>>> # With `dilation_rate` as 2.
>>> input_shape = (4, 28, 28, 3)
>>> x = tf.random.normal(input_shape)
>>> y = tf.keras.layers.Conv2D(
... 2, 3, activation='relu', dilation_rate=2, input_shape=input_shape[1:])(x)
>>> print(y.shape)
(4, 24, 24, 2)
```

```
>>> # With `padding` as "same".
>>> input_shape = (4, 28, 28, 3)
>>> x = tf.random.normal(input_shape)
>>> y = tf.keras.layers.Conv2D(
... 2, 3, activation='relu', padding="same", input_shape=input_shape[1:])(x)
>>> print(y.shape)
(4, 28, 28, 2)
```

```
>>> # With extended batch shape [4, 7]:
>>> input_shape = (4, 7, 28, 28, 3)
>>> x = tf.random.normal(input_shape)
>>> y = tf.keras.layers.Conv2D(
... 2, 3, activation='relu', input_shape=input_shape[2:])(x)
>>> print(y.shape)
(4, 7, 26, 26, 2)
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`filters`
</td>
<td>
Integer, the dimensionality of the output space (i.e. the number of
output filters in the convolution).
</td>
</tr><tr>
<td>
`kernel_size`
</td>
<td>
An integer or tuple/list of 2 integers, specifying the height
and width of the 2D convolution window. Can be a single integer to specify
the same value for all spatial dimensions.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of 2 integers, specifying the strides of
the convolution along the height and width. Can be a single integer to
specify the same value for all spatial dimensions. Specifying any stride
value != 1 is incompatible with specifying any `dilation_rate` value != 1.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
one of `"valid"` or `"same"` (case-insensitive).
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
The ordering of the dimensions in the inputs. `channels_last` corresponds
to inputs with shape `(batch_size, height, width, channels)` while
`channels_first` corresponds to inputs with shape `(batch_size, channels,
height, width)`. It defaults to the `image_data_format` value found in
your Keras config file at `~/.keras/keras.json`. If you never set it, then
it will be `channels_last`.
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
an integer or tuple/list of 2 integers, specifying the
dilation rate to use for dilated convolution. Can be a single integer to
specify the same value for all spatial dimensions. Currently, specifying
any `dilation_rate` value != 1 is incompatible with specifying any stride
value != 1.
</td>
</tr><tr>
<td>
`groups`
</td>
<td>
A positive integer specifying the number of groups in which the
input is split along the channel axis. Each group is convolved separately
with `filters / groups` filters. The output is the concatenation of all
the `groups` results along the channel axis. Input channels and `filters`
must both be divisible by `groups`.
</td>
</tr><tr>
<td>
`activation`
</td>
<td>
Activation function to use. If you don't specify anything, no
activation is applied (see <a href="../../../tf/keras/activations.md"><code>keras.activations</code></a>).
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
Initializer for the `kernel` weights matrix (see
<a href="../../../tf/keras/initializers.md"><code>keras.initializers</code></a>).
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
Initializer for the bias vector (see
<a href="../../../tf/keras/initializers.md"><code>keras.initializers</code></a>).
</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>
Regularizer function applied to the `kernel` weights
matrix (see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Regularizer function applied to the bias vector (see
<a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`activity_regularizer`
</td>
<td>
Regularizer function applied to the output of the
layer (its "activation") (see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Constraint function applied to the kernel matrix (see
<a href="../../../tf/keras/constraints.md"><code>keras.constraints</code></a>).
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
Constraint function applied to the bias vector (see
<a href="../../../tf/keras/constraints.md"><code>keras.constraints</code></a>).
</td>
</tr>
</table>



#### Input shape:

4+D tensor with shape: `batch_shape + (channels, rows, cols)` if
  `data_format='channels_first'`
or 4+D tensor with shape: `batch_shape + (rows, cols, channels)` if
  `data_format='channels_last'`.


#### Output shape:

4+D tensor with shape: `batch_shape + (filters, new_rows, new_cols)` if
`data_format='channels_first'` or 4+D tensor with shape: `batch_shape +
  (new_rows, new_cols, filters)` if `data_format='channels_last'`.  `rows`
  and `cols` values might have changed due to padding.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of rank 4+ representing
`activation(conv2d(inputs, kernel) + bias)`.
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
if `padding` is `"causal"`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
when both `strides > 1` and `dilation_rate > 1`.
</td>
</tr>
</table>



