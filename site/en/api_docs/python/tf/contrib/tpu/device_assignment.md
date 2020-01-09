page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.device_assignment


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/device_assignment.py#L215-L386">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes a device_assignment of a computation across a TPU topology.

``` python
tf.contrib.tpu.device_assignment(
    topology,
    computation_shape=None,
    computation_stride=None,
    num_replicas=1
)
```



<!-- Placeholder for "Used in" -->

Attempts to choose a compact grid of cores for locality.

Returns a `DeviceAssignment` that describes the cores in the topology assigned
to each core of each replica.

`computation_shape` and `computation_stride` values should be powers of 2 for
optimal packing.

#### Args:


* <b>`topology`</b>: A `Topology` object that describes the TPU cluster topology.
  To obtain a TPU topology, evaluate the `Tensor` returned by
  `initialize_system` using <a href="/api_docs/python/tf/InteractiveSession#run"><code>Session.run</code></a>. Either a serialized
  `TopologyProto` or a `Topology` object may be passed. Note: you must
  evaluate the `Tensor` first; you cannot pass an unevaluated `Tensor` here.
* <b>`computation_shape`</b>: A rank 1 int32 numpy array with size equal to the
  topology rank, describing the shape of the computation's block of cores.
  If None, the `computation_shape` is `[1] * topology_rank`.
* <b>`computation_stride`</b>: A rank 1 int32 numpy array of size `topology_rank`,
  describing the inter-core spacing of the `computation_shape` cores in the
  TPU topology. If None, the `computation_stride` is `[1] * topology_rank`.
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
