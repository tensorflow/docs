page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.nn.rnn_cell


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/v1/nn/rnn_cell">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Module for constructing RNN Cells.

<!-- Placeholder for "Used in" -->


## Classes

[`class BasicLSTMCell`](../../../../tf/nn/rnn_cell/BasicLSTMCell): DEPRECATED: Please use <a href="../../../../tf/nn/rnn_cell/LSTMCell"><code>tf.compat.v1.nn.rnn_cell.LSTMCell</code></a> instead.

[`class BasicRNNCell`](../../../../tf/nn/rnn_cell/BasicRNNCell): The most basic RNN cell.

[`class DeviceWrapper`](../../../../tf/nn/rnn_cell/DeviceWrapper): Operator that ensures an RNNCell runs on a particular device.

[`class DropoutWrapper`](../../../../tf/nn/rnn_cell/DropoutWrapper): Operator adding dropout to inputs and outputs of the given cell.

[`class GRUCell`](../../../../tf/nn/rnn_cell/GRUCell): Gated Recurrent Unit cell (cf.

[`class LSTMCell`](../../../../tf/nn/rnn_cell/LSTMCell): Long short-term memory unit (LSTM) recurrent network cell.

[`class LSTMStateTuple`](../../../../tf/nn/rnn_cell/LSTMStateTuple): Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.

[`class MultiRNNCell`](../../../../tf/nn/rnn_cell/MultiRNNCell): RNN cell composed sequentially of multiple simple cells.

[`class RNNCell`](../../../../tf/nn/rnn_cell/RNNCell): Abstract object representing an RNN cell.

[`class ResidualWrapper`](../../../../tf/nn/rnn_cell/ResidualWrapper): RNNCell wrapper that ensures cell inputs are added to the outputs.
