page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.detach


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/edit.py#L141-L169">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Detach both the inputs and the outputs of a subgraph view.

``` python
tf.contrib.graph_editor.detach(
    sgv,
    control_inputs=False,
    control_outputs=None,
    control_ios=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sgv`</b>: the subgraph view to be detached. This argument is converted to a
  subgraph using the same rules as the function subgraph.make_view.
  Note that sgv is modified in place.
* <b>`control_inputs`</b>: A boolean indicating whether control inputs are enabled.
* <b>`control_outputs`</b>: An instance of util.ControlOutputs or None. If not None,
  control outputs are enabled.
* <b>`control_ios`</b>:  An instance of util.ControlOutputs or None. If not None, both
  control inputs and control outputs are enabled. This is equivalent to set
  control_inputs to True and control_outputs to the util.ControlOutputs
  instance.

#### Returns:

A tuple `(sgv, detached_inputs, detached_outputs)` where:
`sgv` is a new subgraph view of the detached subgraph;
`detach_inputs` is a list of the created input placeholders;
`detach_outputs` is a list of the created output placeholders.


#### Raises:


* <b>`StandardError`</b>: if sgv cannot be converted to a SubGraphView using
  the same rules than the function subgraph.make_view.
