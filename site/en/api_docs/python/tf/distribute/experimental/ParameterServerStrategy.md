description: An multi-worker tf.distribute strategy with parameter servers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.ParameterServerStrategy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="distribute_datasets_from_function"/>
<meta itemprop="property" content="experimental_distribute_dataset"/>
<meta itemprop="property" content="experimental_distribute_values_from_function"/>
<meta itemprop="property" content="experimental_local_results"/>
<meta itemprop="property" content="gather"/>
<meta itemprop="property" content="reduce"/>
<meta itemprop="property" content="run"/>
<meta itemprop="property" content="scope"/>
</div>

# tf.distribute.experimental.ParameterServerStrategy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/parameter_server_strategy_v2.py#L44-L477">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An multi-worker tf.distribute strategy with parameter servers.

Inherits From: [`Strategy`](../../../tf/distribute/Strategy.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.ParameterServerStrategy(
    cluster_resolver, variable_partitioner=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Parameter server training is a common data-parallel method to scale up a
machine learning model on multiple machines. A parameter server training
cluster consists of workers and parameter servers. Variables are created on
parameter servers and they are read and updated by workers in each step.
By default, workers read and update these variables independently without
synchronizing with each other. Under this configuration, it is known as
asynchronous training.

In TensorFlow 2, we recommend a central coordiantion-based architecture for
parameter server training, where workers and parameter servers run a
<a href="../../../tf/distribute/Server.md"><code>tf.distribute.Server</code></a> and there is another task that creates resources on
workers and parameter servers, dispatches functions, and coordinates the
training. We refer to this task as “coordinator”. The coordinator uses a
<a href="../../../tf/distribute/experimental/coordinator/ClusterCoordinator.md"><code>tf.distribute.experimental.coordinator.ClusterCoordinator</code></a> to coordinate the
cluster, and a <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> to define
variables on parameter servers and computation on workers.

For the training to work, the coordinator dispatches <a href="../../../tf/function.md"><code>tf.function</code></a>s to be
executed on remote workers. Upon receiving requests from
the coordinator, a worker executes the <a href="../../../tf/function.md"><code>tf.function</code></a> by reading the variables
from parameter servers, executing the ops, and updating the variables on the
parameter servers. Each of the worker only processes the requests from the
coordinator, and communicates with parameter servers, without direct
interactions with other workers in the cluster.

As a result, failures of some workers do not prevent the cluster from
continuing the work, and this allows the cluster to train with instances that
can be occasionally unavailable (e.g. preemptible or spot instances). The
coordinator and parameter servers though, must be available at all times for
the cluster to make progress.

Note that the coordinator is not one of the training workers. Instead, it
creates resources such as variables and datasets, dispatchs <a href="../../../tf/function.md"><code>tf.function</code></a>s,
saving checkpoints and so on. In addition to workers, parameter servers and
the coordinator, an optional evaluator can be run on the side that
periodically reads the checkpoints saved by the coordinator and runs
evaluations against each checkpoint.

<a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> has to work in
conjunction with a <a href="../../../tf/distribute/experimental/coordinator/ClusterCoordinator.md"><code>tf.distribute.experimental.coordinator.ClusterCoordinator</code></a>
object. Standalone usage of
<a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> without central
coordination is not supported at this time.

__Example code for coordinator__

Here's an example usage of the API, with a custom training loop to train a
model. This code snippet is intended to be run on (the only) one task that
is designated as the coordinator. Note that `cluster_resolver`,
`variable_partitioner`, and `dataset_fn` arguments are explained in the
following "Cluster setup", "Variable partitioning", and "Dataset preparation"
sections.

```python
# Set the environment variable to allow reporting worker and ps failure to the
# coordinator. This a short-term workaround.
os.environ["GRPC_FAIL_FAST"] = "use_caller"

# Prepare a strategy to use with the cluster and variable partitioning info.
strategy = tf.distribute.experimental.ParameterServerStrategy(
    cluster_resolver=...,
    variable_partitioner=...)
coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
    strategy=strategy)

# Prepare a distribute dataset that will place datasets on the workers.
distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn=...)

with strategy.scope():
  model = ...
  optimizer, metrics = ...  # Keras optimizer/metrics are great choices
  checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)
  checkpoint_manager = tf.train.CheckpointManager(
      checkpoint, checkpoint_dir, max_to_keep=2)
  # `load_checkpoint` infers initial epoch from `optimizer.iterations`.
  initial_epoch = load_checkpoint(checkpoint_manager) or 0

@tf.function
def worker_fn(iterator):

  def replica_fn(inputs):
    batch_data, labels = inputs
    # calculate gradient, applying gradient, metrics update etc.

  strategy.run(replica_fn, args=(next(iterator),))

for epoch in range(initial_epoch, num_epoch):
  distributed_iterator = iter(distributed_dataset)  # Reset iterator state.
  for step in range(steps_per_epoch):

    # Asynchronously schedule the `worker_fn` to be executed on an arbitrary
    # worker. This call returns immediately.
    coordinator.schedule(worker_fn, args=(distributed_iterator,))

  # `join` blocks until all scheduled `worker_fn`s finish execution. Once it
  # returns, we can read the metrics and save checkpoints as needed.
  coordinator.join()
  logging.info('Metric result: %r', metrics.result())
  train_accuracy.reset_states()
  checkpoint_manager.save()
```

__Example code for worker and parameter servers__

In addition to the coordinator, there should be tasks designated as
"worker" or "ps". They should run the following code to start a TensorFlow
server, waiting for coordinator's requests:

```python
# Set the environment variable to allow reporting worker and ps failure to the
# coordinator.
os.environ["GRPC_FAIL_FAST"] = "use_caller"

# Provide a `tf.distribute.cluster_resolver.ClusterResolver` that serves
# the cluster information. See below "Cluster setup" section.
cluster_resolver = ...

server = tf.distribute.Server(
    cluster_resolver.cluster_spec(),
    job_name=cluster_resolver.task_type,
    task_index=cluster_resolver.task_id,
    protocol="grpc")

# Blocking the process that starts a server from exiting.
server.join()
```

__Cluster setup__

In order for the tasks in the cluster to know other tasks' addresses,
a <a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> is required to be used
in coordinator, worker, and ps. The
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> is responsible for providing
the cluster information, as well as the task type and id of the current task.
See <a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> for more information.

If `TF_CONFIG` environment variable is set, a
<a href="../../../tf/distribute/cluster_resolver/TFConfigClusterResolver.md"><code>tf.distribute.cluster_resolver.TFConfigClusterResolver</code></a> should be used as
well. Note that for legacy reason, on some platform, "chief" is used as the
task type for the coordinator, as the following example demonstrates. Here we
set `TF_CONFIG` for the task designated as a parameter server (task type "ps")
and index 1 (the second task), in a cluster with 1 chief, 2 parameter servers,
and 3 workers. Note that the it needs to be set before the use of
<a href="../../../tf/distribute/cluster_resolver/TFConfigClusterResolver.md"><code>tf.distribute.cluster_resolver.TFConfigClusterResolver</code></a>.

Example code for cluster setup:
```python
os.environ['TF_CONFIG'] = '''
{
  "cluster": {
    "chief": ["chief.example.com:2222"],
    "ps": ["ps0.example.com:2222", "ps1.example.com:2222"],
    "worker": ["worker0.example.com:2222", "worker1.example.com:2222",
               "worker2.example.com:2222"]
  },
  "task": {
    "type": "ps",
    "index": 1
  }
}
'''
```

If you prefer to run the same binary for all tasks, you will need to let the
binary branch into different roles at the beginning of the program:
```python
os.environ["GRPC_FAIL_FAST"] = "use_caller"
cluster_resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()

# If coordinator, create a strategy and start the training program.
if cluster_resolver.task_type == 'chief':
  strategy = tf.distribute.experimental.ParameterServerStrategy(
      cluster_resolver)
  ...

# If worker/ps, create a server
elif cluster_resolver.task_type in ("worker", "ps"):
  server = tf.distribute.Server(...)
  ...
```
Alternatively, you can also start a bunch of TensorFlow servers in advance and
connect to them later. The coordinator can be in the same cluster or on any
machine that has connectivity to workers and parameter server. This is covered
in our guide and tutorial.

__Variable creation with `strategy.scope()`__

<a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> follows the
<a href="../../../tf/distribute.md"><code>tf.distribute</code></a> API contract where variable creation is expected to be inside
the context manager returned by `strategy.scope()`, in order to be correctly
placed on parameter servers in a round-robin manner:

```python
# In this example, we're assuming having 3 ps.
strategy = tf.distribute.experimental.ParameterServerStrategy(
    cluster_resolver=...)
coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
    strategy=strategy)

# Variables should be created inside scope to be placed on parameter servers.
# If created outside scope such as `v1` here, it would be placed on the
# coordinator.
v1 = tf.Variable(initial_value=0.0)

with strategy.scope():
  v2 = tf.Variable(initial_value=1.0)
  v3 = tf.Variable(initial_value=2.0)
  v4 = tf.Variable(initial_value=3.0)
  v5 = tf.Variable(initial_value=4.0)

# v2 through v5 are created in scope and are distributed on parameter servers.
# Default placement is round-robin but the order should not be relied on.
assert v2.device == "/job:ps/replica:0/task:0/device:CPU:0"
assert v3.device == "/job:ps/replica:0/task:1/device:CPU:0"
assert v4.device == "/job:ps/replica:0/task:2/device:CPU:0"
assert v5.device == "/job:ps/replica:0/task:0/device:CPU:0"
```

See <a href="../../../tf/distribute/MirroredStrategy.md#scope"><code>distribute.Strategy.scope</code></a> for more information.

__Variable partitioning__

Having dedicated servers to store variables means being able to divide up, or
"shard" the variables across the ps. Partitioning large variable among ps is a
commonly used technique to boost training throughput and mitigate memory
constraints. It enables parallel computations and updates on different shards
of a variable, and often yields better load balancing across parameter servers
. Without sharding, models with large variables (e.g, embeddings) that can't
fit into one machine's memory would otherwise be unable to train.

With <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a>, if a
`variable_partitioner` is provided to `__init__` and certain conditions are
satisfied, the resulting variables created in scope are sharded across the
parameter servers, in a round-robin fashion. The variable reference returned
from <a href="../../../tf/Variable.md"><code>tf.Variable</code></a> becomes a type that serves as the container of the sharded
variables. One can access `variables` attribute of this container for the
actual variable components. If building model with <a href="../../../tf/Module.md"><code>tf.Module</code></a> or Keras,
the variable components are collected in the `variables` alike attributes.


```python
class Dense(tf.Module):
  def __init__(self, name=None):
    super().__init__(name=name)
    self.w = tf.Variable(tf.random.normal([100, 10]), name='w')

  def __call__(self, x):
    return x * self.w

# Partition the dense layer into 2 shards.
variable_partitioiner  = (
  tf.distribute.experimental.partitioners.FixedShardsPartitioner(
    num_shards = 2))
strategy = ParameterServerStrategy(cluster_resolver=...,
  variable_partitioner = variable_partitioner)
with strategy.scope():
  dense = Dense()
assert len(dense.variables) == 2
assert isinstance(dense.variables[0], tf.Variable)
assert isinstance(dense.variables[1], tf.Variable)
assert dense.variables[0].name == "w/part_0"
assert dense.variables[1].name == "w/part_1"
```

The sharded variable container can be converted to a `Tensor` via
<a href="../../../tf/convert_to_tensor.md"><code>tf.convert_to_tensor</code></a>. This means the container can be directly used in most
Python Ops where such `Tensor` convertion automatically happens. For example
in the above code snippet, `x * self.w` would implicitly apply the said tensor
convertion. Note that such convertion can be expensive, as the variable
components need to be transferred from multiple parameter servers to where
the value is used.

<a href="../../../tf/nn/embedding_lookup.md"><code>tf.nn.embedding_lookup</code></a> on the other hand doesn't apply the tensor convertion
, and performs parallel lookups on the variable components instead. This is
crutial to scale up embedding lookups when the embedding table variable is
large.

When a partitioned variable is saved to `SavedModel`, it will be saved as if
it is one single variable. This improves serving efficiency by eliminating
a number of Ops that handle the partiton aspects.

Known limitations of variable partitioning:

* Number of parttions must not change across Checkpoint save/load.

* After saving partitioned variables to a SavedModel, the SavedModel can't be
  loaded via <a href="../../../tf/saved_model/load.md"><code>tf.saved_model.load</code></a>.

* Partition variable doesn't directly work with <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>, please use
  the `variables` attributes to get the actual variable components and use
  them in gradient APIs instead.

__Dataset preparation__

With <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a>, a dataset is
created in each of the workers to be used for training. This is done by
creating a `dataset_fn` that takes no argument and returns a
<a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>, and passing the `dataset_fn` into
`tf.distribute.experimental.coordinator.
ClusterCoordinator.create_per_worker_dataset`. We recommend the dataset to be
shuffled and repeated to have the examples run through the training as evenly
as possible.

```python
def dataset_fn():
  filenames = ...
  dataset = tf.data.Dataset.from_tensor_slices(filenames)

  # Dataset is recommended to be shuffled, and repeated.
  return dataset.shuffle(buffer_size=...).repeat().batch(batch_size=...)

coordinator =
    tf.distribute.experimental.coordinator.ClusterCoordinator(strategy=...)
distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn)

```

__Limitations__

* <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> in TF2 is experimental,
and the API is subject to further changes.

* <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> does not yet support
training with GPU(s). This is a feature request being developed.

* <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> only supports
[custom training loop
API](https://www.tensorflow.org/tutorials/distribute/custom_training)
currently in TF2. Usage of it with Keras `compile`/`fit` API is being
developed.

* <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> must be used with
<a href="../../../tf/distribute/experimental/coordinator/ClusterCoordinator.md"><code>tf.distribute.experimental.coordinator.ClusterCoordinator</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cluster_resolver`
</td>
<td>
a <a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>
object.
</td>
</tr><tr>
<td>
`variable_partitioner`
</td>
<td>
a <a href="../../../tf/distribute/experimental/partitioners/Partitioner.md"><code>distribute.experimental.partitioners.Partitioner</code></a> that specifies
how to partition variables. If `None`, variables will not be
partitioned.

* Predefined partitioners in <a href="../../../tf/distribute/experimental/partitioners.md"><code>tf.distribute.experimental.partitioners</code></a>
can be used for this argument. A commonly used partitioner is
`MinSizePartitioner(min_shard_bytes = 256 << 10, max_shards = num_ps)`,
which allocates at least 256K per shard, and each ps gets at most one
shard.

* `variable_partitioner` will be called for each variable created under
strategy `scope` to instruct how the variable should be partitioned.
Variables that have only one partition along the partitioning axis
(i.e., no need for partition) will be created as normal <a href="../../../tf/Variable.md"><code>tf.Variable</code></a>.

* Only the first / outermost axis partitioning is supported.

* Div partition strategy is used to partition variables. Assuming we
assign consecutive integer ids along the first axis of a variable, then
ids are assigned to shards in a contiguous manner, while attempting to
keep each shard size identical. If the ids do not evenly divide the
number of shards, each of the first several shards will be assigned one
more id. For instance, a variable whose first dimension is 13 has 13
ids, and they are split across 5 shards as:
`[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.

* Variables created under `strategy.extended.colocate_vars_with` will
not be partitioned.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`cluster_resolver`
</td>
<td>
Returns the cluster resolver associated with this strategy.

In general, when using a multi-worker <a href="../../../tf/distribute.md"><code>tf.distribute</code></a> strategy such as
<a href="../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a> or
<a href="../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy()</code></a>, there is a
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> associated with the
strategy used, and such an instance is returned by this property.

Strategies that intend to have an associated
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> must set the
relevant attribute, or override this property; otherwise, `None` is returned
by default. Those strategies should also provide information regarding what
is returned by this property.

Single-worker strategies usually do not have a
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>, and in those cases this
property will return `None`.

The <a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> may be useful when the
user needs to access information such as the cluster spec, task type or task
id. For example,

```python

os.environ['TF_CONFIG'] = json.dumps({
'cluster': {
'worker': ["localhost:12345", "localhost:23456"],
'ps': ["localhost:34567"]
},
'task': {'type': 'worker', 'index': 0}
})

# This implicitly uses TF_CONFIG for the cluster and current task info.
strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()

...

if strategy.cluster_resolver.task_type == 'worker':
# Perform something that's only applicable on workers. Since we set this
# as a worker above, this block will run on this particular instance.
elif strategy.cluster_resolver.task_type == 'ps':
# Perform something that's only applicable on parameter servers. Since we
# set this as a worker above, this block will not run on this particular
# instance.
```

For more information, please see
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>'s API docstring.
</td>
</tr><tr>
<td>
`extended`
</td>
<td>
<a href="../../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> with additional methods.
</td>
</tr><tr>
<td>
`num_replicas_in_sync`
</td>
<td>
Returns number of replicas over which gradients are aggregated.
</td>
</tr>
</table>



## Methods

<h3 id="distribute_datasets_from_function"><code>distribute_datasets_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1061-L1135">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>distribute_datasets_from_function(
    dataset_fn, options=None
)
</code></pre>

Distributes <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instances created by calls to `dataset_fn`.

The argument `dataset_fn` that users pass in is an input function that has a
<a href="../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> argument and returns a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>
instance. It is expected that the returned dataset from `dataset_fn` is
already batched by per-replica batch size (i.e. global batch size divided by
the number of replicas in sync) and sharded.
<a href="../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a> does
not batch or shard the <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance
returned from the input function. `dataset_fn` will be called on the CPU
device of each of the workers and each generates a dataset where every
replica on that worker will dequeue one batch of inputs (i.e. if a worker
has two replicas, two batches will be dequeued from the `Dataset` every
step).

This method can be used for several purposes. First, it allows you to
specify your own batching and sharding logic. (In contrast,
`tf.distribute.experimental_distribute_dataset` does batching and sharding
for you.) For example, where
`experimental_distribute_dataset` is unable to shard the input files, this
method might be used to manually shard the dataset (avoiding the slow
fallback behavior in `experimental_distribute_dataset`). In cases where the
dataset is infinite, this sharding can be done by creating dataset replicas
that differ only in their random seed.

The `dataset_fn` should take an <a href="../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance where
information about batching and input replication can be accessed.

You can use `element_spec` property of the
<a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> returned by this API to query the
<a href="../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the elements returned by the iterator. This can be used to
set the `input_signature` property of a <a href="../../../tf/function.md"><code>tf.function</code></a>. Follow
<a href="../../../tf/distribute/DistributedDataset.md#element_spec"><code>tf.distribute.DistributedDataset.element_spec</code></a> to see an example.

IMPORTANT: The <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> returned by `dataset_fn` should have a
per-replica batch size, unlike `experimental_distribute_dataset`, which uses
the global batch size. This may be computed using
`input_context.get_per_replica_batch_size`.

Note: If you are using TPUStrategy, the order in which the data is processed
by the workers when using
<a href="../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a> is
not guaranteed. This is typically required if you are using
<a href="../../../tf/distribute.md"><code>tf.distribute</code></a> to scale prediction. You can however insert an index for
each element in the batch and order outputs accordingly. Refer to [this
snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
for an example of how to order outputs.

Note: Stateful dataset transformations are currently not supported with
`tf.distribute.experimental_distribute_dataset` or
`tf.distribute.distribute_datasets_from_function`. Any stateful
ops that the dataset may have are currently ignored. For example, if your
dataset has a `map_fn` that uses <a href="../../../tf/random/uniform.md"><code>tf.random.uniform</code></a> to rotate an image,
then you have a dataset graph that depends on state (i.e the random seed) on
the local machine where the python process is being executed.

For a tutorial on more usage and properties of this method, refer to the
[tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_datasets_from_function)).
If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset_fn`
</td>
<td>
A function taking a <a href="../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance and
returning a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
<a href="../../../tf/distribute/InputOptions.md"><code>tf.distribute.InputOptions</code></a> used to control options on how this
dataset is distributed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.
</td>
</tr>

</table>



<h3 id="experimental_distribute_dataset"><code>experimental_distribute_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L942-L1059">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_dataset(
    dataset, options=None
)
</code></pre>

Creates <a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> from <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.

The returned <a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> can be iterated over
similar to regular datasets.
NOTE: The user cannot add any more transformations to a
<a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>. You can only create an iterator or
examine the <a href="../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the data generated by it. See API docs of
<a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> to learn more.

The following is an example:

```
>>> global_batch_size = 2
>>> # Passing the devices is optional.
... strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
>>> # Create a dataset
... dataset = tf.data.Dataset.range(4).batch(global_batch_size)
>>> # Distribute that dataset
... dist_dataset = strategy.experimental_distribute_dataset(dataset)
>>> @tf.function
... def replica_fn(input):
...   return input*2
>>> result = []
>>> # Iterate over the `tf.distribute.DistributedDataset`
... for x in dist_dataset:
...   # process dataset elements
...   result.append(strategy.run(replica_fn, args=(x,)))
>>> print(result)
[PerReplica:{
  0: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([0])>,
  1: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([2])>
}, PerReplica:{
  0: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([4])>,
  1: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([6])>
}]
```


Three key actions happending under the hood of this method are batching,
sharding, and prefetching.

In the code snippet above, `dataset` is batched by `global_batch_size`, and
calling `experimental_distribute_dataset` on it rebatches `dataset` to a
new batch size that is equal to the global batch size divided by the number
of replicas in sync. We iterate through it using a Pythonic for loop.
`x` is a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing data for all replicas,
and each replica gets data of the new batch size.
<a href="../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> will take care of feeding the right per-replica
data in `x` to the right `replica_fn` executed on each replica.

Sharding contains autosharding across multiple workers and within every
worker. First, in multi-worker distributed training (i.e. when you use
<a href="../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>
or <a href="../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>), autosharding a dataset over a set of
workers means that each worker is assigned a subset of the entire dataset
(if the right <a href="../../../tf/data/experimental/AutoShardPolicy.md"><code>tf.data.experimental.AutoShardPolicy</code></a> is set). This is to
ensure that at each step, a global batch size of non-overlapping dataset
elements will be processed by each worker. Autosharding has a couple of
different options that can be specified using
<a href="../../../tf/data/experimental/DistributeOptions.md"><code>tf.data.experimental.DistributeOptions</code></a>. Then, sharding within each worker
means the method will split the data among all the worker devices (if more
than one a present). This will happen regardless of multi-worker
autosharding.

Note: for autosharding across multiple workers, the default mode is
<a href="../../../tf/data/experimental/AutoShardPolicy.md#AUTO"><code>tf.data.experimental.AutoShardPolicy.AUTO</code></a>. This mode
will attempt to shard the input dataset by files if the dataset is
being created out of reader datasets (e.g. <a href="../../../tf/data/TFRecordDataset.md"><code>tf.data.TFRecordDataset</code></a>,
<a href="../../../tf/data/TextLineDataset.md"><code>tf.data.TextLineDataset</code></a>, etc.) or otherwise shard the dataset by data,
where each of the workers will read the entire dataset and only process the
shard assigned to it. However, if you have less than one input file per
worker, we suggest that you disable dataset autosharding across workers by
setting the <a href="../../../tf/data/experimental/DistributeOptions.md#auto_shard_policy"><code>tf.data.experimental.DistributeOptions.auto_shard_policy</code></a> to be
<a href="../../../tf/data/experimental/AutoShardPolicy.md#OFF"><code>tf.data.experimental.AutoShardPolicy.OFF</code></a>.

By default, this method adds a prefetch transformation at the end of the
user provided <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance. The argument to the prefetch
transformation which is `buffer_size` is equal to the number of replicas in
sync.

If the above batch splitting and dataset sharding logic is undesirable,
please use
<a href="../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a>
instead, which does not do any automatic batching or sharding for you.

Note: If you are using TPUStrategy, the order in which the data is processed
by the workers when using
<a href="../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a> is
not guaranteed. This is typically required if you are using
<a href="../../../tf/distribute.md"><code>tf.distribute</code></a> to scale prediction. You can however insert an index for
each element in the batch and order outputs accordingly. Refer to [this
snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
for an example of how to order outputs.

Note: Stateful dataset transformations are currently not supported with
`tf.distribute.experimental_distribute_dataset` or
`tf.distribute.distribute_datasets_from_function`. Any stateful
ops that the dataset may have are currently ignored. For example, if your
dataset has a `map_fn` that uses <a href="../../../tf/random/uniform.md"><code>tf.random.uniform</code></a> to rotate an image,
then you have a dataset graph that depends on state (i.e the random seed) on
the local machine where the python process is being executed.

For a tutorial on more usage and properties of this method, refer to the
[tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_dataset).
If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset`
</td>
<td>
<a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> that will be sharded across all replicas using
the rules stated above.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
<a href="../../../tf/distribute/InputOptions.md"><code>tf.distribute.InputOptions</code></a> used to control options on how this
dataset is distributed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.
</td>
</tr>

</table>



<h3 id="experimental_distribute_values_from_function"><code>experimental_distribute_values_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1616-L1690">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_values_from_function(
    value_fn
)
</code></pre>

Generates <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> from `value_fn`.

This function is to generate <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> to pass
into `run`, `reduce`, or other methods that take
distributed values when not using datasets.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value_fn`
</td>
<td>
The function to run to generate values. It is called for
each replica with `tf.distribute.ValueContext` as the sole argument. It
must return a Tensor or a type that can be converted to a Tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing a value for each replica.
</td>
</tr>

</table>



#### Example usage:



1. Return constant value per replica:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> def value_fn(ctx):
...   return tf.constant(1.)
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(<tf.Tensor: shape=(), dtype=float32, numpy=1.0>,
 <tf.Tensor: shape=(), dtype=float32, numpy=1.0>)
```

2. Distribute values in array based on replica_id:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> array_value = np.array([3., 2., 1.])
>>> def value_fn(ctx):
...   return array_value[ctx.replica_id_in_sync_group]
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(3.0, 2.0)
```

3. Specify values using num_replicas_in_sync:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> def value_fn(ctx):
...   return ctx.num_replicas_in_sync
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(2, 2)
```

4. Place values on devices and distribute:

```
strategy = tf.distribute.TPUStrategy()
worker_devices = strategy.extended.worker_devices
multiple_values = []
for i in range(strategy.num_replicas_in_sync):
  with tf.device(worker_devices[i]):
    multiple_values.append(tf.constant(1.0))

def value_fn(ctx):
  return multiple_values[ctx.replica_id_in_sync_group]

distributed_values = strategy.
  experimental_distribute_values_from_function(
  value_fn)
```

<h3 id="experimental_local_results"><code>experimental_local_results</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1482-L1499">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_local_results(
    value
)
</code></pre>

Returns the list of all local per-replica values contained in `value`.

Note: This only returns values on the worker initiated by this client.
When using a <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> like
<a href="../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>, each worker
will be its own client, and this function will only return values
computed on that worker.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
A value returned by `experimental_run()`, `run()`,
`extended.call_for_each_replica()`, or a variable created in `scope`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tuple of values contained in `value`. If `value` represents a single
value, this returns `(value,).`
</td>
</tr>

</table>



<h3 id="gather"><code>gather</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1692-L1796">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>gather(
    value, axis
)
</code></pre>

Gather `value` across replicas along `axis` to the current device.

Given a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> or <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>-like
object `value`, this API gathers and concatenates `value` across replicas
along the `axis`-th dimension. The result is copied to the "current" device
- which would typically be the CPU of the worker on which the program is
running. For <a href="../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>, it is the first TPU host. For
multi-client `MultiWorkerMirroredStrategy`, this is CPU of each worker.

This API can only be called in the cross-replica context. For a counterpart
in the replica context, see <a href="../../../tf/distribute/ReplicaContext.md#all_gather"><code>tf.distribute.ReplicaContext.all_gather</code></a>.

Note: For all strategies except <a href="../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>, the input
`value` on different replicas must have the same rank, and their shapes must
be the same in all dimensions except the `axis`-th dimension. In other
words, their shapes cannot be different in a dimension `d` where `d` does
not equal to the `axis` argument. For example, given a
<a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> with component tensors of shape
`(1, 2, 3)` and `(1, 3, 3)` on two replicas, you can call
`gather(..., axis=1, ...)` on it, but not `gather(..., axis=0, ...)` or
`gather(..., axis=2, ...)`. However, for <a href="../../../tf/distribute/TPUStrategy.md#gather"><code>tf.distribute.TPUStrategy.gather</code></a>,
all tensors must have exactly the same rank and same shape.

Note: Given a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> `value`, its component
tensors must have a non-zero rank. Otherwise, consider using
<a href="../../../tf/expand_dims.md"><code>tf.expand_dims</code></a> before gathering them.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> # A DistributedValues with component tensor of shape (2, 1) on each replica
... distributed_values = strategy.experimental_distribute_values_from_function(lambda _: tf.identity(tf.constant([[1], [2]])))
>>> @tf.function
... def run():
...   return strategy.gather(distributed_values, axis=0)
>>> run()
<tf.Tensor: shape=(4, 1), dtype=int32, numpy=
array([[1],
       [2],
       [1],
       [2]], dtype=int32)>
```


Consider the following example for more combinations:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1", "GPU:2", "GPU:3"])
>>> single_tensor = tf.reshape(tf.range(6), shape=(1,2,3))
>>> distributed_values = strategy.experimental_distribute_values_from_function(lambda _: tf.identity(single_tensor))
>>> @tf.function
... def run(axis):
...   return strategy.gather(distributed_values, axis=axis)
>>> axis=0
>>> run(axis)
<tf.Tensor: shape=(4, 2, 3), dtype=int32, numpy=
array([[[0, 1, 2],
        [3, 4, 5]],
       [[0, 1, 2],
        [3, 4, 5]],
       [[0, 1, 2],
        [3, 4, 5]],
       [[0, 1, 2],
        [3, 4, 5]]], dtype=int32)>
>>> axis=1
>>> run(axis)
<tf.Tensor: shape=(1, 8, 3), dtype=int32, numpy=
array([[[0, 1, 2],
        [3, 4, 5],
        [0, 1, 2],
        [3, 4, 5],
        [0, 1, 2],
        [3, 4, 5],
        [0, 1, 2],
        [3, 4, 5]]], dtype=int32)>
>>> axis=2
>>> run(axis)
<tf.Tensor: shape=(1, 2, 12), dtype=int32, numpy=
array([[[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
        [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]]], dtype=int32)>
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> instance, e.g. returned by
<a href="../../../tf/distribute/MirroredStrategy.md#run"><code>Strategy.run</code></a>, to be combined into a single tensor. It can also be a
regular tensor when used with <a href="../../../tf/distribute/OneDeviceStrategy.md"><code>tf.distribute.OneDeviceStrategy</code></a> or the
default strategy. The tensors that constitute the DistributedValues
can only be dense tensors with non-zero rank, NOT a <a href="../../../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a>.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
0-D int32 Tensor. Dimension along which to gather. Must be in the
range [0, rank(value)).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` that's the concatenation of `value` across replicas along
`axis` dimension.
</td>
</tr>

</table>



<h3 id="reduce"><code>reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1261-L1458">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce(
    reduce_op, value, axis
)
</code></pre>

Reduce `value` across replicas and return result on current device.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> def step_fn():
...   i = tf.distribute.get_replica_context().replica_id_in_sync_group
...   return tf.identity(i)
>>>
>>> per_replica_result = strategy.run(step_fn)
>>> total = strategy.reduce("SUM", per_replica_result, axis=None)
>>> total
<tf.Tensor: shape=(), dtype=int32, numpy=1>
```

To see how this would look with multiple replicas, consider the same
example with MirroredStrategy with 2 GPUs:

```python
strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
def step_fn():
  i = tf.distribute.get_replica_context().replica_id_in_sync_group
  return tf.identity(i)

per_replica_result = strategy.run(step_fn)
# Check devices on which per replica result is:
strategy.experimental_local_results(per_replica_result)[0].device
# /job:localhost/replica:0/task:0/device:GPU:0
strategy.experimental_local_results(per_replica_result)[1].device
# /job:localhost/replica:0/task:0/device:GPU:1

total = strategy.reduce("SUM", per_replica_result, axis=None)
# Check device on which reduced result is:
total.device
# /job:localhost/replica:0/task:0/device:CPU:0

```

This API is typically used for aggregating the results returned from
different replicas, for reporting etc. For example, loss computed from
different replicas can be averaged using this API before printing.

Note: The result is copied to the "current" device - which would typically
be the CPU of the worker on which the program is running. For `TPUStrategy`,
it is the first TPU host. For multi client `MultiWorkerMirroredStrategy`,
this is CPU of each worker.

There are a number of different tf.distribute APIs for reducing values
across replicas:
* <a href="../../../tf/distribute/ReplicaContext.md#all_reduce"><code>tf.distribute.ReplicaContext.all_reduce</code></a>: This differs from
<a href="../../../tf/distribute/MirroredStrategy.md#reduce"><code>Strategy.reduce</code></a> in that it is for replica context and does
not copy the results to the host device. `all_reduce` should be typically
used for reductions inside the training step such as gradients.
* <a href="../../../tf/distribute/StrategyExtended.md#reduce_to"><code>tf.distribute.StrategyExtended.reduce_to</code></a> and
<a href="../../../tf/distribute/StrategyExtended.md#batch_reduce_to"><code>tf.distribute.StrategyExtended.batch_reduce_to</code></a>: These APIs are more
advanced versions of <a href="../../../tf/distribute/MirroredStrategy.md#reduce"><code>Strategy.reduce</code></a> as they allow customizing the
destination of the result. They are also called in cross replica context.

_What should axis be?_

Given a per-replica value returned by `run`, say a
per-example loss, the batch will be divided across all the replicas.  This
function allows you to aggregate across replicas and optionally also across
batch elements by specifying the axis parameter accordingly.

For example, if you have a global batch size of 8 and 2
replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and
`[4, 5, 6, 7]` will be on replica 1. With `axis=None`, `reduce` will
aggregate only across replicas, returning `[0+4, 1+5, 2+6, 3+7]`.
This is useful when each replica is computing a scalar or some other value
that doesn't have a "batch" dimension (like a gradient or loss).
```
strategy.reduce("sum", per_replica_result, axis=None)
```

Sometimes, you will want to aggregate across both the global batch _and_
all replicas. You can get this behavior by specifying the batch
dimension as the `axis`, typically `axis=0`. In this case it would return a
scalar `0+1+2+3+4+5+6+7`.
```
strategy.reduce("sum", per_replica_result, axis=0)
```

If there is a last partial batch, you will need to specify an axis so
that the resulting shape is consistent across replicas. So if the last
batch has size 6 and it is divided into [0, 1, 2, 3] and [4, 5], you
would get a shape mismatch unless you specify `axis=0`. If you specify
<a href="../../../tf/distribute/ReduceOp.md#MEAN"><code>tf.distribute.ReduceOp.MEAN</code></a>, using `axis=0` will use the correct
denominator of 6. Contrast this with computing `reduce_mean` to get a
scalar value on each replica and this function to average those means,
which will weigh some values `1/8` and others `1/4`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
a <a href="../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> value specifying how values should
be combined. Allows using string representation of the enum such as
"SUM", "MEAN".
</td>
</tr><tr>
<td>
`value`
</td>
<td>
a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> instance, e.g. returned by
<a href="../../../tf/distribute/MirroredStrategy.md#run"><code>Strategy.run</code></a>, to be combined into a single tensor. It can also be a
regular tensor when used with `OneDeviceStrategy` or default strategy.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
specifies the dimension to reduce along within each
replica's tensor. Should typically be set to the batch dimension, or
`None` to only reduce across replicas (e.g. if the tensor has no batch
dimension).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`.
</td>
</tr>

</table>



<h3 id="run"><code>run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1145-L1259">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    fn, args=(), kwargs=None, options=None
)
</code></pre>

Invokes `fn` on each replica, with the given arguments.

This method is the primary way to distribute your computation with a
tf.distribute object. It invokes `fn` on each replica. If `args` or `kwargs`
have <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, such as those produced by a
<a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> from
<a href="../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a>,
when `fn` is executed on a particular replica, it will be executed with the
component of <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> that correspond to that
replica.

`fn` is invoked under a replica context. `fn` may call
<a href="../../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context()</code></a> to access members such as
`all_reduce`. Please see the module-level docstring of tf.distribute for the
concept of replica context.

All arguments in `args` or `kwargs` should either be Python values of a
nested structure of tensors, e.g. a list of tensors, in which case `args`
and `kwargs` will be passed to the `fn` invoked on each replica. Or `args`
or `kwargs` can be <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing tensors or
composite tensors, i.e. <a href="../../../tf/compat/v1/TensorInfo/CompositeTensor.md"><code>tf.compat.v1.TensorInfo.CompositeTensor</code></a>, in which
case each `fn` call will get the component of a
<a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> corresponding to its replica.

IMPORTANT: Depending on the implementation of <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> and
whether eager execution is enabled, `fn` may be called one or more times. If
`fn` is annotated with <a href="../../../tf/function.md"><code>tf.function</code></a> or <a href="../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> is
called inside a <a href="../../../tf/function.md"><code>tf.function</code></a> (eager execution is disabled inside a
<a href="../../../tf/function.md"><code>tf.function</code></a> by default), `fn` is called once per replica to generate a
Tensorflow graph, which will then be reused for execution with new inputs.
Otherwise, if eager execution is enabled, `fn` will be called once per
replica every step just like regular python code.

#### Example usage:



1. Constant tensor input.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> tensor_input = tf.constant(3.0)
>>> @tf.function
... def replica_fn(input):
...   return input*2.0
>>> result = strategy.run(replica_fn, args=(tensor_input,))
>>> result
PerReplica:{
  0: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>,
  1: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>
}
```

2. DistributedValues input.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> @tf.function
... def run():
...   def value_fn(value_context):
...     return value_context.num_replicas_in_sync
...   distributed_values = (
...     strategy.experimental_distribute_values_from_function(
...       value_fn))
...   def replica_fn2(input):
...     return input*2
...   return strategy.run(replica_fn2, args=(distributed_values,))
>>> result = run()
>>> result
<tf.Tensor: shape=(), dtype=int32, numpy=4>
```

3. Use <a href="../../../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> to allreduce values.

```
>>> strategy = tf.distribute.MirroredStrategy(["gpu:0", "gpu:1"])
>>> @tf.function
... def run():
...    def value_fn(value_context):
...      return tf.constant(value_context.replica_id_in_sync_group)
...    distributed_values = (
...        strategy.experimental_distribute_values_from_function(
...            value_fn))
...    def replica_fn(input):
...      return tf.distribute.get_replica_context().all_reduce("sum", input)
...    return strategy.run(replica_fn, args=(distributed_values,))
>>> result = run()
>>> result
PerReplica:{
  0: <tf.Tensor: shape=(), dtype=int32, numpy=1>,
  1: <tf.Tensor: shape=(), dtype=int32, numpy=1>
}
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
The function to run on each replica.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Optional positional arguments to `fn`. Its element can be a Python
value, a tensor or a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Optional keyword arguments to `fn`. Its element can be a Python
value, a tensor or a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
An optional instance of <a href="../../../tf/distribute/RunOptions.md"><code>tf.distribute.RunOptions</code></a> specifying
the options to run `fn`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Merged return value of `fn` across replicas. The structure of the return
value is the same as the return value from `fn`. Each element in the
structure can either be <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, `Tensor`
objects, or `Tensor`s (for example, if running on a single replica).
</td>
</tr>

</table>



<h3 id="scope"><code>scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L822-L910">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>scope()
</code></pre>

Context manager to make the strategy current and distribute variables.

This method returns a context manager, and is used as follows:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> # Variable created inside scope:
>>> with strategy.scope():
...   mirrored_variable = tf.Variable(1.)
>>> mirrored_variable
MirroredVariable:{
  0: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>,
  1: <tf.Variable 'Variable/replica_1:0' shape=() dtype=float32, numpy=1.0>
}
>>> # Variable created outside scope:
>>> regular_variable = tf.Variable(1.)
>>> regular_variable
<tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>
```

_What happens when Strategy.scope is entered?_

* `strategy` is installed in the global context as the "current" strategy.
  Inside this scope, <a href="../../../tf/distribute/get_strategy.md"><code>tf.distribute.get_strategy()</code></a> will now return this
  strategy. Outside this scope, it returns the default no-op strategy.
* Entering the scope also enters the "cross-replica context". See
  <a href="../../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> for an explanation on cross-replica and
  replica contexts.
* Variable creation inside `scope` is intercepted by the strategy. Each
  strategy defines how it wants to affect the variable creation. Sync
  strategies like `MirroredStrategy`, `TPUStrategy` and
  `MultiWorkerMiroredStrategy` create variables replicated on each replica,
  whereas `ParameterServerStrategy` creates variables on the parameter
  servers. This is done using a custom <a href="../../../tf/variable_creator_scope.md"><code>tf.variable_creator_scope</code></a>.
* In some strategies, a default device scope may also be entered: in
  `MultiWorkerMiroredStrategy`, a default device scope of "/CPU:0" is
  entered on each worker.

Note: Entering a scope does not automatically distribute a computation, except
  in the case of high level training framework like keras `model.fit`. If
  you're not using `model.fit`, you
  need to use `strategy.run` API to explicitly distribute that computation.
  See an example in the [custom training loop tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training).


_What should be in scope and what should be outside?_

There are a number of requirements on what needs to happen inside the scope.
However, in places where we have information about which strategy is in use,
we often enter the scope for the user, so they don't have to do it
explicitly (i.e. calling those either inside or outside the scope is OK).

* Anything that creates variables that should be distributed variables
  must be in `strategy.scope`. This can be either by directly putting it in
  scope, or relying on another API like `strategy.run` or `model.fit` to
  enter it for you. Any variable that is created outside scope will not be
  distributed and may have performance implications. Common things that
  create variables in TF: models, optimizers, metrics. These should always
  be created inside the scope. Another source of variable creation can be
  a checkpoint restore - when variables are created lazily. Note that any
  variable created inside a strategy captures the strategy information. So
  reading and writing to these variables outside the `strategy.scope` can
  also work seamlessly, without the user having to enter the scope.
* Some strategy APIs (such as `strategy.run` and `strategy.reduce`) which
  require to be in a strategy's scope, enter the scope for you
  automatically, which means when using those APIs you don't need to
  enter the scope yourself.
* When a <a href="../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is created inside a `strategy.scope`, we capture
  this information. When high level training frameworks methods such as
  `model.compile`, `model.fit` etc are then called
  on this model, we automatically enter the scope, as well as use this
  strategy to distribute the training etc. See
  detailed example in [distributed keras tutorial](https://www.tensorflow.org/tutorials/distribute/keras).
  Note that simply calling the `model(..)` is not impacted - only high
  level training framework APIs are. `model.compile`, `model.fit`,
  `model.evaluate`, `model.predict` and `model.save` can all be called
  inside or outside the scope.
* The following can be either inside or outside the scope:
    * Creating the input datasets
    * Defining <a href="../../../tf/function.md"><code>tf.function</code></a>s that represent your training step
    * Saving APIs such as <a href="../../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a>. Loading creates variables,
      so that should go inside the scope if you want to train the model in a
      distributed way.
    * Checkpoint saving. As mentioned above - `checkpoint.restore` may
      sometimes need to be inside scope if it creates variables.

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





