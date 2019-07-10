page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.fuse_op

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



Defined in [`contrib/framework/python/framework/graph_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/framework/graph_util.py).

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