page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.reset_default_graph

``` python
tf.reset_default_graph()
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/framework/ops.py).

See the guide: [Building Graphs > Utility functions](../../../api_guides/python/framework#Utility_functions)

Clears the default graph stack and resets the global default graph.

NOTE: The default graph is a property of the current thread. This
function applies only to the current thread.  Calling this function while
a <a href="../tf/Session"><code>tf.Session</code></a> or <a href="../tf/InteractiveSession"><code>tf.InteractiveSession</code></a> is active will result in undefined
behavior. Using any previously created <a href="../tf/Operation"><code>tf.Operation</code></a> or <a href="../tf/Tensor"><code>tf.Tensor</code></a> objects
after calling this function will result in undefined behavior.
#### Raises:

* <b>`AssertionError`</b>: If this function is called within a nested graph.