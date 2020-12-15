description: Convolutional LSTM.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.ConvLSTM2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
</div>

# tf.keras.layers.ConvLSTM2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/convolutional_recurrent.py#L697-L1008">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Convolutional LSTM.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.ConvLSTM2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.ConvLSTM2D(
    filters, kernel_size, strides=(1, 1), padding='valid', data_format=None,
    dilation_rate=(1, 1), activation='tanh', recurrent_activation='hard_sigmoid',
    use_bias=(True), kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal', bias_initializer='zeros',
    unit_forget_bias=(True), kernel_regularizer=None, recurrent_regularizer=None,
    bias_regularizer=None, activity_regularizer=None, kernel_constraint=None,
    recurrent_constraint=None, bias_constraint=None, return_sequences=(False),
    return_state=(False), go_backwards=(False), stateful=(False), dropout=0.0,
    recurrent_dropout=0.0, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

It is similar to an LSTM layer, but the input transformations
and recurrent transformations are both convolutional.

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
An integer or tuple/list of n integers, specifying the
dimensions of the convolution window.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An integer or tuple/list of n integers,
specifying the strides of the convolution.
Specifying any stride value != 1 is incompatible with specifying
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
A string,
one of `channels_last` (default) or `channels_first`.
The ordering of the dimensions in the inputs.
`channels_last` corresponds to inputs with shape
`(batch, time, ..., channels)`
while `channels_first` corresponds to
inputs with shape `(batch, time, channels, ...)`.
It defaults to the `image_data_format` value found in your
Keras config file at `~/.keras/keras.json`.
If you never set it, then it will be "channels_last".
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
An integer or tuple/list of n integers, specifying
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
By default hyperbolic tangent activation function is applied
(`tanh(x)`).
</td>
</tr><tr>
<td>
`recurrent_activation`
</td>
<td>
Activation function to use
for the recurrent step.
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
Initializer for the `kernel` weights matrix,
used for the linear transformation of the inputs.
</td>
</tr><tr>
<td>
`recurrent_initializer`
</td>
<td>
Initializer for the `recurrent_kernel`
weights matrix,
used for the linear transformation of the recurrent state.
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
`unit_forget_bias`
</td>
<td>
Boolean.
If True, add 1 to the bias of the forget gate at initialization.
Use in combination with `bias_initializer="zeros"`.
This is recommended in [Jozefowicz et al., 2015](
http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf)
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
`recurrent_regularizer`
</td>
<td>
Regularizer function applied to
the `recurrent_kernel` weights matrix.
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
Regularizer function applied to.
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Constraint function applied to
the `kernel` weights matrix.
</td>
</tr><tr>
<td>
`recurrent_constraint`
</td>
<td>
Constraint function applied to
the `recurrent_kernel` weights matrix.
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
`return_sequences`
</td>
<td>
Boolean. Whether to return the last output
in the output sequence, or the full sequence. (default False)
</td>
</tr><tr>
<td>
`return_state`
</td>
<td>
Boolean Whether to return the last state
in addition to the output. (default False)
</td>
</tr><tr>
<td>
`go_backwards`
</td>
<td>
Boolean (default False).
If True, process the input sequence backwards.
</td>
</tr><tr>
<td>
`stateful`
</td>
<td>
Boolean (default False). If True, the last state
for each sample at index i in a batch will be used as initial
state for the sample of index i in the following batch.
</td>
</tr><tr>
<td>
`dropout`
</td>
<td>
Float between 0 and 1.
Fraction of the units to drop for
the linear transformation of the inputs.
</td>
</tr><tr>
<td>
`recurrent_dropout`
</td>
<td>
Float between 0 and 1.
Fraction of the units to drop for
the linear transformation of the recurrent state.
</td>
</tr>
</table>



#### Call arguments:


* <b>`inputs`</b>: A 5D tensor.
* <b>`mask`</b>: Binary tensor of shape `(samples, timesteps)` indicating whether
  a given timestep should be masked.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. This argument is passed to the cell
  when calling it. This is only relevant if `dropout` or `recurrent_dropout`
  are set.
* <b>`initial_state`</b>: List of initial state tensors to be passed to the first
  call of the cell.


#### Input shape:

- If data_format='channels_first'
    5D tensor with shape:
    `(samples, time, channels, rows, cols)`
- If data_format='channels_last'
    5D tensor with shape:
    `(samples, time, rows, cols, channels)`



#### Output shape:

- If `return_state`: a list of tensors. The first tensor is
  the output. The remaining tensors are the last states,
  each 4D tensor with shape:
  `(samples, filters, new_rows, new_cols)`
  if data_format='channels_first'
  or 4D tensor with shape:
  `(samples, new_rows, new_cols, filters)`
  if data_format='channels_last'.
  `rows` and `cols` values might have changed due to padding.
- If `return_sequences`: 5D tensor with shape:
  `(samples, timesteps, filters, new_rows, new_cols)`
  if data_format='channels_first'
  or 5D tensor with shape:
  `(samples, timesteps, new_rows, new_cols, filters)`
  if data_format='channels_last'.
- Else, 4D tensor with shape:
  `(samples, filters, new_rows, new_cols)`
  if data_format='channels_first'
  or 4D tensor with shape:
  `(samples, new_rows, new_cols, filters)`
  if data_format='channels_last'.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
in case of invalid constructor arguments.
</td>
</tr>
</table>



#### References:

- [Shi et al., 2015](http://arxiv.org/abs/1506.04214v1)
(the current implementation does not include the feedback loop on the
cells output).




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`activation`
</td>
<td>

</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>

</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>

</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>

</td>
</tr><tr>
<td>
`data_format`
</td>
<td>

</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>

</td>
</tr><tr>
<td>
`dropout`
</td>
<td>

</td>
</tr><tr>
<td>
`filters`
</td>
<td>

</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>

</td>
</tr><tr>
<td>
`kernel_initializer`
</td>
<td>

</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>

</td>
</tr><tr>
<td>
`kernel_size`
</td>
<td>

</td>
</tr><tr>
<td>
`padding`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_activation`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_constraint`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_dropout`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_initializer`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_regularizer`
</td>
<td>

</td>
</tr><tr>
<td>
`states`
</td>
<td>

</td>
</tr><tr>
<td>
`strides`
</td>
<td>

</td>
</tr><tr>
<td>
`unit_forget_bias`
</td>
<td>

</td>
</tr><tr>
<td>
`use_bias`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/convolutional_recurrent.py#L353-L421">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states(
    states=None
)
</code></pre>

Reset the recorded states for the stateful RNN layer.

Can only be used when RNN layer is constructed with `stateful` = `True`.
Args:
  states: Numpy arrays that contains the value for the initial state, which
    will be feed to cell at the first time step. When the value is None,
    zero filled numpy array will be created based on the cell state size.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AttributeError`
</td>
<td>
When the RNN layer is not stateful.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
When the batch size of the RNN layer is unknown.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
When the input numpy array is not compatible with the RNN
layer state, either size wise or dtype wise.
</td>
</tr>
</table>





