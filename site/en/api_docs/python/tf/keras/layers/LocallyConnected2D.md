description: Locally-connected layer for 2D inputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.LocallyConnected2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.LocallyConnected2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/local.py#L338-L661">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Locally-connected layer for 2D inputs.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.LocallyConnected2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.LocallyConnected2D(
    filters, kernel_size, strides=(1, 1), padding='valid', data_format=None,
    activation=None, use_bias=(True), kernel_initializer='glorot_uniform',
    bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None,
    activity_regularizer=None, kernel_constraint=None, bias_constraint=None,
    implementation=1, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `LocallyConnected2D` layer works similarly
to the `Conv2D` layer, except that weights are unshared,
that is, a different set of filters is applied at each
different patch of the input.

Note: layer attributes cannot be modified after the layer has been called
once (except the `trainable` attribute).

#### Examples:


```python
    # apply a 3x3 unshared weights convolution with 64 output filters on a
    32x32 image
    # with `data_format="channels_last"`:
    model = Sequential()
    model.add(LocallyConnected2D(64, (3, 3), input_shape=(32, 32, 3)))
    # now model.output_shape == (None, 30, 30, 64)
    # notice that this layer will consume (30*30)*(3*3*3*64) + (30*30)*64
    parameters

    # add a 3x3 unshared weights convolution on top, with 32 output filters:
    model.add(LocallyConnected2D(32, (3, 3)))
    # now model.output_shape == (None, 28, 28, 32)
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
Integer, the dimensionality of the output space
(i.e. the number of output filters in the convolution).
</td>
</tr><tr>
<td>
`kernel_size`
</td>
<td>
An integer or tuple/list of 2 integers, specifying the
width and height of the 2D convolution window.
Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of 2 integers,
specifying the strides of the convolution along the width and height.
Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
Currently only support `"valid"` (case-insensitive).
`"same"` will be supported in future.
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
`(batch, height, width, channels)` while `channels_first`
corresponds to inputs with shape
`(batch, channels, height, width)`.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be "channels_last".
</td>
</tr><tr>
<td>
`activation`
</td>
<td>
Activation function to use.
If you don't specify anything, no activation is applied
(ie. "linear" activation: `a(x) = x`).
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
the `kernel` weights matrix.
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Regularizer function applied to the bias vector.
</td>
</tr><tr>
<td>
`activity_regularizer`
</td>
<td>
Regularizer function applied to
the output of the layer (its "activation").
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Constraint function applied to the kernel matrix.
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
Constraint function applied to the bias vector.
</td>
</tr><tr>
<td>
`implementation`
</td>
<td>
implementation mode, either `1`, `2`, or `3`.
`1` loops over input spatial locations to perform the forward pass.
It is memory-efficient but performs a lot of (small) ops.

`2` stores layer weights in a dense but sparsely-populated 2D matrix
and implements the forward pass as a single matrix-multiply. It uses
a lot of RAM but performs few (large) ops.

`3` stores layer weights in a sparse tensor and implements the forward
pass as a single sparse matrix-multiply.

How to choose:

`1`: large, dense models,
`2`: small models,
`3`: large, sparse models,

where "large" stands for large input/output activations
(i.e. many `filters`, `input_filters`, large `np.prod(input_size)`,
`np.prod(output_size)`), and "sparse" stands for few connections
between inputs and outputs, i.e. small ratio
`filters * input_filters * np.prod(kernel_size) / (np.prod(input_size)
* np.prod(strides))`, where inputs to and outputs of the layer are
assumed to have shapes `input_size + (input_filters,)`,
`output_size + (filters,)` respectively.

It is recommended to benchmark each in the setting of interest to pick
the most efficient one (in terms of speed and memory usage). Correct
choice of implementation can lead to dramatic speed improvements (e.g.
50X), potentially at the expense of RAM.

Also, only `padding="valid"` is supported by `implementation=1`.
</td>
</tr>
</table>



#### Input shape:

4D tensor with shape:
`(samples, channels, rows, cols)` if data_format='channels_first'
or 4D tensor with shape:
`(samples, rows, cols, channels)` if data_format='channels_last'.



#### Output shape:

4D tensor with shape:
`(samples, filters, new_rows, new_cols)` if data_format='channels_first'
or 4D tensor with shape:
`(samples, new_rows, new_cols, filters)` if data_format='channels_last'.
`rows` and `cols` values might have changed due to padding.


