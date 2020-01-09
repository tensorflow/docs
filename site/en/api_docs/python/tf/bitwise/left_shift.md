page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.bitwise.left_shift


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_bitwise_ops.py`



Elementwise computes the bitwise left-shift of `x` and `y`.

### Aliases:

* `tf.compat.v1.bitwise.left_shift`
* `tf.compat.v2.bitwise.left_shift`


``` python
tf.bitwise.left_shift(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

If `y` is negative, or greater than or equal to the width of `x` in bits the
result is implementation defined.

#### Example:



```python
import tensorflow as tf
from tensorflow.python.ops import bitwise_ops
import numpy as np
dtype_list = [tf.int8, tf.int16, tf.int32, tf.int64]

for dtype in dtype_list:
  lhs = tf.constant([-1, -5, -3, -14], dtype=dtype)
  rhs = tf.constant([5, 0, 7, 11], dtype=dtype)
  
  left_shift_result = bitwise_ops.left_shift(lhs, rhs)
  
  print(left_shift_result)

# This will print:
# tf.Tensor([ -32   -5 -128    0], shape=(4,), dtype=int8)
# tf.Tensor([   -32     -5   -384 -28672], shape=(4,), dtype=int16)
# tf.Tensor([   -32     -5   -384 -28672], shape=(4,), dtype=int32)
# tf.Tensor([   -32     -5   -384 -28672], shape=(4,), dtype=int64)

lhs = np.array([-2, 64, 101, 32], dtype=np.int8)
rhs = np.array([-1, -5, -3, -14], dtype=np.int8)
bitwise_ops.left_shift(lhs, rhs)
# <tf.Tensor: id=139, shape=(4,), dtype=int8, numpy=array([ -2,  64, 101,  32], dtype=int8)>
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
