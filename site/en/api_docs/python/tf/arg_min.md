page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.arg_min


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns the index with the smallest value across dimensions of a tensor.

### Aliases:

* <a href="/api_docs/python/tf/arg_min"><code>tf.compat.v1.arg_min</code></a>


``` python
tf.arg_min(
    input,
    dimension,
    output_type=tf.dtypes.int64,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Note that in case of ties the identity of the return value is not guaranteed.

#### Usage:

```python
import tensorflow as tf
a = [1, 10, 26.9, 2.8, 166.32, 62.3]
b = tf.math.argmin(input = a)
c = tf.keras.backend.eval(b)
# c = 0
# here a[0] = 1 which is the smallest element of a across axis 0
```



#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
* <b>`dimension`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  int32 or int64, must be in the range `[-rank(input), rank(input))`.
  Describes which dimension of the input Tensor to reduce across. For vectors,
  use dimension = 0.
* <b>`output_type`</b>: An optional <a href="../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../tf#int64"><code>tf.int64</code></a>.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `output_type`.
