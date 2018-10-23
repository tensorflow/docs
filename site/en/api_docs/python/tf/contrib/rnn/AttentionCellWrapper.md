

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.AttentionCellWrapper

### `class tf.contrib.rnn.AttentionCellWrapper`



Defined in [`tensorflow/contrib/rnn/python/ops/rnn_cell.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Basic attention cell wrapper.

Implementation based on https://arxiv.org/abs/1409.0473.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    cell,
    attn_length,
    attn_size=None,
    attn_vec_size=None,
    input_size=None,
    state_is_tuple=False,
    reuse=None
)
```

Create a cell with attention.

#### Args:

* <b>`cell`</b>: an RNNCell, an attention is added to it.
* <b>`attn_length`</b>: integer, the size of an attention window.
* <b>`attn_size`</b>: integer, the size of an attention vector. Equal to
      cell.output_size by default.
* <b>`attn_vec_size`</b>: integer, the number of convolutional features calculated
      on attention state and a size of the hidden layer built from
      base cell state. Equal attn_size to by default.
* <b>`input_size`</b>: integer, the size of a hidden linear layer,
      built from inputs and attention. Derived from the input tensor
      by default.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are n-tuples, where
    `n = len(cells)`.  By default (False), the states are all
    concatenated along the column axis.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
    in an existing scope.  If not `True`, and the existing scope already has
    the given variables, an error is raised.


#### Raises:

* <b>`TypeError`</b>: if cell is not an RNNCell.
* <b>`ValueError`</b>: if cell returns a state tuple but the flag
      `state_is_tuple` is `False` or if attn_length is zero or less.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Long short-term memory cell with attention (LSTMA).

<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```

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



