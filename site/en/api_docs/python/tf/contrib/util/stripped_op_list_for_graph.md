page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.util.stripped_op_list_for_graph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/meta_graph.py#L174-L209">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Collect the stripped OpDefs for ops used by a graph.

``` python
tf.contrib.util.stripped_op_list_for_graph(graph_def)
```



<!-- Placeholder for "Used in" -->

This function computes the `stripped_op_list` field of `MetaGraphDef` and
similar protos.  The result can be communicated from the producer to the
consumer, which can then use the C++ function
`RemoveNewDefaultAttrsFromGraphDef` to improve forwards compatibility.

#### Args:


* <b>`graph_def`</b>: A `GraphDef` proto, as from `graph.as_graph_def()`.


#### Returns:

An `OpList` of ops used by the graph.



#### Raises:


* <b>`ValueError`</b>: If an unregistered op is used.
