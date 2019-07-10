page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.to_number

Converts each string in the input Tensor to the specified numeric type.

### Aliases:

* `tf.compat.v1.string_to_number`
* `tf.compat.v1.strings.to_number`
* `tf.string_to_number`
* `tf.strings.to_number`

``` python
tf.strings.to_number(
    string_tensor=None,
    out_type=tf.dtypes.float32,
    name=None,
    input=None
)
```



Defined in [`python/ops/string_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/string_ops.py).

<!-- Placeholder for "Used in" -->

(Note that int32 overflow results in an error while float overflow
results in a rounded value.)

#### Args:


* <b>`string_tensor`</b>: A `Tensor` of type `string`.
* <b>`out_type`</b>: An optional <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.float32, tf.float64, tf.int32, tf.int64`. Defaults to <a href="../../tf#float32"><code>tf.float32</code></a>.
  The numeric type to interpret each string in `string_tensor` as.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `out_type`.
