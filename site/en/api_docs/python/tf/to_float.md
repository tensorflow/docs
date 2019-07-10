page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.to_float

Casts a tensor to type `float32`. (deprecated)

### Aliases:

* `tf.compat.v1.to_float`
* `tf.to_float`

``` python
tf.to_float(
    x,
    name='ToFloat'
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../tf/dtypes/cast"><code>tf.cast</code></a> instead.

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
type `float32`.



#### Raises:


* <b>`TypeError`</b>: If `x` cannot be cast to the `float32`.