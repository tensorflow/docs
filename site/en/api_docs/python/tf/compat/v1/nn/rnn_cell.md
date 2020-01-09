page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.nn.rnn_cell


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Module for constructing RNN Cells.

<!-- Placeholder for "Used in" -->


## Classes

[`class BasicLSTMCell`](../../../../tf/compat/v1/nn/rnn_cell/BasicLSTMCell): DEPRECATED: Please use <a href="../../../../tf/compat/v1/nn/rnn_cell/LSTMCell"><code>tf.compat.v1.nn.rnn_cell.LSTMCell</code></a> instead.

[`class BasicRNNCell`](../../../../tf/compat/v1/nn/rnn_cell/BasicRNNCell): The most basic RNN cell.

[`class DeviceWrapper`](../../../../tf/compat/v1/nn/rnn_cell/DeviceWrapper): Operator that ensures an RNNCell runs on a particular device.

[`class DropoutWrapper`](../../../../tf/compat/v1/nn/rnn_cell/DropoutWrapper): Operator adding dropout to inputs and outputs of the given cell.

[`class GRUCell`](../../../../tf/compat/v1/nn/rnn_cell/GRUCell): Gated Recurrent Unit cell (cf.

[`class LSTMCell`](../../../../tf/compat/v1/nn/rnn_cell/LSTMCell): Long short-term memory unit (LSTM) recurrent network cell.

[`class LSTMStateTuple`](../../../../tf/compat/v1/nn/rnn_cell/LSTMStateTuple): Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.

[`class MultiRNNCell`](../../../../tf/compat/v1/nn/rnn_cell/MultiRNNCell): RNN cell composed sequentially of multiple simple cells.

[`class RNNCell`](../../../../tf/compat/v1/nn/rnn_cell/RNNCell): Abstract object representing an RNN cell.

[`class ResidualWrapper`](../../../../tf/compat/v1/nn/rnn_cell/ResidualWrapper): RNNCell wrapper that ensures cell inputs are added to the outputs.
