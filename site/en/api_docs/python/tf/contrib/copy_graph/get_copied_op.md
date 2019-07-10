page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.copy_graph.get_copied_op

Given an `Operation` instance from some `Graph`, returns

``` python
tf.contrib.copy_graph.get_copied_op(
    org_instance,
    graph,
    scope=''
)
```



Defined in [`contrib/copy_graph/python/util/copy_elements.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/copy_graph/python/util/copy_elements.py).

<!-- Placeholder for "Used in" -->
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
