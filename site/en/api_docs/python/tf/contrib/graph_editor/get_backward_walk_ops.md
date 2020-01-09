page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_backward_walk_ops


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/select.py#L459-L496">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Do a backward graph walk and return all the visited ops. (deprecated)

``` python
tf.contrib.graph_editor.get_backward_walk_ops(
    seed_ops,
    inclusive=True,
    within_ops=None,
    within_ops_fn=None,
    stop_at_ts=(),
    control_inputs=False
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2019-06-06.
Instructions for updating:
Please use tensorflow.python.ops.op_selector.get_backward_walk_ops.

#### Args:


* <b>`seed_ops`</b>: an iterable of operations from which the backward graph
  walk starts. If a list of tensors is given instead, the seed_ops are set
  to be the generators of those tensors.
* <b>`inclusive`</b>: if True the given seed_ops are also part of the resulting set.
* <b>`within_ops`</b>: an iterable of <a href="../../../tf/Operation"><code>tf.Operation</code></a> within which the search is
  restricted. If `within_ops` is `None`, the search is performed within
  the whole graph.
* <b>`within_ops_fn`</b>: if provided, a function on ops that should return True iff
  the op is within the graph traversal. This can be used along within_ops,
  in which case an op is within if it is also in within_ops.
* <b>`stop_at_ts`</b>: an iterable of tensors at which the graph walk stops.
* <b>`control_inputs`</b>: if True, control inputs will be used while moving backward.

#### Returns:

A Python set of all the <a href="../../../tf/Operation"><code>tf.Operation</code></a> behind `seed_ops`.


#### Raises:


* <b>`TypeError`</b>: if `seed_ops` or `within_ops` cannot be converted to a list of
  <a href="../../../tf/Operation"><code>tf.Operation</code></a>.
