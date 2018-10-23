


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.EmbeddingWrapper

### `class tf.contrib.rnn.EmbeddingWrapper`
### `class tf.contrib.rnn.core_rnn_cell.EmbeddingWrapper`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Operator adding input embedding to the given cell.

Note: in many cases it may be more efficient to not use this wrapper,
but instead concatenate the whole sequence of your inputs in time,
do the embedding on this batch-concatenated sequence, then split it and
feed into your RNN.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__(cell, embedding_classes, embedding_size, initializer=None)</code></h3>

Create a cell with an added input embedding.

#### Args:

* <b>`cell`</b>: an RNNCell, an embedding will be put before its inputs.
* <b>`embedding_classes`</b>: integer, how many symbols will be embedded.
* <b>`embedding_size`</b>: integer, the size of the vectors we embed into.
* <b>`initializer`</b>: an initializer to use when creating the embedding;
    if None, the initializer from variable scope or a default one is used.


#### Raises:

* <b>`TypeError`</b>: if cell is not an RNNCell.
* <b>`ValueError`</b>: if embedding_classes is not positive.

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

