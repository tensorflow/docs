page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.container


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L5177-L5188">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Wrapper for <a href="../tf/Graph#container"><code>Graph.container()</code></a> using the default graph.

### Aliases:

* <a href="/api_docs/python/tf/container"><code>tf.compat.v1.container</code></a>


``` python
tf.container(container_name)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`container_name`</b>: The container string to use in the context.


#### Returns:

A context manager that specifies the default container to use for newly
created stateful ops.
