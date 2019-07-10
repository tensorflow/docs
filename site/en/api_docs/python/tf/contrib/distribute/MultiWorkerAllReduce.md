page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.MultiWorkerAllReduce

## Class `MultiWorkerAllReduce`

Inherits From: [`AllReduceCrossDeviceOps`](../../../tf/contrib/distribute/AllReduceCrossDeviceOps)



Defined in [`tensorflow/python/distribute/cross_device_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cross_device_ops.py).

All-reduce algorithms for distributed TensorFlow.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    worker_devices,
    num_gpus_per_worker,
    all_reduce_spec=('pscpu/pscpu', 2, -1),
    num_packs=0,
    agg_small_grads_max_bytes=0,
    agg_small_grads_max_group=10
)
```

Initialize the all-reduce algorithm.

#### Args:

* <b>`worker_devices`</b>: a list of device strings for workers participating in
    all-reduce.
* <b>`num_gpus_per_worker`</b>: number of GPU devices per worker.
* <b>`all_reduce_spec`</b>: a tuple or a named tuple or a list of tuples specifying
    the all-reduce algorithm.
    1. The first element of a tuple is the name of the all-reduce algorithm.
    Valid algorithm names are: "nccl", "nccl/xring", "nccl/rechd",
    "nccl/pscpu", "xring", "pscpu", "psgpu", "pscpu/pscpu". Algorithms with
    a "/" are hierarchical, so two all-reduces are executed, the first one
    aggregates tensors within a worker and the second aggregates across
    workers.
    2. The second element of a tuple is the number of shards when doing
    all-reduce. Let's say its values is M, each tensor after packing will be
    split into M shards and then M parallel all-reduces would be performed
    before finally they are concatenated backed into a complete tensor.
    3. The third element is the maximum size of tensors that will be
    applicable for the algorithm specified by the first element. For
    example, if all_reduce_spec=[("nccl", 2, 1024), ("pscpu/pscpu", 2, -1)],
    tensors with size not larger than 1024 bytes will be applied a 2-shard
    "nccl" all-reduce and other tensors will be applied a 2-shard
    "pscpu/pscpu" algorithm. The third elements should be in increasing
    order across tuples and end with -1 which indicates infinity.
* <b>`num_packs`</b>: see AllReduceCrossDeviceOps.
* <b>`agg_small_grads_max_bytes`</b>: see AllReduceCrossDeviceOps.
* <b>`agg_small_grads_max_group`</b>: see AllReduceCrossDeviceOps.



## Methods

<h3 id="batch_reduce"><code>batch_reduce</code></h3>

``` python
batch_reduce(
    reduce_op,
    value_destination_pairs
)
```

Reduce PerReplica objects in a batch.

Reduce each first element in `value_destination_pairs` to each second
element which indicates the destinations.

#### Args:

* <b>`reduce_op`</b>: Indicates how per_replica_value will be reduced. Accepted
    values are <a href="../../../tf/distribute/ReduceOp#SUM"><code>tf.distribute.ReduceOp.SUM</code></a>, <a href="../../../tf/distribute/ReduceOp#MEAN"><code>tf.distribute.ReduceOp.MEAN</code></a>.
* <b>`value_destination_pairs`</b>: a list or a tuple of tuples of PerReplica objects
    (or tensors with device set if there is one device) and destinations.


#### Returns:

a list of Mirrored objects.


#### Raises:

* <b>`ValueError`</b>: if `value_destination_pairs` is not a list or a tuple of
    tuples of PerReplica objects and destinations

<h3 id="broadcast"><code>broadcast</code></h3>

``` python
broadcast(
    tensor,
    destinations
)
```

Broadcast the `tensor` to destinations.

#### Args:

* <b>`tensor`</b>: the tensor to broadcast.
* <b>`destinations`</b>: the broadcast destinations.


#### Returns:

a Mirrored object.

<h3 id="reduce"><code>reduce</code></h3>

``` python
reduce(
    reduce_op,
    per_replica_value,
    destinations
)
```

Reduce `per_replica_value` to `destinations`.

It runs the reduction operation defined by `reduce_op` and put the
result on `destinations`.

#### Args:

* <b>`reduce_op`</b>: Indicates how per_replica_value will be reduced. Accepted
    values are <a href="../../../tf/distribute/ReduceOp#SUM"><code>tf.distribute.ReduceOp.SUM</code></a>, <a href="../../../tf/distribute/ReduceOp#MEAN"><code>tf.distribute.ReduceOp.MEAN</code></a>.
* <b>`per_replica_value`</b>: a PerReplica object or a tensor with device set.
* <b>`destinations`</b>: the reduction destinations.


#### Returns:

a Mirrored object.


#### Raises:

* <b>`ValueError`</b>: if per_replica_value is not a PerReplica object.



