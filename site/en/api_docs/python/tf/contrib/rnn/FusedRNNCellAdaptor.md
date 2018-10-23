


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.FusedRNNCellAdaptor

### `class tf.contrib.rnn.FusedRNNCellAdaptor`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

This is an adaptor for RNNCell classes to be used with `FusedRNNCell`.

## Methods

<h3 id="__init__"><code>__init__(cell, use_dynamic_rnn=False)</code></h3>

Initialize the adaptor.

#### Args:

* <b>`cell`</b>: an instance of a subclass of a `rnn_cell.RNNCell`.
* <b>`use_dynamic_rnn`</b>: whether to use dynamic (or static) RNN.





Defined in [`tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py).

