page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.Optimizer

## Class `Optimizer`

Updated base class for optimizers.

Inherits From: [`CheckpointableBase`](../../../tf/contrib/checkpoint/CheckpointableBase)

### Aliases:

* Class `tf.compat.v1.keras.optimizers.Optimizer`
* Class `tf.compat.v2.keras.optimizers.Optimizer`
* Class `tf.compat.v2.optimizers.Optimizer`
* Class `tf.keras.optimizers.Optimizer`



Defined in [`python/keras/optimizer_v2/optimizer_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/optimizer_v2/optimizer_v2.py).

<!-- Placeholder for "Used in" -->

This class defines the API to add Ops to train a model.  You never use this
class directly, but instead instantiate one of its subclasses such as
<a href="../../../tf/keras/optimizers/SGD"><code>tf.keras.optimizers.SGD</code></a>, <a href="../../../tf/keras/optimizers/Adam"><code>tf.keras.optimizers.Adam</code></a>.

### Usage

```python
# Create an optimizer with the desired parameters.
opt = tf.keras.optimizers.SGD(learning_rate=0.1)
# `loss` is a callable that takes no argument and returns the value
# to minimize.
loss = lambda: 3 * var1 * var1 + 2 * var2 * var2
# In graph mode, returns op that minimizes the loss by updating the listed
# variables.
opt_op = opt.minimize(loss, var_list=[var1, var2])
opt_op.run()
# In eager mode, simply call minimize to update the list of variables.
opt.minimize(loss, var_list=[var1, var2])
```

### Custom training loop with Keras models

In Keras models, sometimes variables are created when the model is first
called, instead of construction time. Examples include 1) sequential models
without input shape pre-defined, or 2) subclassed models. Pass var_list as
callable in these cases.

#### Example:


```python
opt = tf.keras.optimizers.SGD(learning_rate=0.1)
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(num_hidden, activation='relu'))
model.add(tf.keras.layers.Dense(num_classes, activation='sigmoid')
loss_fn = lambda: tf.keras.losses.mse(model(input), output)
var_list_fn = lambda: model.trainable_weights
for input, output in data:
  opt.minimize(loss_fn, var_list_fn)
```

### Processing gradients before applying them.

Calling `minimize()` takes care of both computing the gradients and
applying them to the variables.  If you want to process the gradients
before applying them you can instead use the optimizer in three steps:

1.  Compute the gradients with <a href="../../../tf/GradientTape"><code>tf.GradientTape</code></a>.
2.  Process the gradients as you wish.
3.  Apply the processed gradients with `apply_gradients()`.

#### Example:



```python
# Create an optimizer.
opt = tf.keras.optimizers.SGD(learning_rate=0.1)

# Compute the gradients for a list of variables.
with tf.GradientTape() as tape:
  loss = <call_loss_function>
vars = <list_of_variables>
grads = tape.gradient(loss, vars)
processed_grads = [process_gradient(g) for g in grads]
grads_and_vars = zip(processed_grads, var_list)

# grads_and_vars is a list of tuples (gradient, variable).  Do whatever you
# need to the 'gradient' part, for example cap them, etc.
capped_grads_and_vars = [(MyCapper(gv[0]), gv[1]) for gv in grads_and_vars]

# Ask the optimizer to apply the capped gradients.
opt.apply_gradients(capped_grads_and_vars)
```

### Use with <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.

This optimizer class is <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> aware, which means it
automatically sums gradients across all replicas. To average gradients,
you divide your loss by the global batch size, which is done
automatically if you use <a href="../../../tf/keras"><code>tf.keras</code></a> built-in training or evaluation loops.
See the `reduction` argument of your loss which should be set to
`tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE` for averaging or
`tf.keras.losses.Reduction.SUM` for not.

If you are not using these and you want to average gradients, you should use
<a href="../../../tf/math/reduce_sum"><code>tf.math.reduce_sum</code></a> to add up your per-example losses and then divide by the
global batch size. Note that when using <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>, the first
component of a tensor's shape is the *replica-local* batch size, which is off
by a factor equal to the number of replicas being used to compute a single
step. As a result, using <a href="../../../tf/math/reduce_mean"><code>tf.math.reduce_mean</code></a> will give the wrong answer,
resulting in gradients that can be many times too big.

### Variable Constraint

All Keras optimizers respect variable constraints. If constraint function is
passed to any variable, the constraint will be applied to the variable after
the gradient has been applied to the variable.
Important: If gradient is sparse tensor, variable constraint is not supported.

### Thread Compatibility

The entire optimizer is currently thread compatible, not thread-safe. The user
needs to perform synchronization if necessary.

### Slots

Many optimizer subclasses, such as `Adam` and `Adagrad` allocate and manage
additional variables associated with the variables to train.  These are called
<i>Slots</i>.  Slots have names and you can ask the optimizer for the names of
the slots that it uses.  Once you have a slot name you can ask the optimizer
for the variable it created to hold the slot value.

This can be useful if you want to log debug a training algorithm, report stats
about the slots, etc.

### Hyper parameters

These are arguments passed to the optimizer subclass constructor
(the `__init__` method), and then passed to `self._set_hyper()`.
They can be either regular Python values (like 1.0), tensors, or
callables. If they are callable, the callable will be called during
`apply_gradients()` to get the value for the hyper parameter.

Hyper parameters can be overwritten through user code:

#### Example:



```python
# Create an optimizer with the desired parameters.
opt = tf.keras.optimizers.SGD(learning_rate=0.1)
# `loss` is a callable that takes no argument and returns the value
# to minimize.
loss = lambda: 3 * var1 + 2 * var2
# In eager mode, simply call minimize to update the list of variables.
opt.minimize(loss, var_list=[var1, var2])
# update learning rate
opt.learning_rate = 0.05
opt.minimize(loss, var_list=[var1, var2])
```

### Write a customized optimizer.
If you intend to create your own optimization algorithm, simply inherit from
this class and override the following methods:

  - resource_apply_dense (update variable given gradient tensor is dense)
  - resource_apply_sparse (update variable given gradient tensor is sparse)
  - create_slots (if your optimizer algorithm requires additional variables)
  - get_config (serialization of the optimizer, include all hyper parameters)

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name,
    **kwargs
)
```

Create a new Optimizer.

This must be called by the constructors of subclasses.
Note that Optimizer instances should not bind to a single graph,
and so shouldn't keep Tensors as member variables. Generally
you should be able to use the _set_hyper()/state.get_hyper()
facility instead.

This class in stateful and thread-compatible.

#### Args:


* <b>`name`</b>: A non-empty string.  The name to use for accumulators created
  for the optimizer.
* <b>`**kwargs`</b>: keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`,
  `decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip
  gradients by value, `decay` is included for backward compatibility to
  allow time inverse decay of learning rate. `lr` is included for backward
  compatibility, recommended to use `learning_rate` instead.


#### Raises:


* <b>`ValueError`</b>: If name is malformed.
* <b>`RuntimeError`</b>: If _create_slots has been overridden instead of
    _create_vars.



## Properties

<h3 id="iterations"><code>iterations</code></h3>

Variable. The number of training steps this Optimizer has run.


<h3 id="weights"><code>weights</code></h3>

Returns variables of this Optimizer based on the order created.




## Methods

<h3 id="add_slot"><code>add_slot</code></h3>

``` python
add_slot(
    var,
    slot_name,
    initializer='zeros'
)
```

Add a new slot variable for `var`.


<h3 id="add_weight"><code>add_weight</code></h3>

``` python
add_weight(
    name,
    shape,
    dtype=None,
    initializer='zeros',
    trainable=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.VariableAggregation.NONE
)
```




<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    name=None
)
```

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that
applies gradients.

#### Args:


* <b>`grads_and_vars`</b>: List of (gradient, variable) pairs.
* <b>`name`</b>: Optional name for the returned operation.  Default to the name
  passed to the `Optimizer` constructor.


#### Returns:

An `Operation` that applies the specified gradients. If `global_step`
was not None, that operation also increments `global_step`.



#### Raises:


* <b>`TypeError`</b>: If `grads_and_vars` is malformed.
* <b>`ValueError`</b>: If none of the variables have gradients.

<h3 id="from_config"><code>from_config</code></h3>

``` python
@classmethod
from_config(
    cls,
    config,
    custom_objects=None
)
```

Creates an optimizer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same optimizer from the config
dictionary.

#### Arguments:


* <b>`config`</b>: A Python dictionary, typically the output of get_config.
* <b>`custom_objects`</b>: A Python dictionary mapping names to additional Python
  objects used to create this optimizer, such as a function used for a
  hyperparameter.


#### Returns:

An optimizer instance.


<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```

Returns the config of the optimimizer.

An optimizer config is a Python dictionary (serializable)
containing the configuration of an optimizer.
The same optimizer can be reinstantiated later
(without any saved state) from this configuration.

#### Returns:

Python dictionary.


<h3 id="get_gradients"><code>get_gradients</code></h3>

``` python
get_gradients(
    loss,
    params
)
```

Returns gradients of `loss` with respect to `params`.


#### Arguments:


* <b>`loss`</b>: Loss tensor.
* <b>`params`</b>: List of variables.


#### Returns:

List of gradient tensors.



#### Raises:


* <b>`ValueError`</b>: In case any gradient cannot be computed (e.g. if gradient
  function not implemented).

<h3 id="get_slot"><code>get_slot</code></h3>

``` python
get_slot(
    var,
    slot_name
)
```




<h3 id="get_slot_names"><code>get_slot_names</code></h3>

``` python
get_slot_names()
```

A list of names for this optimizer's slots.


<h3 id="get_updates"><code>get_updates</code></h3>

``` python
get_updates(
    loss,
    params
)
```




<h3 id="get_weights"><code>get_weights</code></h3>

``` python
get_weights()
```




<h3 id="minimize"><code>minimize</code></h3>

``` python
minimize(
    loss,
    var_list,
    grad_loss=None,
    name=None
)
```

Minimize `loss` by updating `var_list`.

This method simply computes gradient using <a href="../../../tf/GradientTape"><code>tf.GradientTape</code></a> and calls
`apply_gradients()`. If you want to process the gradient before applying
then call <a href="../../../tf/GradientTape"><code>tf.GradientTape</code></a> and `apply_gradients()` explicitly instead
of using this function.

#### Args:


* <b>`loss`</b>: A callable taking no arguments which returns the value to minimize.
* <b>`var_list`</b>: list or tuple of `Variable` objects to update to minimize
  `loss`, or a callable returning the list or tuple of `Variable` objects.
  Use callable when the variable list would otherwise be incomplete before
  `minimize` since the variables are created at the first time `loss` is
  called.
* <b>`grad_loss`</b>: Optional. A `Tensor` holding the gradient computed for `loss`.
* <b>`name`</b>: Optional name for the returned operation.


#### Returns:

An Operation that updates the variables in `var_list`.  If `global_step`
was not `None`, that operation also increments `global_step`.



#### Raises:


* <b>`ValueError`</b>: If some of the variables are not `Variable` objects.

<h3 id="set_weights"><code>set_weights</code></h3>

``` python
set_weights(weights)
```




<h3 id="variables"><code>variables</code></h3>

``` python
variables()
```

Returns variables of this Optimizer based on the order created.




