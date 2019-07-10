page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.matvec

``` python
tf.linalg.matvec(
    a,
    b,
    transpose_a=False,
    adjoint_a=False,
    a_is_sparse=False,
    b_is_sparse=False,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/math_ops.py).

Multiplies matrix `a` by vector `b`, producing `a` * `b`.

The matrix `a` must, following any transpositions, be a tensor of rank >= 2,
and we must have `shape(b) = shape(a)[:-2] + [shape(a)[-1]]`.

Both `a` and `b` must be of the same type. The supported types are:
`float16`, `float32`, `float64`, `int32`, `complex64`, `complex128`.

Matrix `a` can be transposed or adjointed (conjugated and transposed) on
the fly by setting one of the corresponding flag to `True`. These are `False`
by default.

If one or both of the inputs contain a lot of zeros, a more efficient
multiplication algorithm can be used by setting the corresponding
`a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default.
This optimization is only available for plain matrices/vectors (rank-2/1
tensors) with datatypes `bfloat16` or `float32`.

For example:

```python
# 2-D tensor `a`
# [[1, 2, 3],
#  [4, 5, 6]]
a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# 1-D tensor `b`
# [7, 9, 11]
b = tf.constant([7, 9, 11], shape=[3])

# `a` * `b`
# [ 58,  64]
c = tf.matvec(a, b)


# 3-D tensor `a`
# [[[ 1,  2,  3],
#   [ 4,  5,  6]],
#  [[ 7,  8,  9],
#   [10, 11, 12]]]
a = tf.constant(np.arange(1, 13, dtype=np.int32),
                shape=[2, 2, 3])

# 2-D tensor `b`
# [[13, 14, 15],
#  [16, 17, 18]]
b = tf.constant(np.arange(13, 19, dtype=np.int32),
                shape=[2, 3])

# `a` * `b`
# [[ 86, 212],
#  [410, 563]]
c = tf.matvec(a, b)
```

#### Args:

* <b>`a`</b>: `Tensor` of type `float16`, `float32`, `float64`, `int32`, `complex64`,
    `complex128` and rank > 1.
* <b>`b`</b>: `Tensor` with same type and rank = `rank(a) - 1`.
* <b>`transpose_a`</b>: If `True`, `a` is transposed before multiplication.
* <b>`adjoint_a`</b>: If `True`, `a` is conjugated and transposed before
    multiplication.
* <b>`a_is_sparse`</b>: If `True`, `a` is treated as a sparse matrix.
* <b>`b_is_sparse`</b>: If `True`, `b` is treated as a sparse matrix.
* <b>`name`</b>: Name for the operation (optional).


#### Returns:

A `Tensor` of the same type as `a` and `b` where each inner-most vector is
the product of the corresponding matrices in `a` and vectors in `b`, e.g. if
all transpose or adjoint attributes are `False`:

`output`[..., i] = sum_k (`a`[..., i, k] * `b`[..., k]), for all indices i.

* <b>`Note`</b>: This is matrix-vector product, not element-wise product.



#### Raises:

* <b>`ValueError`</b>: If transpose_a and adjoint_a are both set to True.