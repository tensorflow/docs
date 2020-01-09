page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.detach_control_outputs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/edit.py#L51-L67">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Detach all the external control outputs of the subgraph sgv.

``` python
tf.contrib.graph_editor.detach_control_outputs(
    sgv,
    control_outputs
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sgv`</b>: the subgraph view to be detached. This argument is converted to a
  subgraph using the same rules as the function subgraph.make_view.
* <b>`control_outputs`</b>: a util.ControlOutputs instance.
