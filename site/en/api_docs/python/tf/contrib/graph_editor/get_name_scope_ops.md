page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_name_scope_ops

``` python
tf.contrib.graph_editor.get_name_scope_ops(
    ops,
    scope
)
```



Defined in [`tensorflow/contrib/graph_editor/select.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/graph_editor/select.py).

See the guide: [Graph Editor (contrib) > Module: select](../../../../../api_guides/python/contrib.graph_editor#Module_select)

Get all the operations under the given scope path.

#### Args:

* <b>`ops`</b>: an object convertible to a list of tf.Operation.
* <b>`scope`</b>: a scope path.

#### Returns:

A list of tf.Operation.

#### Raises:

* <b>`TypeError`</b>: if ops cannot be converted to a list of tf.Operation.