page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.StrategyExtended

## Class `StrategyExtended`



### Aliases:

* Class `tf.contrib.distribute.DistributionStrategyExtended`
* Class `tf.distribute.StrategyExtended`



Defined in [`tensorflow/python/distribute/distribute_lib.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/distribute_lib.py).

Additional APIs for algorithms that need to be distribution-aware.

The intent is that you can write an algorithm in a stylized way and
it will be usable with a variety of different
<a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>
implementations. Each descendant will implement a different strategy
for distributing the algorithm across multiple devices/machines.
Furthermore, these changes can be hidden inside the specific layers
and other library classes that need special treatment to run in a
distributed setting, so that most users' model definition code can
run unchanged. The <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> API works the same way
with eager and graph execution.

First let's introduce a few high-level concepts:

* _Data parallelism_ is where we run multiple copies of the model
  on different slices of the input data. This is in contrast to
  _model parallelism_ where we divide up a single copy of a model
  across multiple devices.
  Note: we only support data parallelism for now, but
  hope to add support for model parallelism in the future.
* A _replica_ is one copy of the model, running on one slice of the
  input data.
* _Synchronous_, or more commonly _sync_, training is where the
  updates from each replica are aggregated together before updating
  the model variables. This is in contrast to _asynchronous_, or
  _async_ training, where each replica updates the model variables
  independently.
* Furthermore you might run your computation on multiple devices
  on one machine (or "host"), or on multiple machines/hosts.
  If you are running on multiple machines, you might have a
  single master host that drives computation across all of them,
  or you might have multiple clients driving the computation
  asynchronously.

To distribute an algorithm, we might use some of these ingredients:

* Parameter servers: These are hosts that hold a single copy of
  parameters/variables. All replicas that want to operate on a variable
  retrieve it at the beginning of a step and send an update to be
  applied at the end of the step. Can support either sync or async
  training.
* Mirrored variables: These are variables that are copied to multiple
  devices, where we keep the copies in sync by applying the same
  updates to every copy. Normally would only be used with sync training.
* Reductions and Allreduce: A _reduction_ is some method of
  aggregating multiple values into one value, like "sum" or
  "mean". If doing sync training, we will perform a reduction on the
  gradients to a parameter from all replicas before applying the
  update. Allreduce is an algorithm for performing a reduction on
  values from multiple devices and making the result available on
  all of those devices.
* In the future we will have support for TensorFlow's partitioned
  variables, where a single variable is split across multiple
  devices.

We have then a few approaches we want to support:

* Code written (as if) with no knowledge of class <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.
  This code should work as before, even if some of the layers, etc.
  used by that code are written to be distribution-aware. This is done
  by having a default <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> that gives ordinary behavior,
  and by default being in a single replica context.
* Ordinary model code that you want to run using a specific
  <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>. This can be as simple as:

>     with my_strategy.scope():
>       iterator = my_strategy.make_dataset_iterator(dataset)
>       session.run(iterator.initialize())
>       replica_train_ops = my_strategy.extended.call_for_each_replica(
>           replica_fn, args=(iterator.get_next(),))
>       train_op = my_strategy.group(replica_train_ops)

  This takes an ordinary `dataset` and `replica_fn` and runs it
  distributed using a particular <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> in
  `my_strategy`. Any variables created in `replica_fn` are created
  using `my_strategy`'s policy, and library functions called by
  `replica_fn` can use the `get_replica_context()` API to get enhanced
  behavior in this case.

* If you want to write a distributed algorithm, you may use any of
  the <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> APIs inside a
  `with my_strategy.scope():` block of code.

Lower-level concepts:

* Wrapped values: In order to represent values parallel across devices
  (either replicas or the devices associated with a particular value), we
  wrap them in a "PerReplica" or "Mirrored" object that contains a map
  from device to values. "PerReplica" is used when the value may be
  different across replicas, and "Mirrored" when the value are the same.
* Unwrapping and merging: Consider calling a function `fn` on multiple
  replicas, like `extended.call_for_each_replica(fn, args=[w])` with an
  argument `w` that is a wrapped value. This means `w` will have a map taking
  replica device `d0` to `w0`, replica device `d1` to `w1`,
  etc. `extended.call_for_each_replica()` unwraps `w` before calling `fn`, so
  it calls `fn(w0)` on `d0`, `fn(w1)` on `d1`, etc.  It then merges the return
  values from `fn()`, which can possibly result in wrapped values. For
  example, let's say `fn()` returns a tuple with three components: `(x, a,
  v0)` from replica 0, `(x, b, v1)` on replica 1, etc. If the first component
  is the same object `x` from every replica, then the first component of the
  merged result will also be `x`. If the second component is different (`a`,
  `b`, ...)  from each replica, then the merged value will have a wrapped map
  from replica device to the different values. If the third component is the
  members of a mirrored variable (`v` maps `d0` to `v0`, `d1` to `v1`, etc.),
  then the merged result will be that mirrored variable (`v`).
* Replica context vs. Cross-replica context: _replica context_ is when we
  are in some function that is being called once for each replica.
  Otherwise we are in cross-replica context, which is useful for
  calling <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> methods which operate across the
  replicas (like `reduce_to()`). By default you start in a replica context
  (the default "single replica context") and then some methods can
  switch you back and forth, as described below.
* Worker devices vs. parameter devices: Most replica computations will
  happen on worker devices. Since we don't yet support model
  parallelism, there will be one worker device per replica. When using
  parameter servers (see above), the set of devices holding
  variables may be different, otherwise the parameter devices might
  match the worker devices.
* Non-slot devices are some subset of the parameter devices where we
  put all the non-slot variables. We need to ensure that all
  non-slot variables are allocated on the same device, or mirrored
  across the same set of devices. If you have some variable you want
  to colocate all the non-slot variables with, you can use
  `colocate_vars_with()` to get the remaining non-slot variables on
  the same device.  Otherwise you can use `non_slot_devices()` to
  pick a consistent set of devices to pass to both
  `colocate_vars_with()` and `update_non_slot()`.

When using a <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>, we have a new type dimension
called _locality_ that says what values are compatible with which
APIs:

* T: different value for each replica (e.g. a PerReplica-wrapped value).
* M: value is "mirrored" across replicas, i.e. there are copies with the
  same value on each replica (e.g. a Mirrored-wrapped value).
* V(`v`): value is "mirrored" across all the devices which have a
  copy of variable `v` (also a Mirrored-wrapped value, but over
  parameter devices instead of worker devices).
* N: value is "mirrored" across all the "non-slot" devices

Rules for methods with respect to locality and single-replica vs.
cross-replica context:

* `with d.scope()`: default single-replica context -> cross-replica context
  for `d`
* `with d.extended.colocate_vars_with(v)`: in replica/cross-replica context,
  variables will be created with locality V(`v`). That is, if we write
  `with d.extended.colocate_vars_with(v1): v2 = tf.get_variable(...)`,
  then `v2` will have locality V(`v1`), i.e. locality V(`v2`) will equal
  V(`v1`).
* `with d.extended.colocate_vars_with(d.extended.non_slot_devices(...))`: in
  replica/cross-replica context, variables will be created with locality N
* `v = tf.get_variable(...)`: in replica/cross-replica context, creates
  a variable (which by definition will have locality V(`v`), though
  will match another locality if inside a `colocate_vars_with`
  scope).
* `d.make_dataset_iterator(dataset)` (or the deprecated
  `d.distribute_dataset(dataset).make_one_shot_iterator()`): in cross-replica
  context, produces an iterator with locality T
* `d.extended.broadcast_to(t)`: in cross-replica context, produces a value
  with locality M
* `d.extended.broadcast_to(t, v)`: in cross-replica context, produces a value
  with locality V(`v`)
* `d.extended.call_for_each_replica(fn, ...)`: in cross-replica context, runs
  `fn()` in a replica context (and so may call `get_replica_context()` and
  use its API, including `merge_call()` to get back to cross-replica
  context), once for each replica. May use values with locality T or
  M, and any variable.
* `d.extended.reduce_to(m, t, t)`: in cross-replica context, accepts t with
  locality T and produces a value with locality M.
* `d.extended.reduce_to(m, t, v)`: in cross-replica context, accepts t with
  locality T and produces a value with locality V(`v`).
* `d.extended.batch_reduce_to(m, [(t, v)]): see `d.extended.reduce_to()`
* `d.extended.update(v, fn, ...)`: in cross-replica context, runs `fn()` once
  for each device `v` is copied to, all inputs should have locality
  V(`v`), output will have locality V(`v`) as well.
* `d.extended.update_non_slot(d.extended.non_slot_devices(), fn)`: in
  cross-replica context, like `d.extended.update()` except with locality N.
* `d.extended.read_var(v)`: Gets the (read-only) value of the variable `v` (on
  the device determined by the current device scope), aggregating
  across replicas for replica-local variables. Frequently, this will be
  done automatically when using `v` in an expression or fetching it in
  a cross-replica context, but this function can be used to force that
  conversion happens at a particular point in time (for example, to
  add the result of the conversion to a graph collection).

The standard pattern for updating variables is to:

1. Create an input iterator with `d.make_dataset_iterator()`.
2. Define each replica `d.extended.call_for_each_replica()` up to the point of
   getting a list of gradient, variable pairs.
3. Call `d.extended.reduce_to(VariableAggregation.SUM, t, v)` or
   `d.extended.batch_reduce_to()` to sum the gradients (with locality T)
   into values with locality V(`v`).
4. Call `d.extended.update(v)` for each variable to update its value.

Steps 3 and 4 are done automatically by class `Optimizer` if you call
its `apply_gradients` method in a replica context. Otherwise you can
manually call its `_distributed_apply` method in a cross-replica context.

Another thing you might want to do in the middle of your replica function is
an all-reduce of some intermediate value, using `d.extended.reduce_to()` or
`d.extended.batch_reduce_to()`. You simply provide the same tensor as the
input and destination.

Layers should expect to be called in a replica context, and can use
the <a href="../../tf/distribute/get_replica_context"><code>tf.distribute.get_replica_context</code></a> function to get a
<a href="../../tf/distribute/ReplicaContext"><code>tf.distribute.ReplicaContext</code></a> object. The
`ReplicaContext` object has a `merge_call()` method for entering
cross-replica context where you can use `reduce_to()` (or
`batch_reduce_to()`) and then optionally `update()` to update state.

You may use this API whether or not a <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> is
being used, since there is a default implementation of
`ReplicaContext` and <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.

NOTE for new <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> implementations: Please put all logic
in a subclass of <a href="../../tf/distribute/StrategyExtended"><code>tf.distribute.StrategyExtended</code></a>. The only code needed for
the <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> subclass is for instantiating your subclass of
<a href="../../tf/distribute/StrategyExtended"><code>tf.distribute.StrategyExtended</code></a> in the `__init__` method.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(container_strategy)
```

Initialize self.  See help(type(self)) for accurate signature.



## Properties

<h3 id="experimental_between_graph"><code>experimental_between_graph</code></h3>

Whether the strategy uses between-graph replication or not.

This is expected to return a constant value that will not be changed
throughout its life cycle.

<h3 id="experimental_require_static_shapes"><code>experimental_require_static_shapes</code></h3>



<h3 id="experimental_should_init"><code>experimental_should_init</code></h3>

Whether initialization is needed.

<h3 id="parameter_devices"><code>parameter_devices</code></h3>

Returns the tuple of all devices used to place variables.

<h3 id="should_checkpoint"><code>should_checkpoint</code></h3>

Whether checkpointing is needed.

<h3 id="should_save_summary"><code>should_save_summary</code></h3>

Whether saving summaries is needed.

<h3 id="worker_devices"><code>worker_devices</code></h3>

Returns the tuple of all devices used to for compute replica execution.
    



## Methods

<h3 id="batch_reduce_to"><code>batch_reduce_to</code></h3>

``` python
batch_reduce_to(
    reduce_op,
    value_destination_pairs
)
```

Combine multiple `reduce_to` calls into one for faster execution.

#### Args:

* <b>`reduce_op`</b>: Reduction type, an instance of <a href="../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> enum.
    DEPRECATED but still accepted values:
    <a href="../../tf/VariableAggregation#SUM"><code>tf.VariableAggregation.SUM</code></a>,
    <a href="../../tf/VariableAggregation#MEAN"><code>tf.VariableAggregation.MEAN</code></a>,
* <b>`value_destination_pairs`</b>: A sequence of (value, destinations)
    pairs. See `reduce_to()` for a description.


#### Returns:

A list of mirrored values, one per pair in `value_destination_pairs`.

<h3 id="broadcast_to"><code>broadcast_to</code></h3>

``` python
broadcast_to(
    tensor,
    destinations
)
```

Mirror a tensor on one device to all worker devices.

#### Args:

* <b>`tensor`</b>: A Tensor value to broadcast.
* <b>`destinations`</b>: A mirrored variable or device string specifying the
    destination devices to copy `tensor` to.


#### Returns:

A value mirrored to `destinations` devices.

<h3 id="call_for_each_replica"><code>call_for_each_replica</code></h3>

``` python
call_for_each_replica(
    fn,
    args=(),
    kwargs=None
)
```

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
  return sum(distribution.unwrap(three_plus_replica_id))

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
  merged_results = distribution.call_for_each_replica(fn, args=[3])
  # merged_results has the values from every replica execution of `fn`.
  print(distribution.unwrap(merged_results))  # Prints a list
```

#### Args:

* <b>`fn`</b>: function to run (will be run once per replica).
* <b>`args`</b>: Tuple or list with positional arguments for `fn`.
* <b>`kwargs`</b>: Dict with keyword arguments for `fn`.


#### Returns:

Merged return value of `fn` across all replicas.

<h3 id="colocate_vars_with"><code>colocate_vars_with</code></h3>

``` python
colocate_vars_with(colocate_with_variable)
```

Scope that controls which devices variables will be created on.

No operations should be added to the graph inside this scope, it
should only be used when creating variables (some implementations
work by changing variable creation, others work by using a
tf.colocate_with() scope).

This may only be used inside `self.scope()`.

Example usage:

```
with strategy.scope():
  var1 = tf.get_variable(...)
  with strategy.extended.colocate_vars_with(v1):
    # var2 and var3 will be created on the same device(s) as var1
    var2 = tf.get_variable(...)
    var3 = tf.get_variable(...)

  def fn(v1, v2, v3):
    # operates on v1 from var1, v2 from var2, and v3 from var3

  # `fn` runs on every device `v1` is on, `v2` and `v3` will be there too.
  strategy.extended.update(v1, fn, args=(v2, v3))
```

#### Args:

* <b>`colocate_with_variable`</b>: A created in `self.scope()`. Variables created
    while in the returned context manager will be on the same set of
    devices as `colocate_with_variable`.


#### Returns:

A context manager.

<h3 id="experimental_run_steps_on_iterator"><code>experimental_run_steps_on_iterator</code></h3>

``` python
experimental_run_steps_on_iterator(
    fn,
    iterator,
    iterations=1,
    initial_loop_values=None
)
```

Run `fn` with input from `iterator` for `iterations` times.

This method can be used to run a step function for training a number of
times using input from a dataset.

#### Args:

* <b>`fn`</b>: function to run using this distribution strategy. The function must
    have the following signature: `def fn(context, inputs)`.
    `context` is an instance of `MultiStepContext` that will be passed when
    `fn` is run. `context` can be used to specify the outputs to be returned
    from `fn` by calling `context.set_last_step_output`. It can also be used
    to capture non tensor outputs by `context.set_non_tensor_output`.
    See `MultiStepContext` documentation for more information.
    `inputs` will have same type/structure as `iterator.get_next()`.
    Typically, `fn` will use `call_for_each_replica` method of the strategy
    to distribute the computation over multiple replicas.
* <b>`iterator`</b>: Iterator of a dataset that represents the input for `fn`. The
    caller is responsible for initializing the iterator as needed.
* <b>`iterations`</b>: (Optional) Number of iterations that `fn` should be run.
    Defaults to 1.
* <b>`initial_loop_values`</b>: (Optional) Initial values to be passed into the
    loop that runs `fn`. Defaults to `None`. # TODO(priyag): Remove
    initial_loop_values argument when we have a mechanism to infer the
    outputs of `fn`.


#### Returns:

Returns the `MultiStepContext` object which has the following properties,
among other things:
  - run_op: An op that runs `fn` `iterations` times.
  - last_step_outputs: A dictionary containing tensors set using
  `context.set_last_step_output`. Evaluating this returns the value of
  the tensors after the last iteration.
  - non_tensor_outputs: A dictionatry containing anything that was set by
    `fn` by calling `context.set_non_tensor_output`.

<h3 id="non_slot_devices"><code>non_slot_devices</code></h3>

``` python
non_slot_devices(var_list)
```

Device(s) for non-slot variables.

Create variables on these devices in a
`with colocate_vars_with(non_slot_devices(...)):` block.
Update those using `update_non_slot()`.

#### Args:

* <b>`var_list`</b>: The list of variables being optimized, needed with the
    default <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.

<h3 id="read_var"><code>read_var</code></h3>

``` python
read_var(v)
```

Reads the value of a variable.

Returns the aggregate value of a replica-local variable, or the
(read-only) value of any other variable.

#### Args:

* <b>`v`</b>: A variable allocated within the scope of this <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.


#### Returns:

A tensor representing the value of `v`, aggregated across replicas if
necessary.

<h3 id="reduce_to"><code>reduce_to</code></h3>

``` python
reduce_to(
    reduce_op,
    value,
    destinations
)
```

Combine (via e.g. sum or mean) values across replicas.

#### Args:

* <b>`reduce_op`</b>: Reduction type, an instance of <a href="../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> enum.
    DEPRECATED but still accepted values:
    <a href="../../tf/VariableAggregation#SUM"><code>tf.VariableAggregation.SUM</code></a>,
    <a href="../../tf/VariableAggregation#MEAN"><code>tf.VariableAggregation.MEAN</code></a>,
* <b>`value`</b>: A per-replica value with one value per replica.
* <b>`destinations`</b>: A mirrored variable, a per-replica tensor, or a device
    string. The return value will be copied to all destination devices (or
    all the devices where the `destinations` value resides). To perform an
    all-reduction, pass `value` to `destinations`.


#### Returns:

A value mirrored to `destinations`.

<h3 id="update"><code>update</code></h3>

``` python
update(
    var,
    fn,
    args=(),
    kwargs=None,
    group=True
)
```

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

#### Args:

* <b>`var`</b>: Variable, possibly mirrored to multiple devices, to operate on.
* <b>`fn`</b>: Function to call. Should take the variable as the first argument.
* <b>`args`</b>: Tuple or list. Additional positional arguments to pass to `fn()`.
* <b>`kwargs`</b>: Dict with keyword arguments to pass to `fn()`.
* <b>`group`</b>: Boolean. Defaults to True. If False, the return value will be
    unwrapped.


#### Returns:

By default, the merged return value of `fn` across all replicas.  The
merged result has dependencies to make sure that if it is evaluated at
all, the side effects (updates) will happen on every replica. If instead
"group=False" is specified, this function will return a nest of lists
where each list has an element per replica, and the caller is responsible
for ensuring all elements are executed.

<h3 id="update_non_slot"><code>update_non_slot</code></h3>

``` python
update_non_slot(
    colocate_with,
    fn,
    args=(),
    kwargs=None,
    group=True
)
```

Runs `fn(*args, **kwargs)` on `colocate_with` devices.

#### Args:

* <b>`colocate_with`</b>: The return value of `non_slot_devices()`.
* <b>`fn`</b>: Function to execute.
* <b>`args`</b>: Tuple or list. Positional arguments to pass to `fn()`.
* <b>`kwargs`</b>: Dict with keyword arguments to pass to `fn()`.
* <b>`group`</b>: Boolean. Defaults to True. If False, the return value will be
    unwrapped.


#### Returns:

Return value of `fn`, possibly merged across devices.

<h3 id="value_container"><code>value_container</code></h3>

``` python
value_container(value)
```

Returns the container that this per-replica `value` belongs to.

#### Args:

* <b>`value`</b>: A value returned by `call_for_each_replica()` or a variable
    created in `scope()`.


#### Returns:

A container that `value` belongs to.
If value does not belong to any container (including the case of
container having been destroyed), returns the value itself.
`value in unwrap(value_container(value))` will always be true.



