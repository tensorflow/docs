page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.group


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/control_flow_ops.py#L2850-L2908">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create an op that groups multiple operations.

### Aliases:

* `tf.compat.v1.group`
* `tf.compat.v2.group`


``` python
tf.group(
    *inputs,
    **kwargs
)
```



### Used in the guide:

* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)



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
