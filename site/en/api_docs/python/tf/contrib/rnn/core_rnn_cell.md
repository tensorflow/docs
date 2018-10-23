


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.contrib.rnn.core_rnn_cell

### Module `tf.contrib.rnn.core_rnn_cell`

Module for constructing RNN Cells.

## Base interface for all RNN Cells


## RNN Cells for use with TensorFlow's core RNN methods


## Classes storing split `RNNCell` state


## RNN Cell wrappers (RNNCells that wrap other RNNCells)


## Members

[`class BasicLSTMCell`](../../../tf/contrib/rnn/BasicLSTMCell): Basic LSTM recurrent network cell.

[`class BasicRNNCell`](../../../tf/contrib/rnn/BasicRNNCell): The most basic RNN cell.

[`class DropoutWrapper`](../../../tf/contrib/rnn/DropoutWrapper): Operator adding dropout to inputs and outputs of the given cell.

[`class EmbeddingWrapper`](../../../tf/contrib/rnn/EmbeddingWrapper): Operator adding input embedding to the given cell.

[`class GRUCell`](../../../tf/contrib/rnn/GRUCell): Gated Recurrent Unit cell (cf. http://arxiv.org/abs/1406.1078).

[`class InputProjectionWrapper`](../../../tf/contrib/rnn/InputProjectionWrapper): Operator adding an input projection to the given cell.

[`class LSTMCell`](../../../tf/contrib/rnn/LSTMCell): Long short-term memory unit (LSTM) recurrent network cell.

[`class LSTMStateTuple`](../../../tf/contrib/rnn/LSTMStateTuple): Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.

[`class MultiRNNCell`](../../../tf/contrib/rnn/MultiRNNCell): RNN cell composed sequentially of multiple simple cells.

[`class OutputProjectionWrapper`](../../../tf/contrib/rnn/OutputProjectionWrapper): Operator adding an output projection to the given cell.

[`class RNNCell`](../../../tf/contrib/rnn/RNNCell): Abstract object representing an RNN cell.

Defined in [`tensorflow/contrib/rnn/python/ops/core_rnn_cell.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/core_rnn_cell.py).

