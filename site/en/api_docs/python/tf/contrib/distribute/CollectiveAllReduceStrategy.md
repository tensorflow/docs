page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.CollectiveAllReduceStrategy

## Class `CollectiveAllReduceStrategy`

Inherits From: [`Strategy`](../../../tf/distribute/Strategy)



Defined in [`tensorflow/contrib/distribute/python/collective_all_reduce_strategy.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/distribute/python/collective_all_reduce_strategy.py).

Distribution strategy that uses collective ops for all-reduce.

It is similar to the MirroredStrategy but it uses collective ops for
reduction.

When `cluster_spec` is given by the `configure` method, it turns into the
mulit-worker version that works on multiple workers with between-graph
replication.

Note: `configure` will be called by higher-level APIs if running in
distributed environment.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(num_gpus_per_worker=0)
```

Initializes the object.

#### Args:

* <b>`num_gpus_per_worker`</b>: number of local GPUs or GPUs per worker, the default
    is 0 meaning CPU only.



## Properties

<h3 id="extended"><code>extended</code></h3>

<a href="../../../tf/distribute/StrategyExtended"><code>tf.distribute.StrategyExtended</code></a> with additional methods.

<h3 id="num_replicas_in_sync"><code>num_replicas_in_sync</code></h3>

Returns number of replicas over which gradients are aggregated.



## Methods

<h3 id="__deepcopy__"><code>__deepcopy__</code></h3>

``` python
__deepcopy__(memo)
```



<h3 id="experimental_finalize"><code>experimental_finalize</code></h3>

``` python
experimental_finalize()
```

Any final actions to be done at the end of all computations.

In eager mode, it executes any finalize actions as a side effect.
In graph mode, it creates the finalize ops and returns them.

For example, TPU shutdown ops.

#### Returns:

A list of ops to execute.

<h3 id="experimental_initialize"><code>experimental_initialize</code></h3>

``` python
experimental_initialize()
```

Any initialization to be done before running any computations.

In eager mode, it executes any initialization as a side effect.
In graph mode, it creates the initialization ops and returns them.

For example, TPU initialize_system ops.

#### Returns:

A list of ops to execute.

<h3 id="experimental_run"><code>experimental_run</code></h3>

``` python
experimental_run(
    fn,
    input_iterator=None
)
```

Runs ops in `fn` on each replica, with inputs from `input_iterator`.

When eager execution is enabled, executes ops specified by `fn` on each
replica.  Otherwise, builds a graph to execute the ops on each replica.

Each replica will take a single, different input from the inputs provided by
one `get_next` call on the input iterator.

`fn` may call `tf.distribute.get_replica_context()` to access members such
as `replica_id_in_sync_group`.

IMPORTANT: Depending on the `DistributionStrategy` being used, and whether
eager execution is enabled, `fn` may be called one or more times (once for
each replica).

#### Args:

* <b>`fn`</b>: function to run. The inputs to the function must match the outputs of
    `input_iterator.get_next()`. The output must be a `tf.nest` of
    `Tensor`s.
* <b>`input_iterator`</b>: (Optional) input iterator from which the inputs are taken.


#### Returns:

Merged return value of `fn` across replicas. The structure of the return
value is the same as the return value from `fn`. Each element in the
structure can either be `PerReplica` (if the values are unsynchronized),
`Mirrored` (if the values are kept in sync), or `Tensor` (if running on a
single replica).

<h3 id="make_dataset_iterator"><code>make_dataset_iterator</code></h3>

``` python
make_dataset_iterator(dataset)
```

Makes an iterator for input provided via input_dataset.

Data from the given dataset will be distributed evenly across all the
compute replicas. We will assume that the input dataset is batched by the
global batch size. With this assumption, we will make a best effort to
divide each batch across all the replicas (one or more workers).
If this effort fails, an error will be thrown, and the user should instead
use `make_input_fn_iterator` which provides more control to the user, and
does not try to divide a batch across replicas.

The user could also use `make_input_fn_iterator` if they want to
customize which input is fed to which replica/worker etc.

#### Args:

* <b>`dataset`</b>: <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> that will be distributed evenly across all
    replicas.


#### Returns:

An `tf.distribute.InputIterator` which returns inputs for each step of the
computation.  User should call `initialize` on the returned iterator.

<h3 id="make_input_fn_iterator"><code>make_input_fn_iterator</code></h3>

``` python
make_input_fn_iterator(
    input_fn,
    replication_mode=tf.distribute.InputReplicationMode.PER_WORKER
)
```

Returns an iterator split across replicas created from an input function.

The `input_fn` should take an <a href="../../../tf/distribute/InputContext"><code>tf.distribute.InputContext</code></a> object where
information about input sharding can be accessed:

```
def input_fn(input_context):
  d = tf.data.Dataset.from_tensors([[1.]]).repeat()
  return d.shard(input_context.num_input_pipelines,
                 input_context.input_pipeline_id)
with strategy.scope():
  iterator = strategy.make_input_fn_iterator(
      input_fn)
  replica_results = strategy.extended.call_for_each_replica(
      replica_fn, iterator.get_next())
```

#### Args:

* <b>`input_fn`</b>: A function that returns a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>. This function is
    expected to take an <a href="../../../tf/distribute/InputContext"><code>tf.distribute.InputContext</code></a> object.
* <b>`replication_mode`</b>: an enum value of <a href="../../../tf/distribute/InputReplicationMode"><code>tf.distribute.InputReplicationMode</code></a>.
    Only `PER_WORKER` is supported currently.


#### Returns:

An iterator object that can be initialized and fetched next element.

<h3 id="reduce"><code>reduce</code></h3>

``` python
reduce(
    reduce_op,
    value
)
```

Reduce `value` across replicas.

#### Args:

* <b>`reduce_op`</b>: A <a href="../../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> value specifying how values should
    be combined.
* <b>`value`</b>: A "per replica" value to be combined into a single tensor.


#### Returns:

A `Tensor`.

<h3 id="scope"><code>scope</code></h3>

``` python
scope()
```

Returns a context manager selecting this Strategy as current.

Inside a `with strategy.scope():` code block, this thread
will use a variable creator set by `strategy`, and will
enter its "cross-replica context".

#### Returns:

A context manager.

<h3 id="update_config_proto"><code>update_config_proto</code></h3>

``` python
update_config_proto(config_proto)
```

Returns a copy of `config_proto` modified for use with this strategy.

The updated config has something needed to run a strategy, e.g.
configuration to run collective ops, or device filters to improve
distributed training performance.

#### Args:

* <b>`config_proto`</b>: a <a href="../../../tf/ConfigProto"><code>tf.ConfigProto</code></a> object.


#### Returns:

The updated copy of the `config_proto`.



