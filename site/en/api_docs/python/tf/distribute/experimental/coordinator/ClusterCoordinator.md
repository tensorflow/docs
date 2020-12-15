description: An object to schedule and coordinate remote function execution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.coordinator.ClusterCoordinator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_per_worker_dataset"/>
<meta itemprop="property" content="done"/>
<meta itemprop="property" content="fetch"/>
<meta itemprop="property" content="join"/>
<meta itemprop="property" content="schedule"/>
</div>

# tf.distribute.experimental.coordinator.ClusterCoordinator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L918-L1243">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An object to schedule and coordinate remote function execution.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.coordinator.ClusterCoordinator(
    strategy
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class is used to create fault-tolerant resources and dispatch functions
to remote TensorFlow servers.

Currently, this class is not supported to be used in a standalone manner. It
should be used in conjunction with a <a href="../../../../tf/distribute.md"><code>tf.distribute</code></a> strategy that is designed
to work with it. The `ClusterCoordinator` class currently only works
<a href="../../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a>.

__The `schedule`/`join` APIs__

The most important APIs provided by this class is the `schedule`/`join` pair.
The `schedule` API is non-blocking in that it queues a <a href="../../../../tf/function.md"><code>tf.function</code></a> and
returns a `RemoteValue` immediately. The queued functions will be dispatched
to remote workers in background threads and their `RemoteValue`s will be
filled asynchronously. Since `schedule` doesn’t require worker assignment, the
<a href="../../../../tf/function.md"><code>tf.function</code></a> passed in can be executed on any available worker. If the worker
it is executed on becomes unavailable before its completion, it will be
migrated to another worker. Because of this fact and function execution is not
atomic, a function may be executed more than once.

__Handling Task Failure__

This class when used with
<a href="../../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a>, comes with built-in
fault tolerance for worker failures. That is, when some workers are not
available for any reason to be reached from the coordinator, the training
progress continues to be made with the remaining workers. Upon recovery of a
failed worker, it will be added for function execution after datasets created
by `create_per_worker_dataset` are re-built on it.

When a parameter server the coordinator fails, a
<a href="../../../../tf/errors/UnavailableError.md"><code>tf.errors.UnavailableError</code></a> is raised by `schedule`, `join` or `done`. In
this case, in addition to bringing back the failed parameter server, users
should restart the coordinator to so that it reconnects to the parameter
server, re-creates the variables and loads checkpoints. If the coordinator
fails, users need to bring it back as well. The program will automatically
connect to the parameter servers and workers, and continue the progress from a
checkpoint.

It is thus essential that in user's program, a checkpoint file is periodically
saved, and restored at the start of the program. If an
<a href="../../../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a> is checkpointed, after restoring from a
checkpoiont, its `iterations` property roughly indicates the number of steps
that have been made. This can be used to decide how many epochs and steps are
needed before the training completion.

See <a href="../../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> docstring for an
example usage of this API.

This is currently under development, and the API as well as implementation
are subject to changes.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`strategy`
</td>
<td>
a supported <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> object. Currently, only
<a href="../../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> is supported.
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
if the strategy being used is not supported.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`strategy`
</td>
<td>
Returns the `Strategy` associated with the `ClusterCoordinator`.
</td>
</tr>
</table>



## Methods

<h3 id="create_per_worker_dataset"><code>create_per_worker_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1100-L1163">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_per_worker_dataset(
    dataset_fn
)
</code></pre>

Create dataset on workers by calling `dataset_fn` on worker devices.

This creates the given dataset generated by dataset_fn on workers
and returns an object that represents the collection of those individual
datasets. Calling `iter` on such collection of datasets returns a
<a href="../../../../tf/distribute/experimental/coordinator/PerWorkerValues.md"><code>tf.distribute.experimental.coordinator.PerWorkerValues</code></a>, which is a
collection of iterators, where the iterators have been placed on respective
workers.

Calling `next` on a `PerWorkerValues` of iterator is unsupported. The
iterator is meant to be passed as an argument into
<a href="../../../../tf/distribute/experimental/coordinator/ClusterCoordinator.md#schedule"><code>tf.distribute.experimental.coordinator.ClusterCoordinator.schedule</code></a>. When
the scheduled function is about to be executed by a worker, the
function will receive the individual iterator that corresponds to the
worker. The `next` method can be called on an iterator inside a
scheduled function when the iterator is an input of the function.

Currently the `schedule` method assumes workers are all the same and thus
assumes the datasets on different workers are the same, except they may be
shuffled differently if they contain a `dataset.shuffle` operation and a
random seed is not set. Because of this, we also recommend the datasets to
be repeated indefinitely and schedule a finite number of steps instead of
relying on the `OutOfRangeError` from a dataset.


#### Example:



```python
strategy = tf.distribute.experimental.ParameterServerStrategy(
    cluster_resolver=...)
coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
    strategy=strategy)

@tf.function
def worker_fn(iterator):
  return next(iterator)

def per_worker_dataset_fn():
  return strategy.distribute_datasets_from_function(
      lambda x: tf.data.from_tensor_slices([3] * 3)

per_worker_dataset = coordinator.create_per_worker_dataset(
    per_worker_dataset_fn)
per_worker_iter = iter(per_worker_dataset)
remote_value = coordinator.schedule(worker_fn, args=(per_worker_iter,))
assert remote_value.fetch() == 3
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset_fn`
</td>
<td>
The dataset function that returns a dataset. This is to be
executed on the workers.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An object that represents the collection of those individual
datasets. `iter` is expected to be called on this object that returns
a <a href="../../../../tf/distribute/experimental/coordinator/PerWorkerValues.md"><code>tf.distribute.experimental.coordinator.PerWorkerValues</code></a> of the
iterators (that are on the workers).
</td>
</tr>

</table>



<h3 id="done"><code>done</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1082-L1098">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>done()
</code></pre>

Returns whether all the scheduled functions have finished execution.

If any previously scheduled function raises an error, `done` will fail by
raising any one of those errors.

When `done` returns True or raises, it guarantees that there is no function
that is still being executed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Whether all the scheduled functions have finished execution.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`Exception`
</td>
<td>
one of the exceptions caught by the coordinator by any
previously scheduled function since the last time an error was thrown or
since the beginning of the program.
</td>
</tr>
</table>



<h3 id="fetch"><code>fetch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1187-L1243">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>fetch(
    val
)
</code></pre>

Blocking call to fetch results from the remote values.

This is a wrapper around
<a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md#fetch"><code>tf.distribute.experimental.coordinator.RemoteValue.fetch</code></a> for a
`RemoteValue` structure; it returns the execution results of
`RemoteValue`s. If not ready, wait for them while blocking the caller.

#### Example:


```python
strategy = ...
coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
    strategy)

def dataset_fn():
  return tf.data.Dataset.from_tensor_slices([1, 1, 1])

with strategy.scope():
  v = tf.Variable(initial_value=0)

@tf.function
def worker_fn(iterator):
  def replica_fn(x):
    v.assign_add(x)
    return v.read_value()
  return strategy.run(replica_fn, args=(next(iterator),))

distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn)
distributed_iterator = iter(distributed_dataset)
result = coordinator.schedule(worker_fn, args=(distributed_iterator,))
assert coordinator.fetch(result) == 1
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`val`
</td>
<td>
The value to fetch the results from. If this is structure of
<a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a>, `fetch()` will be
called on the individual
<a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a> to get the result.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
If `val` is a <a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a> or a
structure of <a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a>s,
return the fetched <a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a>
values immediately if they are available, or block the call until they are
available, and return the fetched
<a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a> values with the same
structure. If `val` is other types, return it as-is.
</td>
</tr>

</table>



<h3 id="join"><code>join</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L1061-L1080">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>join()
</code></pre>

Blocks until all the scheduled functions have finished execution.

If any previously scheduled function raises an error, `join` will fail by
raising any one of those errors, and clear the errors collected so far. If
this happens, some of the previously scheduled functions may have not been
executed. Users can call `fetch` on the returned
<a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a> to inspect if they have
executed, failed, or cancelled. If some that have been cancelled need to be
rescheduled, users should call `schedule` with the function again.

When `join` returns or raises, it guarantees that there is no function that
is still being executed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`Exception`
</td>
<td>
one of the exceptions caught by the coordinator by any
previously scheduled function since the last time an error was thrown or
since the beginning of the program.
</td>
</tr>
</table>



<h3 id="schedule"><code>schedule</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L999-L1059">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>schedule(
    fn, args=None, kwargs=None
)
</code></pre>

Schedules `fn` to be dispatched to a worker for asynchronous execution.

This method is non-blocking in that it queues the `fn` which will be
executed later and returns a
<a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a> object immediately.
`fetch` can be called on the it to wait for the function execution to finish
and retrieve its output from a remote worker. On the other hand, call
<a href="../../../../tf/distribute/experimental/coordinator/ClusterCoordinator.md#join"><code>tf.distribute.experimental.coordinator.ClusterCoordinator.join</code></a> to wait for
all scheduled functions to finish.

`schedule` guarantees that `fn` will be executed on a worker at least once;
it could be more than once if its corresponding worker fails in the middle
of its execution. Note that since worker can fail at any point when
executing the function, it is possible that the function is partially
executed, but <a href="../../../../tf/distribute/experimental/coordinator/ClusterCoordinator.md"><code>tf.distribute.experimental.coordinator.ClusterCoordinator</code></a>
guarantees that in those events, the function will eventually be executed on
any worker that is available.

If any previously scheduled function raises an error, `schedule` will raise
any one of those errors, and clear the errors collected so far. What happens
here, some of the previously scheduled functions may have not been executed.
User can call `fetch` on the returned
<a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a> to inspect if they have
executed, failed, or cancelled, and reschedule the corresponding function if
needed.

When `schedule` raises, it guarantees that there is no function that is
still being executed.

At this time, there is no support of worker assignment for function
execution, or priority of the workers.

`args` and `kwargs` are the arguments passed into `fn`, when `fn` is
executed on a worker. They can be
<a href="../../../../tf/distribute/experimental/coordinator/PerWorkerValues.md"><code>tf.distribute.experimental.coordinator.PerWorkerValues</code></a> and in this case,
the argument will be substituted with the corresponding component on the
target worker. Arguments that are not
<a href="../../../../tf/distribute/experimental/coordinator/PerWorkerValues.md"><code>tf.distribute.experimental.coordinator.PerWorkerValues</code></a> will be passed into
`fn` as-is. Currently, <a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a>
is not supported to be input `args` or `kwargs`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fn`
</td>
<td>
A <a href="../../../../tf/function.md"><code>tf.function</code></a>; the function to be dispatched to a worker for
execution asynchronously.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Positional arguments for `fn`.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Keyword arguments for `fn`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../../tf/distribute/experimental/coordinator/RemoteValue.md"><code>tf.distribute.experimental.coordinator.RemoteValue</code></a> object that
represents the output of the function scheduled.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`Exception`
</td>
<td>
one of the exceptions caught by the coordinator from any
previously scheduled function, since the last time an error was thrown
or since the beginning of the program.
</td>
</tr>
</table>





