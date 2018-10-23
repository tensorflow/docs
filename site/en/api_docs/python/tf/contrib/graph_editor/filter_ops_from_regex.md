

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.filter_ops_from_regex

### `tf.contrib.graph_editor.filter_ops_from_regex`

``` python
filter_ops_from_regex(
    ops,
    regex
)
```



Defined in [`tensorflow/contrib/graph_editor/select.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/graph_editor/select.py).

See the guide: [Graph Editor (contrib) > Module: select](../../../../../api_guides/python/contrib.graph_editor#Module_select)

Get all the operations that match the given regex.

#### Args:

* <b>`ops`</b>: an object convertible to a list of `tf.Operation`.
* <b>`regex`</b>: a regular expression matching the operation's name.
    For example, `"^foo(/.*)?$"` will match all the operations in the "foo"
    scope.

#### Returns:

  A list of `tf.Operation`.

#### Raises:

* <b>`TypeError`</b>: if ops cannot be converted to a list of `tf.Operation`.