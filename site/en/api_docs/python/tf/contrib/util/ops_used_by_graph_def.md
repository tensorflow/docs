page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.util.ops_used_by_graph_def

``` python
tf.contrib.util.ops_used_by_graph_def(graph_def)
```



Defined in [`tensorflow/python/framework/meta_graph.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/framework/meta_graph.py).

Collect the list of ops used by a graph.

Does not validate that the ops are all registered.

#### Args:

* <b>`graph_def`</b>: A `GraphDef` proto, as from `graph.as_graph_def()`.


#### Returns:

A list of strings, each naming an op used by the graph.