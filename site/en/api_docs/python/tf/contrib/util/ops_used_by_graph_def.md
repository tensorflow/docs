page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.util.ops_used_by_graph_def


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/meta_graph.py#L138-L171">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Collect the list of ops used by a graph.

``` python
tf.contrib.util.ops_used_by_graph_def(graph_def)
```



<!-- Placeholder for "Used in" -->

Does not validate that the ops are all registered.

#### Args:


* <b>`graph_def`</b>: A `GraphDef` proto, as from `graph.as_graph_def()`.


#### Returns:

A list of strings, each naming an op used by the graph.
