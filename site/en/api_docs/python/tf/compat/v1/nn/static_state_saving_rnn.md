description: RNN that accepts a state saver for time-truncated RNN calculation. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.static_state_saving_rnn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.static_state_saving_rnn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/rnn.py#L1420-L1512">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



RNN that accepts a state saver for time-truncated RNN calculation. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.static_state_saving_rnn(
    cell, inputs, state_saver, state_name, sequence_length=None, scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use `keras.layers.RNN(cell, stateful=True)`, which is equivalent to this API

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cell`
</td>
<td>
An instance of `RNNCell`.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A length T list of inputs, each a `Tensor` of shape `[batch_size,
input_size]`.
</td>
</tr><tr>
<td>
`state_saver`
</td>
<td>
A state saver object with methods `state` and `save_state`.
</td>
</tr><tr>
<td>
`state_name`
</td>
<td>
Python string or tuple of strings.  The name to use with the
state_saver. If the cell returns tuples of states (i.e., `cell.state_size`
is a tuple) then `state_name` should be a tuple of strings having the same
length as `cell.state_size`.  Otherwise it should be a single string.
</td>
</tr><tr>
<td>
`sequence_length`
</td>
<td>
(optional) An int32/int64 vector size [batch_size]. See the
documentation for rnn() for more details about sequence_length.
</td>
</tr><tr>
<td>
`scope`
</td>
<td>
VariableScope for the created subgraph; defaults to "rnn".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A pair (outputs, state) where:
outputs is a length T list of outputs (one for each input)
states is the final state
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `cell` is not an instance of RNNCell.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `inputs` is `None` or an empty list, or if the arity and
type of `state_name` does not match that of `cell.state_size`.
</td>
</tr>
</table>

