

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.nccl.broadcast

``` python
broadcast(
    src_tensor,
    dst_devices
)
```



Defined in [`tensorflow/contrib/nccl/python/ops/nccl_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/nccl/python/ops/nccl_ops.py).

Returns a list of tensors on `dst_devices`, each with value `tensor`.

The computation is done with a broadcast nccl operation, so if only some of
the returned tensors and src_tensor are evaluated then the computation will
hang.

#### Args:

* <b>`src_tensor`</b>: The tensor to send; must be assigned to a GPU device.
* <b>`dst_devices`</b>: The GPU devices to receive the sent tensor.


#### Returns:

  List of tensors, each with the value of `src_tensor`, which the device
  of tensor i is `dst_devices[i]`.