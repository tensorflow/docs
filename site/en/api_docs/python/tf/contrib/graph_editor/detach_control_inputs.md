page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.detach_control_inputs

Detach all the external control inputs of the subgraph sgv.

``` python
tf.contrib.graph_editor.detach_control_inputs(sgv)
```



Defined in [`contrib/graph_editor/edit.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/edit.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sgv`</b>: the subgraph view to be detached. This argument is converted to a
  subgraph using the same rules as the function subgraph.make_view.