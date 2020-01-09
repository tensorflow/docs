page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.container

``` python
tf.container(container_name)
```



Defined in [`tensorflow/python/framework/ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/framework/ops.py).

Wrapper for `Graph.container()` using the default graph.

#### Args:

* <b>`container_name`</b>: The container string to use in the context.


#### Returns:

A context manager that specifies the default container to use for newly
created stateful ops.