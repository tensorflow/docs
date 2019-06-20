page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.logical_xor

``` python
tf.logical_xor(
    x,
    y,
    name='LogicalXor'
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/math_ops.py).

See the guide: [Control Flow > Logical Operators](../../../api_guides/python/control_flow_ops#Logical_Operators)

x ^ y = (x | y) & ~(x & y).