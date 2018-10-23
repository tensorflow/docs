


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.LSTMBlockCell

### `class tf.contrib.rnn.LSTMBlockCell`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Basic LSTM recurrent network cell.

The implementation is based on: http://arxiv.org/abs/1409.2329.

We add `forget_bias` (default: 1) to the biases of the forget gate in order to
reduce the scale of forgetting in the beginning of the training.

Unlike `core_rnn_cell.LSTMCell`, this is a monolithic op and should be much
faster.  The weight and bias matrixes should be compatible as long as the
variable scope matches.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__(num_units, forget_bias=1.0, use_peephole=False)</code></h3>

Initialize the basic LSTM cell.

#### Args:

* <b>`num_units`</b>: int, The number of units in the LSTM cell.
* <b>`forget_bias`</b>: float, The bias added to forget gates (see above).
* <b>`use_peephole`</b>: Whether to use peephole connections or not.

<h3 id="zero_state"><code>zero_state(batch_size, dtype)</code></h3>

Return zero-filled state tensor(s).

#### Args:

* <b>`batch_size`</b>: int, float, or unit Tensor representing the batch size.
* <b>`dtype`</b>: the data type to use for the state.


#### Returns:

  If `state_size` is an int or TensorShape, then the return value is a
  `N-D` tensor of shape `[batch_size x state_size]` filled with zeros.

  If `state_size` is a nested list or tuple, then the return value is
  a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size x s]` for each s in `state_size`.





Defined in [`tensorflow/contrib/rnn/python/ops/lstm_ops.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/lstm_ops.py).

