

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.filter_ts

``` python
filter_ts(
    ops,
    positive_filter
)
```



Defined in [`tensorflow/contrib/graph_editor/select.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/graph_editor/select.py).

See the guide: [Graph Editor (contrib) > Module: select](../../../../../api_guides/python/contrib.graph_editor#Module_select)

Get all the tensors which are input or output of an op in ops.

#### Args:

* <b>`ops`</b>: an object convertible to a list of `tf.Operation`.
* <b>`positive_filter`</b>: a function deciding whether to keep a tensor or not.
    If `True`, all the tensors are returned.

#### Returns:

A list of `tf.Tensor`.

#### Raises:

* <b>`TypeError`</b>: if ops cannot be converted to a list of `tf.Operation`.