page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.make_list_of_op

``` python
tf.contrib.graph_editor.make_list_of_op(
    ops,
    check_graph=True,
    allow_graph=True,
    ignore_ts=False
)
```



Defined in [`tensorflow/contrib/graph_editor/util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/graph_editor/util.py).

See the guide: [Graph Editor (contrib) > Module: util](../../../../../api_guides/python/contrib.graph_editor#Module_util)

Convert ops to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.

#### Args:

* <b>`ops`</b>: can be an iterable of <a href="../../../tf/Operation"><code>tf.Operation</code></a>, a <a href="../../../tf/Graph"><code>tf.Graph</code></a> or a single
    operation.
* <b>`check_graph`</b>: if `True` check if all the operations belong to the same graph.
* <b>`allow_graph`</b>: if `False` a <a href="../../../tf/Graph"><code>tf.Graph</code></a> cannot be converted.
* <b>`ignore_ts`</b>: if True, silently ignore <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.

#### Returns:

A newly created list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.

#### Raises:

* <b>`TypeError`</b>: if ops cannot be converted to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a> or,
   if `check_graph` is `True`, if all the ops do not belong to the
   same graph.