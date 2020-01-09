page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.control_dependencies


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/control_dependencies">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L5225-L5254">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Wrapper for <a href="../tf/Graph#control_dependencies"><code>Graph.control_dependencies()</code></a> using the default graph.

### Aliases:

* <a href="/api_docs/python/tf/control_dependencies"><code>tf.compat.v1.control_dependencies</code></a>
* <a href="/api_docs/python/tf/control_dependencies"><code>tf.compat.v2.control_dependencies</code></a>


``` python
tf.control_dependencies(control_inputs)
```



<!-- Placeholder for "Used in" -->

See <a href="../tf/Graph#control_dependencies"><code>tf.Graph.control_dependencies</code></a>
for more details.

When eager execution is enabled, any callable object in the `control_inputs`
list will be called.

#### Args:


* <b>`control_inputs`</b>: A list of `Operation` or `Tensor` objects which must be
  executed or computed before running the operations defined in the context.
  Can also be `None` to clear the control dependencies. If eager execution
  is enabled, any callable object in the `control_inputs` list will be
  called.


#### Returns:

A context manager that specifies control dependencies for all
operations constructed within the context.
