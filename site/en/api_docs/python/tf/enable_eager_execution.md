page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.enable_eager_execution

### Aliases:

* `tf.contrib.eager.enable_eager_execution`
* `tf.enable_eager_execution`

``` python
tf.enable_eager_execution(
    config=None,
    device_policy=None,
    execution_mode=None
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/framework/ops.py).

Enables eager execution for the lifetime of this program.

Eager execution provides an imperative interface to TensorFlow. With eager
execution enabled, TensorFlow functions execute operations immediately (as
opposed to adding to a graph to be executed later in a <a href="../tf/Session"><code>tf.Session</code></a>) and
return concrete values (as opposed to symbolic references to a node in a
computational graph).

For example:

```python
tf.enable_eager_execution()

# After eager execution is enabled, operations are executed as they are
# defined and Tensor objects hold concrete values, which can be accessed as
# numpy.ndarray`s through the numpy() method.
assert tf.multiply(6, 7).numpy() == 42
```

Eager execution cannot be enabled after TensorFlow APIs have been used to
create or execute graphs. It is typically recommended to invoke this function
at program startup and not in a library (as most libraries should be usable
both with and without eager execution).

#### Args:

* <b>`config`</b>: (Optional.) A <a href="../tf/ConfigProto"><code>tf.ConfigProto</code></a> to use to configure the environment
    in which operations are executed. Note that <a href="../tf/ConfigProto"><code>tf.ConfigProto</code></a> is also
    used to configure graph execution (via <a href="../tf/Session"><code>tf.Session</code></a>) and many options
    within <a href="../tf/ConfigProto"><code>tf.ConfigProto</code></a> are not implemented (or are irrelevant) when
    eager execution is enabled.
* <b>`device_policy`</b>: (Optional.) Policy controlling how operations requiring
    inputs on a specific device (e.g., a GPU 0) handle inputs on a different
    device  (e.g. GPU 1 or CPU). When set to None, an appropriate value will be
    picked automatically. The value picked may change between TensorFlow
    releases.
    Valid values:
    - tf.contrib.eager.DEVICE_PLACEMENT_EXPLICIT: raises an error if the
      placement is not correct.
    - tf.contrib.eager.DEVICE_PLACEMENT_WARN: copies the tensors which are not
      on the right device but logs a warning.
    - tf.contrib.eager.DEVICE_PLACEMENT_SILENT: silently copies the tensors.
      Note that this may hide performance problems as there is no notification
      provided when operations are blocked on the tensor being copied between
      devices.
    - tf.contrib.eager.DEVICE_PLACEMENT_SILENT_FOR_INT32: silently copies
      int32 tensors, raising errors on the other ones.
* <b>`execution_mode`</b>: (Optional.) Policy controlling how operations dispatched are
    actually executed. When set to None, an appropriate value will be picked
    automatically. The value picked may change between TensorFlow releases.
    Valid values:
    - tf.contrib.eager.SYNC: executes each operation synchronously.
    - tf.contrib.eager.ASYNC: executes each operation asynchronously. These
      operations may return "non-ready" handles.


#### Raises:

* <b>`ValueError`</b>: If eager execution is enabled after creating/executing a
   TensorFlow graph, or if options provided conflict with a previous call
   to this function.