

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.copy_op_handler

``` python
tf.contrib.graph_editor.copy_op_handler(
    info,
    op,
    new_inputs,
    copy_shape=True
)
```



Defined in [`tensorflow/contrib/graph_editor/transform.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/graph_editor/transform.py).

See the guide: [Graph Editor (contrib) > Module: transform](../../../../../api_guides/python/contrib.graph_editor#Module_transform)

Copy a <a href="../../../tf/Operation"><code>tf.Operation</code></a>.

#### Args:

* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`op`</b>: the <a href="../../../tf/Operation"><code>tf.Operation</code></a> to be copied.
* <b>`new_inputs`</b>: The new inputs for this op.
* <b>`copy_shape`</b>: also copy the shape of the tensor

#### Returns:

A `(op, op_outputs)` tuple containing the transformed op and its outputs.