description: An optimizer that applies loss scaling.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.mixed_precision.experimental.LossScaleOptimizer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_slot"/>
<meta itemprop="property" content="add_weight"/>
<meta itemprop="property" content="apply_gradients"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
<meta itemprop="property" content="get_gradients"/>
<meta itemprop="property" content="get_scaled_loss"/>
<meta itemprop="property" content="get_slot"/>
<meta itemprop="property" content="get_slot_names"/>
<meta itemprop="property" content="get_unscaled_gradients"/>
<meta itemprop="property" content="get_updates"/>
<meta itemprop="property" content="get_weights"/>
<meta itemprop="property" content="minimize"/>
<meta itemprop="property" content="set_weights"/>
<meta itemprop="property" content="variables"/>
</div>

# tf.keras.mixed_precision.experimental.LossScaleOptimizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L52-L374">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An optimizer that applies loss scaling.

Inherits From: [`Optimizer`](../../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.mixed_precision.experimental.LossScaleOptimizer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.experimental.LossScaleOptimizer(
    optimizer, loss_scale
)
</code></pre>



<!-- Placeholder for "Used in" -->

Loss scaling is a process that multiplies the loss by a multiplier called the
loss scale, and divides each gradient by the same multiplier. The pseudocode
for this process is:

```
loss = ...
loss *= loss_scale
grads = gradients(loss, vars)
grads /= loss_scale
```

Mathematically, loss scaling has no effect, but can help avoid numerical
underflow in intermediate gradients when float16 tensors are used. By
multiplying the loss, each intermediate gradient will have the same multiplier
applied.

The loss scale can either be a fixed constant, chosen by the user, or be
dynamically determined. Dynamically determining the loss scale is convenient
as a loss scale does not have to be explicitly chosen. However it reduces
performance.

This optimizer wraps another optimizer and applies loss scaling to it via a
`LossScale`. Loss scaling is applied whenever gradients are
computed, either through `minimize()` or `get_gradients()`. The loss scale is
updated via <a href="../../../../tf/mixed_precision/experimental/LossScale.md#update"><code>LossScale.update()</code></a> whenever gradients are applied, either
through `minimize()` or `apply_gradients()`. For example:

```
>>> opt = tf.keras.optimizers.SGD(0.25)
>>> opt = tf.keras.mixed_precision.experimental.LossScaleOptimizer(opt,
...                                                                "dynamic")
>>> var = tf.Variable(1.)
>>> loss_fn = lambda: var ** 2
>>> # 'minimize' applies loss scaling to the loss and updates the loss sale.
>>> opt.minimize(loss_fn, var_list=var)
>>> var.numpy()
0.5
```

If a <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> is used to compute gradients instead of
<a href="../../../../tf/keras/optimizers/Optimizer.md#minimize"><code>LossScaleOptimizer.minimize</code></a> or <a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#get_gradients"><code>LossScaleOptimizer.get_gradients</code></a>, the loss
and gradients must be scaled manually. This can be done by calling
<a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#get_scaled_loss"><code>LossScaleOptimizer.get_scaled_loss</code></a> before passing the loss to
<a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>, and <a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#get_unscaled_gradients"><code>LossScaleOptimizer.get_unscaled_gradients</code></a> after
computing the gradients with <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. For example:

```
>>> with tf.GradientTape() as tape:
...   loss = loss_fn()
...   scaled_loss = opt.get_scaled_loss(loss)
>>> scaled_grad = tape.gradient(scaled_loss, var)
>>> (grad,) = opt.get_unscaled_gradients([scaled_grad])
>>> opt.apply_gradients([(grad, var)])  # Loss scale is updated here
>>> var.numpy()
0.25
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`optimizer`
</td>
<td>
The Optimizer instance to wrap.
</td>
</tr><tr>
<td>
`loss_scale`
</td>
<td>
The loss scale to scale the loss and gradients. This can
either be an int/float to use a fixed loss scale, the string "dynamic"
to use dynamic loss scaling, or an instance of a LossScale. The string
"dynamic" equivalent to passing `DynamicLossScale()`, and passing an
int/float is equivalent to passing a FixedLossScale with the given loss
scale.
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
`learning_rate`
</td>
<td>

</td>
</tr><tr>
<td>
`loss_scale`
</td>
<td>
The `LossScale` instance associated with this optimizer.
</td>
</tr><tr>
<td>
`lr`
</td>
<td>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L370-L374">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_slot(
    var, slot_name, initializer='zeros'
)
</code></pre>

Add a new slot variable for `var`.


<h3 id="add_weight"><code>add_weight</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L960-L1000">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_weight(
    name, shape, dtype=None, initializer='zeros', trainable=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.compat.v1.VariableAggregation.NONE
)
</code></pre>




<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L234-L247">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_gradients(
    grads_and_vars, name=None, experimental_aggregate_gradients=(True)
)
</code></pre>

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that
applies gradients.

The method sums gradients from all replicas in the presence of
<a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> by default. You can aggregate gradients yourself by
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
replicas in the presense of <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>. If False, it's
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L291-L298">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L283-L289">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L226-L229">View source</a>

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



<h3 id="get_scaled_loss"><code>get_scaled_loss</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L162-L189">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_scaled_loss(
    loss
)
</code></pre>

Scales the loss by the loss scale.

This method is only needed if you compute gradients manually, e.g. with
<a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. In that case, call this method to scale the loss before
passing the loss to <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. If you use
<a href="../../../../tf/keras/optimizers/Optimizer.md#minimize"><code>LossScaleOptimizer.minimize</code></a> or <a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#get_gradients"><code>LossScaleOptimizer.get_gradients</code></a>, loss
scaling is automatically applied and this method is unneeded.

If this method is called, `get_unscaled_gradients` should also be called.
See the <a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.experimental.LossScaleOptimizer</code></a> doc for
an example.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
The loss, which will be multiplied by the loss scale. Can either be
a tensor or a callable returning a tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`loss` multiplied by <a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#loss_scale"><code>LossScaleOptimizer.loss_scale()</code></a>.
</td>
</tr>

</table>



<h3 id="get_slot"><code>get_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L359-L368">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot(
    var, slot_name
)
</code></pre>




<h3 id="get_slot_names"><code>get_slot_names</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L319-L320">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot_names()
</code></pre>

A list of names for this optimizer's slots.


<h3 id="get_unscaled_gradients"><code>get_unscaled_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L191-L215">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_unscaled_gradients(
    grads
)
</code></pre>

Unscales the gradients by the loss scale.

This method is only needed if you compute gradients manually, e.g. with
<a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. In that case, call this method to unscale the gradients
after computing them with <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. If you use
<a href="../../../../tf/keras/optimizers/Optimizer.md#minimize"><code>LossScaleOptimizer.minimize</code></a> or <a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#get_gradients"><code>LossScaleOptimizer.get_gradients</code></a>, loss
scaling is automatically applied and this method is unneeded.

If this method is called, `get_scaled_loss` should also be called. See
the <a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.experimental.LossScaleOptimizer</code></a> doc for an
example.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grads`
</td>
<td>
A list of tensors, each which will be divided by the loss scale.
Can have None values, which are ignored.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A new list the same size as `grads`, where every non-None value in `grads`
is divided by <a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#loss_scale"><code>LossScaleOptimizer.loss_scale()</code></a>.
</td>
</tr>

</table>



<h3 id="get_updates"><code>get_updates</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L606-L613">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_updates(
    loss, params
)
</code></pre>




<h3 id="get_weights"><code>get_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L329-L330">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L307-L336">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>minimize(
    loss, var_list, grad_loss=None, name=None
)
</code></pre>

Minimize `loss` by updating `var_list`.

This method simply computes gradient using <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> and calls
`apply_gradients()`. If you want to process the gradient before applying
then call <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> and `apply_gradients()` explicitly instead
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L332-L333">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/loss_scale_optimizer.py#L322-L323">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variables()
</code></pre>

Returns variables of this Optimizer based on the order created.




