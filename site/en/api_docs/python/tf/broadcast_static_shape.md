page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.broadcast_static_shape

Computes the shape of a broadcast given known shapes.

### Aliases:

* `tf.broadcast_static_shape`
* `tf.compat.v1.broadcast_static_shape`
* `tf.compat.v2.broadcast_static_shape`

``` python
tf.broadcast_static_shape(
    shape_x,
    shape_y
)
```



Defined in [`python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/array_ops.py).

<!-- Placeholder for "Used in" -->

When shape_x and shape_y are fully known TensorShapes this computes a
TensorShape which is the shape of the result of a broadcasting op applied in
tensors of shapes shape_x and shape_y.

For example, if shape_x is [1, 2, 3] and shape_y is [5, 1, 3], the result is a
TensorShape whose value is [5, 2, 3].

This is useful when validating the result of a broadcasting operation when the
tensors have statically known shapes.

#### Args:


* <b>`shape_x`</b>: A `TensorShape`
* <b>`shape_y`</b>: A `TensorShape`


#### Returns:

A `TensorShape` representing the broadcasted shape.



#### Raises:


* <b>`ValueError`</b>: If the two shapes can not be broadcasted.