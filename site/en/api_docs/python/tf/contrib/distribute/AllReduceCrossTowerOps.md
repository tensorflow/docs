

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.AllReduceCrossTowerOps

## Class `AllReduceCrossTowerOps`

Inherits From: [`CrossTowerOps`](../../../tf/contrib/distribute/CrossTowerOps)



Defined in [`tensorflow/contrib/distribute/python/cross_tower_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/distribute/python/cross_tower_ops.py).

Reduction using all reduce.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    all_reduce_alg='nccl',
    num_packs=1,
    agg_small_grads_max_bytes=0,
    agg_small_grads_max_group=10
)
```

All-reduce implementation of CrossTowerOps.

Before performing all-reduce, tensors will be repacked or aggregated for
more efficient cross-device transportation:
  1) If `num_packs` is non-zero, pack values into
    `num_packs` splits.
  2) Otherwise, if `agg_small_grads_max_bytes` > 0 and
    `agg_small_grads_max_group` > 0, aggregate values smaller than
    `agg_small_grads_max_bytes` into groups with at most
    `agg_small_grads_max_group` values.
  3) Otherwise, no repacking or grouping will happen.

#### Args:

* <b>`all_reduce_alg`</b>: the all-reduce algorithm to use, currently only "nccl" or
    "hierarchical_copy" are supported.
* <b>`num_packs`</b>: see above.
* <b>`agg_small_grads_max_bytes`</b>: see above.
* <b>`agg_small_grads_max_group`</b>: see above.
    tensors.

<h3 id="batch_reduce"><code>batch_reduce</code></h3>

``` python
batch_reduce(
    method_string,
    value_destination_pairs
)
```

Reduce PerDevice objects in a batch.

Reduce each first element in `value_destination_pairs` to each second
element which indicates the destinations.

#### Args:

* <b>`method_string`</b>: either 'sum' or 'mean' specifying the reduction method.
* <b>`value_destination_pairs`</b>: a list or a tuple of tuples of PerDevice objects
    and destinations. If a destination is None, then the destinations
    are set to match the devices of the input PerDevice object.


#### Returns:

a list of Mirrored objects.


#### Raises:

* <b>`ValueError`</b>: if `value_destination_pairs` is not a list or a tuple of
    tuples of PerDevice objects and destinations

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
    method_string,
    per_device_value,
    destinations=None
)
```

Reduce `per_device_value` to `destinations`.

It runs the reduction operation defined by `method_string` and put the
result on `destinations`.

#### Args:

* <b>`method_string`</b>: either 'sum' or 'mean' specifying the reduction method.
* <b>`per_device_value`</b>: a PerDevice object.
* <b>`destinations`</b>: the reduction destinations.


#### Returns:

a Mirrored object.


#### Raises:

* <b>`ValueError`</b>: if per_device_value is not a PerDevice object.



