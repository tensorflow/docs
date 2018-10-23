

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.NASCell

### `class tf.contrib.rnn.NASCell`



Defined in [`tensorflow/contrib/rnn/python/ops/rnn_cell.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

Neural Architecture Search (NAS) recurrent network cell.

This implements the recurrent cell from the paper:

  https://arxiv.org/abs/1611.01578

Barret Zoph and Quoc V. Le.
"Neural Architecture Search with Reinforcement Learning" Proc. ICLR 2017.

The class uses an optional projection layer.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    num_units,
    num_proj=None,
    use_biases=False,
    reuse=None
)
```

Initialize the parameters for a NAS cell.

#### Args:

* <b>`num_units`</b>: int, The number of units in the NAS cell
* <b>`num_proj`</b>: (optional) int, The output dimensionality for the projection
    matrices.  If None, no projection is performed.
* <b>`use_biases`</b>: (optional) bool, If True then use biases within the cell. This
    is False by default.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
    in an existing scope.  If not `True`, and the existing scope already has
    the given variables, an error is raised.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Run one step of NAS Cell.

#### Args:

* <b>`inputs`</b>: input Tensor, 2D, batch x num_units.
* <b>`state`</b>: This must be a tuple of state Tensors, both `2-D`, with column
    sizes `c_state` and `m_state`.
* <b>`scope`</b>: VariableScope for the created subgraph; defaults to "nas_rnn".


#### Returns:

  A tuple containing:
  - A `2-D, [batch x output_dim]`, Tensor representing the output of the
    NAS Cell after reading `inputs` when previous state was `state`.
    Here output_dim is:
       num_proj if num_proj was set,
       num_units otherwise.
  - Tensor(s) representing the new state of NAS Cell after reading `inputs`
    when the previous state was `state`.  Same type and shape(s) as `state`.


#### Raises:

* <b>`ValueError`</b>: If input size cannot be inferred from inputs via
    static shape inference.

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



