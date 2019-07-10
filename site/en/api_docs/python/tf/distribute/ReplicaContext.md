page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.ReplicaContext

## Class `ReplicaContext`



### Aliases:

* Class `tf.contrib.distribute.ReplicaContext`
* Class `tf.distribute.ReplicaContext`



Defined in [`tensorflow/python/distribute/distribute_lib.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/distribute_lib.py).

<a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> API when in a replica context.

To be used inside your replicated step function, such as in a
<a href="../../tf/distribute/StrategyExtended#call_for_each_replica"><code>tf.distribute.StrategyExtended.call_for_each_replica</code></a> call.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    strategy,
    replica_id_in_sync_group
)
```

Initialize self.  See help(type(self)) for accurate signature.



## Properties

<h3 id="devices"><code>devices</code></h3>

The devices this replica is to be executed on, as a tuple of strings.

<h3 id="num_replicas_in_sync"><code>num_replicas_in_sync</code></h3>

Returns number of replicas over which gradients are aggregated.

<h3 id="replica_id_in_sync_group"><code>replica_id_in_sync_group</code></h3>

Which replica is being defined, from 0 to `num_replicas_in_sync - 1`.

<h3 id="strategy"><code>strategy</code></h3>

The current <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.



## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```



<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    exception_type,
    exception_value,
    traceback
)
```



<h3 id="merge_call"><code>merge_call</code></h3>

``` python
merge_call(
    merge_fn,
    args=(),
    kwargs=None
)
```

Merge args across replicas and run `merge_fn` in a cross-replica context.

This allows communication and coordination when there are multiple calls
to a model function triggered by a call to
`strategy.extended.call_for_each_replica(model_fn, ...)`.

See <a href="../../tf/distribute/StrategyExtended#call_for_each_replica"><code>tf.distribute.StrategyExtended.call_for_each_replica</code></a> for an
explanation.

If not inside a distributed scope, this is equivalent to:

```
strategy = tf.distribute.get_strategy()
with cross-replica-context(strategy):
  return merge_fn(strategy, *args, **kwargs)
```

#### Args:

* <b>`merge_fn`</b>: function that joins arguments from threads that are given as
    PerReplica. It accepts <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object as
    the first argument.
* <b>`args`</b>: List or tuple with positional per-thread arguments for `merge_fn`.
* <b>`kwargs`</b>: Dict with keyword per-thread arguments for `merge_fn`.


#### Returns:

The return value of `merge_fn`, except for `PerReplica` values which are
unpacked.



