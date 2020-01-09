page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Layer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L86-L2422">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Layer`

Base layer class.

Inherits From: [`Module`](../../../tf/Module)

### Aliases:

* Class `tf.compat.v1.keras.layers.Layer`
* Class `tf.compat.v2.keras.layers.Layer`


<!-- Placeholder for "Used in" -->

This is the class from which all layers inherit.

A layer is a class implementing common neural networks operations, such
as convolution, batch norm, etc. These operations require managing weights,
losses, updates, and inter-layer connectivity.

Users will just instantiate a layer and then treat it as a callable.

We recommend that descendants of `Layer` implement the following methods:

* `__init__()`: Save configuration in member variables
* `build()`: Called once from `__call__`, when we know the shapes of inputs
  and `dtype`. Should have the calls to `add_weight()`, and then
  call the super's `build()` (which sets `self.built = True`, which is
  nice in case the user wants to call `build()` manually before the
  first `__call__`).
* `call()`: Called in `__call__` after making sure `build()` has been called
  once. Should actually perform the logic of applying the layer to the
  input tensors (which should be passed in as the first argument).

#### Arguments:


* <b>`trainable`</b>: Boolean, whether the layer's variables should be trainable.
* <b>`name`</b>: String name of the layer.
* <b>`dtype`</b>: The dtype of the layer's computations and weights (default of
  `None` means use <a href="../../../tf/keras/backend/floatx"><code>tf.keras.backend.floatx</code></a> in TensorFlow 2, or the type
  of the first input in TensorFlow 1).
* <b>`dynamic`</b>: Set this to `True` if your layer should only be run eagerly, and
  should not be used to generate a static computation graph.
  This would be the case for a Tree-RNN or a recursive network,
  for example, or generally for any layer that manipulates tensors
  using Python control flow. If `False`, we assume that the layer can
  safely be used to generate a static computation graph.

Read-only properties:
  name: The name of the layer (string).
  dtype: The dtype of the layer's computations and weights. If mixed
    precision is used with a <a href="../../../tf/keras/mixed_precision/experimental/Policy"><code>tf.keras.mixed_precision.experimental.Policy</code></a>,
    this is instead just the dtype of the layer's weights, as the computations
    are done in a different dtype.
  updates: List of update ops of this layer.
  losses: List of losses added by this layer.
  trainable_weights: List of variables to be included in backprop.
  non_trainable_weights: List of variables that should not be
    included in backprop.
  weights: The concatenation of the lists trainable_weights and
    non_trainable_weights (in this order).

#### Mutable properties:


* <b>`trainable`</b>: Whether the layer should be trained (boolean).
* <b>`input_spec`</b>: Optional (list of) `InputSpec` object(s) specifying the
  constraints on inputs that can be accepted by the layer.

### Dtypes and casting
Each layer has a dtype, which is typically the dtype of the layer's
computations and variables. A layer's dtype can be queried via the
<a href="../../../tf/keras/layers/Layer#dtype"><code>Layer.dtype</code></a> property. The dtype is specified with the `dtype` constructor
argument. In TensorFlow 2, the dtype defaults to <a href="../../../tf/keras/backend/floatx"><code>tf.keras.backend.floatx()</code></a>
if no dtype is passed. `floatx()` itself defaults to "float32". Additionally,
layers will cast their inputs to the layer's dtype in TensorFlow 2. For
example:

```
x = tf.ones((4, 4, 4, 4), dtype='float64')
layer = tf.keras.layers.Conv2D(filters=4, kernel_size=2)
print(layer.dtype)  # float32

# `layer` casts it's inputs to layer.dtype, which is float32, and does
# computations in float32.
y = layer(x)
```

Currently, only tensors in the first argument to the layer's `call` method are
casted. For example:

```
class MyLayer(tf.keras.layers.Layer):
  # Bug! `b` will not be casted.
  def call(self, a, b):
    return a + 1., b + 1.

a = tf.constant(1., dtype="float32")
b = tf.constant(1., dtype="float32")

layer = MyLayer(dtype="float64")
x, y = layer(a, b)
print(x.dtype)  # float64
print(y.dtype)  # float32. Not casted since `b` was not passed to first input
```

It is recommended to accept tensors only in the first argument. This way,
all tensors are casted to the layer's dtype. `MyLayer` should therefore be
written as:

```
class MyLayer(tf.keras.layers.Layer):
  # Now, all tensor inputs will be casted.
  def call(self, inputs):
    a, b = inputs
    return a + 1., b + 1.

a = tf.constant(1., dtype="float32")
b = tf.constant(1., dtype="float32")

layer = MyLayer(dtype="float64")
x, y = layer((a, b))
print(x.dtype)  # float64
print(y.dtype)  # float64.
```

In a future minor release, tensors in other arguments may be casted as well.

Currently, other arguments are not automatically casted for
technical reasons, but this may change in a future minor release.

A layer subclass can prevent its inputs from being autocasted by passing
`autocast=False` to the layer constructor. For example:

```
class MyLayer(tf.keras.layers.Layer):

  def __init__(self, **kwargs):
    kwargs['autocast']=False
    super(MyLayer, self).__init__(**kwargs)

  def call(self, inp):
    return inp

x = tf.ones((4, 4, 4, 4), dtype='float64')
layer = MyLayer()
print(layer.dtype)  # float32.
y = layer(x)  # MyLayer will not cast inputs to it's dtype of float32
print(y.dtype)  # float64
```

#### Running models in float64 in TensorFlow 2

If you want to run a Model in float64, you can set floatx to be float64 by
calling `tf.keras.backend.set_floatx('float64')`. This will cause all layers
to default to float64 instead of float32:

```
tf.keras.backend.set_floatx('float64')
layer1 = tf.keras.layers.Dense(4)
layer2 = tf.keras.layers.Dense(4)

x = tf.ones((4, 4))
y = layer2(layer1(x))  # Both layers run in float64
```

Alternatively, you can pass `dtype='float64'` to each individual layer. Note
that if you have any layers which contain other layers as members, you must
ensure each sublayer gets `dtype='float64'` passed to it's constructor as
well:

```
layer1 = tf.keras.layers.Dense(4, dtype='float64')
layer2 = tf.keras.layers.Dense(4, dtype='float64')

x = tf.ones((4, 4))
y = layer2(layer1(x))  # Both layers run in float64

class NestedLayer(tf.keras.layers.Layer):
  def __init__(self, **kwargs):
    super(NestedLayer, self).__init__(**kwargs)
    self.dense = tf.keras.layers.Dense(4, dtype=kwargs.get('dtype'))

  def call(self, inp):
    return self.dense(inp)

layer3 = NestedLayer(dtype='float64')
z = layer3(x)  # layer3's dense layer runs in float64, since NestedLayer
               # correcty passed it's dtype to it's dense layer

```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L277-L363">View source</a>

``` python
__init__(
    trainable=True,
    name=None,
    dtype=None,
    dynamic=False,
    **kwargs
)
```






## Properties

<h3 id="activity_regularizer"><code>activity_regularizer</code></h3>

Optional regularizer function for the output of this layer.


<h3 id="dtype"><code>dtype</code></h3>




<h3 id="dynamic"><code>dynamic</code></h3>




<h3 id="input"><code>input</code></h3>

Retrieves the input tensor(s) of a layer.

Only applicable if the layer has exactly one input,
i.e. if it is connected to one incoming layer.

#### Returns:

Input tensor or list of input tensors.



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

<h3 id="input_spec"><code>input_spec</code></h3>




<h3 id="losses"><code>losses</code></h3>

Losses which are associated with this `Layer`.

Variable regularization tensors are created when this property is accessed,
so it is eager safe: accessing `losses` under a <a href="../../../tf/GradientTape"><code>tf.GradientTape</code></a> will
propagate gradients back to the corresponding variables.

#### Returns:

A list of tensors.


<h3 id="metrics"><code>metrics</code></h3>




<h3 id="name"><code>name</code></h3>

Returns the name of this module as passed or determined in the ctor.

NOTE: This is not the same as the `self.name_scope.name` which includes
parent module names.

<h3 id="non_trainable_variables"><code>non_trainable_variables</code></h3>




<h3 id="non_trainable_weights"><code>non_trainable_weights</code></h3>




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

<h3 id="trainable"><code>trainable</code></h3>




<h3 id="trainable_variables"><code>trainable_variables</code></h3>

Sequence of variables owned by this module and it's submodules.

Note: this method uses reflection to find variables on the current instance
and submodules. For performance reasons you may wish to cache the result
of calling this method if you don't expect the return value to change.

#### Returns:

A sequence of variables for the current module (sorted by attribute
name) followed by variables from all submodules recursively (breadth
first).


<h3 id="trainable_weights"><code>trainable_weights</code></h3>




<h3 id="updates"><code>updates</code></h3>




<h3 id="variables"><code>variables</code></h3>

Returns the list of all layer variables/weights.

Alias of `self.weights`.

#### Returns:

A list of variables.


<h3 id="weights"><code>weights</code></h3>

Returns the list of all layer variables/weights.


#### Returns:

A list of variables.




## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L703-L895">View source</a>

``` python
__call__(
    inputs,
    *args,
    **kwargs
)
```

Wraps `call`, applying pre- and post-processing steps.


#### Arguments:


* <b>`inputs`</b>: input tensor(s).
* <b>`*args`</b>: additional positional arguments to be passed to `self.call`.
* <b>`**kwargs`</b>: additional keyword arguments to be passed to `self.call`.


#### Returns:

Output tensor(s).



#### Note:

- The following optional keyword arguments are reserved for specific uses:
  * `training`: Boolean scalar tensor of Python boolean indicating
    whether the `call` is meant for training or inference.
  * `mask`: Boolean input mask.
- If the layer's `call` method takes a `mask` argument (as some Keras
  layers do), its default value will be set to the mask generated
  for `inputs` by the previous layer (if `input` did come from
  a layer that generated a corresponding mask, i.e. if it came from
  a Keras layer with masking support.



#### Raises:


* <b>`ValueError`</b>: if the layer's `call` method returns None (an invalid value).

<h3 id="add_loss"><code>add_loss</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1017-L1135">View source</a>

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

This method can be used inside a subclassed layer or model's `call`
function, in which case `losses` should be a Tensor or list of Tensors.

#### Example:



```python
class MyLayer(tf.keras.layers.Layer):
  def call(inputs, self):
    self.add_loss(tf.abs(tf.reduce_mean(inputs)), inputs=True)
    return inputs
```

This method can also be called directly on a Functional Model during
construction. In this case, any loss Tensors passed to this Model must
be symbolic and be able to be traced back to the model's `Input`s. These
losses become part of the model's topology and are tracked in `get_config`.

#### Example:



```python
inputs = tf.keras.Input(shape=(10,))
x = tf.keras.layers.Dense(10)(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs, outputs)
# Actvity regularization.
model.add_loss(tf.abs(tf.reduce_mean(x)))
```

If this is not the case for your loss (if, for example, your loss references
a `Variable` of one of the model's layers), you can wrap your loss in a
zero-argument lambda. These losses are not tracked as part of the model's
topology since they can't be serialized.

#### Example:



```python
inputs = tf.keras.Input(shape=(10,))
x = tf.keras.layers.Dense(10)(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs, outputs)
# Weight regularization.
model.add_loss(lambda: tf.reduce_mean(x.kernel))
```

The `get_losses_for` method allows to retrieve the losses relevant to a
specific set of inputs.

#### Arguments:


* <b>`losses`</b>: Loss tensor, or list/tuple of tensors. Rather than tensors, losses
  may also be zero-argument callables which create a loss tensor.
* <b>`inputs`</b>: Ignored when executing eagerly. If anything other than None is
  passed, it signals the losses are conditional on some of the layer's
  inputs, and thus they should only be run where these inputs are
  available. This is the case for activity regularization losses, for
  instance. If `None` is passed, the losses are assumed
  to be unconditional, and will apply across all dataflows of the layer
  (e.g. weight regularization losses).

<h3 id="add_metric"><code>add_metric</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1150-L1219">View source</a>

``` python
add_metric(
    value,
    aggregation=None,
    name=None
)
```

Adds metric tensor to the layer.


#### Args:


* <b>`value`</b>: Metric tensor.
* <b>`aggregation`</b>: Sample-wise metric reduction function. If `aggregation=None`,
  it indicates that the metric tensor provided has been aggregated
  already. eg, `bin_acc = BinaryAccuracy(name='acc')` followed by
  `model.add_metric(bin_acc(y_true, y_pred))`. If aggregation='mean', the
  given metric tensor will be sample-wise reduced using `mean` function.
  eg, `model.add_metric(tf.reduce_sum(outputs), name='output_mean',
  aggregation='mean')`.
* <b>`name`</b>: String metric name.


#### Raises:


* <b>`ValueError`</b>: If `aggregation` is anything other than None or `mean`.

<h3 id="add_update"><code>add_update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1221-L1305">View source</a>

``` python
add_update(
    updates,
    inputs=None
)
```

Add update op(s), potentially dependent on layer inputs. (deprecated arguments)

Warning: SOME ARGUMENTS ARE DEPRECATED: `(inputs)`. They will be removed in a future version.
Instructions for updating:
`inputs` is now automatically inferred

Weight updates (for instance, the updates of the moving mean and variance
in a BatchNormalization layer) may be dependent on the inputs passed
when calling a layer. Hence, when reusing the same layer on
different inputs `a` and `b`, some entries in `layer.updates` may be
dependent on `a` and some on `b`. This method automatically keeps track
of dependencies.

The `get_updates_for` method allows to retrieve the updates relevant to a
specific set of inputs.

This call is ignored when eager execution is enabled (in that case, variable
updates are run on the fly and thus do not need to be tracked for later
execution).

#### Arguments:


* <b>`updates`</b>: Update op, or list/tuple of update ops, or zero-arg callable
  that returns an update op. A zero-arg callable should be passed in
  order to disable running the updates by setting `trainable=False`
  on this Layer, when executing in Eager mode.
* <b>`inputs`</b>: Deprecated, will be automatically inferred.

<h3 id="add_weight"><code>add_weight</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L394-L537">View source</a>

``` python
add_weight(
    name=None,
    shape=None,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=None,
    constraint=None,
    partitioner=None,
    use_resource=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.compat.v1.VariableAggregation.NONE,
    **kwargs
)
```

Adds a new variable to the layer.


#### Arguments:


* <b>`name`</b>: Variable name.
* <b>`shape`</b>: Variable shape. Defaults to scalar if unspecified.
* <b>`dtype`</b>: The type of the variable. Defaults to `self.dtype` or `float32`.
* <b>`initializer`</b>: Initializer instance (callable).
* <b>`regularizer`</b>: Regularizer instance (callable).
* <b>`trainable`</b>: Boolean, whether the variable should be part of the layer's
  "trainable_variables" (e.g. variables, biases)
  or "non_trainable_variables" (e.g. BatchNorm mean and variance).
  Note that `trainable` cannot be `True` if `synchronization`
  is set to `ON_READ`.
* <b>`constraint`</b>: Constraint instance (callable).
* <b>`partitioner`</b>: Partitioner to be passed to the `Trackable` API.
* <b>`use_resource`</b>: Whether to use `ResourceVariable`.
* <b>`synchronization`</b>: Indicates when a distributed a variable will be
  aggregated. Accepted values are constants defined in the class
  <a href="../../../tf/VariableSynchronization"><code>tf.VariableSynchronization</code></a>. By default the synchronization is set to
  `AUTO` and the current `DistributionStrategy` chooses
  when to synchronize. If `synchronization` is set to `ON_READ`,
  `trainable` must not be set to `True`.
* <b>`aggregation`</b>: Indicates how a distributed variable will be aggregated.
  Accepted values are constants defined in the class
  <a href="../../../tf/VariableAggregation"><code>tf.VariableAggregation</code></a>.
* <b>`**kwargs`</b>: Additional keyword arguments. Accepted values are `getter` and
  `collections`.


#### Returns:

The created variable. Usually either a `Variable` or `ResourceVariable`
instance. If `partitioner` is not `None`, a `PartitionedVariable`
instance is returned.



#### Raises:


* <b>`RuntimeError`</b>: If called with partitioned variable regularization and
  eager execution is enabled.
* <b>`ValueError`</b>: When giving unsupported dtype and no initializer or when
  trainable has been set to True with synchronization set as `ON_READ`.

<h3 id="build"><code>build</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L365-L379">View source</a>

``` python
build(input_shape)
```

Creates the variables of the layer (optional, for subclass implementers).

This is a method that implementers of subclasses of `Layer` or `Model`
can override if they need a state-creation step in-between
layer instantiation and layer call.

This is typically used to create the weights of `Layer` subclasses.

#### Arguments:


* <b>`input_shape`</b>: Instance of `TensorShape`, or list of instances of
  `TensorShape` if the layer expects a list of inputs
  (one instance per input).

<h3 id="call"><code>call</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L381-L392">View source</a>

``` python
call(
    inputs,
    **kwargs
)
```

This is where the layer's logic lives.


#### Arguments:


* <b>`inputs`</b>: Input tensor, or list/tuple of input tensors.
* <b>`**kwargs`</b>: Additional keyword arguments.


#### Returns:

A tensor or list/tuple of tensors.


<h3 id="compute_mask"><code>compute_mask</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L681-L701">View source</a>

``` python
compute_mask(
    inputs,
    mask=None
)
```

Computes an output mask tensor.


#### Arguments:


* <b>`inputs`</b>: Tensor or list of tensors.
* <b>`mask`</b>: Tensor or list of tensors.


#### Returns:

None or a tensor (or list of tensors,
    one per output tensor of the layer).


<h3 id="compute_output_shape"><code>compute_output_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L596-L639">View source</a>

``` python
compute_output_shape(input_shape)
```

Computes the output shape of the layer.

If the layer has not been built, this method will call `build` on the
layer. This assumes that the layer will later be used with inputs that
match the input shape provided here.

#### Arguments:


* <b>`input_shape`</b>: Shape tuple (tuple of integers)
    or list of shape tuples (one per output tensor of the layer).
    Shape tuples can include None for free dimensions,
    instead of an integer.


#### Returns:

An input shape tuple.


<h3 id="compute_output_signature"><code>compute_output_signature</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L641-L679">View source</a>

``` python
compute_output_signature(input_signature)
```

Compute the output tensor signature of the layer based on the inputs.

Unlike a TensorShape object, a TensorSpec object contains both shape
and dtype information for a tensor. This method allows layers to provide
output dtype information if it is different from the input dtype.
For any layer that doesn't implement this function,
the framework will fall back to use `compute_output_shape`, and will
assume that the output dtype matches the input dtype.

#### Args:


* <b>`input_signature`</b>: Single TensorSpec or nested structure of TensorSpec
  objects, describing a candidate input for the layer.


#### Returns:

Single TensorSpec or nested structure of TensorSpec objects, describing
  how the layer would transform the provided input.



#### Raises:


* <b>`TypeError`</b>: If input_signature contains a non-TensorSpec object.

<h3 id="count_params"><code>count_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1611-L1630">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L578-L594">View source</a>

``` python
@classmethod
from_config(
    cls,
    config
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Network), nor weights (handled by `set_weights`).

#### Arguments:


* <b>`config`</b>: A Python dictionary, typically the
    output of get_config.


#### Returns:

A layer instance.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L539-L576">View source</a>

``` python
get_config()
```

Returns the config of the layer.

A layer config is a Python dictionary (serializable)
containing the configuration of a layer.
The same layer can be reinstantiated later
(without its trained weights) from this configuration.

The config of a layer does not include connectivity
information, nor the layer class name. These are handled
by `Network` (one layer of abstraction above).

#### Returns:

Python dictionary.


<h3 id="get_input_at"><code>get_input_at</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1505-L1521">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1387-L1404">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1467-L1484">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1368-L1385">View source</a>

``` python
get_losses_for(inputs)
```

Retrieves losses relevant to a specific set of inputs.


#### Arguments:


* <b>`inputs`</b>: Input tensor or list/tuple of input tensors.


#### Returns:

List of loss tensors of the layer that depend on `inputs`.


<h3 id="get_output_at"><code>get_output_at</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1523-L1539">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1406-L1423">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1486-L1503">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1349-L1366">View source</a>

``` python
get_updates_for(inputs)
```

Retrieves updates relevant to a specific set of inputs.


#### Arguments:


* <b>`inputs`</b>: Input tensor or list/tuple of input tensors.


#### Returns:

List of update ops of the layer that depend on `inputs`.


<h3 id="get_weights"><code>get_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1340-L1347">View source</a>

``` python
get_weights()
```

Returns the current weights of the layer.


#### Returns:

Weights values as a list of numpy arrays.


<h3 id="set_weights"><code>set_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/base_layer.py#L1307-L1338">View source</a>

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
