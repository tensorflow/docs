page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_default_graph

Returns the default graph for the current thread.

### Aliases:

* `tf.compat.v1.get_default_graph`
* `tf.get_default_graph`

``` python
tf.get_default_graph()
```



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->

The returned graph will be the innermost graph on which a
<a href="../tf/Graph#as_default"><code>Graph.as_default()</code></a> context has been entered, or a global default
graph if none has been explicitly created.

NOTE: The default graph is a property of the current thread. If you
create a new thread, and wish to use the default graph in that
thread, you must explicitly add a `with g.as_default():` in that
thread's function.

#### Returns:

The default `Graph` being used in the current thread.
