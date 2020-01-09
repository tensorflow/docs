page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.copy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/transform.py#L591-L623">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Copy a subgraph.

``` python
tf.contrib.graph_editor.copy(
    sgv,
    dst_graph=None,
    dst_scope='',
    src_scope='',
    reuse_dst_scope=False
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sgv`</b>: the source subgraph-view. This argument is converted to a subgraph
  using the same rules than the function subgraph.make_view.
* <b>`dst_graph`</b>: the destination graph.
* <b>`dst_scope`</b>: the destination scope.
* <b>`src_scope`</b>: the source scope.
* <b>`reuse_dst_scope`</b>: if True the dst_scope is re-used if it already exists.
  Otherwise, the scope is given a unique name based on the one given
  by appending an underscore followed by a digit (default).

#### Returns:

A tuple `(sgv, info)` where:
  `sgv` is the transformed subgraph view;
  `info` is an instance of TransformerInfo containing
  information about the transform, including mapping between
  original and transformed tensors and operations.


#### Raises:


* <b>`TypeError`</b>: if `dst_graph` is not a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.
* <b>`StandardError`</b>: if sgv cannot be converted to a SubGraphView using
  the same rules than the function subgraph.make_view.
