description: <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> API when in a replica context.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.ReplicaContext" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="all_reduce"/>
<meta itemprop="property" content="merge_call"/>
</div>

# tf.distribute.ReplicaContext

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2355-L2511">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



<a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> API when in a replica context.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.ReplicaContext`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.ReplicaContext(
    strategy, replica_id_in_sync_group
)
</code></pre>



<!-- Placeholder for "Used in" -->

You can use <a href="../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context</code></a> to get an instance of
`ReplicaContext`. This should be inside your replicated step function, such
as in a <a href="../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> call.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`devices`
</td>
<td>
The devices this replica is to be executed on, as a tuple of strings.
</td>
</tr><tr>
<td>
`num_replicas_in_sync`
</td>
<td>
Returns number of replicas over which gradients are aggregated.
</td>
</tr><tr>
<td>
`replica_id_in_sync_group`
</td>
<td>
Returns the id of the replica being defined.

This identifies the replica that is part of a sync group. Currently we
assume that all sync groups contain the same number of replicas. The value
of the replica id can range from 0 to `num_replica_in_sync` - 1.

NOTE: This is not guaranteed to be the same ID as the XLA replica ID use
for low-level operations such as collective_permute.
</td>
</tr><tr>
<td>
`strategy`
</td>
<td>
The current <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> object.
</td>
</tr>
</table>



## Methods

<h3 id="all_reduce"><code>all_reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2461-L2511">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>all_reduce(
    reduce_op, value, experimental_hints=None
)
</code></pre>

All-reduces the given `value Tensor` nest across replicas.

If `all_reduce` is called in any replica, it must be called in all replicas.
The nested structure and `Tensor` shapes must be identical in all replicas.

IMPORTANT: The ordering of communications must be identical in all replicas.

Example with two replicas:
  Replica 0 `value`: {'a': 1, 'b': [40, 1]}
  Replica 1 `value`: {'a': 3, 'b': [ 2, 98]}

  If `reduce_op` == `SUM`:
    Result (on all replicas): {'a': 4, 'b': [42, 99]}

  If `reduce_op` == `MEAN`:
    Result (on all replicas): {'a': 2, 'b': [21, 49.5]}

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
Reduction type, an instance of <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> enum.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
The nested structure of `Tensor`s to all-reduce. The structure must
be compatible with <a href="../../tf/nest.md"><code>tf.nest</code></a>.
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
A `Tensor` nest with the reduced `value`s from each replica.
</td>
</tr>

</table>



<h3 id="merge_call"><code>merge_call</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2388-L2420">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>merge_call(
    merge_fn, args=(), kwargs=None
)
</code></pre>

Merge args across replicas and run `merge_fn` in a cross-replica context.

This allows communication and coordination when there are multiple calls
to the step_fn triggered by a call to `strategy.run(step_fn, ...)`.

See <a href="../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> for an explanation.

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
PerReplica. It accepts <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> object as
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



<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2370-L2380">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>




<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L2382-L2386">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    exception_type, exception_value, traceback
)
</code></pre>






