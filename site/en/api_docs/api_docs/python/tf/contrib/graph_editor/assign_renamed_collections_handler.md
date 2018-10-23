

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.assign_renamed_collections_handler

``` python
assign_renamed_collections_handler(
    info,
    elem,
    elem_
)
```



Defined in [`tensorflow/contrib/graph_editor/transform.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/graph_editor/transform.py).

See the guide: [Graph Editor (contrib) > Module: transform](../../../../../api_guides/python/contrib.graph_editor#Module_transform)

Add the transformed elem to the (renamed) collections of elem.

A collection is renamed only if is not a known key, as described in
`tf.GraphKeys`.

#### Args:

* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`elem`</b>: the original element (`tf.Tensor` or `tf.Operation`)
* <b>`elem_`</b>: the transformed element