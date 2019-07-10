page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.cross_replica_sum

Sum the input tensor across replicas according to group_assignment.

### Aliases:

* `tf.compat.v1.tpu.cross_replica_sum`
* `tf.contrib.tpu.cross_replica_sum`
* `tf.tpu.cross_replica_sum`

``` python
tf.tpu.cross_replica_sum(
    x,
    group_assignment=None,
    name=None
)
```



Defined in [`python/tpu/ops/tpu_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/tpu/ops/tpu_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: The local tensor to the sum.
* <b>`group_assignment`</b>: Optional 2d int32 lists with shape [num_groups,
  num_replicas_per_group]. `group_assignment[i]` represents the replica
  ids in the ith subgroup.
* <b>`name`</b>: Optional op name.


#### Returns:

A `Tensor` which is summed across replicas.
