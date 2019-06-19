

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_default_graph

``` python
tf.get_default_graph()
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/framework/ops.py).

See the guide: [Building Graphs > Utility functions](../../../api_guides/python/framework#Utility_functions)

Returns the default graph for the current thread.

The returned graph will be the innermost graph on which a
`Graph.as_default()` context has been entered, or a global default
graph if none has been explicitly created.

NOTE: The default graph is a property of the current thread. If you
create a new thread, and wish to use the default graph in that
thread, you must explicitly add a `with g.as_default():` in that
thread's function.

#### Returns:

The default `Graph` being used in the current thread.