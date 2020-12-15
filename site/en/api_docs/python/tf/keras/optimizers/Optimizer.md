description: Base class for Keras optimizers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.Optimizer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_slot"/>
<meta itemprop="property" content="add_weight"/>
<meta itemprop="property" content="apply_gradients"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
<meta itemprop="property" content="get_gradients"/>
<meta itemprop="property" content="get_slot"/>
<meta itemprop="property" content="get_slot_names"/>
<meta itemprop="property" content="get_updates"/>
<meta itemprop="property" content="get_weights"/>
<meta itemprop="property" content="minimize"/>
<meta itemprop="property" content="set_weights"/>
<meta itemprop="property" content="variables"/>
</div>

# tf.keras.optimizers.Optimizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L81-L1253">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class for Keras optimizers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.Optimizer`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.Optimizer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.Optimizer(
    name, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

You should not use this class directly, but instead instantiate one of its
subclasses such as <a href="../../../tf/keras/optimizers/SGD.md"><code>tf.keras.optimizers.SGD</code></a>, <a href="../../../tf/keras/optimizers/Adam.md"><code>tf.keras.optimizers.Adam</code></a>, etc.

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

### Usage in custom training loops

In Keras models, sometimes variables are created when the model is first
called, instead of construction time. Examples include 1) sequential models
without input shape pre-defined, or 2) subclassed models. Pass var_list as
callable in these cases.

#### Example:



```python
opt = tf.keras.optimizers.SGD(learning_rate=0.1)
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(num_hidden, activation='relu'))
model.add(tf.keras.layers.Dense(num_classes, activation='sigmoid'))
loss_fn = lambda: tf.keras.losses.mse(model(input), output)
var_list_fn = lambda: model.trainable_weights
for input, output in data:
  opt.minimize(loss_fn, var_list_fn)
```

### Processing gradients before applying them

Calling `minimize()` takes care of both computing the gradients and
applying them to the variables.  If you want to process the gradients
before applying them you can instead use the optimizer in three steps:

1.  Compute the gradients with <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>.
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

# Process the gradients, for example cap them, etc.
# capped_grads = [MyCapper(g) for g in grads]
processed_grads = [process_gradient(g) for g in grads]

# Ask the optimizer to apply the processed gradients.
opt.apply_gradients(zip(processed_grads, var_list))
```

### Use with <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>

This optimizer class is <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> aware, which means it
automatically sums gradients across all replicas. To average gradients,
you divide your loss by the global batch size, which is done
automatically if you use <a href="../../../tf/keras.md"><code>tf.keras</code></a> built-in training or evaluation loops.
See the `reduction` argument of your loss which should be set to
<a href="../../../tf/keras/losses/Reduction.md#SUM_OVER_BATCH_SIZE"><code>tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE</code></a> for averaging or
<a href="../../../tf/keras/losses/Reduction.md#SUM"><code>tf.keras.losses.Reduction.SUM</code></a> for not.

To aggregate gradients yourself, call `apply_gradients` with
`experimental_aggregate_gradients` set to False. This is useful if you need to
process aggregated gradients.

If you are not using these and you want to average gradients, you should use
<a href="../../../tf/math/reduce_sum.md"><code>tf.math.reduce_sum</code></a> to add up your per-example losses and then divide by the
global batch size. Note that when using <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>, the first
component of a tensor's shape is the *replica-local* batch size, which is off
by a factor equal to the number of replicas being used to compute a single
step. As a result, using <a href="../../../tf/math/reduce_mean.md"><code>tf.math.reduce_mean</code></a> will give the wrong answer,
resulting in gradients that can be many times too big.

### Variable Constraints

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

### Hyperparameters

These are arguments passed to the optimizer subclass constructor
(the `__init__` method), and then passed to `self._set_hyper()`.
They can be either regular Python values (like 1.0), tensors, or
callables. If they are callable, the callable will be called during
`apply_gradients()` to get the value for the hyper parameter.

Hyperparameters can be overwritten through user code:

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

### Callable learning rate

Optimizer accepts a callable learning rate in two ways. The first way is
through built-in or customized
<a href="../../../tf/keras/optimizers/schedules/LearningRateSchedule.md"><code>tf.keras.optimizers.schedules.LearningRateSchedule</code></a>. The schedule will be
called on each iteration with `schedule(iteration)`, a <a href="../../../tf/Variable.md"><code>tf.Variable</code></a>
owned by the optimizer.

#### Example:



```
>>> var = tf.Variable(np.random.random(size=(1,)))
>>> learning_rate = tf.keras.optimizers.schedules.ExponentialDecay(
... initial_learning_rate=.01, decay_steps=20, decay_rate=.1)
>>> opt = tf.keras.optimizers.SGD(learning_rate=learning_rate)
>>> loss = lambda: 3 * var
>>> opt.minimize(loss, var_list=[var])
<tf.Variable...
```

The second way is through a callable function that
does not accept any arguments.

#### Example:



```
>>> var = tf.Variable(np.random.random(size=(1,)))
>>> def lr_callable():
...   return .1
>>> opt = tf.keras.optimizers.SGD(learning_rate=lr_callable)
>>> loss = lambda: 3 * var
>>> opt.minimize(loss, var_list=[var])
<tf.Variable...
```

### Creating a custom optimizer

If you intend to create your own optimization algorithm, simply inherit from
this class and override the following methods:

  - `_resource_apply_dense` (update variable given gradient tensor is dense)
  - `_resource_apply_sparse` (update variable given gradient tensor is sparse)
  - `_create_slots`
    (if your optimizer algorithm requires additional variables)
  - `get_config`
    (serialization of the optimizer, include all hyper parameters)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
A non-empty string.  The name to use for accumulators created
for the optimizer.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`,
`decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip
gradients by value, `decay` is included for backward compatibility to
allow time inverse decay of learning rate. `lr` is included for backward
compatibility, recommended to use `learning_rate` instead.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If name is malformed.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`iterations`
</td>
<td>
Variable. The number of training steps this Optimizer has run.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Returns variables of this Optimizer based on the order created.
</td>
</tr>
</table>



## Methods

<h3 id="add_slot"><code>add_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L735-L771">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_slot(
    var, slot_name, initializer='zeros'
)
</code></pre>

Add a new slot variable for `var`.


<h3 id="add_weight"><code>add_weight</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L1003-L1043">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_weight(
    name, shape, dtype=None, initializer='zeros', trainable=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.compat.v1.VariableAggregation.NONE
)
</code></pre>




<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L473-L550">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_gradients(
    grads_and_vars, name=None, experimental_aggregate_gradients=(True)
)
</code></pre>

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that
applies gradients.

The method sums gradients from all replicas in the presence of
<a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> by default. You can aggregate gradients yourself by
passing `experimental_aggregate_gradients=False`.

#### Example:



```python
grads = tape.gradient(loss, vars)
grads = tf.distribute.get_replica_context().all_reduce('sum', grads)
# Processing aggregated gradients.
optimizer.apply_gradients(zip(grads, vars),
    experimental_aggregate_gradients=False)

```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grads_and_vars`
</td>
<td>
List of (gradient, variable) pairs.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned operation. Default to the name passed
to the `Optimizer` constructor.
</td>
</tr><tr>
<td>
`experimental_aggregate_gradients`
</td>
<td>
Whether to sum gradients from different
replicas in the presense of <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>. If False, it's
user responsibility to aggregate the gradients. Default to True.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Operation` that applies the specified gradients. The `iterations`
will be automatically increased by 1.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `grads_and_vars` is malformed.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If none of the variables have gradients.
</td>
</tr>
</table>



<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L879-L902">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config, custom_objects=None
)
</code></pre>

Creates an optimizer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same optimizer from the config
dictionary.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`config`
</td>
<td>
A Python dictionary, typically the output of get_config.
</td>
</tr><tr>
<td>
`custom_objects`
</td>
<td>
A Python dictionary mapping names to additional Python
objects used to create this optimizer, such as a function used for a
hyperparameter.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An optimizer instance.
</td>
</tr>

</table>



<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L860-L877">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>get_config()
</code></pre>

Returns the config of the optimizer.

An optimizer config is a Python dictionary (serializable)
containing the configuration of an optimizer.
The same optimizer can be reinstantiated later
(without any saved state) from this configuration.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Python dictionary.
</td>
</tr>

</table>



<h3 id="get_gradients"><code>get_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L445-L471">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_gradients(
    loss, params
)
</code></pre>

Returns gradients of `loss` with respect to `params`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`loss`
</td>
<td>
Loss tensor.
</td>
</tr><tr>
<td>
`params`
</td>
<td>
List of variables.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
List of gradient tensors.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
In case any gradient cannot be computed (e.g. if gradient
function not implemented).
</td>
</tr>
</table>



<h3 id="get_slot"><code>get_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L773-L776">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot(
    var, slot_name
)
</code></pre>




<h3 id="get_slot_names"><code>get_slot_names</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L731-L733">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot_names()
</code></pre>

A list of names for this optimizer's slots.


<h3 id="get_updates"><code>get_updates</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L647-L654">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_updates(
    loss, params
)
</code></pre>




<h3 id="get_weights"><code>get_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L924-L952">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_weights()
</code></pre>

Returns the current weights of the optimizer.

The weights of an optimizer are its state (ie, variables).
This function returns the weight values associated with this
optimizer as a list of Numpy arrays. The first value is always the
iterations count of the optimizer, followed by the optimizer's state
variables in the order they were created. The returned list can in turn
be used to load state into similarly parameterized optimizers.

For example, the RMSprop optimizer for this simple model returns a list of
three values-- the iteration count, followed by the root-mean-square value
of the kernel and bias of the single Dense layer:

```
>>> opt = tf.keras.optimizers.RMSprop()
>>> m = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
>>> m.compile(opt, loss='mse')
>>> data = np.arange(100).reshape(5, 20)
>>> labels = np.zeros(5)
>>> print('Training'); results = m.fit(data, labels)
Training ...
>>> len(opt.get_weights())
3
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Weights values as a list of numpy arrays.
</td>
</tr>

</table>



<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L348-L377">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>minimize(
    loss, var_list, grad_loss=None, name=None
)
</code></pre>

Minimize `loss` by updating `var_list`.

This method simply computes gradient using <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> and calls
`apply_gradients()`. If you want to process the gradient before applying
then call <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> and `apply_gradients()` explicitly instead
of using this function.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
A callable taking no arguments which returns the value to minimize.
</td>
</tr><tr>
<td>
`var_list`
</td>
<td>
list or tuple of `Variable` objects to update to minimize
`loss`, or a callable returning the list or tuple of `Variable` objects.
Use callable when the variable list would otherwise be incomplete before
`minimize` since the variables are created at the first time `loss` is
called.
</td>
</tr><tr>
<td>
`grad_loss`
</td>
<td>
Optional. A `Tensor` holding the gradient computed for `loss`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Operation` that updates the variables in `var_list`. The `iterations`
will be automatically increased by 1.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If some of the variables are not `Variable` objects.
</td>
</tr>
</table>



<h3 id="set_weights"><code>set_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L955-L1001">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_weights(
    weights
)
</code></pre>

Set the weights of the optimizer.

The weights of an optimizer are its state (ie, variables).
This function takes the weight values associated with this
optimizer as a list of Numpy arrays. The first value is always the
iterations count of the optimizer, followed by the optimizer's state
variables in the order they are created. The passed values are used to set
the new state of the optimizer.

For example, the RMSprop optimizer for this simple model takes a list of
three values-- the iteration count, followed by the root-mean-square value
of the kernel and bias of the single Dense layer:

```
>>> opt = tf.keras.optimizers.RMSprop()
>>> m = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
>>> m.compile(opt, loss='mse')
>>> data = np.arange(100).reshape(5, 20)
>>> labels = np.zeros(5)
>>> print('Training'); results = m.fit(data, labels)
Training ...
>>> new_weights = [np.array(10), np.ones([20, 10]), np.zeros([10])]
>>> opt.set_weights(new_weights)
>>> opt.iterations
<tf.Variable 'RMSprop/iter:0' shape=() dtype=int64, numpy=10>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`weights`
</td>
<td>
weight values as a list of numpy arrays.
</td>
</tr>
</table>



<h3 id="variables"><code>variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L915-L917">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variables()
</code></pre>

Returns variables of this Optimizer based on the order created.




