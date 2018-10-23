


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.LSTMBlockFusedCell

### `class tf.contrib.rnn.LSTMBlockFusedCell`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

FusedRNNCell implementation of LSTM.

This is an extremely efficient LSTM implementation, that uses a single TF op
for the entire LSTM. It should be both faster and more memory-efficient than
LSTMBlockCell defined above.

The implementation is based on: http://arxiv.org/abs/1409.2329.

We add forget_bias (default: 1) to the biases of the forget gate in order to
reduce the scale of forgetting in the beginning of the training.

The variable naming is consistent with `core_rnn_cell.LSTMCell`.

## Properties

<h3 id="num_units"><code>num_units</code></h3>

Number of units in this cell (output dimension).



## Methods

<h3 id="__init__"><code>__init__(num_units, forget_bias=1.0, cell_clip=None, use_peephole=False)</code></h3>

Initialize the LSTM cell.

#### Args:

* <b>`num_units`</b>: int, The number of units in the LSTM cell.
* <b>`forget_bias`</b>: float, The bias added to forget gates (see above).
* <b>`cell_clip`</b>: clip the cell to this value. Defaults to `3`.
* <b>`use_peephole`</b>: Whether to use peephole connections or not.





Defined in [`tensorflow/contrib/rnn/python/ops/lstm_ops.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/lstm_ops.py).

