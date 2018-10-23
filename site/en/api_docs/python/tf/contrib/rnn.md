

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.rnn



Defined in [`tensorflow/contrib/rnn/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/rnn/__init__.py).

RNN Cells and additional RNN operations.

See <a href="../../../../api_guides/python/contrib.rnn">RNN and Cells (contrib)</a> guide.

<!--From core-->

<!--Used to be in core, but kept in contrib.-->

<!--Created in contrib, eventual plans to move to core.-->

<!--RNNCell wrappers-->

<!--RNN functions-->

## Classes

[`class AttentionCellWrapper`](../../tf/contrib/rnn/AttentionCellWrapper): Basic attention cell wrapper.

[`class BasicLSTMCell`](../../tf/contrib/rnn/BasicLSTMCell): Basic LSTM recurrent network cell.

[`class BasicRNNCell`](../../tf/contrib/rnn/BasicRNNCell): The most basic RNN cell.

[`class BidirectionalGridLSTMCell`](../../tf/contrib/rnn/BidirectionalGridLSTMCell): Bidirectional GridLstm cell.

[`class CompiledWrapper`](../../tf/contrib/rnn/CompiledWrapper): Wraps step execution in an XLA JIT scope.

[`class Conv1DLSTMCell`](../../tf/contrib/rnn/Conv1DLSTMCell): 1D Convolutional LSTM recurrent network cell.

[`class Conv2DLSTMCell`](../../tf/contrib/rnn/Conv2DLSTMCell): 2D Convolutional LSTM recurrent network cell.

[`class Conv3DLSTMCell`](../../tf/contrib/rnn/Conv3DLSTMCell): 3D Convolutional LSTM recurrent network cell.

[`class ConvLSTMCell`](../../tf/contrib/rnn/ConvLSTMCell): Convolutional LSTM recurrent network cell.

[`class CoupledInputForgetGateLSTMCell`](../../tf/contrib/rnn/CoupledInputForgetGateLSTMCell): Long short-term memory unit (LSTM) recurrent network cell.

[`class DeviceWrapper`](../../tf/contrib/rnn/DeviceWrapper): Operator that ensures an RNNCell runs on a particular device.

[`class DropoutWrapper`](../../tf/contrib/rnn/DropoutWrapper): Operator adding dropout to inputs and outputs of the given cell.

[`class EmbeddingWrapper`](../../tf/contrib/rnn/EmbeddingWrapper): Operator adding input embedding to the given cell.

[`class FusedRNNCell`](../../tf/contrib/rnn/FusedRNNCell): Abstract object representing a fused RNN cell.

[`class FusedRNNCellAdaptor`](../../tf/contrib/rnn/FusedRNNCellAdaptor): This is an adaptor for RNNCell classes to be used with `FusedRNNCell`.

[`class GLSTMCell`](../../tf/contrib/rnn/GLSTMCell): Group LSTM cell (G-LSTM).

[`class GRUBlockCell`](../../tf/contrib/rnn/GRUBlockCell): Block GRU cell implementation.

[`class GRUBlockCellV2`](../../tf/contrib/rnn/GRUBlockCellV2): Temporary GRUBlockCell impl with a different variable naming scheme.

[`class GRUCell`](../../tf/contrib/rnn/GRUCell): Gated Recurrent Unit cell (cf. http://arxiv.org/abs/1406.1078).

[`class GridLSTMCell`](../../tf/contrib/rnn/GridLSTMCell): Grid Long short-term memory unit (LSTM) recurrent network cell.

[`class HighwayWrapper`](../../tf/contrib/rnn/HighwayWrapper): RNNCell wrapper that adds highway connection on cell input and output.

[`class InputProjectionWrapper`](../../tf/contrib/rnn/InputProjectionWrapper): Operator adding an input projection to the given cell.

[`class IntersectionRNNCell`](../../tf/contrib/rnn/IntersectionRNNCell): Intersection Recurrent Neural Network (+RNN) cell.

[`class LSTMBlockCell`](../../tf/contrib/rnn/LSTMBlockCell): Basic LSTM recurrent network cell.

[`class LSTMBlockFusedCell`](../../tf/contrib/rnn/LSTMBlockFusedCell): FusedRNNCell implementation of LSTM.

[`class LSTMBlockWrapper`](../../tf/contrib/rnn/LSTMBlockWrapper): This is a helper class that provides housekeeping for LSTM cells.

[`class LSTMCell`](../../tf/contrib/rnn/LSTMCell): Long short-term memory unit (LSTM) recurrent network cell.

[`class LSTMStateTuple`](../../tf/contrib/rnn/LSTMStateTuple): Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.

[`class LayerNormBasicLSTMCell`](../../tf/contrib/rnn/LayerNormBasicLSTMCell): LSTM unit with layer normalization and recurrent dropout.

[`class MultiRNNCell`](../../tf/contrib/rnn/MultiRNNCell): RNN cell composed sequentially of multiple simple cells.

[`class NASCell`](../../tf/contrib/rnn/NASCell): Neural Architecture Search (NAS) recurrent network cell.

[`class OutputProjectionWrapper`](../../tf/contrib/rnn/OutputProjectionWrapper): Operator adding an output projection to the given cell.

[`class PhasedLSTMCell`](../../tf/contrib/rnn/PhasedLSTMCell): Phased LSTM recurrent network cell.

[`class RNNCell`](../../tf/contrib/rnn/RNNCell): Abstract object representing an RNN cell.

[`class ResidualWrapper`](../../tf/contrib/rnn/ResidualWrapper): RNNCell wrapper that ensures cell inputs are added to the outputs.

[`class TimeFreqLSTMCell`](../../tf/contrib/rnn/TimeFreqLSTMCell): Time-Frequency Long short-term memory unit (LSTM) recurrent network cell.

[`class TimeReversedFusedRNN`](../../tf/contrib/rnn/TimeReversedFusedRNN): This is an adaptor to time-reverse a FusedRNNCell.

[`class UGRNNCell`](../../tf/contrib/rnn/UGRNNCell): Update Gate Recurrent Neural Network (UGRNN) cell.

## Functions

[`stack_bidirectional_dynamic_rnn(...)`](../../tf/contrib/rnn/stack_bidirectional_dynamic_rnn): Creates a dynamic bidirectional recurrent neural network.

[`stack_bidirectional_rnn(...)`](../../tf/contrib/rnn/stack_bidirectional_rnn): Creates a bidirectional recurrent neural network.

[`static_bidirectional_rnn(...)`](../../tf/nn/static_bidirectional_rnn): Creates a bidirectional recurrent neural network.

[`static_rnn(...)`](../../tf/nn/static_rnn): Creates a recurrent neural network specified by RNNCell `cell`.

[`static_state_saving_rnn(...)`](../../tf/nn/static_state_saving_rnn): RNN that accepts a state saver for time-truncated RNN calculation.

