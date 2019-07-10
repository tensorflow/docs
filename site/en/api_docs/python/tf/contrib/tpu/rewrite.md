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



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/tpu/python/tpu/tpu.py).

Rewrites `computation` for execution on a TPU system.

#### Args:

* <b>`computation`</b>: A Python function that builds a computation to apply to the
    input. If the function takes n inputs, 'inputs' should be a list of n
    tensors.

    `computation` may return a list of operations and tensors. Tensors must
    come before operations in the returned list.  The return value of
    `rewrite` is a list of tensors corresponding to the tensors from the
    output of `computation`.

    All `Operation`s constructed during `computation` will be executed when
    evaluating any of the returned output tensors, not just the ones returned.
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