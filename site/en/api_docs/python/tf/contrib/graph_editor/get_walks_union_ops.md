page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_walks_union_ops


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/select.py#L558-L613">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return the union of a forward and a backward walk.

``` python
tf.contrib.graph_editor.get_walks_union_ops(
    forward_seed_ops,
    backward_seed_ops,
    forward_inclusive=True,
    backward_inclusive=True,
    within_ops=None,
    within_ops_fn=None,
    control_inputs=False,
    control_outputs=None,
    control_ios=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`forward_seed_ops`</b>: an iterable of operations from which the forward graph
  walk starts. If a list of tensors is given instead, the seed_ops are set
  to be the consumers of those tensors.
* <b>`backward_seed_ops`</b>: an iterable of operations from which the backward graph
  walk starts. If a list of tensors is given instead, the seed_ops are set
  to be the generators of those tensors.
* <b>`forward_inclusive`</b>: if True the given forward_seed_ops are also part of the
  resulting set.
* <b>`backward_inclusive`</b>: if True the given backward_seed_ops are also part of the
  resulting set.
* <b>`within_ops`</b>: restrict the search within those operations. If within_ops is
  None, the search is done within the whole graph.
* <b>`within_ops_fn`</b>: if provided, a function on ops that should return True iff
  the op is within the graph traversal. This can be used along within_ops,
  in which case an op is within if it is also in within_ops.
* <b>`control_inputs`</b>: A boolean indicating whether control inputs are enabled.
* <b>`control_outputs`</b>: An instance of util.ControlOutputs or None. If not None,
  control outputs are enabled.
* <b>`control_ios`</b>:  An instance of util.ControlOutputs or None. If not None, both
  control inputs and control outputs are enabled. This is equivalent to set
  control_inputs to True and control_outputs to the util.ControlOutputs
  instance.

#### Returns:

A Python set of all the tf.Operation in the union of a forward and a
  backward walk.


#### Raises:


* <b>`TypeError`</b>: if forward_seed_ops or backward_seed_ops or within_ops cannot be
  converted to a list of tf.Operation.
