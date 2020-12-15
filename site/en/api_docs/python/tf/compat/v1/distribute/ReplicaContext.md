description: A class with a collection of APIs that can be called in a replica context.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distribute.ReplicaContext" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="all_reduce"/>
<meta itemprop="property" content="merge_call"/>
</div>

# tf.compat.v1.distribute.ReplicaContext

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L3272-L3273">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A class with a collection of APIs that can be called in a replica context.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.distribute.ReplicaContext(
    strategy, replica_id_in_sync_group
)
</code></pre>



<!-- Placeholder for "Used in" -->

You can use <a href="../../../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context</code></a> to get an instance of
`ReplicaContext`, which can only be called inside the function passed to
<a href="../../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a>.

```
>>> strategy = tf.distribute.MirroredStrategy(['GPU:0', 'GPU:1'])
>>> def func():
...   replica_context = tf.distribute.get_replica_context()
...   return replica_context.replica_id_in_sync_group
>>> strategy.run(func)
PerReplica:{
  0: <tf.Tensor: shape=(), dtype=int32, numpy=0>,
  1: <tf.Tensor: shape=(), dtype=int32, numpy=1>
}
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`strategy`
</td>
<td>
A <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.
</td>
</tr><tr>
<td>
`replica_id_in_sync_group`
</td>
<td>
An integer, a `Tensor` or None. Prefer an
integer whenever possible to avoid issues with nested <a href="../../../../tf/function.md"><code>tf.function</code></a>. It
accepts a `Tensor` only to be compatible with `tpu.replicate`.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`devices`
</td>
<td>
Returns the devices this replica is to be executed on, as a tuple of strings. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please avoid relying on devices property.

NOTE: For <a href="../../../../tf/distribute/MirroredStrategy.md"><code>tf.distribute.MirroredStrategy</code></a> and
<a href="../../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>, this returns a
nested
list of device strings, e.g, [["GPU:0"]].
</td>
</tr><tr>
<td>
`num_replicas_in_sync`
</td>
<td>
Returns number of replicas that are kept in sync.
</td>
</tr><tr>
<td>
`replica_id_in_sync_group`
</td>
<td>
Returns the id of the replica.

This identifies the replica among all replicas that are kept in sync. The
value of the replica id can range from 0 to
<a href="../../../../tf/distribute/ReplicaContext.md#num_replicas_in_sync"><code>tf.distribute.ReplicaContext.num_replicas_in_sync</code></a> - 1.

NOTE: This is not guaranteed to be the same ID as the XLA replica ID use
for low-level operations such as collective_permute.
</td>
</tr><tr>
<td>
`strategy`
</td>
<td>
The current <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> object.
</td>
</tr>
</table>



## Methods

<h3 id="all_reduce"><code>all_reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L3009-L3094">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>all_reduce(
    reduce_op, value, options=None
)
</code></pre>

All-reduces `value` across all replicas.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> def step_fn():
...   ctx = tf.distribute.get_replica_context()
...   value = tf.identity(1.)
...   return ctx.all_reduce(tf.distribute.ReduceOp.SUM, value)
>>> strategy.experimental_local_results(strategy.run(step_fn))
(<tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
 <tf.Tensor: shape=(), dtype=float32, numpy=2.0>)
```

It supports batched operations. You can pass a list of values and it
attempts to batch them when possible. You can also specify `options`
to indicate the desired batching behavior, e.g. batch the values into
multiple packs so that they can better overlap with computations.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> def step_fn():
...   ctx = tf.distribute.get_replica_context()
...   value1 = tf.identity(1.)
...   value2 = tf.identity(2.)
...   return ctx.all_reduce(tf.distribute.ReduceOp.SUM, [value1, value2])
>>> strategy.experimental_local_results(strategy.run(step_fn))
([PerReplica:{
  0: <tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
  1: <tf.Tensor: shape=(), dtype=float32, numpy=2.0>
}, PerReplica:{
  0: <tf.Tensor: shape=(), dtype=float32, numpy=4.0>,
  1: <tf.Tensor: shape=(), dtype=float32, numpy=4.0>
}],)
```

Note that all replicas need to participate in the all-reduce, otherwise this
operation hangs. Note that if there're multiple all-reduces, they need to
execute in the same order on all replicas. Dispatching all-reduce based on
conditions is usually error-prone.

This API currently can only be called in the replica context. Other
variants to reduce values across replicas are:
* <a href="../../../../tf/distribute/StrategyExtended.md#reduce_to"><code>tf.distribute.StrategyExtended.reduce_to</code></a>: the reduce and all-reduce API
  in the cross-replica context.
* <a href="../../../../tf/distribute/StrategyExtended.md#batch_reduce_to"><code>tf.distribute.StrategyExtended.batch_reduce_to</code></a>: the batched reduce and
  all-reduce API in the cross-replica context.
* <a href="../../../../tf/distribute/Strategy.md#reduce"><code>tf.distribute.Strategy.reduce</code></a>: a more convenient method to reduce
  to the host in cross-replica context.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
a <a href="../../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> value specifying how values should
be combined. Allows using string representation of the enum such as
"SUM", "MEAN".
</td>
</tr><tr>
<td>
`value`
</td>
<td>
a nested structure of <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> which <a href="../../../../tf/nest/flatten.md"><code>tf.nest.flatten</code></a> accepts.
The structure and the shapes of the <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> need to be same on all
replicas.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
a <a href="../../../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a>. Options to
perform collective operations. This overrides the default options if the
<a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> takes one in the constructor. See
<a href="../../../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a> for details of the
options.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A nested structure of <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> with the reduced values. The structure
is the same as `value`.
</td>
</tr>

</table>



<h3 id="merge_call"><code>merge_call</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L2908-L2941">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>merge_call(
    merge_fn, args=(), kwargs=None
)
</code></pre>

Merge args across replicas and run `merge_fn` in a cross-replica context.

This allows communication and coordination when there are multiple calls
to the step_fn triggered by a call to `strategy.run(step_fn, ...)`.

See <a href="../../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> for an explanation.

If not inside a distributed scope, this is equivalent to:

```
strategy = tf.distribute.get_strategy()
with cross-replica-context(strategy):
  return merge_fn(strategy, *args, **kwargs)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`merge_fn`
</td>
<td>
Function that joins arguments from threads that are given as
PerReplica. It accepts <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> object as
the first argument.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
List or tuple with positional per-thread arguments for `merge_fn`.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Dict with keyword per-thread arguments for `merge_fn`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The return value of `merge_fn`, except for `PerReplica` values which are
unpacked.
</td>
</tr>

</table>





