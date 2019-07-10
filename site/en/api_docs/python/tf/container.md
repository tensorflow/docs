page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.container

Wrapper for <a href="../tf/Graph#container"><code>Graph.container()</code></a> using the default graph.

### Aliases:

* `tf.compat.v1.container`
* `tf.container`

``` python
tf.container(container_name)
```



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`container_name`</b>: The container string to use in the context.


#### Returns:

A context manager that specifies the default container to use for newly
created stateful ops.
