

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.detach_outputs

``` python
tf.contrib.graph_editor.detach_outputs(
    sgv,
    control_outputs=None
)
```



Defined in [`tensorflow/contrib/graph_editor/edit.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/graph_editor/edit.py).

See the guide: [Graph Editor (contrib) > Module: edit](../../../../../api_guides/python/contrib.graph_editor#Module_edit)

Detach the output of a subgraph view.

#### Args:

* <b>`sgv`</b>: the subgraph view to be detached. This argument is converted to a
    subgraph using the same rules as the function subgraph.make_view.
    Note that sgv is modified in place.
* <b>`control_outputs`</b>: a util.ControlOutputs instance or None. If not None the
    control outputs are also detached.

#### Returns:

A tuple `(sgv, output_placeholders)` where
  `sgv` is a new subgraph view of the detached subgraph;
  `output_placeholders` is a list of the created output placeholders.

#### Raises:

* <b>`StandardError`</b>: if sgv cannot be converted to a SubGraphView using
    the same rules than the function subgraph.make_view.