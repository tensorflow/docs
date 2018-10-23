

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.graph_util.extract_sub_graph

``` python
extract_sub_graph(
    graph_def,
    dest_nodes
)
```



Defined in [`tensorflow/python/framework/graph_util_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/framework/graph_util_impl.py).

Extract the subgraph that can reach any of the nodes in 'dest_nodes'.

#### Args:

* <b>`graph_def`</b>: A graph_pb2.GraphDef proto.
* <b>`dest_nodes`</b>: A list of strings specifying the destination node names.

#### Returns:

  The GraphDef of the sub-graph.


#### Raises:

* <b>`TypeError`</b>: If 'graph_def' is not a graph_pb2.GraphDef proto.