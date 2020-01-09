page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_default_graph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L5858-L5874">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the default graph for the current thread.

### Aliases:

* <a href="/api_docs/python/tf/get_default_graph"><code>tf.compat.v1.get_default_graph</code></a>


``` python
tf.get_default_graph()
```



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
