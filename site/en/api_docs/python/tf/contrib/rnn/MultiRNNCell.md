


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.MultiRNNCell

### `class tf.contrib.rnn.MultiRNNCell`
### `class tf.contrib.rnn.core_rnn_cell.MultiRNNCell`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

RNN cell composed sequentially of multiple simple cells.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__(cells, state_is_tuple=True)</code></h3>

Create a RNN cell composed sequentially of a number of RNNCells.

#### Args:

* <b>`cells`</b>: list of RNNCells that will be composed in this order.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are n-tuples, where
    `n = len(cells)`.  If False, the states are all
    concatenated along the column axis.  This latter behavior will soon be
    deprecated.


#### Raises:

* <b>`ValueError`</b>: if cells is empty (not allowed), or at least one of the cells
    returns a state tuple but the flag `state_is_tuple` is `False`.

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

