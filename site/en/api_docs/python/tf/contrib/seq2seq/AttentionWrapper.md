

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.seq2seq.AttentionWrapper

### `class tf.contrib.seq2seq.AttentionWrapper`



Defined in [`tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py).

Wraps another `RNNCell` with attention.
  

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
    cell,
    attention_mechanism,
    attention_layer_size=None,
    alignment_history=False,
    cell_input_fn=None,
    output_attention=True,
    initial_cell_state=None,
    name=None
)
```

Construct the `AttentionWrapper`.

#### Args:

* <b>`cell`</b>: An instance of `RNNCell`.
* <b>`attention_mechanism`</b>: An instance of `AttentionMechanism`.
* <b>`attention_layer_size`</b>: Python integer, the depth of the attention (output)
    layer. If None (default), use the context as attention at each time
    step. Otherwise, feed the context and cell output into the attention
    layer to generate attention at each time step.
* <b>`alignment_history`</b>: Python boolean, whether to store alignment history
    from all time steps in the final output state (currently stored as a
    time major `TensorArray` on which you must call `stack()`).
* <b>`cell_input_fn`</b>: (optional) A `callable`.  The default is:
    `lambda inputs, attention: array_ops.concat([inputs, attention], -1)`.
* <b>`output_attention`</b>: Python bool.  If `True` (default), the output at each
    time step is the attention value.  This is the behavior of Luong-style
    attention mechanisms.  If `False`, the output at each time step is
    the output of `cell`.  This is the beahvior of Bhadanau-style
    attention mechanisms.  In both cases, the `attention` tensor is
    propagated to the next time step via the state and is used there.
    This flag only controls whether the attention mechanism is propagated
    up to the next cell in an RNN stack or to the top RNN output.
* <b>`initial_cell_state`</b>: The initial state value to use for the cell when
    the user calls `zero_state()`.  Note that if this value is provided
    now, and the user uses a `batch_size` argument of `zero_state` which
    does not match the batch size of `initial_cell_state`, proper
    behavior is not guaranteed.
* <b>`name`</b>: Name to use when creating ops.

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

Perform a step of attention-wrapped RNN.

- Step 1: Mix the `inputs` and previous step's `attention` output via
  `cell_input_fn`.
- Step 2: Call the wrapped `cell` with this input and its previous state.
- Step 3: Score the cell's output with `attention_mechanism`.
- Step 4: Calculate the alignments by passing the score through the
  `normalizer`.
- Step 5: Calculate the context vector as the inner product between the
  alignments and the attention_mechanism's values (memory).
- Step 6: Calculate the attention output by concatenating the cell output
  and context through the attention layer (a linear layer with
  `attention_size` outputs).

#### Args:

* <b>`inputs`</b>: (Possibly nested tuple of) Tensor, the input at this time step.
* <b>`state`</b>: An instance of `AttentionWrapperState` containing
    tensors from the previous time step.


#### Returns:

  A tuple `(attention_or_cell_output, next_state)`, where:

  - `attention_or_cell_output` depending on `output_attention`.
  - `next_state` is an instance of `DynamicAttentionWrapperState`
     containing the state calculated at this time step.

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





