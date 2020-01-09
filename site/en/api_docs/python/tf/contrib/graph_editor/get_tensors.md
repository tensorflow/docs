page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_tensors

``` python
tf.contrib.graph_editor.get_tensors(graph)
```



Defined in [`tensorflow/contrib/graph_editor/util.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/graph_editor/util.py).

See the guide: [Graph Editor (contrib) > Module: util](../../../../../api_guides/python/contrib.graph_editor#Module_util)

get all the tensors which are input or output of an op in the graph.

#### Args:

* <b>`graph`</b>: a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.

#### Returns:

A list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.

#### Raises:

* <b>`TypeError`</b>: if graph is not a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.