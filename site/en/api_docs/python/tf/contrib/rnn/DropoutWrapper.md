

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.DropoutWrapper

### `class tf.contrib.rnn.DropoutWrapper`
### `class tf.contrib.rnn.core_rnn_cell.DropoutWrapper`



Defined in [`tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Operator adding dropout to inputs and outputs of the given cell.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    cell,
    input_keep_prob=1.0,
    output_keep_prob=1.0,
    state_keep_prob=1.0,
    variational_recurrent=False,
    input_size=None,
    dtype=None,
    seed=None
)
```

Create a cell with added input, state, and/or output dropout.

If `variational_recurrent` is set to `True` (**NOT** the default behavior),
then the the same dropout mask is applied at every step, as described in:

Y. Gal, Z Ghahramani.  "A Theoretically Grounded Application of Dropout in
Recurrent Neural Networks".  https://arxiv.org/abs/1512.05287

Otherwise a different dropout mask is applied at every time step.

#### Args:

* <b>`cell`</b>: an RNNCell, a projection to output_size is added to it.
* <b>`input_keep_prob`</b>: unit Tensor or float between 0 and 1, input keep
    probability; if it is constant and 1, no input dropout will be added.
* <b>`output_keep_prob`</b>: unit Tensor or float between 0 and 1, output keep
    probability; if it is constant and 1, no output dropout will be added.
* <b>`state_keep_prob`</b>: unit Tensor or float between 0 and 1, output keep
    probability; if it is constant and 1, no output dropout will be added.
    State dropout is performed on the *output* states of the cell.
* <b>`variational_recurrent`</b>: Python bool.  If `True`, then the same
    dropout pattern is applied across all time steps per run call.
    If this parameter is set, `input_size` **must** be provided.
* <b>`input_size`</b>: (optional) (possibly nested tuple of) `TensorShape` objects
    containing the depth(s) of the input tensors expected to be passed in to
    the `DropoutWrapper`.  Required and used **iff**
     `variational_recurrent = True` and `input_keep_prob < 1`.
* <b>`dtype`</b>: (optional) The `dtype` of the input, state, and output tensors.
    Required and used **iff** `variational_recurrent = True`.
* <b>`seed`</b>: (optional) integer, the randomness seed.


#### Raises:

* <b>`TypeError`</b>: if cell is not an RNNCell.
* <b>`ValueError`</b>: if any of the keep_probs are not between 0 and 1.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Run the cell with the declared dropouts.

<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```





