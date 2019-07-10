page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.graph_util.tensor_shape_from_node_def_name

``` python
tf.graph_util.tensor_shape_from_node_def_name(
    graph,
    input_name
)
```



Defined in [`tensorflow/python/framework/graph_util_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/framework/graph_util_impl.py).

Convenience function to get a shape from a NodeDef's input string. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.compat.v1.graph_util.remove_training_nodes