

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.detach_inputs

``` python
tf.contrib.graph_editor.detach_inputs(
    sgv,
    control_inputs=False
)
```



Defined in [`tensorflow/contrib/graph_editor/edit.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/graph_editor/edit.py).

See the guide: [Graph Editor (contrib) > Module: edit](../../../../../api_guides/python/contrib.graph_editor#Module_edit)

Detach the inputs of a subgraph view.

#### Args:

* <b>`sgv`</b>: the subgraph view to be detached. This argument is converted to a
    subgraph using the same rules as the function subgraph.make_view.
    Note that sgv is modified in place.
* <b>`control_inputs`</b>: if True control_inputs are also detached.

#### Returns:

A tuple `(sgv, input_placeholders)` where
  `sgv` is a new subgraph view of the detached subgraph;
  `input_placeholders` is a list of the created input placeholders.

#### Raises:

* <b>`StandardError`</b>: if sgv cannot be converted to a SubGraphView using
    the same rules than the function subgraph.make_view.