description: Optimizer that implements the RMSprop algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.RMSprop" />
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

# tf.keras.optimizers.RMSprop

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/rmsprop.py#L35-L298">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the RMSprop algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.RMSprop`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.RMSprop`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.RMSprop(
    learning_rate=0.001, rho=0.9, momentum=0.0, epsilon=1e-07, centered=(False),
    name='RMSprop', **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The gist of RMSprop is to:

- Maintain a moving (discounted) average of the square of gradients
- Divide the gradient by the root of this average

This implementation of RMSprop uses plain momentum, not Nesterov momentum.

The centered version additionally maintains a moving average of the
gradients, and uses that average to estimate the variance.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`
</td>
<td>
A `Tensor`, floating point value, or a schedule that is a
<a href="../../../tf/keras/optimizers/schedules/LearningRateSchedule.md"><code>tf.keras.optimizers.schedules.LearningRateSchedule</code></a>, or a callable
that takes no arguments and returns the actual value to use. The
learning rate. Defeaults to 0.001.
</td>
</tr><tr>
<td>
`rho`
</td>
<td>
Discounting factor for the history/coming gradient. Defaults to 0.9.
</td>
</tr><tr>
<td>
`momentum`
</td>
<td>
A scalar or a scalar `Tensor`. Defaults to 0.0.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A small constant for numerical stability. This epsilon is
"epsilon hat" in the Kingma and Ba paper (in the formula just before
Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to
1e-7.
</td>
</tr><tr>
<td>
`centered`
</td>
<td>
Boolean. If `True`, gradients are normalized by the estimated
variance of the gradient; if False, by the uncentered second moment.
Setting this to `True` may help with training, but is slightly more
expensive in terms of computation and memory. Defaults to `False`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the operations created when applying
gradients. Defaults to `"RMSprop"`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments. Allowed to be one of
`"clipnorm"` or `"clipvalue"`.
`"clipnorm"` (float) clips gradients by norm; `"clipvalue"` (float) clips
gradients by value.
</td>
</tr>
</table>


Note that in the dense implementation of this algorithm, variables and their
corresponding accumulators (momentum, gradient moving average, square
gradient moving average) will be updated even if the gradient is zero
(i.e. accumulators will decay, momentum will be applied). The sparse
implementation (used when the gradient is an `IndexedSlices` object,
typically because of <a href="../../../tf/gather.md"><code>tf.gather</code></a> or an embedding lookup in the forward pass)
will not update variable slices or their accumulators unless those slices
were used in the forward pass (nor is there an "eventual" correction to
account for these omitted updates). This leads to more efficient updates for
large embedding lookup tables (where most of the slices are not accessed in
a particular graph execution), but differs from the published algorithm.

#### Usage:



```
>>> opt = tf.keras.optimizers.RMSprop(learning_rate=0.1)
>>> var1 = tf.Variable(10.0)
>>> loss = lambda: (var1 ** 2) / 2.0    # d(loss) / d(var1) = var1
>>> step_count = opt.minimize(loss, [var1]).numpy()
>>> var1.numpy()
9.683772
```

#### Reference:

- [Hinton, 2012](
  http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`
</td>
<td>
A `Tensor`, floating point value, or a schedule that is a
<a href="../../../tf/keras/optimizers/schedules/LearningRateSchedule.md"><code>tf.keras.optimizers.schedules.LearningRateSchedule</code></a>, or a callable
that takes no arguments and returns the actual value to use. The
learning rate. Defeaults to 0.001.
</td>
</tr><tr>
<td>
`rho`
</td>
<td>
Discounting factor for the history/coming gradient. Defaults to 0.9.
</td>
</tr><tr>
<td>
`momentum`
</td>
<td>
A scalar or a scalar `Tensor`. Defaults to 0.0.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A small constant for numerical stability. This epsilon is
"epsilon hat" in the Kingma and Ba paper (in the formula just before
Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to
1e-7.
</td>
</tr><tr>
<td>
`centered`
</td>
<td>
Boolean. If `True`, gradients are normalized by the estimated
variance of the gradient; if False, by the uncentered second moment.
Setting this to `True` may help with training, but is slightly more
expensive in terms of computation and memory. Defaults to `False`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the operations created when applying
gradients. Defaults to "RMSprop".
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/rmsprop.py#L288-L298">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/rmsprop.py#L279-L286">View source</a>

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




