

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.cast

``` python
cast(
    x,
    dtype,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/math_ops.py).

See the guide: [Tensor Transformations > Casting](../../../api_guides/python/array_ops#Casting)

Casts a tensor to a new type.

The operation casts `x` (in case of `Tensor`) or `x.values`
(in case of `SparseTensor`) to `dtype`.

For example:

```python
# tensor `a` is [1.8, 2.2], dtype=tf.float
tf.cast(a, tf.int32) ==> [1, 2]  # dtype=tf.int32
```

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor`.
* <b>`dtype`</b>: The destination type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` or `SparseTensor` with same shape as `x`.


#### Raises:

* <b>`TypeError`</b>: If `x` cannot be cast to the `dtype`.