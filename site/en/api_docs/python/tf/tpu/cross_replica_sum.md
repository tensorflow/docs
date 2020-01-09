page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.cross_replica_sum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/ops/tpu_ops.py#L93-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sum the input tensor across replicas according to group_assignment.

### Aliases:

* <a href="/api_docs/python/tf/tpu/cross_replica_sum"><code>tf.compat.v1.tpu.cross_replica_sum</code></a>
* <a href="/api_docs/python/tf/tpu/cross_replica_sum"><code>tf.contrib.tpu.cross_replica_sum</code></a>


``` python
tf.tpu.cross_replica_sum(
    x,
    group_assignment=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: The local tensor to the sum.
* <b>`group_assignment`</b>: Optional 2d int32 lists with shape [num_groups,
  num_replicas_per_group]. `group_assignment[i]` represents the replica
  ids in the ith subgroup.
* <b>`name`</b>: Optional op name.


#### Returns:

A `Tensor` which is summed across replicas.
