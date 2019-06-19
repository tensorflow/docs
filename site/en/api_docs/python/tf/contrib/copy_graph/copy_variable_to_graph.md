

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.copy_graph.copy_variable_to_graph

``` python
tf.contrib.copy_graph.copy_variable_to_graph(
    org_instance,
    to_graph,
    scope=''
)
```



Defined in [`tensorflow/contrib/copy_graph/python/util/copy_elements.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/copy_graph/python/util/copy_elements.py).

Given a `Variable` instance from one `Graph`, initializes and returns
a copy of it from another `Graph`, under the specified scope
(default `""`).

#### Args:

* <b>`org_instance`</b>: A `Variable` from some `Graph`.
* <b>`to_graph`</b>: The `Graph` to copy the `Variable` to.
* <b>`scope`</b>: A scope for the new `Variable` (default `""`).


#### Returns:

The copied `Variable` from `to_graph`.


#### Raises:

* <b>`TypeError`</b>: If `org_instance` is not a `Variable`.