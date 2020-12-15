description: A RNN backed by cuDNN.

robots: noindex

# tf.raw_ops.CudnnRNNV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A RNN backed by cuDNN.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CudnnRNNV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CudnnRNNV2(
    input, input_h, input_c, params, rnn_mode='lstm', input_mode='linear_input',
    direction='unidirectional', dropout=0, seed=0, seed2=0, is_training=(True),
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the RNN from the input and initial states, with respect to the params
buffer. Produces one extra output "host_reserved" than CudnnRNN.

rnn_mode: Indicates the type of the RNN model.
input_mode: Indicates whether there is a linear projection between the input and
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
is_training: Indicates whether this operation is used for inference or
  training.
reserve_space: An opaque tensor that can be used in backprop calculation. It
  is only produced if is_training is true.
host_reserved: An opaque tensor that can be used in backprop calculation. It is
  only produced if is_training is true. It is output on host memory rather than
  device memory.

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
`is_training`
</td>
<td>
An optional `bool`. Defaults to `True`.
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
A tuple of `Tensor` objects (output, output_h, output_c, reserve_space, host_reserved).
</td>
</tr>
<tr>
<td>
`output`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`output_h`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`output_c`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`reserve_space`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`host_reserved`
</td>
<td>
A `Tensor` of type `int8`.
</td>
</tr>
</table>

