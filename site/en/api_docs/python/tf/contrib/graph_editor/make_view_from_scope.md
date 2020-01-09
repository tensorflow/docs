page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.make_view_from_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/subgraph.py#L658-L668">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Make a subgraph from a name scope.

### Aliases:

* <a href="/api_docs/python/tf/contrib/graph_editor/make_view_from_scope"><code>tf.contrib.graph_editor.sgv_scope</code></a>


``` python
tf.contrib.graph_editor.make_view_from_scope(
    scope,
    graph
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`scope`</b>: the name of the scope.
* <b>`graph`</b>: the <a href="../../../tf/Graph"><code>tf.Graph</code></a>.

#### Returns:

A subgraph view representing the given scope.
