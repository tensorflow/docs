


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.LSTMStateTuple

### `class tf.contrib.rnn.LSTMStateTuple`
### `class tf.contrib.rnn.core_rnn_cell.LSTMStateTuple`

See the guide: [RNN and Cells (contrib) > Classes storing split `RNNCell` state](../../../../../api_guides/python/contrib.rnn#Classes_storing_split_RNNCell_state)

Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.

Stores two elements: `(c, h)`, in that order.

Only used when `state_is_tuple=True`.

## Properties

<h3 id="c"><code>c</code></h3>

Alias for field number 0

<h3 id="dtype"><code>dtype</code></h3>



<h3 id="h"><code>h</code></h3>

Alias for field number 1



## Class Members

<h3 id="__init__"><code>__init__</code></h3>

<h3 id="count"><code>count</code></h3>

<h3 id="index"><code>index</code></h3>



Defined in [`tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py).

