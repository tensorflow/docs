

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.MultiRNNCell

### `class tf.contrib.rnn.MultiRNNCell`
### `class tf.contrib.rnn.core_rnn_cell.MultiRNNCell`



Defined in [`tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

RNN cell composed sequentially of multiple simple cells.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    cells,
    state_is_tuple=True
)
```

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

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Run this multi-layer cell on inputs, starting from state.

<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```





