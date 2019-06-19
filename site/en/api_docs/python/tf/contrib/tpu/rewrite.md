

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.rewrite

``` python
tf.contrib.tpu.rewrite(
    computation,
    inputs=None,
    infeed_queue=None,
    device_assignment=None,
    name=None
)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/tpu/python/tpu/tpu.py).

Rewrites `computation` for execution on a TPU system.

#### Args:

* <b>`computation`</b>: A Python function that builds a computation to apply
    to the input. If the function takes n inputs, 'inputs' should be
    a list of n tensors. If the function returns m outputs, rewrite
    will return a list of m tensors.
* <b>`inputs`</b>: A list of input tensors or `None` (equivalent to an empty list).
* <b>`infeed_queue`</b>: If not `None`, the `InfeedQueue` from which to append a tuple
    of arguments as inputs to `computation`.
* <b>`device_assignment`</b>: if not `None`, a `DeviceAssignment` describing the
    mapping between logical cores in the computation with physical cores in
    the TPU topology. May be omitted for a single-core computation, in which
    case the core attached to task 0, TPU device 0 is used.
* <b>`name`</b>: (Deprecated) Does nothing.

#### Returns:

A list of output tensors.