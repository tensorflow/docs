

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.make_placeholder_from_tensor

``` python
tf.contrib.graph_editor.make_placeholder_from_tensor(
    t,
    scope=None,
    prefix=_DEFAULT_PLACEHOLDER_PREFIX
)
```



Defined in [`tensorflow/contrib/graph_editor/util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/graph_editor/util.py).

See the guide: [Graph Editor (contrib) > Module: util](../../../../../api_guides/python/contrib.graph_editor#Module_util)

Create a <a href="../../../tf/placeholder"><code>tf.placeholder</code></a> for the Graph Editor.

Note that the correct graph scope must be set by the calling function.

#### Args:

* <b>`t`</b>: a <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> whose name will be used to create the placeholder
    (see function placeholder_name).
* <b>`scope`</b>: absolute scope within which to create the placeholder. None
    means that the scope of `t` is preserved. `""` means the root scope.
* <b>`prefix`</b>: placeholder name prefix.

#### Returns:

A newly created <a href="../../../tf/placeholder"><code>tf.placeholder</code></a>.

#### Raises:

* <b>`TypeError`</b>: if `t` is not `None` or a <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.