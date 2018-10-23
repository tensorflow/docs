


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.OutputProjectionWrapper

### `class tf.contrib.rnn.OutputProjectionWrapper`
### `class tf.contrib.rnn.core_rnn_cell.OutputProjectionWrapper`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Operator adding an output projection to the given cell.

Note: in many cases it may be more efficient to not use this wrapper,
but instead concatenate the whole sequence of your outputs in time,
do the projection on this batch-concatenated sequence, then split it
if needed or directly feed into a softmax.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__(cell, output_size)</code></h3>

Create a cell with output projection.

#### Args:

* <b>`cell`</b>: an RNNCell, a projection to output_size is added to it.
* <b>`output_size`</b>: integer, the size of the output after projection.


#### Raises:

* <b>`TypeError`</b>: if cell is not an RNNCell.
* <b>`ValueError`</b>: if output_size is not positive.

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





Defined in [`tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py).

