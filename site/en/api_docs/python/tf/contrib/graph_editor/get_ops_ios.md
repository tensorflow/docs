page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_ops_ios


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/select.py#L247-L277">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return all the <a href="../../../tf/Operation"><code>tf.Operation</code></a> which are connected to an op in ops.

``` python
tf.contrib.graph_editor.get_ops_ios(
    ops,
    control_inputs=False,
    control_outputs=None,
    control_ios=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ops`</b>: an object convertible to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.
* <b>`control_inputs`</b>: A boolean indicating whether control inputs are enabled.
* <b>`control_outputs`</b>: An instance of `util.ControlOutputs` or `None`. If not
  `None`, control outputs are enabled.
* <b>`control_ios`</b>:  An instance of `util.ControlOutputs` or `None`. If not `None`,
  both control inputs and control outputs are enabled. This is equivalent to
  set `control_inputs` to `True` and `control_outputs` to the
  `util.ControlOutputs` instance.

#### Returns:

All the <a href="../../../tf/Operation"><code>tf.Operation</code></a> surrounding the given ops.


#### Raises:


* <b>`TypeError`</b>: if `ops` cannot be converted to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.
