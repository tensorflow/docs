page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.DistributionStrategy

## Class `DistributionStrategy`





Defined in [`tensorflow/python/training/distribute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/training/distribute.py).

A list of devices with a state & compute distribution policy.

The intent is that you can write an algorithm in a stylized way and
it will be usable with a variety of different `DistributionStrategy`
implementations. Each descendant will implement a different strategy
for distributing the algorithm across multiple devices/machines.
Furthermore, these changes can be hidden inside the specific layers
and other library classes that need special treatment to run in a
distributed setting, so that most users' model definition code can
run unchanged. The `DistributionStrategy` API works the same way
with eager and graph execution.

First let's introduce a few high-level concepts:

* _Data parallelism_ is where we run multiple copies of the model
  on different slices of the input data. This is in contrast to
  _model parallelism_ where we divide up a single copy of a model
  across multiple devices.
  Note: we only support data parallelism for now, but
  hope to add support for model parallelism in the future.
* A _tower_ is one copy of the model, running on one slice of the
  input data.
* _Synchronous_, or more commonly _sync_, training is where the
  updates from each tower are aggregated together before updating
  the model variables. This is in contrast to _asynchronous_, or
  _async_ training, where each tower updates the model variables
  independently.
* Furthermore you might run your computation on multiple devices
  on one machine (or "host"), or on multiple machines/hosts.
  If you are running on multiple machines, you might have a
  single master host that drives computation across all of them,
  or you might have multiple clients driving the computation
  asynchronously.

To distribute an algorithm, we might use some of these ingredients:

* Parameter servers: These are hosts that hold a single copy of
  parameters/variables. All towers that want to operate on a variable
  retrieve it at the beginning of a step and send an update to be
  applied at the end of the step. Can support either sync or async
  training.
* Mirrored variables: These are variables that are copied to multiple
  devices, where we keep the copies in sync by applying the same
  updates to every copy. Normally would only be used with sync training.
* Reductions and Allreduce: A _reduction_ is some method of
  aggregating multiple values into one value, like "sum" or
  "mean". If doing sync training, we will perform a reduction on the
  gradients to a parameter from all towers before applying the
  update. Allreduce is an algorithm for performing a reduction on
  values from multiple devices and making the result available on
  all of those devices.
* In the future we will have support for TensorFlow's partitioned
  variables, where a single variable is split across multiple
  devices.

We have then a few approaches we want to support:
* Code written (as if) with no knowledge of class `DistributionStrategy`.
  This code should work as before, even if some of the layers, etc.
  used by that code are written to be distribution-aware. This is done
  by having a default `DistributionStrategy` that gives ordinary behavior,
  and by default being in a single tower context.
* Ordinary model code that you want to run using a specific
  `DistributionStrategy`. This can be as simple as:

>     with my_distribution.scope():
>       iterator = my_distribution.distribute_dataset(
>           dataset).make_one_shot_iterator()
>       tower_train_ops = my_distribution.call_for_each_tower(
>           tower_fn, iterator.get_next())
>       train_op = tf.group(my_distribution.unwrap(tower_train_ops))

  This takes an ordinary `dataset` and `tower_fn` and runs it
  distributed using a particular `DistributionStrategy` in
  `my_distribution`. Any variables created in `tower_fn` are created
  using `my_distribution`'s policy, and library functions called by
  `tower_fn` can use the `get_tower_context()` API to get enhanced
  behavior in this case.

  You can also create an initializable iterator instead of a one-shot
  iterator. In that case, you will need to ensure that you initialize the
  iterator before calling get_next.

>     iterator = my_distribution.distribute_dataset(
>         dataset).make_initializable_iterator())
>     session.run(iterator.initializer)

* If you want to write a distributed algorithm, you may use any of
  the `DistributionStrategy` APIs inside a
  `with my_distribution.scope():` block of code.

Lower-level concepts:

* Wrapped values: In order to represent values parallel across devices
  (either towers or the devices associated with a particular value), we
  wrap them in a "PerDevice" or "Mirrored" object that contains a map
  from device to values. "PerDevice" is used when the value may be
  different across devices, and "Mirrored" when the value are the same.
* Unwrapping and merging: Consider calling a function `fn` on
  multiple devices, like `call_for_each_tower(fn, w)` with an
  argument `w` that is a wrapped value. This means `w` will have a
  map taking tower device `d0` to `w0`, tower device `d1` to `w1`,
  etc. `call_for_each_tower()` unwraps `w` before calling `fn`, so
  it calls `fn(w0)` on `d0`, `fn(w1)` on `d1`, etc.  It then merges
  the return values from `fn()`, which can possibly result in
  wrapped values. For example, let's say `fn()` returns a tuple with
  three components: `(x, a, v0)` from tower 0, `(x, b, v1)` on tower 1,
  etc. If the first component is the same object `x` from every
  tower, then the first component of the merged result will also be
  `x`. If the second component is different (`a`, `b`, ...)  from
  each tower, then the merged value will have a wrapped map from
  tower device to the different values. If the third component is
  the members of a mirrored variable (`v` maps `d0` to `v0`, `d1` to
  `v1`, etc.), then the merged result will be that mirrored variable
  (`v`).
* Tower context vs. Cross-tower context: _tower context_ is when we
  are in some function that is being called once for each tower.
  Otherwise we are in cross-tower context, which is useful for
  calling `DistributionStrategy` methods which operate across the
  towers (like `reduce()`). By default you start in a tower context
  (the default "single tower context") and then some methods can
  switch you back and forth, as described below.
* Worker devices vs. parameter devices: Most tower computations will
  happen on worker devices. Since we don't yet support model
  parallelism, there will be one worker device per tower. When using
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

When using a `DistributionStrategy`, we have a new type dimension
called _locality_ that says what values are compatible with which
APIs:

* T: different value for each tower (e.g. a PerDevice-wrapped value).
* M: value is "mirrored" across towers, i.e. there are copies with the
  same value on each tower (e.g. a Mirrored-wrapped value).
* V(`v`): value is "mirrored" across all the devices which have a
  copy of variable `v` (also a Mirrored-wrapped value, but over
  parameter devices instead of worker devices).
* N: value is "mirrored" across all the "non-slot" devices

Rules for methods with respect to locality and single-tower vs.
cross-tower context:

* `with d.scope()`: default single-tower context -> cross-tower context for
  `d`
* `with d.colocate_vars_with(v)`: in tower/cross-tower context, variables
  will be created with locality V(`v`). That is, if we write
  `with d.colocate_vars_with(v1): v2 = tf.get_variable(...)`, then
  `v2` will have locality V(`v1`), i.e. locality V(`v2`) will equal
  V(`v1`).
* `with d.colocate_vars_with(d.non_slot_devices(...))`: in
  tower/cross-tower context, variables will be created with locality N
* `v = tf.get_variable(...)`: in tower/cross-tower context, creates
  a variable (which by definition will have locality V(`v`), though
  will match another locality if inside a `colocate_vars_with`
  scope).
* `d.distribute_dataset(dataset).make_one_shot_iterator()`: in cross-tower
  context, produces an iterator with locality T
* `d.broadcast(t)`: in cross-tower context, produces a value with locality M
* `d.broadcast(t, v)`: in cross-tower context, produces a value with
  locality V(`v`)
* `d.call_for_each_tower(fn, ...)`: in cross-tower context, runs
  `fn()` in a tower context (and so may call `get_tower_context()` and
  use its API, including `merge_call()` to get back to cross-tower
  context), once for each tower. May use values with locality T or
  M, and any variable.
* `d.reduce(m, t)`: in cross-tower context, accepts t with locality T
  and produces a value with locality M.
* `d.reduce(m, t, v)`: in cross-tower context, accepts t with
  locality T and produces a value with locality V(`v`).
* `d.batch_reduce(m, [(t, v)]): see `d.reduce()`
* `d.update(v, fn, ...)`: in cross-tower context, runs `fn()` once
  for each device `v` is copied to, all inputs should have locality
  V(`v`), output will have locality V(`v`) as well.
* `d.update_non_slot(d.non_slot_devices(), fn)`: in cross-tower
  context, like `d.update()` except with locality N.
* `d.fetch(t)`: Copy `t` with any locality to the client's CPU device.

The standard pattern for updating variables is to:

1. Wrap your input dataset in `d.distribute_dataset()` and create an iterator.
2. Define each tower `d.call_for_each_tower()` up to the point of
   getting a list of gradient, variable pairs.
3. Call `d.reduce("sum", t, v)` or `d.batch_reduce()` to sum the
   gradients (with locality T) into values with locality V(`v`).
4. Call `d.update(v)` for each variable to update its value.

Steps 3 and 4 are done automatically by class `Optimizer` if you call
its `apply_gradients` method in a tower context. Otherwise you can
manually call its `_distributed_apply` method in a cross-tower context.

Another thing you might want to do in the middle of your tower function
is an all-reduce of some intermediate value, using `d.reduce()` or
`d.batch_reduce()` without supplying a variable as the destination.

Layers should expect to be called in a tower context, and can use
the `get_tower_context()` function to get a `TowerContext` object.  The
`TowerContext` object has a `merge_call()` method for entering
cross-tower context where you can use `reduce()` (or
`batch_reduce()`) and then optionally `update()` to update state.

You may use this API whether or not a `DistributionStrategy` is
being used, since there is a default implementation of
`TowerContext` and `DistributionStrategy`. Or you can use the
`get_tower_context().is_single_tower` property to run different code
in the distributed vs. single tower cases.

## Properties

<h3 id="is_single_tower"><code>is_single_tower</code></h3>

Returns whether there is a single tower or multiple.

#### Returns:

A boolean. If `True`, `call_for_each_tower(fn)` will only call `fn` once.
If `False`, `call_for_each_tower(fn)` may call `fn` multiple times.

<h3 id="num_towers"><code>num_towers</code></h3>

Returns number of towers, for purposes of averaging across towers.

<h3 id="parameter_devices"><code>parameter_devices</code></h3>

Returns the list of devices used for variable and `update` placement.

<h3 id="worker_device_index"><code>worker_device_index</code></h3>

An object mapping worker device to an id.

This might be passed as an argument to `call_for_each_tower()`, as in:

```
with distribution_strategy.scope():

  def fn(device_id):
    # device_id is an integer. `fn` is being executed on device:
    #    distribution_strategy.worker_devices[device_id].

  distribution_strategy.call_for_each_tower(
      fn, distribution_strategy.worker_device_index)
```

#### Returns:

An index object, or the integer 0 if there is only a single tower.

<h3 id="worker_devices"><code>worker_devices</code></h3>

Returns the list of devices used to run `call_for_each_tower()` calls.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__()
```



<h3 id="batch_reduce"><code>batch_reduce</code></h3>

``` python
batch_reduce(
    method_string,
    value_destination_pairs
)
```

Combine multiple `reduce` calls into one for faster execution.

#### Args:

* <b>`method_string`</b>: A string indicating how to combine values, either
    "sum" or "mean".
* <b>`value_destination_pairs`</b>: A sequence of (value, destinations)
    pairs. See `reduce()` for a description.


#### Returns:

A list of mirrored values, one per pair in `value_destination_pairs`.

<h3 id="broadcast"><code>broadcast</code></h3>

``` python
broadcast(
    tensor,
    destinations=None
)
```

Mirror a tensor on one device to all worker devices.

#### Args:

* <b>`tensor`</b>: A Tensor value to broadcast.
* <b>`destinations`</b>: An optional mirrored variable, device string, or
    list of device strings, specifying the destination devices
    to copy `tensor` to. Defaults to `self.worker_devices`.


#### Returns:

A value mirrored to `destinations` devices.

<h3 id="call_for_each_tower"><code>call_for_each_tower</code></h3>

``` python
call_for_each_tower(
    fn,
    *args,
    **kwargs
)
```

Run `fn` once per tower.

`fn` may call `tf.get_tower_context()` to access methods such as
`tower_id()` and `merge_call()`.

`merge_call()` is used to communicate between the towers and
re-enter the cross-tower context. All towers pause their execution
having encountered a `merge_call()` call. After that the
`merge_fn`-function is executed. Its results are then unwrapped and
given back to each tower call. After that execution resumes until
`fn` is complete or encounters another `merge_call()`.  Example:

```python
# Called once in "cross-tower" context.
def merge_fn(distribution, three_plus_tower_id):
  # sum the values across towers
  return sum(distribution.unwrap(three_plus_tower_id))

# Called once per tower in `distribution`, in a "tower" context.
def fn(three):
  tower_ctx = tf.get_tower_context()
  v = three + tower_ctx.tower_id
  # Computes the sum of the `v` values across all towers.
  s = tower_ctx.merge_call(merge_fn, v)
  return s + v

with distribution.scope():
  # in "cross-tower" context
  ...
  merged_results = distribution.call_for_each_tower(fn, 3)
  # merged_results has the values from every tower execution of `fn`.
  print(distribution.unwrap(merged_results))  # Prints a list
```

#### Args:

* <b>`fn`</b>: function to run (will be run once per tower).
* <b>`*args`</b>: positional arguments for `fn`
* <b>`**kwargs`</b>: keyword arguments for `fn`.
      `"run_concurrently"`: Boolean indicating whether executions of `fn`
         can be run concurrently (under eager execution only), defaults to
         `True`.


#### Returns:

Merged return value of `fn` across all towers.

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
with distribution_strategy.scope():
  var1 = tf.get_variable(...)
  with distribution_strategy.colocate_vars_with(v1):
    # var2 and var3 will be created on the same device(s) as var1
    var2 = tf.get_variable(...)
    var3 = tf.get_variable(...)

  def fn(v1, v2, v3):
    # operates on v1 from var1, v2 from var2, and v3 from var3

  # `fn` runs on every device `v1` is on, `v2` and `v3` will be there too.
  distribution_strategy.update(v1, fn, v2, v3)
```

#### Args:

* <b>`colocate_with_variable`</b>: A created in `self.scope()`. Variables created
    while in the returned context manager will be on the same set of
    devices as `colocate_with_variable`.


#### Returns:

A context manager.

<h3 id="configure"><code>configure</code></h3>

``` python
configure(session_config=None)
```

Find the best configuration given a tensorflow session config.

<h3 id="distribute_dataset"><code>distribute_dataset</code></h3>

``` python
distribute_dataset(dataset_fn)
```

Return a `dataset` split across all towers.

Suitable for providing input to for `call_for_each_tower()` by creating an
iterator:

```
def dataset_fn():
  return tf.data.Dataset.from_tensors([[1.]]).repeat()
with distribution_strategy.scope():
  distributed_dataset = distribution_strategy.distribute_dataset(dataset_fn)
  iterator = distributed_dataset.make_one_shot_iterator()
  tower_results = distribution_strategy.call_for_each_tower(
      tower_fn, iterator.get_next())
```

#### Args:

* <b>`dataset_fn`</b>: A function that returns a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>.


#### Returns:

A `PerDeviceDataset` that will produce data for each tower.

<h3 id="fetch"><code>fetch</code></h3>

``` python
fetch(
    val,
    destination='/device:CPU:0',
    fn=(lambda x: x)
)
```

Return a copy of `val` or `fn(val)` on `destination`.

This is useful for getting a mirrored value onto a device.  It
will attempt to avoid a copy by checking if the value is already
on the destination device.

#### Args:

* <b>`val`</b>: Value (which may be mirrored) to copy.
* <b>`destination`</b>: A device string to copy the value to.
* <b>`fn`</b>: An optional function to apply to the value on the source
      device, before copying.


#### Returns:

A `Tensor` on `destination`.

<h3 id="group"><code>group</code></h3>

``` python
group(
    value,
    name=None
)
```

Shortcut for `tf.group(distribution.unwrap(value))`.

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
    default `DistributionStrategy`.

<h3 id="reduce"><code>reduce</code></h3>

``` python
reduce(
    method_string,
    value,
    destinations=None
)
```

Combine (via e.g. sum or mean) values across towers.

#### Args:

* <b>`method_string`</b>: A string indicating how to combine values, either
    "sum" or "mean".
* <b>`value`</b>: A per-device value with one value per tower.
* <b>`destinations`</b>: An optional mirrored variable, a device string,
    list of device strings. The return value will be copied to all
    destination devices (or all the devices where the mirrored
    variable resides). If `None` or unspecified, the destinations
    will match the devices `value` resides on.


#### Returns:

A value mirrored to `destinations`.

<h3 id="scope"><code>scope</code></h3>

``` python
scope()
```

Returns a context manager selecting this DistributionStrategy as current.

Inside a `with distribution_strategy.scope():` code block, this thread
will use a variable creator set by `distribution_strategy`, and will
enter its "cross-tower context".

#### Returns:

A context manager.

<h3 id="tower_local_var_scope"><code>tower_local_var_scope</code></h3>

``` python
tower_local_var_scope(reduce_method)
```

Inside this scope, new variables will not be mirrored.

There will still be one component variable per tower, but there is
no requirement that they stay in sync. Instead, when saving them
or calling `fetch()`, we use the value that results when calling
`reduce()` on all the towers' variables.

Note: tower-local implies not trainable. Instead, it is expected
that each tower will directly update (using `assign_add()` or
whatever) its local variable instance but only the aggregated
value (accessible using `fetch()`) will be exported from the
model. When it is acceptable to only aggregate on export, we
greatly reduce communication overhead by using tower-local
variables.

Note: All component variables will be initialized to the same
value, using the initialization expression from the first tower.
The values will match even if the initialization expression uses
random numbers.

#### Args:

* <b>`reduce_method`</b>: String used as a `method_string` to `reduce()`
    to get the value to save when checkpointing.


#### Returns:

A context manager.

<h3 id="unwrap"><code>unwrap</code></h3>

``` python
unwrap(value)
```

Returns the list of all per-device values contained in `value`.

#### Args:

* <b>`value`</b>: A value returned by `call_for_each_tower()` or a variable
    created in `scope()`.


#### Returns:

A list of values contained in `value`. If `value` represents a single
value, this returns `[value].`

<h3 id="update"><code>update</code></h3>

``` python
update(
    var,
    fn,
    *args,
    **kwargs
)
```

Run `fn` to update `var` using inputs mirrored to the same devices.

If `var` is mirrored across multiple devices, then this implements
logic like:

```
results = {}
for device, v in var:
  with tf.device(device):
    # *args and **kwargs will be unwrapped if they are mirrored.
    results[device] = fn(v, *args, **kwargs)
return merged(results)
```

Otherwise this returns `fn(var, *args, **kwargs)` colocated with `var`.'

Neither *args nor **kwargs may contain per-device values.
If they contain mirrored values, they will be unwrapped before
calling `fn`.

#### Args:

* <b>`var`</b>: Variable, possibly mirrored to multiple devices, to operate on.
* <b>`fn`</b>: Function to call. Should take the variable as the first argument.
* <b>`*args`</b>: Additional positional arguments to pass to `fn()`.
* <b>`**kwargs`</b>: Keyword arguments to pass to `fn()`.


#### Returns:

Merged return value of `fn` across all towers.

<h3 id="update_non_slot"><code>update_non_slot</code></h3>

``` python
update_non_slot(
    colocate_with,
    fn,
    *args,
    **kwargs
)
```

Runs `fn(*args, **kwargs)` on `colocate_with` devices.

#### Args:

* <b>`colocate_with`</b>: The return value of `non_slot_devices()`.
* <b>`fn`</b>: Function to execute.
* <b>`*args`</b>: Positional arguments to pass to `fn()`.
* <b>`**kwargs`</b>: Keyword arguments to pass to `fn()`.


#### Returns:

Return value of `fn`, possibly merged across devices.



