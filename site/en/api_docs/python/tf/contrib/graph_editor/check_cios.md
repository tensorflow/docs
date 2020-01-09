page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.check_cios


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/select.py#L209-L244">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Do various check on control_inputs and control_outputs.

``` python
tf.contrib.graph_editor.check_cios(
    control_inputs=False,
    control_outputs=None,
    control_ios=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`control_inputs`</b>: A boolean indicating whether control inputs are enabled.
* <b>`control_outputs`</b>: An instance of util.ControlOutputs or None. If not None,
  control outputs are enabled.
* <b>`control_ios`</b>:  An instance of util.ControlOutputs or None. If not None, both
  control inputs and control outputs are enabled. This is equivalent to set
  control_inputs to True and control_outputs to the util.ControlOutputs
  instance.

#### Returns:

A tuple `(control_inputs, control_outputs)` where:
  `control_inputs` is a boolean indicating whether to use control inputs.
  `control_outputs` is an instance of util.ControlOutputs or None


#### Raises:


* <b>`ValueError`</b>: if control_inputs is an instance of util.ControlOutputs but
  control_outputs is not None
* <b>`TypeError`</b>: if control_outputs is not None and is not a util.ControlOutputs.
