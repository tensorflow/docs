page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.to_int32

``` python
tf.to_int32(
    x,
    name='ToInt32'
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/math_ops.py).

Casts a tensor to type `int32`. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.cast instead.

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
type `int32`.


#### Raises:

* <b>`TypeError`</b>: If `x` cannot be cast to the `int32`.