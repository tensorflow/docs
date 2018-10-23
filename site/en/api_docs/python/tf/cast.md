

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.cast

``` python
tf.cast(
    x,
    dtype,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/ops/math_ops.py).

See the guide: [Tensor Transformations > Casting](../../../api_guides/python/array_ops#Casting)

Casts a tensor to a new type.

The operation casts `x` (in case of `Tensor`) or `x.values`
(in case of `SparseTensor`) to `dtype`.

For example:

```python
x = tf.constant([1.8, 2.2], dtype=tf.float32)
tf.cast(x, tf.int32)  # [1, 2], dtype=tf.int32
```

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor`.
* <b>`dtype`</b>: The destination type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor` with same shape as `x`.


#### Raises:

* <b>`TypeError`</b>: If `x` cannot be cast to the `dtype`.