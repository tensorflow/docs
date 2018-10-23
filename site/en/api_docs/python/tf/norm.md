

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.norm

### Aliases:

* `tf.linalg.norm`
* `tf.norm`

``` python
norm(
    tensor,
    ord='euclidean',
    axis=None,
    keepdims=None,
    name=None,
    keep_dims=None
)
```



Defined in [`tensorflow/python/ops/linalg_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/linalg_ops.py).

See the guide: [Math > Matrix Math Functions](../../../api_guides/python/math_ops#Matrix_Math_Functions)

Computes the norm of vectors, matrices, and tensors. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

This function can compute several different vector norms (the 1-norm, the
Euclidean or 2-norm, the inf-norm, and in general the p-norm for p > 0) and
matrix norms (Frobenius, 1-norm, and inf-norm).

#### Args:

* <b>`tensor`</b>: `Tensor` of types `float32`, `float64`, `complex64`, `complex128`
* <b>`ord`</b>: Order of the norm. Supported values are 'fro', 'euclidean',
    `1`, `2`, `np.inf` and any positive real number yielding the corresponding
    p-norm. Default is 'euclidean' which is equivalent to Frobenius norm if
    `tensor` is a matrix and equivalent to 2-norm for vectors.
    Some restrictions apply:
      a) The Frobenius norm `fro` is not defined for vectors,
      b) If axis is a 2-tuple (matrix norm), only 'euclidean', 'fro', `1`,
         `np.inf` are supported.
    See the description of `axis` on how to compute norms for a batch of
    vectors or matrices stored in a tensor.
* <b>`axis`</b>: If `axis` is `None` (the default), the input is considered a vector
    and a single vector norm is computed over the entire set of values in the
    tensor, i.e. `norm(tensor, ord=ord)` is equivalent to
    `norm(reshape(tensor, [-1]), ord=ord)`.
    If `axis` is a Python integer, the input is considered a batch of vectors,
    and `axis` determines the axis in `tensor` over which to compute vector
    norms.
    If `axis` is a 2-tuple of Python integers it is considered a batch of
    matrices and `axis` determines the axes in `tensor` over which to compute
    a matrix norm.
    Negative indices are supported. Example: If you are passing a tensor that
    can be either a matrix or a batch of matrices at runtime, pass
    `axis=[-2,-1]` instead of `axis=None` to make sure that matrix norms are
    computed.
* <b>`keepdims`</b>: If True, the axis indicated in `axis` are kept with size 1.
    Otherwise, the dimensions in `axis` are removed from the output shape.
* <b>`name`</b>: The name of the op.
* <b>`keep_dims`</b>: Deprecated alias for `keepdims`.


#### Returns:

* <b>`output`</b>: A `Tensor` of the same type as tensor, containing the vector or
    matrix norms. If `keepdims` is True then the rank of output is equal to
    the rank of `tensor`. Otherwise, if `axis` is none the output is a scalar,
    if `axis` is an integer, the rank of `output` is one less than the rank
    of `tensor`, if `axis` is a 2-tuple the rank of `output` is two less
    than the rank of `tensor`.


#### Raises:

* <b>`ValueError`</b>: If `ord` or `axis` is invalid.



#### Numpy Compatibility
Mostly equivalent to numpy.linalg.norm.
Not supported: ord <= 0, 2-norm for matrices, nuclear norm.
Other differences:
  a) If axis is `None`, treats the flattened `tensor` as a vector
   regardless of rank.
  b) Explicitly supports 'euclidean' norm as the default, including for
   higher order tensors.

