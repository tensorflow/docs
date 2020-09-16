description: A class wrapping information needed by a distribute function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.ValueContext" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.distribute.experimental.ValueContext

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L514-L574">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A class wrapping information needed by a distribute function.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.ValueContext(
    replica_id_in_sync_group=0, num_replicas_in_sync=1
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a context class that is passed to the `value_fn` in
`strategy.experimental_distribute_values_from_function` and contains
information about the compute replicas. The `num_replicas_in_sync` and
`replica_id` can be used to customize the value on each replica.

#### Example usage:



1. Directly constructed.

```
>>> def value_fn(context):
...   return context.replica_id_in_sync_group/context.num_replicas_in_sync
>>> context = tf.distribute.experimental.ValueContext(
...   replica_id_in_sync_group=2, num_replicas_in_sync=4)
>>> per_replica_value = value_fn(context)
>>> per_replica_value
0.5
```

2. Passed in by `experimental_distribute_values_from_function`.

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> def value_fn(value_context):
...   return value_context.num_replicas_in_sync
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(1,)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`replica_id_in_sync_group`
</td>
<td>
the current replica_id, should be an int in
[0,`num_replicas_in_sync`).
</td>
</tr><tr>
<td>
`num_replicas_in_sync`
</td>
<td>
the number of replicas that are in sync.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`num_replicas_in_sync`
</td>
<td>
Returns the number of compute replicas in sync.
</td>
</tr><tr>
<td>
`replica_id_in_sync_group`
</td>
<td>
Returns the replica ID.
</td>
</tr>
</table>



