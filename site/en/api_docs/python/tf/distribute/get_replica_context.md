page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.get_replica_context

### Aliases:

* `tf.contrib.distribute.get_replica_context`
* `tf.distribute.get_replica_context`

``` python
tf.distribute.get_replica_context()
```



Defined in [`tensorflow/python/distribute/distribution_strategy_context.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/distribution_strategy_context.py).

Returns the current <a href="../../tf/distribute/ReplicaContext"><code>tf.distribute.ReplicaContext</code></a> or `None`.

Returns `None` if in a cross-replica context.

Note that execution:

1. starts in the default (single-replica) replica context (this function
   will return the default `ReplicaContext` object);
2. switches to cross-replica context (in which case this will return
   `None`) when entering a `with tf.distribute.Strategy.scope():` block;
3. switches to a (non-default) replica context inside
   `extended.call_for_each_replica(fn, ...)`;
4. if `fn` calls `get_replica_context().merge_call(merge_fn, ...)`, then
   inside `merge_fn` you are back in the cross-replica context (and again
   this function will return `None`).

Note that you can also go directly from step 1 to 4 to switch to a
cross-replica context for the default <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>. You may
also switch from the cross-replica context of 4 to a replica context by
calling `extended.call_for_each_replica()`, jumping back to step 3.

Most <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> methods may only be executed in
a cross-replica context, in a replica context you should use the
`ReplicaContext` API instead.

#### Returns:

The current `ReplicaContext` object when in a replica context scope,
else `None`.

Within a particular block, exactly one of these two things will be true:

* `get_replica_context()` returns non-`None`, or
* `tf.distribute.is_cross_replica_context()` returns True.