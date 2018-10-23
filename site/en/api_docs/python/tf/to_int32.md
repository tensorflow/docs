

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.to_int32

### `tf.to_int32`

``` python
to_int32(
    x,
    name='ToInt32'
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/math_ops.py).

See the guide: [Tensor Transformations > Casting](../../../api_guides/python/array_ops#Casting)

Casts a tensor to type `int32`.

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` or `SparseTensor` with same shape as `x` with type `int32`.


#### Raises:

* <b>`TypeError`</b>: If `x` cannot be cast to the `int32`.