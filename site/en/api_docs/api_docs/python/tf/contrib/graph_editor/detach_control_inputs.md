

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.detach_control_inputs

``` python
detach_control_inputs(sgv)
```



Defined in [`tensorflow/contrib/graph_editor/edit.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/graph_editor/edit.py).

See the guide: [Graph Editor (contrib) > Module: edit](../../../../../api_guides/python/contrib.graph_editor#Module_edit)

Detach all the external control inputs of the subgraph sgv.

#### Args:

* <b>`sgv`</b>: the subgraph view to be detached. This argument is converted to a
    subgraph using the same rules as the function subgraph.make_view.