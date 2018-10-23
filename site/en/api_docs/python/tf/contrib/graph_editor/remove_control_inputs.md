

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.remove_control_inputs

``` python
remove_control_inputs(
    op,
    cops
)
```



Defined in [`tensorflow/contrib/graph_editor/reroute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/graph_editor/reroute.py).

See the guide: [Graph Editor (contrib) > Module: reroute](../../../../../api_guides/python/contrib.graph_editor#Module_reroute)

Remove the control inputs cops from co.

Warning: this function is directly manipulating the internals of the
`tf.Graph`.

#### Args:

* <b>`op`</b>: a `tf.Operation` from which to remove the control inputs.
* <b>`cops`</b>: an object convertible to a list of `tf.Operation`.

#### Raises:

* <b>`TypeError`</b>: if op is not a `tf.Operation`.
* <b>`ValueError`</b>: if any cop in cops is not a control input of op.