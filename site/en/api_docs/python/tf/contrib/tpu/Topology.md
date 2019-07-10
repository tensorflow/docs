page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.Topology

## Class `Topology`

Describes a set of TPU devices.





Defined in [`python/tpu/topology.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/tpu/topology.py).

<!-- Placeholder for "Used in" -->

Represents both the shape of the physical mesh, and the mapping between
TensorFlow TPU devices to physical mesh coordinates.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    serialized=None,
    mesh_shape=None,
    device_coordinates=None
)
```

Builds a Topology object.

If `serialized` is not `None`, the topology is parsed from `serialized` and
the other arguments are ignored. Otherwise, the topology is computed from
`mesh_shape` and `device_coordinates`.

#### Args:


* <b>`serialized`</b>: A serialized `TopologyProto`, or `None`. If not `None`, the
  serialized proto is parsed to discover the topology.
* <b>`mesh_shape`</b>: A sequence of 3 positive integers, or `None`. If not `None`,
  the shape of the TPU topology, in number of cores. Ignored if
  `serialized` is not `None`.
* <b>`device_coordinates`</b>: A rank 3 numpy array that describes the mapping from
  TensorFlow TPU devices to TPU fabric coordinates, or `None`. Ignored
  if `serialized is not `None`.


#### Raises:


* <b>`ValueError`</b>: If `serialized` does not describe a well-formed topology.
* <b>`ValueError`</b>: If `serialized` is `None` and `mesh_shape` is not a sequence
  of 3 positive integers.
* <b>`ValueError`</b>: If `serialized` is `None` and `device_coordinates` is not a
  rank 3 numpy int32 array that describes a valid coordinate mapping.



## Properties

<h3 id="device_coordinates"><code>device_coordinates</code></h3>

Describes the mapping from TPU devices to topology coordinates.


#### Returns:

A rank 3 int32 array with shape `[tasks, devices, axis]`.
`tasks` is the number of tasks in the TPU cluster, `devices` is the number
of TPU devices per task, and `axis` is the number of axes in the TPU
cluster topology. Each entry gives the `axis`-th coordinate in the
topology of a task/device pair. TPU topologies are 3-dimensional, with
dimensions `(x, y, core number)`.


<h3 id="mesh_rank"><code>mesh_rank</code></h3>

Returns the number of dimensions in the mesh.


<h3 id="mesh_shape"><code>mesh_shape</code></h3>

A rank 1 int32 array describing the shape of the TPU topology.


<h3 id="num_tasks"><code>num_tasks</code></h3>

Returns the number of TensorFlow tasks in the TPU slice.


<h3 id="num_tpus_per_task"><code>num_tpus_per_task</code></h3>

Returns the number of TPU devices per task in the TPU slice.




## Methods

<h3 id="cpu_device_name_at_coordinates"><code>cpu_device_name_at_coordinates</code></h3>

``` python
cpu_device_name_at_coordinates(
    device_coordinates,
    job=None
)
```

Returns the CPU device attached to a logical core.


<h3 id="serialized"><code>serialized</code></h3>

``` python
serialized()
```

Returns the serialized form of the topology.


<h3 id="task_ordinal_at_coordinates"><code>task_ordinal_at_coordinates</code></h3>

``` python
task_ordinal_at_coordinates(device_coordinates)
```

Returns the TensorFlow task number attached to `device_coordinates`.


#### Args:


* <b>`device_coordinates`</b>: An integer sequence describing a device's physical
  coordinates in the TPU fabric.


#### Returns:

Returns the TensorFlow task number that contains the TPU device with those
physical coordinates.


<h3 id="tpu_device_name_at_coordinates"><code>tpu_device_name_at_coordinates</code></h3>

``` python
tpu_device_name_at_coordinates(
    device_coordinates,
    job=None
)
```

Returns the name of the TPU device assigned to a logical core.


<h3 id="tpu_device_ordinal_at_coordinates"><code>tpu_device_ordinal_at_coordinates</code></h3>

``` python
tpu_device_ordinal_at_coordinates(device_coordinates)
```

Returns the TensorFlow device number at `device_coordinates`.


#### Args:


* <b>`device_coordinates`</b>: An integer sequence describing a device's physical
  coordinates in the TPU fabric.


#### Returns:

Returns the TensorFlow device number within the task corresponding to
attached to the device with those physical coordinates.




