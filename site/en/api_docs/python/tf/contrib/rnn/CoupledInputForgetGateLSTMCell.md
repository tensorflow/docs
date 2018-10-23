

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.rnn.CoupledInputForgetGateLSTMCell

### `class tf.contrib.rnn.CoupledInputForgetGateLSTMCell`



Defined in [`tensorflow/contrib/rnn/python/ops/rnn_cell.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Long short-term memory unit (LSTM) recurrent network cell.

The default non-peephole implementation is based on:

  http://deeplearning.cs.cmu.edu/pdfs/Hochreiter97_lstm.pdf

S. Hochreiter and J. Schmidhuber.
"Long Short-Term Memory". Neural Computation, 9(8):1735-1780, 1997.

The peephole implementation is based on:

  https://research.google.com/pubs/archive/43905.pdf

Hasim Sak, Andrew Senior, and Francoise Beaufays.
"Long short-term memory recurrent neural network architectures for
 large scale acoustic modeling." INTERSPEECH, 2014.

The coupling of input and forget gate is based on:

  http://arxiv.org/pdf/1503.04069.pdf

Greff et al. "LSTM: A Search Space Odyssey"

The class uses optional peep-hole connections, and an optional projection
layer.

## Properties

<h3 id="graph"><code>graph</code></h3>



<h3 id="losses"><code>losses</code></h3>



<h3 id="non_trainable_variables"><code>non_trainable_variables</code></h3>



<h3 id="non_trainable_weights"><code>non_trainable_weights</code></h3>



<h3 id="output_size"><code>output_size</code></h3>



<h3 id="scope_name"><code>scope_name</code></h3>



<h3 id="state_size"><code>state_size</code></h3>



<h3 id="trainable_variables"><code>trainable_variables</code></h3>



<h3 id="trainable_weights"><code>trainable_weights</code></h3>



<h3 id="updates"><code>updates</code></h3>



<h3 id="variables"><code>variables</code></h3>

Returns the list of all layer variables/weights.

#### Returns:

  A list of variables.

<h3 id="weights"><code>weights</code></h3>

Returns the list of all layer variables/weights.

#### Returns:

  A list of variables.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    num_units,
    use_peepholes=False,
    initializer=None,
    num_proj=None,
    proj_clip=None,
    num_unit_shards=1,
    num_proj_shards=1,
    forget_bias=1.0,
    state_is_tuple=True,
    activation=tf.tanh,
    reuse=None
)
```

Initialize the parameters for an LSTM cell.

#### Args:

* <b>`num_units`</b>: int, The number of units in the LSTM cell
* <b>`use_peepholes`</b>: bool, set True to enable diagonal/peephole connections.
* <b>`initializer`</b>: (optional) The initializer to use for the weight and
    projection matrices.
* <b>`num_proj`</b>: (optional) int, The output dimensionality for the projection
    matrices.  If None, no projection is performed.
* <b>`proj_clip`</b>: (optional) A float value.  If `num_proj > 0` and `proj_clip` is
  provided, then the projected values are clipped elementwise to within
  `[-proj_clip, proj_clip]`.
* <b>`num_unit_shards`</b>: How to split the weight matrix.  If >1, the weight
    matrix is stored across num_unit_shards.
* <b>`num_proj_shards`</b>: How to split the projection matrix.  If >1, the
    projection matrix is stored across num_proj_shards.
* <b>`forget_bias`</b>: Biases of the forget gate are initialized by default to 1
    in order to reduce the scale of forgetting at the beginning of
    the training.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are 2-tuples of
    the `c_state` and `m_state`.  By default (False), they are concatenated
    along the column axis.  This default behavior will soon be deprecated.
* <b>`activation`</b>: Activation function of the inner states.
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

Run this RNN cell on inputs, starting from the given state.

#### Args:

* <b>`inputs`</b>: `2-D` tensor with shape `[batch_size x input_size]`.
* <b>`state`</b>: if `self.state_size` is an integer, this should be a `2-D Tensor`
    with shape `[batch_size x self.state_size]`.  Otherwise, if
    `self.state_size` is a tuple of integers, this should be a tuple
    with shapes `[batch_size x s] for s in self.state_size`.
* <b>`scope`</b>: VariableScope for the created subgraph; defaults to class name.


#### Returns:

  A pair containing:

  - Output: A `2-D` tensor with shape `[batch_size x self.output_size]`.
  - New state: Either a single `2-D` tensor, or a tuple of tensors matching
    the arity and shapes of `state`.

<h3 id="__deepcopy__"><code>__deepcopy__</code></h3>

``` python
__deepcopy__(memo)
```



<h3 id="add_loss"><code>add_loss</code></h3>

``` python
add_loss(
    losses,
    inputs=None
)
```

Add loss tensor(s), potentially dependent on layer inputs.

Some losses (for instance, activity regularization losses) may be dependent
on the inputs passed when calling a layer. Hence, when reusing a same layer
on different inputs `a` and `b`, some entries in `layer.losses` may be
dependent on `a` and some on `b`. This method automatically keeps track
of dependencies.

The `get_losses_for` method allows to retrieve the losses relevant to a
specific set of inputs.

#### Arguments:

* <b>`losses`</b>: Loss tensor, or list/tuple of tensors.
* <b>`inputs`</b>: Optional input tensor(s) that the loss(es) depend on. Must
    match the `inputs` argument passed to the `__call__` method at the time
    the losses are created. If `None` is passed, the losses are assumed
    to be unconditional, and will apply across all dataflows of the layer
    (e.g. weight regularization losses).

<h3 id="add_update"><code>add_update</code></h3>

``` python
add_update(
    updates,
    inputs=None
)
```

Add update op(s), potentially dependent on layer inputs.

Weight updates (for instance, the updates of the moving mean and variance
in a BatchNormalization layer) may be dependent on the inputs passed
when calling a layer. Hence, when reusing a same layer on
different inputs `a` and `b`, some entries in `layer.updates` may be
dependent on `a` and some on `b`. This method automatically keeps track
of dependencies.

The `get_updates_for` method allows to retrieve the updates relevant to a
specific set of inputs.

#### Arguments:

* <b>`updates`</b>: Update op, or list/tuple of update ops.
* <b>`inputs`</b>: Optional input tensor(s) that the update(s) depend on. Must
    match the `inputs` argument passed to the `__call__` method at the time
    the updates are created. If `None` is passed, the updates are assumed
    to be unconditional, and will apply across all dataflows of the layer.

<h3 id="add_variable"><code>add_variable</code></h3>

``` python
add_variable(
    name,
    shape,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=True
)
```

Adds a new variable to the layer, or gets an existing one; returns it.

#### Arguments:

* <b>`name`</b>: variable name.
* <b>`shape`</b>: variable shape.
* <b>`dtype`</b>: The type of the variable. Defaults to `self.dtype`.
* <b>`initializer`</b>: initializer instance (callable).
* <b>`regularizer`</b>: regularizer instance (callable).
* <b>`trainable`</b>: whether the variable should be part of the layer's
    "trainable_variables" (e.g. variables, biases)
    or "non_trainable_variables" (e.g. BatchNorm mean, stddev).


#### Returns:

  The created variable.

<h3 id="apply"><code>apply</code></h3>

``` python
apply(
    inputs,
    *args,
    **kwargs
)
```

Apply the layer on a input.

This simply wraps `self.__call__`.

#### Arguments:

* <b>`inputs`</b>: Input tensor(s).
  *args: additional positional arguments to be passed to `self.call`.
  **kwargs: additional keyword arguments to be passed to `self.call`.


#### Returns:

  Output tensor(s).

<h3 id="build"><code>build</code></h3>

``` python
build(_)
```



<h3 id="call"><code>call</code></h3>

``` python
call(
    inputs,
    state
)
```

Run one step of LSTM.

#### Args:

* <b>`inputs`</b>: input Tensor, 2D, batch x num_units.
* <b>`state`</b>: if `state_is_tuple` is False, this must be a state Tensor,
    `2-D, batch x state_size`.  If `state_is_tuple` is True, this must be a
    tuple of state Tensors, both `2-D`, with column sizes `c_state` and
    `m_state`.


#### Returns:

  A tuple containing:
  - A `2-D, [batch x output_dim]`, Tensor representing the output of the
    LSTM after reading `inputs` when previous state was `state`.
    Here output_dim is:
       num_proj if num_proj was set,
       num_units otherwise.
  - Tensor(s) representing the new state of LSTM after reading `inputs` when
    the previous state was `state`.  Same type and shape(s) as `state`.


#### Raises:

* <b>`ValueError`</b>: If input size cannot be inferred from inputs via
    static shape inference.

<h3 id="get_losses_for"><code>get_losses_for</code></h3>

``` python
get_losses_for(inputs)
```

Retrieves losses relevant to a specific set of inputs.

#### Arguments:

* <b>`inputs`</b>: Input tensor or list/tuple of input tensors.
    Must match the `inputs` argument passed to the `__call__`
    method at the time the losses were created.
    If you pass `inputs=None`, unconditional losses are returned,
    such as weight regularization losses.


#### Returns:

  List of loss tensors of the layer that depend on `inputs`.

<h3 id="get_updates_for"><code>get_updates_for</code></h3>

``` python
get_updates_for(inputs)
```

Retrieves updates relevant to a specific set of inputs.

#### Arguments:

* <b>`inputs`</b>: Input tensor or list/tuple of input tensors.
    Must match the `inputs` argument passed to the `__call__` method
    at the time the updates were created.
    If you pass `inputs=None`, unconditional updates are returned.


#### Returns:

  List of update ops of the layer that depend on `inputs`.

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



