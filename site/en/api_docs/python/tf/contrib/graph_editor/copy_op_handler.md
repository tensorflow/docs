

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.copy_op_handler

``` python
tf.contrib.graph_editor.copy_op_handler(
    info,
    op,
    new_inputs,
    copy_shape=True,
    nodedef_fn=None
)
```



Defined in [`tensorflow/contrib/graph_editor/transform.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/graph_editor/transform.py).

See the guide: [Graph Editor (contrib) > Module: transform](../../../../../api_guides/python/contrib.graph_editor#Module_transform)

Copy a <a href="../../../tf/Operation"><code>tf.Operation</code></a>.

#### Args:

* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`op`</b>: the <a href="../../../tf/Operation"><code>tf.Operation</code></a> to be copied.
* <b>`new_inputs`</b>: The new inputs for this op.
* <b>`copy_shape`</b>: also copy the shape of the tensor
* <b>`nodedef_fn`</b>: If provided, a function that will be run on the NodeDef
    and should return a mutated NodeDef before a new Operation is created.
    This is useful as certain features cannot be set on the Operation and
    must be modified in NodeDef.


#### Returns:

A `(op, op_outputs)` tuple containing the transformed op and its outputs.