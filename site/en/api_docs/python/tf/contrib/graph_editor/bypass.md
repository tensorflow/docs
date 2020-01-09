page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.bypass


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/edit.py#L201-L221">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Bypass the given subgraph by connecting its inputs to its outputs.

``` python
tf.contrib.graph_editor.bypass(sgv)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sgv`</b>: the subgraph view to be bypassed. This argument is converted to a
  subgraph using the same rules than the function subgraph.make_view.
  Note that sgv is modified in place.

#### Returns:

A tuple `(sgv, detached_inputs)` where:
  `sgv` is a new subgraph view of the bypassed subgraph;
  `detached_inputs` is a list of the created input placeholders.


#### Raises:


* <b>`StandardError`</b>: if sgv cannot be converted to a SubGraphView using
  the same rules than the function subgraph.make_view.
