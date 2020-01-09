page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.fuse_op


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/framework/graph_util.py#L37-L135">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Fuse subgraph between input_nodes and output_nodes into a single custom op.

``` python
tf.contrib.framework.fuse_op(
    graph_def,
    input_nodes,
    output_nodes,
    output_dtypes,
    output_quantized,
    op_name,
    op_type
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`graph_def`</b>: A graph_pb2.GraphDef proto.
* <b>`input_nodes`</b>: input nodes to the subgraph to be fused.
* <b>`output_nodes`</b>: output nodes to the subgraph to be fused.
* <b>`output_dtypes`</b>: A list of output datatypes for the custom op
* <b>`output_quantized`</b>: A boolean flag that indicates if output is quantized
* <b>`op_name`</b>: fused op name.
* <b>`op_type`</b>: fused op type.

#### Returns:

The GraphDef of the new graph.



#### Raises:


* <b>`TypeError`</b>: If 'graph_def' is not a graph_pb2.GraphDef proto.
