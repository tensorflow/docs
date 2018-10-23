

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.make_view

### Aliases:

* `tf.contrib.graph_editor.make_view`
* `tf.contrib.graph_editor.sgv`

``` python
make_view(
    *args,
    **kwargs
)
```



Defined in [`tensorflow/contrib/graph_editor/subgraph.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/graph_editor/subgraph.py).

See the guides: [Graph Editor (contrib) > Module: subgraph](../../../../../api_guides/python/contrib.graph_editor#Module_subgraph), [Graph Editor (contrib) > Useful aliases](../../../../../api_guides/python/contrib.graph_editor#Useful_aliases)

Create a SubGraphView from selected operations and passthrough tensors.

#### Args:

* <b>`*args`</b>: list of 1) regular expressions (compiled or not) or 2) (array of)
    `tf.Operation` 3) (array of) `tf.Tensor`. Those objects will be converted
    into a list of operations and a list of candidate for passthrough tensors.
* <b>`**kwargs`</b>: keyword graph is used 1) to check that the ops and ts are from
    the correct graph 2) for regular expression query

#### Returns:

A subgraph view.

#### Raises:

* <b>`TypeError`</b>: if the optional keyword argument graph is not a `tf.Graph`
    or if an argument in args is not an (array of) `tf.Tensor`
    or an (array of) `tf.Operation` or a string or a regular expression.
* <b>`ValueError`</b>: if one of the keyword arguments is unexpected.