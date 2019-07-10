page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.get_cross_replica_context

``` python
tf.contrib.distribute.get_cross_replica_context()
```



Defined in [`tensorflow/python/distribute/distribution_strategy_context.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/distribution_strategy_context.py).

Returns the current tf.distribute.Strategy if in a cross-replica context.

DEPRECATED: Please use `in_cross_replica_context()` and
`get_distribution_strategy()` instead.

Note that execution:

1. starts in the default (single-replica) replica context;
2. switches to cross-replica context when entering a
   `with tf.distribute.Strategy.scope():` block;
3. switches to a (non-default) replica context inside
   `call_for_each_replica(fn, ...)`;
4. if `fn` calls `get_replica_context()->merge_call(merge_fn, ...)`, then
   inside `merge_fn` you are back in the cross-replica context.

Note that you can also go directly from step 1 to 4 to switch to a
cross-replica context for the default <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>. You may
also switch from the cross-replica context of 4 to a replica context by
calling `call_for_each_replica()`, jumping back to step 3.

Most <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> methods may only be executed in
a cross-replica context.

#### Returns:

Returns the current <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object in a cross-replica
context, or `None`.

Exactly one of `get_replica_context()` and `get_cross_replica_context()`
will return `None` in a particular block.