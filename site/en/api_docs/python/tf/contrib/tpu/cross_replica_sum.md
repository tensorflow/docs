page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.cross_replica_sum

``` python
tf.contrib.tpu.cross_replica_sum(
    x,
    group_assignment=None,
    name=None
)
```



Defined in [`tensorflow/contrib/tpu/python/ops/tpu_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/tpu/python/ops/tpu_ops.py).

Sum the input tensor accorss replicas according to group_assignment.

#### Args:

* <b>`x`</b>: The local tensor to the sum.
* <b>`group_assignment`</b>: Optional 2d int32 lists with shape [num_groups,
    num_replicas_per_group]. `group_assignment[i]` represents the replica
    ids in the ith subgroup.
* <b>`name`</b>: Optional op name.


#### Returns:

A `Tensor` which is summed across replicas.