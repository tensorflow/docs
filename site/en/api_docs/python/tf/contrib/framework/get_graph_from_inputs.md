page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_graph_from_inputs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/ops.py#L28-L55">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the appropriate graph to use for the given inputs.

``` python
tf.contrib.framework.get_graph_from_inputs(
    op_input_list,
    graph=None
)
```



<!-- Placeholder for "Used in" -->

1. If `graph` is provided, we validate that all inputs in `op_input_list` are
   from the same graph.
2. Otherwise, we attempt to select a graph from the first Operation- or
   Tensor-valued input in `op_input_list`, and validate that all other
   such inputs are in the same graph.
3. If the graph was not specified and it could not be inferred from
   `op_input_list`, we attempt to use the default graph.

#### Args:


* <b>`op_input_list`</b>: A list of inputs to an operation, which may include `Tensor`,
  `Operation`, and other objects that may be converted to a graph element.
* <b>`graph`</b>: (Optional) The explicit graph to use.


#### Raises:


* <b>`TypeError`</b>: If `op_input_list` is not a list or tuple, or if graph is not a
  Graph.
* <b>`ValueError`</b>: If a graph is explicitly passed and not all inputs are from it,
  or if the inputs are from multiple graphs, or we could not find a graph
  and there was no default graph.


#### Returns:

The appropriate graph to use for the given inputs.
