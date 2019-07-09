page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

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



Defined in [`tensorflow/contrib/graph_editor/subgraph.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/graph_editor/subgraph.py).

Make a subgraph from a name scope.

#### Args:

* <b>`scope`</b>: the name of the scope.
* <b>`graph`</b>: the <a href="../../../tf/Graph"><code>tf.Graph</code></a>.

#### Returns:

A subgraph view representing the given scope.