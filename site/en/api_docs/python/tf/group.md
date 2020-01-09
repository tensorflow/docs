page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.group


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/group">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/control_flow_ops.py#L2850-L2908">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create an op that groups multiple operations.

### Aliases:

* <a href="/api_docs/python/tf/group"><code>tf.compat.v1.group</code></a>
* <a href="/api_docs/python/tf/group"><code>tf.compat.v2.group</code></a>


``` python
tf.group(
    *inputs,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

When this op finishes, all ops in `inputs` have finished. This op has no
output.

See also <a href="../tf/tuple"><code>tf.tuple</code></a> and
<a href="../tf/control_dependencies"><code>tf.control_dependencies</code></a>.

#### Args:


* <b>`*inputs`</b>: Zero or more tensors to group.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

An Operation that executes all its inputs.



#### Raises:


* <b>`ValueError`</b>: If an unknown keyword argument is provided.
