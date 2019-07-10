page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.experimental.DeviceAssignment

## Class `DeviceAssignment`

Mapping from logical cores in a computation to the physical TPU topology.



### Aliases:

* Class `tf.compat.v1.tpu.experimental.DeviceAssignment`
* Class `tf.compat.v2.tpu.experimental.DeviceAssignment`
* Class `tf.contrib.tpu.DeviceAssignment`
* Class `tf.tpu.experimental.DeviceAssignment`



Defined in [`python/tpu/device_assignment.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/tpu/device_assignment.py).

<!-- Placeholder for "Used in" -->

Prefer to use the <a href="../../../tf/tpu/experimental/DeviceAssignment#build"><code>DeviceAssignment.build()</code></a> helper to construct a
`DeviceAssignment`; it is easier if less flexible than constructing a
`DeviceAssignment` directly.

<h2 id="__init__"><code>__init__</code></h2>

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



## Properties

<h3 id="core_assignment"><code>core_assignment</code></h3>

The logical to physical core mapping.


#### Returns:

An integer numpy array of rank 3, with shape
`[num_replicas, num_cores_per_replica, topology_rank]`. Maps
(replica, logical core) pairs to physical topology coordinates.


<h3 id="num_cores_per_replica"><code>num_cores_per_replica</code></h3>

The number of cores per replica.


<h3 id="num_replicas"><code>num_replicas</code></h3>

The number of replicas of the computation.


<h3 id="topology"><code>topology</code></h3>

A `Topology` that describes the TPU topology.




## Methods

<h3 id="build"><code>build</code></h3>

``` python
@staticmethod
build(
    topology,
    computation_shape=None,
    computation_stride=None,
    num_replicas=1
)
```




<h3 id="coordinates"><code>coordinates</code></h3>

``` python
coordinates(
    replica,
    logical_core
)
```

Returns the physical topology coordinates of a logical core.


<h3 id="host_device"><code>host_device</code></h3>

``` python
host_device(
    replica=0,
    logical_core=0,
    job=None
)
```

Returns the CPU device attached to a logical core.


<h3 id="lookup_replicas"><code>lookup_replicas</code></h3>

``` python
lookup_replicas(
    task_id,
    logical_core
)
```

Lookup replica ids by task number and logical core.


#### Args:


* <b>`task_id`</b>: TensorFlow task number.
* <b>`logical_core`</b>: An integer, identifying a logical core.

#### Returns:

A sorted list of the replicas that are attached to that task and
logical_core.


#### Raises:


* <b>`ValueError`</b>: If no replica exists in the task which contains the logical
core.

<h3 id="tpu_device"><code>tpu_device</code></h3>

``` python
tpu_device(
    replica=0,
    logical_core=0,
    job=None
)
```

Returns the name of the TPU device assigned to a logical core.


<h3 id="tpu_ordinal"><code>tpu_ordinal</code></h3>

``` python
tpu_ordinal(
    replica=0,
    logical_core=0
)
```

Returns the ordinal of the TPU device assigned to a logical core.




