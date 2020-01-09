page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.graph_util.must_run_on_cpu


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/graph_util_impl.py#L63-L108">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns True if the given node_def must run on CPU, otherwise False. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/graph_util/must_run_on_cpu"><code>tf.compat.v1.graph_util.must_run_on_cpu</code></a>


``` python
tf.graph_util.must_run_on_cpu(
    node,
    pin_variables_on_cpu=False
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/graph_util/must_run_on_cpu"><code>tf.compat.v1.graph_util.must_run_on_cpu</code></a>

#### Args:


* <b>`node`</b>: The node to be assigned to a device. Could be either an ops.Operation
  or NodeDef.
* <b>`pin_variables_on_cpu`</b>: If True, this function will return False if node_def
  represents a variable-related op.


#### Returns:

True if the given node must run on CPU, otherwise False.
