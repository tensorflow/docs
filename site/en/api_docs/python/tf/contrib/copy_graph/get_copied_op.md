

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.copy_graph.get_copied_op

### `tf.contrib.copy_graph.get_copied_op`

``` python
get_copied_op(
    org_instance,
    graph,
    scope=''
)
```



Defined in [`tensorflow/contrib/copy_graph/python/util/copy_elements.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/copy_graph/python/util/copy_elements.py).

Given an `Operation` instance from some `Graph`, returns
its namesake from `graph`, under the specified scope
(default `""`).

If a copy of `org_instance` is present in `graph` under the given
`scope`, it will be returned.

#### Args:

* <b>`org_instance`</b>: An `Operation` from some `Graph`.
* <b>`graph`</b>: The `Graph` to be searched for a copr of `org_instance`.
* <b>`scope`</b>: The scope `org_instance` is present in.


#### Returns:

  The `Operation` copy from `graph`.