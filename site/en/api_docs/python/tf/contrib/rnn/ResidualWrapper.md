

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.ResidualWrapper

### `class tf.contrib.rnn.ResidualWrapper`
### `class tf.contrib.rnn.core_rnn_cell.ResidualWrapper`



Defined in [`tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

RNNCell wrapper that ensures cell inputs are added to the outputs.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(cell)
```

Constructs a `ResidualWrapper` for `cell`.

#### Args:

* <b>`cell`</b>: An instance of `RNNCell`.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Run the cell and add its inputs to its outputs.

#### Args:

* <b>`inputs`</b>: cell inputs.
* <b>`state`</b>: cell state.
* <b>`scope`</b>: optional cell scope.


#### Returns:

  Tuple of cell outputs and new state.


#### Raises:

* <b>`TypeError`</b>: If cell inputs and outputs have different structure (type).
* <b>`ValueError`</b>: If cell inputs and outputs have different structure (value).

<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```





