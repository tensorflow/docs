


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.FusedRNNCell

### `class tf.contrib.rnn.FusedRNNCell`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Abstract object representing a fused RNN cell.

A fused RNN cell represents the entire RNN expanded over the time
dimension. In effect, this represents an entire recurrent network.

Unlike RNN cells which are subclasses of `rnn_cell.RNNCell`, a `FusedRNNCell`
operates on the entire time sequence at once, by putting the loop over time
inside the cell. This usually leads to much more efficient, but more complex
and less flexible implementations.

Every `FusedRNNCell` must implement `__call__` with the following signature.

## Class Members

<h3 id="__init__"><code>__init__</code></h3>



Defined in [`tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py).

