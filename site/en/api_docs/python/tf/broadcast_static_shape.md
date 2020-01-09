page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.broadcast_static_shape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L382-L406">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the shape of a broadcast given known shapes.

### Aliases:

* `tf.compat.v1.broadcast_static_shape`
* `tf.compat.v2.broadcast_static_shape`


``` python
tf.broadcast_static_shape(
    shape_x,
    shape_y
)
```



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
