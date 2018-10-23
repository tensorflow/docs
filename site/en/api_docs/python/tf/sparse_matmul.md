

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.sparse_matmul

### `tf.sparse_matmul`

``` python
sparse_matmul(
    a,
    b,
    transpose_a=None,
    transpose_b=None,
    a_is_sparse=None,
    b_is_sparse=None,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_math_ops.py`.

Multiply matrix "a" by matrix "b".

The inputs must be two-dimensional matrices and the inner dimension of "a" must
match the outer dimension of "b". This op is optimized for the case where at
least one of "a" or "b" is sparse. The breakeven for using this versus a dense
matrix multiply on one platform was 30% zero values in the sparse matrix.

#### Args:

* <b>`a`</b>: A `Tensor`. Must be one of the following types: `float32`, `bfloat16`.
* <b>`b`</b>: A `Tensor`. Must be one of the following types: `float32`, `bfloat16`.
* <b>`transpose_a`</b>: An optional `bool`. Defaults to `False`.
* <b>`transpose_b`</b>: An optional `bool`. Defaults to `False`.
* <b>`a_is_sparse`</b>: An optional `bool`. Defaults to `False`.
* <b>`b_is_sparse`</b>: An optional `bool`. Defaults to `False`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `float32`.