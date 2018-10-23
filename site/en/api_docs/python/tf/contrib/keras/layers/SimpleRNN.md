

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.layers.SimpleRNN

### `class tf.contrib.keras.layers.SimpleRNN`



Defined in [`tensorflow/contrib/keras/python/keras/layers/recurrent.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/layers/recurrent.py).

Fully-connected RNN where the output is to be fed back to input.

#### Arguments:

    units: Positive integer, dimensionality of the output space.
    activation: Activation function to use.
        If you don't specify anything, no activation is applied
        If you pass None, no activation is applied
        (ie. "linear" activation: `a(x) = x`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix,
        used for the linear transformation of the inputs..
    recurrent_initializer: Initializer for the `recurrent_kernel`
        weights matrix,
        used for the linear transformation of the recurrent state..
    bias_initializer: Initializer for the bias vector.
    kernel_regularizer: Regularizer function applied to
        the `kernel` weights matrix.
    recurrent_regularizer: Regularizer function applied to
        the `recurrent_kernel` weights matrix.
    bias_regularizer: Regularizer function applied to the bias vector.
    activity_regularizer: Regularizer function applied to
        the output of the layer (its "activation")..
    kernel_constraint: Constraint function applied to
        the `kernel` weights matrix.
    recurrent_constraint: Constraint function applied to
        the `recurrent_kernel` weights matrix.
    bias_constraint: Constraint function applied to the bias vector.
    dropout: Float between 0 and 1.
        Fraction of the units to drop for
        the linear transformation of the inputs.
    recurrent_dropout: Float between 0 and 1.
        Fraction of the units to drop for
        the linear transformation of the recurrent state.

References:
    - [A Theoretically Grounded Application of Dropout in Recurrent Neural
      Networks](http://arxiv.org/abs/1512.05287)

## Properties

<h3 id="constraints"><code>constraints</code></h3>



<h3 id="graph"><code>graph</code></h3>



<h3 id="input"><code>input</code></h3>

Retrieves the input tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Input tensor or list of input tensors.


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="input_mask"><code>input_mask</code></h3>

Retrieves the input mask tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Input mask tensor (potentially None) or list of input
    mask tensors.


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="input_shape"><code>input_shape</code></h3>

Retrieves the input shape(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Input shape, as `TensorShape`
    (or list of `TensorShape`, one tuple per input tensor).


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="losses"><code>losses</code></h3>



<h3 id="non_trainable_variables"><code>non_trainable_variables</code></h3>



<h3 id="non_trainable_weights"><code>non_trainable_weights</code></h3>



<h3 id="output"><code>output</code></h3>

Retrieves the output tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Output tensor or list of output tensors.


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="output_mask"><code>output_mask</code></h3>

Retrieves the output mask tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Output mask tensor (potentially None) or list of output
    mask tensors.


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="output_shape"><code>output_shape</code></h3>

Retrieves the output shape(s) of a layer.

Only applicable if the layer has one inbound node,
or if all inbound nodes have the same output shape.

#### Returns:

    Output shape, as `TensorShape`
    (or list of `TensorShape`, one tuple per output tensor).


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="scope_name"><code>scope_name</code></h3>



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
    units,
    activation='tanh',
    use_bias=True,
    kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal',
    bias_initializer='zeros',
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    **kwargs
)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    initial_state=None,
    **kwargs
)
```



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

<h3 id="add_weight"><code>add_weight</code></h3>

``` python
add_weight(
    name,
    shape,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=True,
    constraint=None
)
```

Adds a weight variable to the layer.

#### Arguments:

    name: String, the name for the weight variable.
    shape: The shape tuple of the weight.
    dtype: The dtype of the weight.
    initializer: An Initializer instance (callable).
    regularizer: An optional Regularizer instance.
    trainable: A boolean, whether the weight should
        be trained via backprop or not (assuming
        that the layer itself is also trainable).
    constraint: An optional Constraint instance.


#### Returns:

    The created weight variable.

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
build(input_shape)
```



<h3 id="call"><code>call</code></h3>

``` python
call(
    inputs,
    mask=None,
    initial_state=None,
    training=None
)
```



<h3 id="compute_mask"><code>compute_mask</code></h3>

``` python
compute_mask(
    inputs,
    mask
)
```



<h3 id="count_params"><code>count_params</code></h3>

``` python
count_params()
```

Count the total number of scalars composing the weights.

#### Returns:

    An integer count.


#### Raises:

    RuntimeError: if the layer isn't yet built
        (in which case its weights aren't yet defined).

<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Container), nor weights (handled by `set_weights`).

#### Arguments:

    config: A Python dictionary, typically the
        output of get_config.


#### Returns:

    A layer instance.

<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```



<h3 id="get_constants"><code>get_constants</code></h3>

``` python
get_constants(
    inputs,
    training=None
)
```



<h3 id="get_initial_states"><code>get_initial_states</code></h3>

``` python
get_initial_states(inputs)
```



<h3 id="get_input_at"><code>get_input_at</code></h3>

``` python
get_input_at(node_index)
```

Retrieves the input tensor(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A tensor (or list of tensors if the layer has multiple inputs).

<h3 id="get_input_mask_at"><code>get_input_mask_at</code></h3>

``` python
get_input_mask_at(node_index)
```

Retrieves the input mask tensor(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A mask tensor
    (or list of tensors if the layer has multiple inputs).

<h3 id="get_input_shape_at"><code>get_input_shape_at</code></h3>

``` python
get_input_shape_at(node_index)
```

Retrieves the input shape(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A shape tuple
    (or list of shape tuples if the layer has multiple inputs).

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

<h3 id="get_output_at"><code>get_output_at</code></h3>

``` python
get_output_at(node_index)
```

Retrieves the output tensor(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A tensor (or list of tensors if the layer has multiple outputs).

<h3 id="get_output_mask_at"><code>get_output_mask_at</code></h3>

``` python
get_output_mask_at(node_index)
```

Retrieves the output mask tensor(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A mask tensor
    (or list of tensors if the layer has multiple outputs).

<h3 id="get_output_shape_at"><code>get_output_shape_at</code></h3>

``` python
get_output_shape_at(node_index)
```

Retrieves the output shape(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A shape tuple
    (or list of shape tuples if the layer has multiple outputs).

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

<h3 id="get_weights"><code>get_weights</code></h3>

``` python
get_weights()
```

Returns the current weights of the layer.

#### Returns:

    Weights values as a list of numpy arrays.

<h3 id="preprocess_input"><code>preprocess_input</code></h3>

``` python
preprocess_input(
    inputs,
    training=None
)
```



<h3 id="reset_states"><code>reset_states</code></h3>

``` python
reset_states(states_value=None)
```



<h3 id="set_weights"><code>set_weights</code></h3>

``` python
set_weights(weights)
```

Sets the weights of the layer, from Numpy arrays.

#### Arguments:

    weights: a list of Numpy arrays. The number
        of arrays and their shape must match
        number of the dimensions of the weights
        of the layer (i.e. it should match the
        output of `get_weights`).


#### Raises:

    ValueError: If the provided weights list does not match the
        layer's specifications.

<h3 id="step"><code>step</code></h3>

``` python
step(
    inputs,
    states
)
```





