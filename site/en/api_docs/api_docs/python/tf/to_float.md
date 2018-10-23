

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.to_float

``` python
to_float(
    x,
    name='ToFloat'
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/math_ops.py).

See the guide: [Tensor Transformations > Casting](../../../api_guides/python/array_ops#Casting)

Casts a tensor to type `float32`.

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` or `SparseTensor` with same shape as `x` with type `float32`.


#### Raises:

* <b>`TypeError`</b>: If `x` cannot be cast to the `float32`.