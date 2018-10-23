

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.nccl.all_min

``` python
all_min(tensors)
```



Defined in [`tensorflow/contrib/nccl/python/ops/nccl_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/nccl/python/ops/nccl_ops.py).

Returns a list of tensors with the all-reduce min across `tensors`.

The computation is done with an all-reduce operation, so if only some of the
returned tensors are evaluated then the computation will hang.

#### Args:

* <b>`tensors`</b>: The input tensors across which to reduce; must be assigned
    to GPU devices.


#### Returns:

List of tensors, each with the minimum of the input tensors, where tensor i
has the same device as `tensors[i]`.