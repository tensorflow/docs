

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Lambda

## Class `Lambda`

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)



Defined in [`tensorflow/python/keras/_impl/keras/layers/core.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/layers/core.py).

Wraps arbitrary expression as a `Layer` object.

Examples:

```python
    # add a x -> x^2 layer
    model.add(Lambda(lambda x: x ** 2))
```

```python
    # add a layer that returns the concatenation
    # of the positive part of the input and
    # the opposite of the negative part

    def antirectifier(x):
        x -= K.mean(x, axis=1, keepdims=True)
        x = K.l2_normalize(x, axis=1)
        pos = K.relu(x)
        neg = K.relu(-x)
        return K.concatenate([pos, neg], axis=1)

    model.add(Lambda(antirectifier))
```

#### Arguments:

* <b>`function`</b>: The function to be evaluated.
        Takes input tensor as first argument.
* <b>`output_shape`</b>: Expected output shape from function.
          This argument can be inferred if not explicitly provided.
          Can be a tuple or function.
          If a tuple, it only specifies the first dimension onward;
               sample dimension is assumed either the same as the input:
               `output_shape = (input_shape[0], ) + output_shape`
               or, the input is `None` and
               the sample dimension is also `None`:
               `output_shape = (None, ) + output_shape`
          If a function, it specifies the entire shape as a function of the
          input shape: `output_shape = f(input_shape)`
* <b>`arguments`</b>: optional dictionary of keyword arguments to be passed
          to the function.

Input shape:
    Arbitrary. Use the keyword argument input_shape
    (tuple of integers, does not include the samples axis)
    when using this layer as the first layer in a model.

Output shape:
    Specified by `output_shape` argument

## Properties

<h3 id="activity_regularizer"><code>activity_regularizer</code></h3>

Optional regularizer function for the output of this layer.

<h3 id="dtype"><code>dtype</code></h3>



<h3 id="graph"><code>graph</code></h3>



<h3 id="inbound_nodes"><code>inbound_nodes</code></h3>

Deprecated, do NOT use! Only for compatibility with external Keras.

<h3 id="input"><code>input</code></h3>

Retrieves the input tensor(s) of a layer.

Only applicable if the layer has exactly one input,
i.e. if it is connected to one incoming layer.

#### Returns:

Input tensor or list of input tensors.


#### Raises:

* <b>`AttributeError`</b>: if the layer is connected to
    more than one incoming layers.


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.
* <b>`AttributeError`</b>: If no inbound nodes are found.

<h3 id="input_mask"><code>input_mask</code></h3>

Retrieves the input mask tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

Input mask tensor (potentially None) or list of input
mask tensors.


#### Raises:

* <b>`AttributeError`</b>: if the layer is connected to
    more than one incoming layers.

<h3 id="input_shape"><code>input_shape</code></h3>

Retrieves the input shape(s) of a layer.

Only applicable if the layer has exactly one input,
i.e. if it is connected to one incoming layer, or if all inputs
have the same shape.

#### Returns:

Input shape, as an integer shape tuple
(or list of shape tuples, one tuple per input tensor).


#### Raises:

* <b>`AttributeError`</b>: if the layer has no defined input_shape.
* <b>`RuntimeError`</b>: if called in Eager mode.

<h3 id="losses"><code>losses</code></h3>

Losses which are associated with this `Layer`.

Note that when executing eagerly, getting this property evaluates
regularizers. When using graph execution, variable regularization ops have
already been created and are simply returned here.

#### Returns:

A list of tensors.

<h3 id="name"><code>name</code></h3>



<h3 id="non_trainable_variables"><code>non_trainable_variables</code></h3>



<h3 id="non_trainable_weights"><code>non_trainable_weights</code></h3>



<h3 id="outbound_nodes"><code>outbound_nodes</code></h3>

Deprecated, do NOT use! Only for compatibility with external Keras.

<h3 id="output"><code>output</code></h3>

Retrieves the output tensor(s) of a layer.

Only applicable if the layer has exactly one output,
i.e. if it is connected to one incoming layer.

#### Returns:

Output tensor or list of output tensors.


#### Raises:

* <b>`AttributeError`</b>: if the layer is connected to more than one incoming
    layers.
* <b>`RuntimeError`</b>: if called in Eager mode.

<h3 id="output_mask"><code>output_mask</code></h3>

Retrieves the output mask tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

Output mask tensor (potentially None) or list of output
mask tensors.


#### Raises:

* <b>`AttributeError`</b>: if the layer is connected to
    more than one incoming layers.

<h3 id="output_shape"><code>output_shape</code></h3>

Retrieves the output shape(s) of a layer.

Only applicable if the layer has one output,
or if all outputs have the same shape.

#### Returns:

Output shape, as an integer shape tuple
(or list of shape tuples, one tuple per output tensor).


#### Raises:

* <b>`AttributeError`</b>: if the layer has no defined output shape.
* <b>`RuntimeError`</b>: if called in Eager mode.

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
    function,
    output_shape=None,
    mask=None,
    arguments=None,
    **kwargs
)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    *args,
    **kwargs
)
```

Wrapper around self.call(), for handling internal references.

If a Keras tensor is passed:
    - We call self._add_inbound_node().
    - If necessary, we `build` the layer to match
        the shape of the input(s).
    - We update the _keras_history of the output tensor(s)
        with the current layer.
        This is done as part of _add_inbound_node().

#### Arguments:

* <b>`inputs`</b>: Can be a tensor or list/tuple of tensors.
* <b>`*args`</b>: Additional positional arguments to be passed to `call()`. Only
      allowed in subclassed Models with custom call() signatures. In other
      cases, `Layer` inputs must be passed using the `inputs` argument and
      non-inputs must be keyword arguments.
* <b>`**kwargs`</b>: Additional keyword arguments to be passed to `call()`.


#### Returns:

Output of the layer's `call` method.


#### Raises:

* <b>`ValueError`</b>: in case the layer is missing shape information
        for its `build` call.
* <b>`TypeError`</b>: If positional arguments are passed and this `Layer` is not a
        subclassed `Model`.

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
on the inputs passed when calling a layer. Hence, when reusing the same
layer on different inputs `a` and `b`, some entries in `layer.losses` may
be dependent on `a` and some on `b`. This method automatically keeps track
of dependencies.

The `get_losses_for` method allows to retrieve the losses relevant to a
specific set of inputs.

Note that `add_loss` is not supported when executing eagerly. Instead,
variable regularizers may be added through `add_variable`. Activity
regularization is not supported directly (but such losses may be returned
from `Layer.call()`).

#### Arguments:

* <b>`losses`</b>: Loss tensor, or list/tuple of tensors.
* <b>`inputs`</b>: If anything other than None is passed, it signals the losses
    are conditional on some of the layer's inputs,
    and thus they should only be run where these inputs are available.
    This is the case for activity regularization losses, for instance.
    If `None` is passed, the losses are assumed
    to be unconditional, and will apply across all dataflows of the layer
    (e.g. weight regularization losses).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

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
when calling a layer. Hence, when reusing the same layer on
different inputs `a` and `b`, some entries in `layer.updates` may be
dependent on `a` and some on `b`. This method automatically keeps track
of dependencies.

The `get_updates_for` method allows to retrieve the updates relevant to a
specific set of inputs.

This call is ignored in Eager mode.

#### Arguments:

* <b>`updates`</b>: Update op, or list/tuple of update ops.
* <b>`inputs`</b>: If anything other than None is passed, it signals the updates
    are conditional on some of the layer's inputs,
    and thus they should only be run where these inputs are available.
    This is the case for BatchNormalization updates, for instance.
    If None, the updates will be taken into account unconditionally,
    and you are responsible for making sure that any dependency they might
    have is available at runtime.
    A step counter might fall into this category.

<h3 id="add_variable"><code>add_variable</code></h3>

``` python
add_variable(
    name,
    shape,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=True,
    constraint=None,
    partitioner=None
)
```

Adds a new variable to the layer, or gets an existing one; returns it.

#### Arguments:

* <b>`name`</b>: variable name.
* <b>`shape`</b>: variable shape.
* <b>`dtype`</b>: The type of the variable. Defaults to `self.dtype` or `float32`.
* <b>`initializer`</b>: initializer instance (callable).
* <b>`regularizer`</b>: regularizer instance (callable).
* <b>`trainable`</b>: whether the variable should be part of the layer's
    "trainable_variables" (e.g. variables, biases)
    or "non_trainable_variables" (e.g. BatchNorm mean, stddev).
    Note, if the current variable scope is marked as non-trainable
    then this parameter is ignored and any added variables are also
    marked as non-trainable.
* <b>`constraint`</b>: constraint instance (callable).
* <b>`partitioner`</b>: (optional) partitioner instance (callable).  If
    provided, when the requested variable is created it will be split
    into multiple partitions according to `partitioner`.  In this case,
    an instance of `PartitionedVariable` is returned.  Available
    partitioners include <a href="../../../tf/fixed_size_partitioner"><code>tf.fixed_size_partitioner</code></a> and
    <a href="../../../tf/variable_axis_size_partitioner"><code>tf.variable_axis_size_partitioner</code></a>.  For more details, see the
    documentation of <a href="../../../tf/get_variable"><code>tf.get_variable</code></a> and the  "Variable Partitioners
    and Sharding" section of the API guide.


#### Returns:

The created variable.  Usually either a `Variable` or `ResourceVariable`
instance.  If `partitioner` is not `None`, a `PartitionedVariable`
instance is returned.


#### Raises:

* <b>`RuntimeError`</b>: If called with partioned variable regularization and
    eager execution is enabled.

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

* <b>`name`</b>: String, the name for the weight variable.
* <b>`shape`</b>: The shape tuple of the weight.
* <b>`dtype`</b>: The dtype of the weight.
* <b>`initializer`</b>: An Initializer instance (callable).
* <b>`regularizer`</b>: An optional Regularizer instance.
* <b>`trainable`</b>: A boolean, whether the weight should
        be trained via backprop or not (assuming
        that the layer itself is also trainable).
* <b>`constraint`</b>: An optional Constraint instance.


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
* <b>`*args`</b>: additional positional arguments to be passed to `self.call`.
* <b>`**kwargs`</b>: additional keyword arguments to be passed to `self.call`.


#### Returns:

Output tensor(s).

<h3 id="build"><code>build</code></h3>

``` python
build(_)
```

Creates the variables of the layer.

<h3 id="call"><code>call</code></h3>

``` python
call(
    inputs,
    mask=None
)
```



<h3 id="compute_mask"><code>compute_mask</code></h3>

``` python
compute_mask(
    inputs,
    mask=None
)
```



<h3 id="compute_output_shape"><code>compute_output_shape</code></h3>

``` python
compute_output_shape(input_shape)
```

Computes the output shape of the layer.

Assumes that the layer will be built
to match that input shape provided.

#### Arguments:

* <b>`input_shape`</b>: Shape tuple (tuple of integers)
        or list of shape tuples (one per output tensor of the layer).
        Shape tuples can include None for free dimensions,
        instead of an integer.


#### Returns:

An input shape tuple.

<h3 id="count_params"><code>count_params</code></h3>

``` python
count_params()
```

Count the total number of scalars composing the weights.

#### Returns:

An integer count.


#### Raises:

* <b>`ValueError`</b>: if the layer isn't yet built
      (in which case its weights aren't yet defined).

<h3 id="from_config"><code>from_config</code></h3>

``` python
@classmethod
from_config(
    cls,
    config,
    custom_objects=None
)
```



<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```



<h3 id="get_input_at"><code>get_input_at</code></h3>

``` python
get_input_at(node_index)
```

Retrieves the input tensor(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A tensor (or list of tensors if the layer has multiple inputs).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_input_mask_at"><code>get_input_mask_at</code></h3>

``` python
get_input_mask_at(node_index)
```

Retrieves the input mask tensor(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
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

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A shape tuple
(or list of shape tuples if the layer has multiple inputs).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_losses_for"><code>get_losses_for</code></h3>

``` python
get_losses_for(inputs)
```

Retrieves losses relevant to a specific set of inputs.

#### Arguments:

* <b>`inputs`</b>: Input tensor or list/tuple of input tensors.


#### Returns:

List of loss tensors of the layer that depend on `inputs`.


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_output_at"><code>get_output_at</code></h3>

``` python
get_output_at(node_index)
```

Retrieves the output tensor(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A tensor (or list of tensors if the layer has multiple outputs).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_output_mask_at"><code>get_output_mask_at</code></h3>

``` python
get_output_mask_at(node_index)
```

Retrieves the output mask tensor(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
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

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A shape tuple
(or list of shape tuples if the layer has multiple outputs).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_updates_for"><code>get_updates_for</code></h3>

``` python
get_updates_for(inputs)
```

Retrieves updates relevant to a specific set of inputs.

#### Arguments:

* <b>`inputs`</b>: Input tensor or list/tuple of input tensors.


#### Returns:

List of update ops of the layer that depend on `inputs`.


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_weights"><code>get_weights</code></h3>

``` python
get_weights()
```

Returns the current weights of the layer.

#### Returns:

Weights values as a list of numpy arrays.

<h3 id="set_weights"><code>set_weights</code></h3>

``` python
set_weights(weights)
```

Sets the weights of the layer, from Numpy arrays.

#### Arguments:

* <b>`weights`</b>: a list of Numpy arrays. The number
        of arrays and their shape must match
        number of the dimensions of the weights
        of the layer (i.e. it should match the
        output of `get_weights`).


#### Raises:

* <b>`ValueError`</b>: If the provided weights list does not match the
        layer's specifications.



