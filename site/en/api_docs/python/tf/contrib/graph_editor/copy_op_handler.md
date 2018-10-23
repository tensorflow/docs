

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.copy_op_handler

``` python
copy_op_handler(
    info,
    op,
    copy_shape=True
)
```



Defined in [`tensorflow/contrib/graph_editor/transform.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/graph_editor/transform.py).

See the guide: [Graph Editor (contrib) > Module: transform](../../../../../api_guides/python/contrib.graph_editor#Module_transform)

Copy a `tf.Operation`.

#### Args:

* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`op`</b>: the `tf.Operation` to be copied.
* <b>`copy_shape`</b>: also copy the shape of the tensor

#### Returns:

A `(op, op_outputs)` tuple containing the transformed op and its outputs.