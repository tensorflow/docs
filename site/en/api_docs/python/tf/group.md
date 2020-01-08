page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.group

``` python
tf.group(
    *inputs,
    **kwargs
)
```



Defined in [`tensorflow/python/ops/control_flow_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/control_flow_ops.py).

Create an op that groups multiple operations.

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