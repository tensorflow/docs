page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.graph_util.extract_sub_graph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/graph_util_impl.py#L172-L210">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Extract the subgraph that can reach any of the nodes in 'dest_nodes'. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/graph_util/extract_sub_graph"><code>tf.compat.v1.graph_util.extract_sub_graph</code></a>


``` python
tf.graph_util.extract_sub_graph(
    graph_def,
    dest_nodes
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/graph_util/extract_sub_graph"><code>tf.compat.v1.graph_util.extract_sub_graph</code></a>

#### Args:


* <b>`graph_def`</b>: A graph_pb2.GraphDef proto.
* <b>`dest_nodes`</b>: A list of strings specifying the destination node names.

#### Returns:

The GraphDef of the sub-graph.



#### Raises:


* <b>`TypeError`</b>: If 'graph_def' is not a graph_pb2.GraphDef proto.
