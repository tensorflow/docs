description: 1D convolution layer (e.g. temporal convolution).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Conv1D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Conv1D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/convolutional.py#L329-L446">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



1D convolution layer (e.g. temporal convolution).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.layers.Convolution1D`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Conv1D`, `tf.compat.v1.keras.layers.Convolution1D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Conv1D(
    filters, kernel_size, strides=1, padding='valid', data_format='channels_last',
    dilation_rate=1, activation=None, use_bias=(True),
    kernel_initializer='glorot_uniform', bias_initializer='zeros',
    kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None,
    kernel_constraint=None, bias_constraint=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer creates a convolution kernel that is convolved
with the layer input over a single spatial (or temporal) dimension
to produce a tensor of outputs.
If `use_bias` is True, a bias vector is created and added to the outputs.
Finally, if `activation` is not `None`,
it is applied to the outputs as well.

When using this layer as the first layer in a model,
provide an `input_shape` argument
(tuple of integers or `None`, e.g.
`(10, 128)` for sequences of 10 vectors of 128-dimensional vectors,
or `(None, 128)` for variable-length sequences of 128-dimensional vectors.

#### Examples:



```
>>> # The inputs are 128-length vectors with 10 timesteps, and the batch size
>>> # is 4.
>>> input_shape = (4, 10, 128)
>>> x = tf.random.normal(input_shape)
>>> y = tf.keras.layers.Conv1D(
... 32, 3, activation='relu',input_shape=input_shape)(x)
>>> print(y.shape)
(4, 8, 32)
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
An integer or tuple/list of a single integer,
specifying the length of the 1D convolution window.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of a single integer,
specifying the stride length of the convolution.
Specifying any stride value != 1 is incompatible with specifying
any `dilation_rate` value != 1.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
One of `"valid"`, `"causal"` or `"same"` (case-insensitive).
`"causal"` results in causal (dilated) convolutions, e.g. `output[t]`
does not depend on `input[t+1:]`. Useful when modeling temporal data
where the model should not violate the temporal order.
See [WaveNet: A Generative Model for Raw Audio, section
2.1](https://arxiv.org/abs/1609.03499).
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string,
one of `channels_last` (default) or `channels_first`.
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
an integer or tuple/list of a single integer, specifying
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
`kernel_initializer`
</td>
<td>
Initializer for the `kernel` weights matrix (
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
`kernel_regularizer`
</td>
<td>
Regularizer function applied to
the `kernel` weights matrix (see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
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

3D tensor with shape: `(batch_size, steps, input_dim)`



#### Output shape:

3D tensor with shape: `(batch_size, new_steps, filters)`
  `steps` value might have changed due to padding or strides.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of rank 3 representing
`activation(conv1d(inputs, kernel) + bias)`.
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



