

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.graph_util.must_run_on_cpu

``` python
tf.graph_util.must_run_on_cpu(
    node,
    pin_variables_on_cpu=False
)
```



Defined in [`tensorflow/python/framework/graph_util_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/framework/graph_util_impl.py).

Returns True if the given node_def must run on CPU, otherwise False.

#### Args:

* <b>`node`</b>: The node to be assigned to a device. Could be either an ops.Operation
    or NodeDef.
* <b>`pin_variables_on_cpu`</b>: If True, this function will return False if node_def
    represents a variable-related op.


#### Returns:

True if the given node must run on CPU, otherwise False.