

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.graph_util

### Module `tf.graph_util`



Defined in [`tensorflow/python/framework/graph_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/framework/graph_util.py).

Helpers to manipulate a tensor graph in python.

## Functions

[`convert_variables_to_constants(...)`](../tf/graph_util/convert_variables_to_constants): Replaces all the variables in a graph with constants of the same values.

[`extract_sub_graph(...)`](../tf/graph_util/extract_sub_graph): Extract the subgraph that can reach any of the nodes in 'dest_nodes'.

[`must_run_on_cpu(...)`](../tf/graph_util/must_run_on_cpu): Returns True if the given node_def must run on CPU, otherwise False.

[`remove_training_nodes(...)`](../tf/graph_util/remove_training_nodes): Prunes out nodes that aren't needed for inference.

[`tensor_shape_from_node_def_name(...)`](../tf/graph_util/tensor_shape_from_node_def_name): Convenience function to get a shape from a NodeDef's input string.

