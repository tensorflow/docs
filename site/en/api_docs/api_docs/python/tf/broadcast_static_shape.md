

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.broadcast_static_shape

``` python
broadcast_static_shape(
    shape_x,
    shape_y
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/array_ops.py).

See the guide: [Tensor Transformations > Shapes and Shaping](../../../api_guides/python/array_ops#Shapes_and_Shaping)

Returns the broadcasted static shape between `shape_x` and `shape_y`.

#### Args:

* <b>`shape_x`</b>: A `TensorShape`
* <b>`shape_y`</b>: A `TensorShape`


#### Returns:

A `TensorShape` representing the broadcasted shape.


#### Raises:

* <b>`ValueError`</b>: If the two shapes can not be broadcasted.