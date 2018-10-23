

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.group

``` python
tf.group(
    *inputs,
    **kwargs
)
```



Defined in [`tensorflow/python/ops/control_flow_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/ops/control_flow_ops.py).

See the guide: [Control Flow > Control Flow Operations](../../../api_guides/python/control_flow_ops#Control_Flow_Operations)

Create an op that groups multiple operations.

When this op finishes, all ops in `inputs` have finished. This op has no
output.

See also <a href="../tf/tuple">tuple</a> and
<a href="../tf/control_dependencies">control_dependencies</a>.

#### Args:

* <b>`*inputs`</b>: Zero or more tensors to group.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

An Operation that executes all its inputs.


#### Raises:

* <b>`ValueError`</b>: If an unknown keyword argument is provided.