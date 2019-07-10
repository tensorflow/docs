page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.CrossDeviceOps

## Class `CrossDeviceOps`





Defined in [`tensorflow/python/distribute/cross_device_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cross_device_ops.py).

Base class for cross-device reduction and broadcasting algorithms.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.



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



