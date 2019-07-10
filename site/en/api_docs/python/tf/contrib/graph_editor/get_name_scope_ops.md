page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_name_scope_ops

Get all the operations under the given scope path.

``` python
tf.contrib.graph_editor.get_name_scope_ops(
    ops,
    scope
)
```



Defined in [`contrib/graph_editor/select.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/select.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ops`</b>: an object convertible to a list of tf.Operation.
* <b>`scope`</b>: a scope path.

#### Returns:

A list of tf.Operation.


#### Raises:


* <b>`TypeError`</b>: if ops cannot be converted to a list of tf.Operation.