description: Retrieves CudnnRNN params in canonical form. It supports the projection in LSTM.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CudnnRNNParamsToCanonicalV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CudnnRNNParamsToCanonicalV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Retrieves CudnnRNN params in canonical form. It supports the projection in LSTM.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CudnnRNNParamsToCanonicalV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CudnnRNNParamsToCanonicalV2(
    num_layers, num_units, input_size, params, num_params_weights,
    num_params_biases, rnn_mode='lstm', input_mode='linear_input',
    direction='unidirectional', dropout=0, seed=0, seed2=0, num_proj=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Retrieves a set of weights from the opaque params buffer that can be saved and
restored in a way compatible with future runs.

Note that the params buffer may not be compatible across different GPUs. So any
save and restoration should be converted to and from the canonical weights and
biases.

num_layers: Specifies the number of layers in the RNN model.
num_units: Specifies the size of the hidden state.
input_size: Specifies the size of the input state.
num_params_weights: number of weight parameter matrix for all layers.
num_params_biases: number of bias parameter vector for all layers.
weights: the canonical form of weights that can be used for saving
    and restoration. They are more likely to be compatible across different
    generations.
biases: the canonical form of biases that can be used for saving
    and restoration. They are more likely to be compatible across different
    generations.
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
num_proj: The output dimensionality for the projection matrices. If None or 0,
    no projection is performed.

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
`params`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`num_params_weights`
</td>
<td>
An `int` that is `>= 1`.
</td>
</tr><tr>
<td>
`num_params_biases`
</td>
<td>
An `int` that is `>= 1`.
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
A tuple of `Tensor` objects (weights, biases).
</td>
</tr>
<tr>
<td>
`weights`
</td>
<td>
A list of `num_params_weights` `Tensor` objects with the same type as `params`.
</td>
</tr><tr>
<td>
`biases`
</td>
<td>
A list of `num_params_biases` `Tensor` objects with the same type as `params`.
</td>
</tr>
</table>

