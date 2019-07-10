page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.reroute_inputs

Re-route all the inputs of two subgraphs.

``` python
tf.contrib.graph_editor.reroute_inputs(
    sgv0,
    sgv1
)
```



Defined in [`contrib/graph_editor/reroute.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/reroute.py).

<!-- Placeholder for "Used in" -->


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