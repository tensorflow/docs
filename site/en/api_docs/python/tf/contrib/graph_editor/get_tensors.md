page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_tensors

get all the tensors which are input or output of an op in the graph.

``` python
tf.contrib.graph_editor.get_tensors(graph)
```



Defined in [`contrib/graph_editor/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/util.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`graph`</b>: a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.

#### Returns:

A list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.


#### Raises:


* <b>`TypeError`</b>: if graph is not a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.