description: Return a device function to use when building a Graph for replicas.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.replica_device_setter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.replica_device_setter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/device_setter.py#L136-L231">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return a `device function` to use when building a Graph for replicas.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.replica_device_setter(
    ps_tasks=0, ps_device='/job:ps', worker_device='/job:worker',
    merge_devices=(True), cluster=None, ps_ops=None, ps_strategy=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Device Functions are used in `with tf.device(device_function):` statement to
automatically assign devices to `Operation` objects as they are constructed,
Device constraints are added from the inner-most context first, working
outwards. The merging behavior adds constraints to fields that are yet unset
by a more inner context. Currently the fields are (job, task, cpu/gpu).

If `cluster` is `None`, and `ps_tasks` is 0, the returned function is a no-op.
Otherwise, the value of `ps_tasks` is derived from `cluster`.

By default, only Variable ops are placed on ps tasks, and the placement
strategy is round-robin over all ps tasks. A custom `ps_strategy` may be used
to do more intelligent placement, such as
`tf.contrib.training.GreedyLoadBalancingStrategy`.

For example,

```python
# To build a cluster with two ps jobs on hosts ps0 and ps1, and 3 worker
# jobs on hosts worker0, worker1 and worker2.
cluster_spec = {
    "ps": ["ps0:2222", "ps1:2222"],
    "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]}
with
tf.device(tf.compat.v1.train.replica_device_setter(cluster=cluster_spec)):
  # Build your graph
  v1 = tf.Variable(...)  # assigned to /job:ps/task:0
  v2 = tf.Variable(...)  # assigned to /job:ps/task:1
  v3 = tf.Variable(...)  # assigned to /job:ps/task:0
# Run compute
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ps_tasks`
</td>
<td>
Number of tasks in the `ps` job.  Ignored if `cluster` is
provided.
</td>
</tr><tr>
<td>
`ps_device`
</td>
<td>
String.  Device of the `ps` job.  If empty no `ps` job is used.
Defaults to `ps`.
</td>
</tr><tr>
<td>
`worker_device`
</td>
<td>
String.  Device of the `worker` job.  If empty no `worker`
job is used.
</td>
</tr><tr>
<td>
`merge_devices`
</td>
<td>
`Boolean`. If `True`, merges or only sets a device if the
device constraint is completely unset. merges device specification rather
than overriding them.
</td>
</tr><tr>
<td>
`cluster`
</td>
<td>
`ClusterDef` proto or `ClusterSpec`.
</td>
</tr><tr>
<td>
`ps_ops`
</td>
<td>
List of strings representing `Operation` types that need to be
placed on `ps` devices.  If `None`, defaults to `STANDARD_PS_OPS`.
</td>
</tr><tr>
<td>
`ps_strategy`
</td>
<td>
A callable invoked for every ps `Operation` (i.e. matched by
`ps_ops`), that takes the `Operation` and returns the ps task index to
use.  If `None`, defaults to a round-robin strategy across all `ps`
devices.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A function to pass to <a href="../../../../tf/device.md"><code>tf.device()</code></a>.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
TypeError if `cluster` is not a dictionary or `ClusterDef` protocol buffer,
or if `ps_strategy` is provided but not a callable.
</td>
</tr>

</table>

