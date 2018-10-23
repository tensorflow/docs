


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.group

### `tf.group`

```
tf.group(*inputs, **kwargs)
```


See the guide: [Control Flow > Control Flow Operations](../../../api_guides/python/control_flow_ops#Control_Flow_Operations)

Create an op that groups multiple operations.

When this op finishes, all ops in `input` have finished. This op has no
output.

See also `tuple` and `with_dependencies`.

#### Args:

  *inputs: Zero or more tensors to group.
  **kwargs: Optional parameters to pass when constructing the NodeDef.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

  An Operation that executes all its inputs.


#### Raises:

* <b>`ValueError`</b>: If an unknown keyword argument is provided.

Defined in [`tensorflow/python/ops/control_flow_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/control_flow_ops.py).

