


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.control_dependencies

### `tf.control_dependencies`

```
tf.control_dependencies(control_inputs)
```


See the guide: [Building Graphs > Utility functions](../../../api_guides/python/framework#Utility_functions)

Wrapper for `Graph.control_dependencies()` using the default graph.

See [`tf.Graph.control_dependencies`](../tf/Graph#control_dependencies)
for more details.

#### Args:

* <b>`control_inputs`</b>: A list of `Operation` or `Tensor` objects which
    must be executed or computed before running the operations
    defined in the context.  Can also be `None` to clear the control
    dependencies.


#### Returns:

 A context manager that specifies control dependencies for all
 operations constructed within the context.

Defined in [`tensorflow/python/framework/ops.py`](https://www.tensorflow.org/code/tensorflow/python/framework/ops.py).

