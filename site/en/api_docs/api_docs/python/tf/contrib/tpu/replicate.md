

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.replicate

``` python
tf.contrib.tpu.replicate(
    computation,
    inputs=None,
    infeed_queue=None,
    device_assignment=None,
    name=None
)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/tpu/python/tpu/tpu.py).

Builds a graph operator that runs a replicated TPU computation.

#### Args:

* <b>`computation`</b>: A Python function that builds the computation to replicate.
* <b>`inputs`</b>: A list of lists of input tensors or `None` (equivalent to
    `[[]]`), indexed by `[replica_num][input_num]`. All replicas must
    have the same number of inputs.
* <b>`infeed_queue`</b>: If not `None`, the `InfeedQueue` from which to append a tuple
    of arguments as inputs to computation.
* <b>`device_assignment`</b>: If not `None`, a `DeviceAssignment` describing the
    mapping between logical cores in the computation with physical cores in
    the TPU topology. Uses a default device assignment if `None`. The
    `DeviceAssignment` may be omitted if each replica of the computation uses
    only one core, and there is either only one replica, or the number of
    replicas is equal to the number of cores in the TPU system.
* <b>`name`</b>: (Deprecated) Does nothing.

#### Returns:

A list of lists of output tensors, indexed by `[replica_num][output_num]`.

#### Raises:

* <b>`ValueError`</b>: If all replicas do not have equal numbers of input tensors.
* <b>`ValueError`</b>: If the number of inputs per replica does not match
    the number of formal parameters to `computation`.