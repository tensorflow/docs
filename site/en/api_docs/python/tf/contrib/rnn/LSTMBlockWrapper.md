


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.LSTMBlockWrapper

### `class tf.contrib.rnn.LSTMBlockWrapper`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

This is a helper class that provides housekeeping for LSTM cells.

This may be useful for alternative LSTM and similar type of cells.
The subclasses must implement `_call_cell` method and `num_units` property.

## Properties

<h3 id="num_units"><code>num_units</code></h3>

Number of units in this cell (output dimension).



## Class Members

<h3 id="__init__"><code>__init__</code></h3>



Defined in [`tensorflow/contrib/rnn/python/ops/lstm_ops.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/lstm_ops.py).

