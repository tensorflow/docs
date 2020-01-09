page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.detach_inputs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/edit.py#L70-L98">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Detach the inputs of a subgraph view.

``` python
tf.contrib.graph_editor.detach_inputs(
    sgv,
    control_inputs=False
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sgv`</b>: the subgraph view to be detached. This argument is converted to a
  subgraph using the same rules as the function subgraph.make_view.
  Note that sgv is modified in place.
* <b>`control_inputs`</b>: if True control_inputs are also detached.

#### Returns:

A tuple `(sgv, input_placeholders)` where
  `sgv` is a new subgraph view of the detached subgraph;
  `input_placeholders` is a list of the created input placeholders.


#### Raises:


* <b>`StandardError`</b>: if sgv cannot be converted to a SubGraphView using
  the same rules than the function subgraph.make_view.
