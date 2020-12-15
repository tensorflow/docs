description: Computes size of weights that can be used by a Cudnn RNN model.

robots: noindex

# tf.raw_ops.CudnnRNNParamsSize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes size of weights that can be used by a Cudnn RNN model.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CudnnRNNParamsSize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CudnnRNNParamsSize(
    num_layers, num_units, input_size, T, S, rnn_mode='lstm',
    input_mode='linear_input', direction='unidirectional', dropout=0, seed=0,
    seed2=0, num_proj=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Return the params size that can be used by the Cudnn RNN model. Subsequent
weight allocation and initialization should use this size.

num_layers: Specifies the number of layers in the RNN model.
num_units: Specifies the size of the hidden state.
input_size: Specifies the size of the input state.
rnn_mode: Indicates the type of the RNN model.
input_mode: Indicate whether there is a linear projection between the input and
  The actual computation before the first layer. 'skip_input' is only allowed
  when input_size == num_units; 'auto_select' implies 'skip_input' when
  input_size == num_units; otherwise, it implies 'linear_input'.
direction: Indicates whether a bidirectional model will be used.
  dir = (direction == bidirectional) ? 2 : 1
dropout: dropout probability. When set to 0., dropout is disabled.
seed: the 1st part of a seed to initialize dropout.
seed2: the 2nd part of a seed to initialize dropout.
params_size: The size of the params buffer that should be allocated and
  initialized for this RNN model. Note that this params buffer may not be
  compatible across GPUs. Please use CudnnRNNParamsWeights and
  CudnnRNNParamsBiases to save and restore them in a way that is compatible
  across different runs.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_layers`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`num_units`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`input_size`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`T`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.half, tf.float32, tf.float64`.
</td>
</tr><tr>
<td>
`S`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`.
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
`num_proj`
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
A `Tensor` of type `S`.
</td>
</tr>

</table>

