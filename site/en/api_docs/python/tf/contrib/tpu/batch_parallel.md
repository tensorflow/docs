page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.batch_parallel

``` python
tf.contrib.tpu.batch_parallel(
    computation,
    inputs=None,
    num_shards=1,
    infeed_queue=None,
    device_assignment=None,
    name=None
)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/tpu/python/tpu/tpu.py).

Shards `computation` along the batch dimension for parallel execution.

Convenience wrapper around shard().

`inputs` must be a list of Tensors or None (equivalent to an empty
list). Each input is split into `num_shards` pieces along the 0-th
dimension, and computation is applied to each shard in parallel.

Tensors are broadcast to all shards if they are lexically captured by
`computation`. e.g.,

x = tf.constant(7)
def computation():
  return x + 3
... = shard(computation, ...)

The outputs from all shards are concatenated back together along their 0-th
dimension.

Inputs and outputs of the computation must be at least rank-1 Tensors.

#### Args:

* <b>`computation`</b>: A Python function that builds a computation to apply to each
    shard of the input.
* <b>`inputs`</b>: A list of input tensors or None (equivalent to an empty
    list). The 0-th dimension of each Tensor must have size
    divisible by `num_shards`.
* <b>`num_shards`</b>: The number of shards.
* <b>`infeed_queue`</b>: If not `None`, the `InfeedQueue` from which to append a tuple
    of arguments as inputs to `computation`.
* <b>`device_assignment`</b>: If not `None`, a `DeviceAssignment` describing the
    mapping between logical cores in the computation with physical cores in
    the TPU topology. Uses a default device assignment if `None`. The
    `DeviceAssignment` may be omitted if each shard of the computation uses
    only one core, and there is either only one shard, or the number of shards
    is equal to the number of cores in the TPU system.
* <b>`name`</b>: (Deprecated) Does nothing.

#### Returns:

A list of output tensors.

#### Raises:

* <b>`ValueError`</b>: If `num_shards <= 0`