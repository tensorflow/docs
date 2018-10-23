

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.get_ops_ios

``` python
tf.contrib.graph_editor.get_ops_ios(
    ops,
    control_inputs=False,
    control_outputs=None,
    control_ios=None
)
```



Defined in [`tensorflow/contrib/graph_editor/select.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/graph_editor/select.py).

See the guide: [Graph Editor (contrib) > Module: select](../../../../../api_guides/python/contrib.graph_editor#Module_select)

Return all the `tf.Operation` which are connected to an op in ops.

#### Args:

* <b>`ops`</b>: an object convertible to a list of `tf.Operation`.
* <b>`control_inputs`</b>: A boolean indicating whether control inputs are enabled.
* <b>`control_outputs`</b>: An instance of `util.ControlOutputs` or `None`. If not
    `None`, control outputs are enabled.
* <b>`control_ios`</b>:  An instance of `util.ControlOutputs` or `None`. If not `None`,
    both control inputs and control outputs are enabled. This is equivalent to
    set `control_inputs` to `True` and `control_outputs` to the
    `util.ControlOutputs` instance.

#### Returns:

All the `tf.Operation` surrounding the given ops.

#### Raises:

* <b>`TypeError`</b>: if `ops` cannot be converted to a list of `tf.Operation`.