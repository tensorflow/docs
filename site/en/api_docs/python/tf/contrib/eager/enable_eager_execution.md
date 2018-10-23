

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.enable_eager_execution

``` python
tf.contrib.eager.enable_eager_execution(
    config=None,
    device_policy=None
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/framework/ops.py).

Enables, for the rest of the lifetime of this program, eager execution.

If not called immediately on startup risks creating breakage and bugs.

Example:

```python
tfe.enable_eager_execution()

# After eager execution is enabled, operations are executed as they are
# defined and `Tensor`s hold concrete values, which can be accessed as
# `numpy.ndarray`s through the `numpy()` method.
assert tf.multiply(6, 7).numpy() == 42
```

#### Args:

* <b>`config`</b>: (Optional.) A `ConfigProto` protocol buffer with configuration
   options for the Context. Note that a lot of these options may be
   currently unimplemented or irrelevant when eager execution is enabled.
* <b>`device_policy`</b>: (Optional.) What policy to use when trying to run an
   operation on a device with inputs which are not on that device.
   Valid values:
     tfe.DEVICE_PLACEMENT_EXPLICIT: raises an error if the placement is not
       correct.
     tfe.DEVICE_PLACEMENT_WARN: copies the tensors which are not on the
       right device but raises a warning.
     tfe.DEVICE_PLACEMENT_SILENT: silently copies the tensors. This might
       hide performance problems.
     tfe.DEVICE_PLACEMENT_SILENT_FOR_INT32: silently copies int32 tensors,
       raising errors on the other ones.


#### Raises:

* <b>`ValueError`</b>: If trying to create a context after using graph operations
   or if trying to create a context with nontrivial options which differ
   from those of the existing context.