page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.MirroredStrategy

## Class `MirroredStrategy`

Inherits From: [`DistributionStrategy`](../../../tf/contrib/distribute/DistributionStrategy)



Defined in [`tensorflow/contrib/distribute/python/mirrored_strategy.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/distribute/python/mirrored_strategy.py).

Mirrors vars to distribute across multiple devices and machines.

This strategy uses one tower per device and sync replication for its multi-GPU
version.

When `cluster_spec` is given by the `configure` method., it turns into the
mulit-worker version that works on multiple workers with in-graph replication.
Note: `configure` will be called by higher-level APIs if running in
distributed environment.

There are several important concepts for distributed TensorFlow, e.g.
`client`, `job`, 'task', `cluster`, `in-graph replication` and
'synchronous training' and they have already been defined in the
[TensorFlow's documentation](https://www.tensorflow.org/deploy/distributed).
The distribution strategy inherits these concepts as well and in addition to
that we also clarify several more concepts:
  * **In-graph replication**: the `client` creates a single <a href="../../../tf/Graph"><code>tf.Graph</code></a> that
  specifies tasks for devices on all workers. The `client` then creates a
  client session which will talk to the `master` service of a `worker`. Then
  the `master` will partition the graph and distribute the work to all
  participating workers.
  * **Worker**: A `worker` is a TensorFlow `task` that usually maps to one
  physical machine. We will have multiple `worker`s with different `task`
  index. They all do similar things except for one worker checkpointing model
  variables, writing summaries, etc. in addition to its ordinary work.

The multi-worker version of this class maps one tower to one device on a
worker. It mirrors all model variables on all towers. For example, if you have
two `worker`s and each `worker` has 4 GPUs, it will create 8 copies of the
model variables on these 8 GPUs. Then like in MirroredStrategy, each tower
performs their computation with their own copy of variables unless in
cross-tower model where variable or tensor reduction happens.

#### Args:

* <b>`devices`</b>: a list of device strings.
* <b>`num_gpus`</b>: number of GPUs. For local training, either specify `devices` or
    `num_gpus`. In distributed training, this must be specified as number of
    GPUs on each worker.
* <b>`num_gpus_per_worker`</b>: number of GPUs per worker. This is the same as
    `num_gpus` and only one of `num_gpus` and `num_gpus_per_worker` can be
    specified.
* <b>`cross_tower_ops`</b>: optional, a descedant of `CrossTowerOps`. If this is not
    set, the `configure` method will try to find the best one.
* <b>`prefetch_on_device`</b>: optional boolean to specify whether to prefetch input
    data to devices.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    devices=None,
    num_gpus=None,
    num_gpus_per_worker=None,
    cross_tower_ops=None,
    prefetch_on_device=None
)
```





## Properties

<h3 id="between_graph"><code>between_graph</code></h3>



<h3 id="is_single_tower"><code>is_single_tower</code></h3>



<h3 id="num_towers"><code>num_towers</code></h3>



<h3 id="parameter_devices"><code>parameter_devices</code></h3>



<h3 id="should_checkpoint"><code>should_checkpoint</code></h3>



<h3 id="should_init"><code>should_init</code></h3>



<h3 id="should_save_summary"><code>should_save_summary</code></h3>



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





## Methods

<h3 id="batch_reduce"><code>batch_reduce</code></h3>

``` python
batch_reduce(
    aggregation,
    value_destination_pairs
)
```

Combine multiple `reduce` calls into one for faster execution.

#### Args:

* <b>`aggregation`</b>: Indicates how a variable will be aggregated. Accepted values
    are <a href="../../../tf/VariableAggregation#SUM"><code>tf.VariableAggregation.SUM</code></a>, <a href="../../../tf/VariableAggregation#MEAN"><code>tf.VariableAggregation.MEAN</code></a>,
    <a href="../../../tf/VariableAggregation#ONLY_FIRST_TOWER"><code>tf.VariableAggregation.ONLY_FIRST_TOWER</code></a>.
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
configure(
    session_config=None,
    cluster_spec=None,
    task_type=None,
    task_id=None
)
```



<h3 id="distribute_dataset"><code>distribute_dataset</code></h3>

``` python
distribute_dataset(dataset_fn)
```



<h3 id="finalize"><code>finalize</code></h3>

``` python
finalize()
```

Any final actions to be done at the end of all computations.

In eager mode, it executes any finalize actions as a side effect.
In graph mode, it creates the finalize ops and returns them.

For example, TPU shutdown ops.

#### Returns:

In eager mode, returns `None`.
In graph mode, a list of ops to execute. Empty list if nothing to be done.

<h3 id="group"><code>group</code></h3>

``` python
group(
    value,
    name=None
)
```

Shortcut for `tf.group(distribution.unwrap(value))`.

<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize()
```

Any initialization to be done before running any computations.

In eager mode, it executes any initialization as a side effect.
In graph mode, it creates the initialization ops and returns them.

For example, TPU initialize_system ops.

#### Returns:

In eager mode, returns `None`.
In graph mode, a list of ops to execute. Empty list if nothing to be done.

<h3 id="map"><code>map</code></h3>

``` python
map(
    map_over,
    fn,
    *args,
    **kwargs
)
```



<h3 id="non_slot_devices"><code>non_slot_devices</code></h3>

``` python
non_slot_devices(var_list)
```



<h3 id="read_var"><code>read_var</code></h3>

``` python
read_var(tower_local_var)
```

Read the aggregate value of a tower-local variable.

<h3 id="reduce"><code>reduce</code></h3>

``` python
reduce(
    aggregation,
    value,
    destinations
)
```

Combine (via e.g. sum or mean) values across towers.

#### Args:

* <b>`aggregation`</b>: Indicates how a variable will be aggregated. Accepted values
    are <a href="../../../tf/VariableAggregation#SUM"><code>tf.VariableAggregation.SUM</code></a>, <a href="../../../tf/VariableAggregation#MEAN"><code>tf.VariableAggregation.MEAN</code></a>,
    <a href="../../../tf/VariableAggregation#ONLY_FIRST_TOWER"><code>tf.VariableAggregation.ONLY_FIRST_TOWER</code></a>.
* <b>`value`</b>: A per-device value with one value per tower.
* <b>`destinations`</b>: A mirrored variable, a per-device tensor, a device string,
    or list of device strings. The return value will be copied to all
    destination devices (or all the devices where the `destinations` value
    resides). To perform an all-reduction, pass `value` to `destinations`.


#### Returns:

A value mirrored to `destinations`.

<h3 id="run_steps_on_dataset"><code>run_steps_on_dataset</code></h3>

``` python
run_steps_on_dataset(
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
    have the following signature: def fn(context, *inputs).
    `context` is an instance of `MultiStepContext` that will be passed when
    `fn` is run. `context` can be used to specify the outputs to be returned
    from `fn` by calling `context.set_last_step_output`. It can also be used
    to capture non tensor outputs by `context.set_non_tensor_output`.
    See `MultiStepContext` documentation for more information.
    `inputs` will have same type/structure as `iterator.get_next()`. If the
    `iterator.get_next()` returns a tuple say `return x, y` then whose will
    be unpacked and passed to the `step_fn`; and step_fn signature would
    look like `def step_fn(context, x, y)`. If the iterator returns a single
    value say `return x` then the value is passed as is; the step_fn
    signature would look like `def step_fn(context, x)`.
    Typically, `fn` will use `call_for_each_tower` method of the strategy
    to distribute the computation over multiple towers.
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

<h3 id="value_container"><code>value_container</code></h3>

``` python
value_container(val)
```





