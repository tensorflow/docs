page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_tensors


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/util.py#L257-L272">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



get all the tensors which are input or output of an op in the graph.

``` python
tf.contrib.graph_editor.get_tensors(graph)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`graph`</b>: a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.

#### Returns:

A list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.


#### Raises:


* <b>`TypeError`</b>: if graph is not a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.
