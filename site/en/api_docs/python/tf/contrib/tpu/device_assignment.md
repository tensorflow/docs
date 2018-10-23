

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.device_assignment

``` python
device_assignment(
    topology,
    computation_shape=None,
    computation_stride=None,
    num_replicas=1
)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/device_assignment.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/tpu/python/tpu/device_assignment.py).

Computes a device_assignment of a computation across a TPU topology.

Returns a `DeviceAssignment` that describes the cores in the topology assigned
to each core of each replica.

`computation_shape` and `computation_stride` values should be powers of 2 for
optimal packing.

#### Args:

* <b>`topology`</b>: A `Topology` object that describes the TPU cluster topology.
    To obtain a TPU topology, evaluate the `Tensor` returned by
    `initialize_system` using `Session.run`. Either a serialized
    `TopologyProto` or a `Topology` object may be passed. Note: you must
    evaluate the `Tensor` first; you cannot pass an unevaluated `Tensor` here.
* <b>`computation_shape`</b>: A rank 1 int32 numpy array of size 3, describing the
    shape of the computation's block of cores. If None, the
    `computation_shape` is `[1, 1, 1]`.
* <b>`computation_stride`</b>: A rank 1 int32 numpy array of size 3, describing the
    inter-core spacing of the `computation_shape` cores in the TPU topology.
    If None, the `computation_stride` is `[1, 1, 1]`.
* <b>`num_replicas`</b>: The number of computation replicas to run. The replicas will
    be packed into the free spaces of the topology.


#### Returns:

A DeviceAssignment object, which describes the mapping between the logical
cores in each computation replica and the physical cores in the TPU
topology.


#### Raises:

* <b>`ValueError`</b>: If `topology` is not a valid `Topology` object.
* <b>`ValueError`</b>: If `computation_shape` or `computation_stride` are not 1D int32
    numpy arrays with shape [3] where all values are positive.
* <b>`ValueError`</b>: If computation's replicas cannot fit into the TPU topology.