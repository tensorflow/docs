page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.all_reduce.build_shuffle_all_reduce

``` python
tf.contrib.all_reduce.build_shuffle_all_reduce(
    input_tensors,
    gather_devices,
    red_op,
    un_op=None
)
```



Defined in [`tensorflow/contrib/all_reduce/python/all_reduce.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/all_reduce/python/all_reduce.py).

Construct a subgraph for shuffle all-reduce.

Shuffle reduce is essentially the algorithm implemented when using
parameter servers.  Suppose tensor length is n, there are d devices
and g gather shards.  Each device sends a n/g length sub-tensor to
each gather shard.  The gather shards perform a reduction across d
fragments, then broadcast the result back to each device.  The
devices then join the g fully reduced fragments they receive from
the shards.  The gather shards could perform d-1 pairwise
reductions, or one d-way reduction.  The first is better where
reduction Op time is low compared to transmission time, the second
better in the other case.

#### Args:

* <b>`input_tensors`</b>: list of T @(tf.Tensor} values to be reduced.
* <b>`gather_devices`</b>: list of names of devices on which reduction shards
    should be placed.
* <b>`red_op`</b>: an n-array elementwise reduction Op
* <b>`un_op`</b>: optional elementwise unary Op to be applied to fully-reduced values.


#### Returns:

list of T <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> which are the fully reduced tensors.