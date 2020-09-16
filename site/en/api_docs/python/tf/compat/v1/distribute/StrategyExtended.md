description: Additional APIs for algorithms that need to be distribution-aware.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distribute.StrategyExtended" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="batch_reduce_to"/>
<meta itemprop="property" content="broadcast_to"/>
<meta itemprop="property" content="call_for_each_replica"/>
<meta itemprop="property" content="colocate_vars_with"/>
<meta itemprop="property" content="experimental_make_numpy_dataset"/>
<meta itemprop="property" content="experimental_run_steps_on_iterator"/>
<meta itemprop="property" content="non_slot_devices"/>
<meta itemprop="property" content="read_var"/>
<meta itemprop="property" content="reduce_to"/>
<meta itemprop="property" content="update"/>
<meta itemprop="property" content="update_non_slot"/>
<meta itemprop="property" content="value_container"/>
<meta itemprop="property" content="variable_created_in_scope"/>
</div>

# tf.compat.v1.distribute.StrategyExtended

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2144-L2332">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Additional APIs for algorithms that need to be distribution-aware.

Inherits From: [`StrategyExtended`](../../../../tf/distribute/StrategyExtended.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.distribute.StrategyExtended(
    container_strategy
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: For most usage of <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>, there should be no need to
call these methods, since TensorFlow libraries (such as optimizers) already
call these methods when needed on your behalf.

Lower-level concepts:

* Wrapped values: In order to represent values parallel across devices
  (either replicas or the devices associated with a particular value), we
  wrap them in a "PerReplica" or "Mirrored" object that contains a map
  from replica id to values. "PerReplica" is used when the value may be
  different across replicas, and "Mirrored" when the value are the same.
* Unwrapping and merging: Consider calling a function `fn` on multiple
  replicas, like `run(fn, args=[w])` with an
  argument `w` that is a wrapped value. This means `w` will have a map taking
  replica id `0` to `w0`, replica id `11` to `w1`, etc.
  `run()` unwraps `w` before calling `fn`, so
  it calls `fn(w0)` on `d0`, `fn(w1)` on `d1`, etc.  It then merges the return
  values from `fn()`, which can possibly result in wrapped values. For
  example, let's say `fn()` returns a tuple with three components: `(x, a,
  v0)` from replica 0, `(x, b, v1)` on replica 1, etc. If the first component
  is the same object `x` from every replica, then the first component of the
  merged result will also be `x`. If the second component is different (`a`,
  `b`, ...)  from each replica, then the merged value will have a wrapped map
  from replica device to the different values. If the third component is the
  members of a mirrored variable (`v` maps `d0` to `v0`, `d1` to <a href="../../../../tf/compat/v1.md"><code>v1</code></a>, etc.),
  then the merged result will be that mirrored variable (`v`).
* Worker devices vs. parameter devices: Most replica computations will
  happen on worker devices. Since we don't yet support model
  parallelism, there will be one worker device per replica. When using
  parameter servers or central storage, the set of devices holding
  variables may be different, otherwise the parameter devices might
  match the worker devices.

*Replica context vs. Cross-replica context*

A _replica context_ applies when we are in some function that is being called
once for each replica.  Otherwise we are in cross-replica context, which is
useful for calling <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> methods which operate across the
replicas (like `reduce_to()`). By default you start in a replica context
(the "default single replica context") and then some methods can switch you
back and forth. There is a third mode you can be in called _update context_
used when updating variables.

* <a href="../../../../tf/distribute/Strategy.md#scope"><code>tf.distribute.Strategy.scope</code></a>: enters cross-replica context when
  no other strategy is in scope.
* <a href="../../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a>: calls a function in
  replica context.
* <a href="../../../../tf/distribute/ReplicaContext.md#merge_call"><code>tf.distribute.ReplicaContext.merge_call</code></a>: transitions from replica
  context to cross-replica context.
* <a href="../../../../tf/distribute/StrategyExtended.md#update"><code>tf.distribute.StrategyExtended.update</code></a>: calls a function in an update
  context from a cross-replica context.

In a replica context, you may freely read the values of variables, but
you may only update their value if they specify a way to aggregate the
update using the `aggregation` parameter in the variable's constructor.
In a cross-replica context, you may read or write variables (writes may
need to be broadcast to all copies of the variable if it is mirrored).

*Sync on read variables*

In some cases, such as a metric, we want to accumulate a bunch of updates on
each replica independently and only aggregate when reading. This can be a big
performance win when the value is read only rarely (maybe the value is only
read at the end of an epoch or when checkpointing).  These are variables
created by passing `synchronization=ON_READ` to the variable's constructor
(and some value for `aggregation`).

The strategy may choose to put the variable on multiple devices, like mirrored
variables, but unlike mirrored variables we don't synchronize the updates to
them to make sure they have the same value. Instead, the synchronization is
performed when reading in cross-replica context.  In a replica context, reads
and writes are performed on the local copy (we allow reads so you can write
code like `v = 0.9*v + 0.1*update`).  We don't allow operations like
`v.assign_add` in a cross-replica context for sync on read variables; right
now we don't have a use case for such updates and depending on the aggregation
mode such updates may not be sensible.

*Locality*

Depending on how a value is produced, it will have a type that will determine
how it may be used.

"Per-replica" values exist on the worker devices, with a different value for
each replica. They are produced by iterating through a "distributed `Dataset`"
returned by <a href="../../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> and
<a href="../../../../tf/distribute/Strategy.md#experimental_distribute_datasets_from_function"><code>tf.distribute.Strategy.experimental_distribute_datasets_from_function</code></a>.  They
are also the typical result returned by
<a href="../../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a>. You typically can't use a
per-replica value directly in a cross-replica context, without first resolving
how to aggregate the values across replicas, for instance by using
<a href="../../../../tf/distribute/Strategy.md#reduce"><code>tf.distribute.Strategy.reduce</code></a>.

"Mirrored" values are like per-replica values, except we know that the value
on all replicas are the same. We can safely read a mirrored value in a
cross-replica context by using the value on any replica. You can convert
a per-replica value into a mirrored value by using
<a href="../../../../tf/distribute/ReplicaContext.md#all_reduce"><code>tf.distribute.ReplicaContext.all_reduce</code></a>.

Values can also have the same locality as a variable, which is a mirrored
value but residing on the same devices as the variable (as opposed to the
compute devices). Such values may be passed to a call to
<a href="../../../../tf/distribute/StrategyExtended.md#update"><code>tf.distribute.StrategyExtended.update</code></a> to update the value of a variable.
You may use <a href="../../../../tf/distribute/StrategyExtended.md#colocate_vars_with"><code>tf.distribute.StrategyExtended.colocate_vars_with</code></a> to give a
variable the same locality as another variable. This is useful, for example,
for "slot" variables used by an optimizer for keeping track of statistics
used to update a primary/model variable. You may convert a per-replica
value to a variable's locality by using
<a href="../../../../tf/distribute/StrategyExtended.md#reduce_to"><code>tf.distribute.StrategyExtended.reduce_to</code></a> or
<a href="../../../../tf/distribute/StrategyExtended.md#batch_reduce_to"><code>tf.distribute.StrategyExtended.batch_reduce_to</code></a>.

In addition to slot variables which should be colocated with their primary
variables, optimizers also define non-slot variables. These can be things like
"number of step updates performed" or "beta1^t" and "beta2^t".  Each strategy
has some policy for which devices those variables should be copied too, called
the "non-slot devices" (some subset of the parameter devices). We require that
all non-slot variables are allocated on the same device, or mirrored across
the same set of devices. You can use
<a href="../../../../tf/distribute/StrategyExtended.md#non_slot_devices"><code>tf.distribute.StrategyExtended.non_slot_devices</code></a> to pick a consistent set of
devices to pass to both <a href="../../../../tf/distribute/StrategyExtended.md#colocate_vars_with"><code>tf.distribute.StrategyExtended.colocate_vars_with</code></a>
and <a href="../../../../tf/distribute/StrategyExtended.md#update_non_slot"><code>tf.distribute.StrategyExtended.update_non_slot</code></a>.

*How to update a variable*

The standard pattern for updating variables is to:

1. In your function passed to <a href="../../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a>,
   compute a list of (update, variable) pairs. For example, the update might
   be a the gradient of the loss with respect to the variable.
2. Switch to cross-replica mode by calling
   `tf.distribute.get_replica_context().merge_call()` with the updates and
   variables as arguments.
3. Call
   <a href="../../../../tf/distribute/StrategyExtended.md#reduce_to"><code>tf.distribute.StrategyExtended.reduce_to(VariableAggregation.SUM, t, v)</code></a>
   (for one variable) or <a href="../../../../tf/distribute/StrategyExtended.md#batch_reduce_to"><code>tf.distribute.StrategyExtended.batch_reduce_to</code></a>
   (for a list of variables) to sum the updates.
   and broadcast the result to the variable's devices.
4. Call <a href="../../../../tf/distribute/StrategyExtended.md#update"><code>tf.distribute.StrategyExtended.update(v)</code></a> for each variable to update
   its value.

Steps 2 through 4 are done automatically by class
<a href="../../../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a> if you call its
<a href="../../../../tf/keras/optimizers/Optimizer.md#apply_gradients"><code>tf.keras.optimizers.Optimizer.apply_gradients</code></a> method in a replica context.
They are also done automatically if you call an `assign*` method on a (non
sync-on-read) variable that was constructed with an aggregation method (which
is used to determine the reduction used in step 3).

*Distribute-aware layers*

Layers are generally called in a replica context, except when defining a
functional model. <a href="../../../../tf/distribute/in_cross_replica_context.md"><code>tf.distribute.in_cross_replica_context</code></a> will let you
determine which case you are in. If in a replica context,
the <a href="../../../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context</code></a> function will return a
<a href="../../../../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> object. The `ReplicaContext` object has an
`all_reduce` method for aggregating across all replicas. Alternatively, you
can update variables following steps 2-4 above.

Note: For new <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> implementations, please put all logic
in a subclass of <a href="../../../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a>. The only code needed for
the <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> subclass is for instantiating your subclass of
<a href="../../../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> in the `__init__` method.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`experimental_between_graph`
</td>
<td>
Whether the strategy uses between-graph replication or not.

This is expected to return a constant value that will not be changed
throughout its life cycle.
</td>
</tr><tr>
<td>
`experimental_require_static_shapes`
</td>
<td>
Returns `True` if static shape is required; `False` otherwise.
</td>
</tr><tr>
<td>
`experimental_should_init`
</td>
<td>
Whether initialization is needed.
</td>
</tr><tr>
<td>
`parameter_devices`
</td>
<td>
Returns the tuple of all devices used to place variables.
</td>
</tr><tr>
<td>
`should_checkpoint`
</td>
<td>
Whether checkpointing is needed.
</td>
</tr><tr>
<td>
`should_save_summary`
</td>
<td>
Whether saving summaries is needed.
</td>
</tr><tr>
<td>
`worker_devices`
</td>
<td>
Returns the tuple of all devices used to for compute replica execution.
</td>
</tr>
</table>



## Methods

<h3 id="batch_reduce_to"><code>batch_reduce_to</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1936-L1960">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_reduce_to(
    reduce_op, value_destination_pairs, experimental_hints=None
)
</code></pre>

Combine multiple `reduce_to` calls into one for faster execution.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
Reduction type, an instance of <a href="../../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> enum.
</td>
</tr><tr>
<td>
`value_destination_pairs`
</td>
<td>
A sequence of (value, destinations) pairs. See
`reduce_to()` for a description.
</td>
</tr><tr>
<td>
`experimental_hints`
</td>
<td>
A `tf.distrbute.experimental.CollectiveHints`. Hints
to perform collective operations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of mirrored values, one per pair in `value_destination_pairs`.
</td>
</tr>

</table>



<h3 id="broadcast_to"><code>broadcast_to</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2171-L2186">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>broadcast_to(
    tensor, destinations
)
</code></pre>

Mirror a tensor on one device to all worker devices.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor`
</td>
<td>
A Tensor value to broadcast.
</td>
</tr><tr>
<td>
`destinations`
</td>
<td>
A mirrored variable or device string specifying the
destination devices to copy `tensor` to.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A value mirrored to `destinations` devices.
</td>
</tr>

</table>



<h3 id="call_for_each_replica"><code>call_for_each_replica</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2242-L2290">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>call_for_each_replica(
    fn, args=(), kwargs=None
)
</code></pre>

Run `fn` once per replica.

`fn` may call `tf.get_replica_context()` to access methods such as
`replica_id_in_sync_group` and `merge_call()`.

`merge_call()` is used to communicate between the replicas and
re-enter the cross-replica context. All replicas pause their execution
having encountered a `merge_call()` call. After that the
`merge_fn`-function is executed. Its results are then unwrapped and
given back to each replica call. After that execution resumes until
`fn` is complete or encounters another `merge_call()`.  Example:

```python
# Called once in "cross-replica" context.
def merge_fn(distribution, three_plus_replica_id):
  # sum the values across replicas
  return sum(distribution.experimental_local_results(three_plus_replica_id))

# Called once per replica in `distribution`, in a "replica" context.
def fn(three):
  replica_ctx = tf.get_replica_context()
  v = three + replica_ctx.replica_id_in_sync_group
  # Computes the sum of the `v` values across all replicas.
  s = replica_ctx.merge_call(merge_fn, args=(v,))
  return s + v

with distribution.scope():
  # in "cross-replica" context
  ...
  merged_results = distribution.run(fn, args=[3])
  # merged_results has the values from every replica execution of `fn`.
  # This statement prints a list:
  print(distribution.experimental_local_results(merged_results))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fn`
</td>
<td>
function to run (will be run once per replica).
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Tuple or list with positional arguments for `fn`.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Dict with keyword arguments for `fn`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Merged return value of `fn` across all replicas.
</td>
</tr>

</table>



<h3 id="colocate_vars_with"><code>colocate_vars_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1820-L1865">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>colocate_vars_with(
    colocate_with_variable
)
</code></pre>

Scope that controls which devices variables will be created on.

No operations should be added to the graph inside this scope, it
should only be used when creating variables (some implementations
work by changing variable creation, others work by using a
tf.compat.v1.colocate_with() scope).

This may only be used inside `self.scope()`.

#### Example usage:



```
with strategy.scope():
  var1 = tf.Variable(...)
  with strategy.extended.colocate_vars_with(var1):
    # var2 and var3 will be created on the same device(s) as var1
    var2 = tf.Variable(...)
    var3 = tf.Variable(...)

  def fn(v1, v2, v3):
    # operates on v1 from var1, v2 from var2, and v3 from var3

  # `fn` runs on every device `var1` is on, `var2` and `var3` will be there
  # too.
  strategy.extended.update(var1, fn, args=(var2, var3))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`colocate_with_variable`
</td>
<td>
A variable created in this strategy's `scope()`.
Variables created while in the returned context manager will be on the
same set of devices as `colocate_with_variable`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager.
</td>
</tr>

</table>



<h3 id="experimental_make_numpy_dataset"><code>experimental_make_numpy_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2148-L2166">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_make_numpy_dataset(
    numpy_input, session=None
)
</code></pre>

Makes a dataset for input provided via a numpy array.

This avoids adding `numpy_input` as a large constant in the graph,
and copies the data to the machine or machines that will be processing
the input.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`numpy_input`
</td>
<td>
A nest of NumPy input arrays that will be distributed evenly
across all replicas. Note that lists of Numpy arrays are stacked, as
that is normal <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> behavior.
</td>
</tr><tr>
<td>
`session`
</td>
<td>
(TensorFlow v1.x graph execution only) A session used for
initialization.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> representing `numpy_input`.
</td>
</tr>

</table>



<h3 id="experimental_run_steps_on_iterator"><code>experimental_run_steps_on_iterator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2191-L2236">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_run_steps_on_iterator(
    fn, iterator, iterations=1, initial_loop_values=None
)
</code></pre>

DEPRECATED: please use `run` instead.

Run `fn` with input from `iterator` for `iterations` times.

This method can be used to run a step function for training a number of
times using input from a dataset.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fn`
</td>
<td>
function to run using this distribution strategy. The function must
have the following signature: `def fn(context, inputs)`. `context` is an
instance of `MultiStepContext` that will be passed when `fn` is run.
`context` can be used to specify the outputs to be returned from `fn`
by calling `context.set_last_step_output`. It can also be used to
capture non tensor outputs by `context.set_non_tensor_output`. See
`MultiStepContext` documentation for more information. `inputs` will
have same type/structure as `iterator.get_next()`. Typically, `fn`
will use `call_for_each_replica` method of the strategy to distribute
the computation over multiple replicas.
</td>
</tr><tr>
<td>
`iterator`
</td>
<td>
Iterator of a dataset that represents the input for `fn`. The
caller is responsible for initializing the iterator as needed.
</td>
</tr><tr>
<td>
`iterations`
</td>
<td>
(Optional) Number of iterations that `fn` should be run.
Defaults to 1.
</td>
</tr><tr>
<td>
`initial_loop_values`
</td>
<td>
(Optional) Initial values to be passed into the
loop that runs `fn`. Defaults to `None`. 
initial_loop_values argument when we have a mechanism to infer the
outputs of `fn`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Returns the `MultiStepContext` object which has the following properties,
among other things:
- run_op: An op that runs `fn` `iterations` times.
- last_step_outputs: A dictionary containing tensors set using
`context.set_last_step_output`. Evaluating this returns the value of
the tensors after the last iteration.
- non_tensor_outputs: A dictionary containing anything that was set by
`fn` by calling `context.set_non_tensor_output`.
</td>
</tr>

</table>



<h3 id="non_slot_devices"><code>non_slot_devices</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2097-L2110">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>non_slot_devices(
    var_list
)
</code></pre>

Device(s) for non-slot variables.

Create variables on these devices in a
`with colocate_vars_with(non_slot_devices(...)):` block.
Update those using `update_non_slot()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var_list`
</td>
<td>
The list of variables being optimized, needed with the
default <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A sequence of devices for non-slot variables.
</td>
</tr>

</table>



<h3 id="read_var"><code>read_var</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2295-L2308">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>read_var(
    v
)
</code></pre>

Reads the value of a variable.

Returns the aggregate value of a replica-local variable, or the
(read-only) value of any other variable.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`v`
</td>
<td>
A variable allocated within the scope of this <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor representing the value of `v`, aggregated across replicas if
necessary.
</td>
</tr>

</table>



<h3 id="reduce_to"><code>reduce_to</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1905-L1931">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce_to(
    reduce_op, value, destinations, experimental_hints=None
)
</code></pre>

Combine (via e.g. sum or mean) values across replicas.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
Reduction type, an instance of <a href="../../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> enum.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A per-replica value with one value per replica.
</td>
</tr><tr>
<td>
`destinations`
</td>
<td>
A mirrored variable, a per-replica tensor, or a device
string. The return value will be copied to all destination devices (or
all the devices where the `destinations` value resides). To perform an
all-reduction, pass `value` to `destinations`.
</td>
</tr><tr>
<td>
`experimental_hints`
</td>
<td>
A `tf.distrbute.experimental.CollectiveHints`. Hints
to perform collective operations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor or value mirrored to `destinations`.
</td>
</tr>

</table>



<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1970-L2013">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update(
    var, fn, args=(), kwargs=None, group=(True)
)
</code></pre>

Run `fn` to update `var` using inputs mirrored to the same devices.

If `var` is mirrored across multiple devices, then this implements
logic like:

```
results = {}
for device, v in var:
  with tf.device(device):
    # args and kwargs will be unwrapped if they are mirrored.
    results[device] = fn(v, *args, **kwargs)
return merged(results)
```

Otherwise this returns `fn(var, *args, **kwargs)` colocated with `var`.

Neither `args` nor `kwargs` may contain per-replica values.
If they contain mirrored values, they will be unwrapped before
calling `fn`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var`
</td>
<td>
Variable, possibly mirrored to multiple devices, to operate on.
</td>
</tr><tr>
<td>
`fn`
</td>
<td>
Function to call. Should take the variable as the first argument.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Tuple or list. Additional positional arguments to pass to `fn()`.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Dict with keyword arguments to pass to `fn()`.
</td>
</tr><tr>
<td>
`group`
</td>
<td>
Boolean. Defaults to True. If False, the return value will be
unwrapped.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
By default, the merged return value of `fn` across all replicas.  The
merged result has dependencies to make sure that if it is evaluated at
all, the side effects (updates) will happen on every replica. If instead
"group=False" is specified, this function will return a nest of lists
where each list has an element per replica, and the caller is responsible
for ensuring all elements are executed.
</td>
</tr>

</table>



<h3 id="update_non_slot"><code>update_non_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2018-L2039">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_non_slot(
    colocate_with, fn, args=(), kwargs=None, group=(True)
)
</code></pre>

Runs `fn(*args, **kwargs)` on `colocate_with` devices.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`colocate_with`
</td>
<td>
The return value of `non_slot_devices()`.
</td>
</tr><tr>
<td>
`fn`
</td>
<td>
Function to execute.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Tuple or list. Positional arguments to pass to `fn()`.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Dict with keyword arguments to pass to `fn()`.
</td>
</tr><tr>
<td>
`group`
</td>
<td>
Boolean. Defaults to True. If False, the return value will be
unwrapped.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Return value of `fn`, possibly merged across devices.
</td>
</tr>

</table>



<h3 id="value_container"><code>value_container</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2047-L2060">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>value_container(
    value
)
</code></pre>

Returns the container that this per-replica `value` belongs to.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
A value returned by `run()` or a variable created in `scope()`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A container that `value` belongs to.
If value does not belong to any container (including the case of
container having been destroyed), returns the value itself.
`value in experimental_local_results(value_container(value))` will
always be true.
</td>
</tr>

</table>



<h3 id="variable_created_in_scope"><code>variable_created_in_scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1791-L1818">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variable_created_in_scope(
    v
)
</code></pre>

Tests whether `v` was created while this strategy scope was active.

Variables created inside the strategy scope are "owned" by it:

```python
strategy = tf.distribute.StrategyExtended()
with strategy.scope():
  v = tf.Variable(1.)
strategy.variable_created_in_scope(v)
True
```

Variables created outside the strategy are not owned by it:

```python
v = tf.Variable(1.)
strategy.variable_created_in_scope(v)
False
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`v`
</td>
<td>
A <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a> instance.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
True if `v` was created inside the scope, False if not.
</td>
</tr>

</table>





