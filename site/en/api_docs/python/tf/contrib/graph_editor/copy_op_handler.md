page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.copy_op_handler


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/transform.py#L131-L191">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Copy a <a href="../../../tf/Operation"><code>tf.Operation</code></a>.

``` python
tf.contrib.graph_editor.copy_op_handler(
    info,
    op,
    new_inputs,
    copy_shape=False,
    nodedef_fn=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`op`</b>: the <a href="../../../tf/Operation"><code>tf.Operation</code></a> to be copied.
* <b>`new_inputs`</b>: The new inputs for this op.
* <b>`copy_shape`</b>: also copy the shape of the tensor
* <b>`nodedef_fn`</b>: If provided, a function that will be run on the NodeDef
  and should return a mutated NodeDef before a new Operation is created.
  This is useful as certain features cannot be set on the Operation and
  must be modified in NodeDef.


#### Returns:

A `(op, op_outputs)` tuple containing the transformed op and its outputs.
