

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.copy_graph.copy_variable_to_graph

### `tf.contrib.copy_graph.copy_variable_to_graph`

``` python
copy_variable_to_graph(
    org_instance,
    to_graph,
    scope=''
)
```



Defined in [`tensorflow/contrib/copy_graph/python/util/copy_elements.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/copy_graph/python/util/copy_elements.py).

Given a `Variable` instance from one `Graph`, initializes and returns
a copy of it from another `Graph`, under the specified scope
(default `""`).

#### Args:

org_instance: A `Variable` from some `Graph`.
to_graph: The `Graph` to copy the `Variable` to.
scope: A scope for the new `Variable` (default `""`).


#### Returns:

    The copied `Variable` from `to_graph`.


#### Raises:

    TypeError: If `org_instance` is not a `Variable`.