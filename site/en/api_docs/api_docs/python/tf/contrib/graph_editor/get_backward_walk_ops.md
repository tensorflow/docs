

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.get_backward_walk_ops

``` python
get_backward_walk_ops(
    seed_ops,
    inclusive=True,
    within_ops=None,
    stop_at_ts=(),
    control_inputs=False
)
```



Defined in [`tensorflow/contrib/graph_editor/select.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/graph_editor/select.py).

See the guide: [Graph Editor (contrib) > Module: select](../../../../../api_guides/python/contrib.graph_editor#Module_select)

Do a backward graph walk and return all the visited ops.

#### Args:

* <b>`seed_ops`</b>: an iterable of operations from which the backward graph
    walk starts. If a list of tensors is given instead, the seed_ops are set
    to be the generators of those tensors.
* <b>`inclusive`</b>: if True the given seed_ops are also part of the resulting set.
* <b>`within_ops`</b>: an iterable of `tf.Operation` within which the search is
    restricted. If `within_ops` is `None`, the search is performed within
    the whole graph.
* <b>`stop_at_ts`</b>: an iterable of tensors at which the graph walk stops.
* <b>`control_inputs`</b>: if True, control inputs will be used while moving backward.

#### Returns:

  A Python set of all the `tf.Operation` behind `seed_ops`.

#### Raises:

* <b>`TypeError`</b>: if `seed_ops` or `within_ops` cannot be converted to a list of
    `tf.Operation`.