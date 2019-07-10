page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.reroute_inputs

``` python
tf.contrib.graph_editor.reroute_inputs(
    sgv0,
    sgv1
)
```



Defined in [`tensorflow/contrib/graph_editor/reroute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/graph_editor/reroute.py).

See the guide: [Graph Editor (contrib) > Module: reroute](../../../../../api_guides/python/contrib.graph_editor#Module_reroute)

Re-route all the inputs of two subgraphs.

#### Args:

* <b>`sgv0`</b>: the first subgraph to have its inputs swapped. This argument is
    converted to a subgraph using the same rules than the function
    subgraph.make_view.
* <b>`sgv1`</b>: the second subgraph to have its inputs swapped. This argument is
    converted to a subgraph using the same rules than the function
    subgraph.make_view.

#### Returns:

A tuple `(sgv0, sgv1)` of subgraph views with their inputs swapped.
  Note that the function argument sgv0 and sgv1 are also modified in place.

#### Raises:

* <b>`StandardError`</b>: if sgv0 or sgv1 cannot be converted to a SubGraphView using
    the same rules than the function subgraph.make_view.