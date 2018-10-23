

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.make_view_from_scope

### Aliases:

* `tf.contrib.graph_editor.make_view_from_scope`
* `tf.contrib.graph_editor.sgv_scope`

``` python
tf.contrib.graph_editor.make_view_from_scope(
    scope,
    graph
)
```



Defined in [`tensorflow/contrib/graph_editor/subgraph.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/graph_editor/subgraph.py).

See the guides: [Graph Editor (contrib) > Module: subgraph](../../../../../api_guides/python/contrib.graph_editor#Module_subgraph), [Graph Editor (contrib) > Useful aliases](../../../../../api_guides/python/contrib.graph_editor#Useful_aliases)

Make a subgraph from a name scope.

#### Args:

* <b>`scope`</b>: the name of the scope.
* <b>`graph`</b>: the `tf.Graph`.

#### Returns:

A subgraph view representing the given scope.