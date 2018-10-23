

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.InputProjectionWrapper

### `class tf.contrib.rnn.InputProjectionWrapper`
### `class tf.contrib.rnn.core_rnn_cell.InputProjectionWrapper`



Defined in [`tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Operator adding an input projection to the given cell.

Note: in many cases it may be more efficient to not use this wrapper,
but instead concatenate the whole sequence of your inputs in time,
do the projection on this batch-concatenated sequence, then split it.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    cell,
    num_proj,
    input_size=None
)
```

Create a cell with input projection.

#### Args:

* <b>`cell`</b>: an RNNCell, a projection of inputs is added before it.
* <b>`num_proj`</b>: Python integer.  The dimension to project to.
* <b>`input_size`</b>: Deprecated and unused.


#### Raises:

* <b>`TypeError`</b>: if cell is not an RNNCell.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Run the input projection and then the cell.

<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```





