


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.RNNCell

### `class tf.contrib.rnn.RNNCell`
### `class tf.contrib.rnn.core_rnn_cell.RNNCell`

See the guide: [RNN and Cells (contrib) > Base interface for all RNN Cells](../../../../../api_guides/python/contrib.rnn#Base_interface_for_all_RNN_Cells)

Abstract object representing an RNN cell.

The definition of cell in this package differs from the definition used in the
literature. In the literature, cell refers to an object with a single scalar
output. The definition in this package refers to a horizontal array of such
units.

An RNN cell, in the most abstract setting, is anything that has
a state and performs some operation that takes a matrix of inputs.
This operation results in an output matrix with `self.output_size` columns.
If `self.state_size` is an integer, this operation also results in a new
state matrix with `self.state_size` columns.  If `self.state_size` is a
tuple of integers, then it results in a tuple of `len(state_size)` state
matrices, each with a column size corresponding to values in `state_size`.

This module provides a number of basic commonly used RNN cells, such as
LSTM (Long Short Term Memory) or GRU (Gated Recurrent Unit), and a number
of operators that allow add dropouts, projections, or embeddings for inputs.
Constructing multi-layer cells is supported by the class `MultiRNNCell`,
or by calling the `rnn` ops several times. Every `RNNCell` must have the
properties below and implement `__call__` with the following signature.

## Properties

<h3 id="output_size"><code>output_size</code></h3>

Integer or TensorShape: size of outputs produced by this cell.

<h3 id="state_size"><code>state_size</code></h3>

size(s) of state(s) used by this cell.

It can be represented by an Integer, a TensorShape or a tuple of Integers
or TensorShapes.



## Methods

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



## Class Members

<h3 id="__init__"><code>__init__</code></h3>



Defined in [`tensorflow/python/ops/rnn_cell_impl.py`](https://www.tensorflow.org/code/tensorflow/python/ops/rnn_cell_impl.py).

