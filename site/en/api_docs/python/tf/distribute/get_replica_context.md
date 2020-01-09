page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.get_replica_context


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/distribute/get_replica_context">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribution_strategy_context.py#L89-L135">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the current <a href="../../tf/distribute/ReplicaContext"><code>tf.distribute.ReplicaContext</code></a> or `None`.

### Aliases:

* <a href="/api_docs/python/tf/distribute/get_replica_context"><code>tf.compat.v1.distribute.get_replica_context</code></a>
* <a href="/api_docs/python/tf/distribute/get_replica_context"><code>tf.compat.v2.distribute.get_replica_context</code></a>
* <a href="/api_docs/python/tf/distribute/get_replica_context"><code>tf.contrib.distribute.get_replica_context</code></a>


``` python
tf.distribute.get_replica_context()
```



<!-- Placeholder for "Used in" -->

Returns `None` if in a cross-replica context.

#### Note that execution:



1. starts in the default (single-replica) replica context (this function
   will return the default `ReplicaContext` object);
2. switches to cross-replica context (in which case this will return
   `None`) when entering a `with tf.distribute.Strategy.scope():` block;
3. switches to a (non-default) replica context inside
   `strategy.experimental_run_v2(fn, ...)`;
4. if `fn` calls `get_replica_context().merge_call(merge_fn, ...)`, then
   inside `merge_fn` you are back in the cross-replica context (and again
   this function will return `None`).

Most <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> methods may only be executed in
a cross-replica context, in a replica context you should use the
API of the <a href="../../tf/distribute/ReplicaContext"><code>tf.distribute.ReplicaContext</code></a> object returned by this
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

  strategy.experimental_run_v2(f)
```

#### Returns:

The current <a href="../../tf/distribute/ReplicaContext"><code>tf.distribute.ReplicaContext</code></a> object when in a replica context
scope, else `None`.

Within a particular block, exactly one of these two things will be true:

* `get_replica_context()` returns non-`None`, or
* `tf.distribute.is_cross_replica_context()` returns True.
