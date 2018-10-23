

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.add_check_numerics_ops

``` python
add_check_numerics_ops()
```



Defined in [`tensorflow/python/ops/numerics.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/numerics.py).

See the guide: [Control Flow > Debugging Operations](../../../api_guides/python/control_flow_ops#Debugging_Operations)

Connect a `check_numerics` to every floating point tensor.

`check_numerics` operations themselves are added for each `half`, `float`,
or `double` tensor in the graph. For all ops in the graph, the
`check_numerics` op for all of its (`half`, `float`, or `double`) inputs
is guaranteed to run before the `check_numerics` op on any of its outputs.

Note: This API is not compatible with the use of [`tf.cond`](../tf/cond) or
[`tf.while_loop`](../tf/while_loop), and will raise a `ValueError` if you attempt to call it
in such a graph.

#### Returns:

A `group` op depending on all `check_numerics` ops added.


#### Raises:

* <b>`ValueError`</b>: If the graph contains any numeric operations in a control flow
    structure.