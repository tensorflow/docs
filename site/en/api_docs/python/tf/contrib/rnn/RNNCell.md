

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.rnn.RNNCell

### `class tf.contrib.rnn.RNNCell`
### `class tf.nn.rnn_cell.RNNCell`



Defined in [`tensorflow/python/ops/rnn_cell_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/rnn_cell_impl.py).

See the guides: [RNN and Cells (contrib) > Base interface for all RNN Cells](../../../../../api_guides/python/contrib.rnn#Base_interface_for_all_RNN_Cells), [Seq2seq Library (contrib)](../../../../../api_guides/python/contrib.seq2seq)

Abstract object representing an RNN cell.

Every `RNNCell` must have the properties below and implement `call` with
the signature `(output, next_state) = call(input, state)`.  The optional
third input argument, `scope`, is allowed for backwards compatibility
purposes; but should be left off for new subclasses.

This definition of cell differs from the definition used in the literature.
In the literature, 'cell' refers to an object with a single scalar output.
This definition refers to a horizontal array of such units.

An RNN cell, in the most abstract setting, is anything that has
a state and performs some operation that takes a matrix of inputs.
This operation results in an output matrix with `self.output_size` columns.
If `self.state_size` is an integer, this operation also results in a new
state matrix with `self.state_size` columns.  If `self.state_size` is a
(possibly nested tuple of) TensorShape object(s), then it should return a
matching structure of Tensors having shape `[batch_size].concatenate(s)`
for each `s` in `self.batch_size`.

## Properties

<h3 id="graph"><code>graph</code></h3>



<h3 id="losses"><code>losses</code></h3>



<h3 id="non_trainable_variables"><code>non_trainable_variables</code></h3>



<h3 id="non_trainable_weights"><code>non_trainable_weights</code></h3>



<h3 id="output_size"><code>output_size</code></h3>

Integer or TensorShape: size of outputs produced by this cell.

<h3 id="scope_name"><code>scope_name</code></h3>



<h3 id="state_size"><code>state_size</code></h3>

size(s) of state(s) used by this cell.

It can be represented by an Integer, a TensorShape or a tuple of Integers
or TensorShapes.

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
    trainable=True,
    name=None,
    dtype=tf.float32,
    **kwargs
)
```



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
    **kwargs
)
```

The logic of the layer lives here.

#### Arguments:

* <b>`inputs`</b>: input tensor(s).
 **kwargs: additional keyword arguments.


#### Returns:

  Output tensor(s).

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



