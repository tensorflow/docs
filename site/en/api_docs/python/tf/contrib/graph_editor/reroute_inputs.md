page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.reroute_inputs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/reroute.py#L399-L416">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Re-route all the inputs of two subgraphs.

``` python
tf.contrib.graph_editor.reroute_inputs(
    sgv0,
    sgv1
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sgv0`</b>: the first subgraph to have its inputs swapped. This argument is
  converted to a subgraph using the same rules than the function
  subgraph.make_view.
* <b>`sgv1`</b>: the second subgraph to have its inputs swapped. This argument is
  converted to a subgraph using the same rules than the function
  subgraph.make_view.

#### Returns:

A tuple `(sgv0, sgv1)` of subgraph views with their inputs swapped.
  Note that the function argument sgv0 and sgv1 are also modified in place.


#### Raises:


* <b>`StandardError`</b>: if sgv0 or sgv1 cannot be converted to a SubGraphView using
  the same rules than the function subgraph.make_view.
