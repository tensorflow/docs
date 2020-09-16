description: Backprop step of CudnnRNN.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CudnnRNNBackprop" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CudnnRNNBackprop

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Backprop step of CudnnRNN.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CudnnRNNBackprop`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CudnnRNNBackprop(
    input, input_h, input_c, params, output, output_h, output_c, output_backprop,
    output_h_backprop, output_c_backprop, reserve_space, rnn_mode='lstm',
    input_mode='linear_input', direction='unidirectional', dropout=0, seed=0,
    seed2=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Compute the backprop of both data and weights in a RNN.

rnn_mode: Indicates the type of the RNN model.
input_mode: Indicate whether there is a linear projection between the input and
    the actual computation before the first layer. 'skip_input' is only allowed
    when input_size == num_units; 'auto_select' implies 'skip_input' when
    input_size == num_units; otherwise, it implies 'linear_input'.
direction: Indicates whether a bidirectional model will be used. Should be
  "unidirectional" or "bidirectional".
dropout: Dropout probability. When set to 0., dropout is disabled.
seed: The 1st part of a seed to initialize dropout.
seed2: The 2nd part of a seed to initialize dropout.
input: A 3-D tensor with the shape of [seq_length, batch_size, input_size].
input_h: A 3-D tensor with the shape of [num_layer * dir, batch_size,
    num_units].
input_c: For LSTM, a 3-D tensor with the shape of
    [num_layer * dir, batch, num_units]. For other models, it is ignored.
params: A 1-D tensor that contains the weights and biases in an opaque layout.
    The size must be created through CudnnRNNParamsSize, and initialized
    separately. Note that they might not be compatible across different
    generations. So it is a good idea to save and restore
output: A 3-D tensor with the shape of [seq_length, batch_size,
    dir * num_units].
output_h: The same shape has input_h.
output_c: The same shape as input_c for LSTM. An empty tensor for other models.
output_backprop: A 3-D tensor with the same shape as output in the forward pass.
output_h_backprop: A 3-D tensor with the same shape as output_h in the forward
    pass.
output_c_backprop: A 3-D tensor with the same shape as output_c in the forward
    pass.
reserve_space: The same reserve_space produced in for forward operation.
input_backprop: The backprop to input in the forward pass. Has the same shape
    as input.
input_h_backprop: The backprop to input_h in the forward pass. Has the same
    shape as input_h.
input_c_backprop: The backprop to input_c in the forward pass. Has the same
    shape as input_c.
params_backprop: The backprop to the params buffer in the forward pass. Has the
    same shape as params.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`input_h`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`input_c`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`params`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`output`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`output_h`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`output_c`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`output_backprop`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`output_h_backprop`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`output_c_backprop`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`reserve_space`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`rnn_mode`
</td>
<td>
An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
</td>
</tr><tr>
<td>
`input_mode`
</td>
<td>
An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
</td>
</tr><tr>
<td>
`direction`
</td>
<td>
An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
</td>
</tr><tr>
<td>
`dropout`
</td>
<td>
An optional `float`. Defaults to `0`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`seed2`
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple of `Tensor` objects (input_backprop, input_h_backprop, input_c_backprop, params_backprop).
</td>
</tr>
<tr>
<td>
`input_backprop`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`input_h_backprop`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`input_c_backprop`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`params_backprop`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr>
</table>

