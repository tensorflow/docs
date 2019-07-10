page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.shape_n

Returns shape of tensors.

### Aliases:

* `tf.compat.v1.shape_n`
* `tf.compat.v2.shape_n`
* `tf.shape_n`

``` python
tf.shape_n(
    input,
    out_type=tf.dtypes.int32,
    name=None
)
```



Defined in [`python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/array_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input`</b>: A list of at least 1 `Tensor` object with the same type.
* <b>`out_type`</b>: The specified output type of the operation (`int32` or `int64`).
  Defaults to <a href="../tf#int32"><code>tf.int32</code></a>(optional).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list with the same length as `input` of `Tensor` objects with
  type `out_type`.
