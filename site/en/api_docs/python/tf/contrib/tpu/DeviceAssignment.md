

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.DeviceAssignment

## Class `DeviceAssignment`





Defined in [`tensorflow/contrib/tpu/python/tpu/device_assignment.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/tpu/python/tpu/device_assignment.py).

Mapping from logical cores in a computation to the physical TPU topology.

Prefer to use the `device_assignment()` helper to construct a
`DeviceAssignment`; it is easier if less flexible than constructing a
`DeviceAssignment` directly.

## Properties

<h3 id="computation_shape"><code>computation_shape</code></h3>

The computation shape.

#### Returns:

A rank-1 int32 numpy array with size equal to the TPU topology rank.
Describes the logical shape in numbers of core of each replica of the
computation in the TPU topology.


#### Returns:

The computation shape.

<h3 id="core_assignment"><code>core_assignment</code></h3>

The logical to physical core mapping.

#### Returns:

A numpy array of rank `topology_rank + 2`, with shape
`[num_replicas] + computation_shape + [topology_rank]`. Maps
(replica, logical core coordinates) pairs to physical topology
coordinates.

<h3 id="num_replicas"><code>num_replicas</code></h3>

The number of replicas of the computation.

<h3 id="topology"><code>topology</code></h3>

A `Topology` that describes the TPU topology.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    topology,
    core_assignment
)
```

Constructs a `DeviceAssignment` object.

#### Args:

* <b>`topology`</b>: A `Topology` object that describes the physical TPU topology.
* <b>`core_assignment`</b>: A logical to physical core mapping, represented as a
    rank 3 numpy array. See the description of the `core_assignment`
    property for more details.


#### Raises:

* <b>`ValueError`</b>: If `topology` is not `Topology` object.
* <b>`ValueError`</b>: If `core_assignment` is not a rank 3 numpy array.

<h3 id="host_device"><code>host_device</code></h3>

``` python
host_device(
    replica=0,
    logical_core=None,
    job=None
)
```

Returns the CPU device attached to a logical core.

<h3 id="tpu_device"><code>tpu_device</code></h3>

``` python
tpu_device(
    replica=0,
    logical_core=None,
    job=None
)
```

Returns the name of the TPU device assigned to a logical core.

<h3 id="tpu_ordinal"><code>tpu_ordinal</code></h3>

``` python
tpu_ordinal(
    replica=0,
    logical_core=None
)
```

Returns the ordinal of the TPU device assigned to a logical core.



