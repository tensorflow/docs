

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.to_double

### `tf.to_double`

``` python
to_double(
    x,
    name='ToDouble'
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/math_ops.py).

See the guide: [Tensor Transformations > Casting](../../../api_guides/python/array_ops#Casting)

Casts a tensor to type `float64`.

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` or `SparseTensor` with same shape as `x` with type `float64`.


#### Raises:

* <b>`TypeError`</b>: If `x` cannot be cast to the `float64`.