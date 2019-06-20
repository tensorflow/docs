page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.nccl.all_max

``` python
tf.contrib.nccl.all_max(tensors)
```



Defined in [`tensorflow/contrib/nccl/python/ops/nccl_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/nccl/python/ops/nccl_ops.py).

Returns a list of tensors with the all-reduce max across `tensors`.

The computation is done with an all-reduce operation, so if only some of the
returned tensors are evaluated then the computation will hang.

#### Args:

* <b>`tensors`</b>: The input tensors across which to reduce; must be assigned
    to GPU devices.


#### Returns:

List of tensors, each with the maximum of the input tensors, where tensor i
has the same device as `tensors[i]`.