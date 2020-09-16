description: Helpers to manipulate a tensor graph in python.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.graph_util" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.graph_util

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Helpers to manipulate a tensor graph in python.



## Functions

[`convert_variables_to_constants(...)`](../../../tf/compat/v1/graph_util/convert_variables_to_constants.md): Replaces all the variables in a graph with constants of the same values. (deprecated)

[`extract_sub_graph(...)`](../../../tf/compat/v1/graph_util/extract_sub_graph.md): Extract the subgraph that can reach any of the nodes in 'dest_nodes'. (deprecated)

[`import_graph_def(...)`](../../../tf/graph_util/import_graph_def.md): Imports the graph from `graph_def` into the current default `Graph`. (deprecated arguments)

[`must_run_on_cpu(...)`](../../../tf/compat/v1/graph_util/must_run_on_cpu.md): Returns True if the given node_def must run on CPU, otherwise False. (deprecated)

[`remove_training_nodes(...)`](../../../tf/compat/v1/graph_util/remove_training_nodes.md): Prunes out nodes that aren't needed for inference. (deprecated)

[`tensor_shape_from_node_def_name(...)`](../../../tf/compat/v1/graph_util/tensor_shape_from_node_def_name.md): Convenience function to get a shape from a NodeDef's input string. (deprecated)

