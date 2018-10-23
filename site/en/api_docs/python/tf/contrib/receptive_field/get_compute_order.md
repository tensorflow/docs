

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.receptive_field.get_compute_order

``` python
tf.contrib.receptive_field.get_compute_order(
    graph_def,
    input_node_name='',
    input_node_size=None
)
```



Defined in [`tensorflow/contrib/receptive_field/python/util/graph_compute_order.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/receptive_field/python/util/graph_compute_order.py).

Computes order of computation for a given CNN graph.

Optionally, the function may also compute the input and output feature map
resolutions at each node. In this case, input_node_name and input_node_size
must be set. Note that if a node's op type is unknown, the input and output
resolutions are ignored and set to None.

#### Args:

* <b>`graph_def`</b>: GraphDef object.
* <b>`input_node_name`</b>: Name of node with fixed input resolution (optional). This
    is usually the node name for the input image in a CNN.
* <b>`input_node_size`</b>: 2D list of integers, fixed input resolution to use
    (optional). This is usually the input resolution used for the input image
    in a CNN (common examples are: [224, 224], [299, 299], [321, 321]).

#### Returns:

* <b>`node_info`</b>: Default dict keyed by node name, mapping to a named tuple with
    the following fields:
    - order: Integer denoting topological order;
    - node: NodeDef for the given node;
    - input_size: 2D list of integers, denoting the input spatial resolution
      to the node;
    - output_size: 2D list of integers, denoting the output spatial resolution
      of the node.
* <b>`name_to_node`</b>: Dict keyed by node name, each entry containing the node's
    NodeDef.