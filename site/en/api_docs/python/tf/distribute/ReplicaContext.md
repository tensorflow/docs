page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.ReplicaContext

## Class `ReplicaContext`

<a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> API when in a replica context.



### Aliases:

* Class `tf.compat.v1.distribute.ReplicaContext`
* Class `tf.compat.v2.distribute.ReplicaContext`
* Class `tf.contrib.distribute.ReplicaContext`
* Class `tf.distribute.ReplicaContext`



Defined in [`python/distribute/distribute_lib.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/distribute_lib.py).

<!-- Placeholder for "Used in" -->

To be used inside your replicated step function, such as in a
<a href="../../tf/distribute/Strategy#experimental_run_v2"><code>tf.distribute.Strategy.experimental_run_v2</code></a> call.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    strategy,
    replica_id_in_sync_group
)
```






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




<h3 id="all_reduce"><code>all_reduce</code></h3>

``` python
all_reduce(
    reduce_op,
    value
)
```

All-reduces the given `Tensor` nest across replicas.

If `all_reduce` is called in any replica, it must be called in all replicas.
The nested structure and `Tensor` shapes must be identical in all replicas.

IMPORTANT: The ordering of communications must be identical in all replicas.

Example with two replicas:
  Replica 0 `value`: {'a': 1, 'b': [40,  1]}
  Replica 1 `value`: {'a': 3, 'b': [ 2, 98]}

  If `reduce_op` == `SUM`:
    Result (on all replicas): {'a': 4, 'b': [42, 99]}

  If `reduce_op` == `MEAN`:
    Result (on all replicas): {'a': 2, 'b': [21, 49.5]}

#### Args:


* <b>`reduce_op`</b>: Reduction type, an instance of <a href="../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> enum.
* <b>`value`</b>: The nested structure of `Tensor`s to all-reduced.
  The structure must be compatible with <a href="../../tf/nest"><code>tf.nest</code></a>.


#### Returns:

A `Tensor` nest with the reduced `value`s from each replica.


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
`strategy.experimental_run_v2(model_fn, ...)`.

See <a href="../../tf/distribute/Strategy#experimental_run_v2"><code>tf.distribute.Strategy.experimental_run_v2</code></a> for an
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




