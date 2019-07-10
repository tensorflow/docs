page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.broadcast_dynamic_shape

Computes the shape of a broadcast given symbolic shapes.

### Aliases:

* `tf.broadcast_dynamic_shape`
* `tf.compat.v1.broadcast_dynamic_shape`
* `tf.compat.v2.broadcast_dynamic_shape`

``` python
tf.broadcast_dynamic_shape(
    shape_x,
    shape_y
)
```



Defined in [`python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/array_ops.py).

<!-- Placeholder for "Used in" -->

When shape_x and shape_y are Tensors representing shapes (i.e. the result of
calling tf.shape on another Tensor) this computes a Tensor which is the shape
of the result of a broadcasting op applied in tensors of shapes shape_x and
shape_y.

For example, if shape_x is [1, 2, 3] and shape_y is [5, 1, 3], the result is a
Tensor whose value is [5, 2, 3].

This is useful when validating the result of a broadcasting operation when the
tensors do not have statically known shapes.

#### Args:


* <b>`shape_x`</b>: A rank 1 integer `Tensor`, representing the shape of x.
* <b>`shape_y`</b>: A rank 1 integer `Tensor`, representing the shape of y.


#### Returns:

A rank 1 integer `Tensor` representing the broadcasted shape.
