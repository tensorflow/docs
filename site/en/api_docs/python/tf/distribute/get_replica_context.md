description: Returns the current <a href="../../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> or None.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.get_replica_context" />
<meta itemprop="path" content="Stable" />
</div>

# tf.distribute.get_replica_context

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribution_strategy_context.py#L90-L135">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the current <a href="../../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> or `None`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.get_replica_context`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.get_replica_context()
</code></pre>



<!-- Placeholder for "Used in" -->

Returns `None` if in a cross-replica context.

#### Note that execution:



1. starts in the default (single-replica) replica context (this function
   will return the default `ReplicaContext` object);
2. switches to cross-replica context (in which case this will return
   `None`) when entering a `with tf.distribute.Strategy.scope():` block;
3. switches to a (non-default) replica context inside `strategy.run(fn, ...)`;
4. if `fn` calls `get_replica_context().merge_call(merge_fn, ...)`, then
   inside `merge_fn` you are back in the cross-replica context (and again
   this function will return `None`).

Most <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> methods may only be executed in
a cross-replica context, in a replica context you should use the
API of the <a href="../../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> object returned by this
method instead.

```
assert tf.distribute.get_replica_context() is not None  # default
with strategy.scope():
  assert tf.distribute.get_replica_context() is None

  def f():
    replica_context = tf.distribute.get_replica_context()  # for strategy
    assert replica_context is not None
    tf.print("Replica id: ", replica_context.replica_id_in_sync_group,
             " of ", replica_context.num_replicas_in_sync)

  strategy.run(f)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The current <a href="../../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> object when in a replica context
scope, else `None`.

Within a particular block, exactly one of these two things will be true:

* `get_replica_context()` returns non-`None`, or
* `tf.distribute.is_cross_replica_context()` returns True.
</td>
</tr>

</table>

