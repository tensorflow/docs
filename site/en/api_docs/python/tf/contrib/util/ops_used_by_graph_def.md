page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.util.ops_used_by_graph_def

Collect the list of ops used by a graph.

``` python
tf.contrib.util.ops_used_by_graph_def(graph_def)
```



Defined in [`python/framework/meta_graph.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/meta_graph.py).

<!-- Placeholder for "Used in" -->

Does not validate that the ops are all registered.

#### Args:


* <b>`graph_def`</b>: A `GraphDef` proto, as from `graph.as_graph_def()`.


#### Returns:

A list of strings, each naming an op used by the graph.
