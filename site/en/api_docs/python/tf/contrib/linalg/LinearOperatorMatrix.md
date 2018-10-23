


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.linalg.LinearOperatorMatrix

### `class tf.contrib.linalg.LinearOperatorMatrix`

See the guide: [Linear Algebra (contrib) > `LinearOperator`](../../../../../api_guides/python/contrib.linalg#_LinearOperator_)

`LinearOperator` that wraps a [batch] matrix.

This operator wraps a [batch] matrix `A` (which is a `Tensor`) with shape
`[B1,...,Bb, M, N]` for some `b >= 0`.  The first `b` indices index a
batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
an `M x N` matrix.

```python
# Create a 2 x 2 linear operator.
matrix = [[1., 2.], [3., 4.]]
operator = LinearOperatorMatrix(matrix)

operator.to_dense()
==> [[1., 2.]
     [3., 4.]]

operator.shape
==> [2, 2]

operator.log_determinant()
==> scalar Tensor

x = ... Shape [2, 4] Tensor
operator.apply(x)
==> Shape [2, 4] Tensor

# Create a [2, 3] batch of 4 x 4 linear operators.
matrix = tf.random_normal(shape=[2, 3, 4, 4])
operator = LinearOperatorMatrix(matrix)
```

#### Shape compatibility

This operator acts on [batch] matrix with compatible shape.
`x` is a batch matrix with compatible shape for `apply` and `solve` if

```
operator.shape = [B1,...,Bb] + [M, N],  with b >= 0
x.shape =        [B1,...,Bb] + [N, R],  with R >= 0.
```

#### Performance

`LinearOperatorMatrix` has exactly the same performance as would be achieved
by using standard `TensorFlow` matrix ops.  Intelligent choices are made
based on the following initialization hints.

* If `dtype` is real, and `is_self_adjoint` and `is_positive_definite`, a
  Cholesky factorization is used for the determinant and solve.

In all cases, suppose `operator` is a `LinearOperatorMatrix` of shape
`[M, N]`, and `x.shape = [N, R]`.  Then

* `operator.apply(x)` is `O(M * N * R)`.
* If `M=N`, `operator.solve(x)` is `O(N^3 * R)`.
* If `M=N`, `operator.determinant()` is `O(N^3)`.

If instead `operator` and `x` have shape `[B1,...,Bb, M, N]` and
`[B1,...,Bb, N, R]`, every operation increases in complexity by `B1*...*Bb`.

#### Matrix property hints

This `LinearOperator` is initialized with boolean flags of the form `is_X`,
for `X = non_singular, self_adjoint, positive_definite`.
These have the following meaning
* If `is_X == True`, callers should expect the operator to have the
  property `X`.  This is a promise that should be fulfilled, but is *not* a
  runtime assert.  For example, finite floating point precision may result
  in these promises being violated.
* If `is_X == False`, callers should expect the operator to not have `X`.
* If `is_X == None` (the default), callers should have no expectation either
  way.

## Properties

<h3 id="batch_shape"><code>batch_shape</code></h3>

`TensorShape` of batch dimensions of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb])`, equivalent to `A.get_shape()[:-2]`

#### Returns:

  `TensorShape`, statically determined, may be undefined.

<h3 id="domain_dimension"><code>domain_dimension</code></h3>

Dimension (in the sense of vector spaces) of the domain of this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `N`.

#### Returns:

  `Dimension` object.

<h3 id="dtype"><code>dtype</code></h3>

The `DType` of `Tensor`s handled by this `LinearOperator`.

<h3 id="graph_parents"><code>graph_parents</code></h3>

List of graph dependencies of this `LinearOperator`.

<h3 id="is_non_singular"><code>is_non_singular</code></h3>



<h3 id="is_positive_definite"><code>is_positive_definite</code></h3>



<h3 id="is_self_adjoint"><code>is_self_adjoint</code></h3>



<h3 id="name"><code>name</code></h3>

Name prepended to all ops created by this `LinearOperator`.

<h3 id="range_dimension"><code>range_dimension</code></h3>

Dimension (in the sense of vector spaces) of the range of this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `M`.

#### Returns:

  `Dimension` object.

<h3 id="shape"><code>shape</code></h3>

`TensorShape` of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb, M, N])`, equivalent to `A.get_shape()`.

#### Returns:

  `TensorShape`, statically determined, may be undefined.

<h3 id="tensor_rank"><code>tensor_rank</code></h3>

Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

  Python integer, or None if the tensor rank is undefined.



## Methods

<h3 id="__init__"><code>__init__(matrix, is_non_singular=None, is_self_adjoint=None, is_positive_definite=None, name='LinearOperatorMatrix')</code></h3>

Initialize a `LinearOperatorMatrix`.

#### Args:

* <b>`matrix`</b>:  Shape `[B1,...,Bb, M, N]` with `b >= 0`, `M, N >= 0`.
    Allowed dtypes: `float32`, `float64`, `complex64`, `complex128`.
* <b>`is_non_singular`</b>:  Expect that this operator is non-singular.
* <b>`is_self_adjoint`</b>:  Expect that this operator is equal to its hermitian
    transpose.
* <b>`is_positive_definite`</b>:  Expect that this operator is positive definite,
    meaning the real part of all eigenvalues is positive.  We do not require
    the operator to be self-adjoint to be positive-definite.  See:
    https://en.wikipedia.org/wiki/Positive-definite_matrix
        #Extension_for_non_symmetric_matrices
* <b>`name`</b>: A name for this `LinearOperator`.


#### Raises:

* <b>`TypeError`</b>:  If `diag.dtype` is not an allowed type.

<h3 id="add_to_tensor"><code>add_to_tensor(x, name='add_to_tensor')</code></h3>

Add matrix represented by this operator to `x`.  Equivalent to `A + x`.

#### Args:

* <b>`x`</b>:  `Tensor` with same `dtype` and shape broadcastable to `self.shape`.
* <b>`name`</b>:  A name to give this `Op`.


#### Returns:

  A `Tensor` with broadcast shape and same `dtype` as `self`.

<h3 id="apply"><code>apply(x, adjoint=False, name='apply')</code></h3>

Transform `x` with left multiplication:  `x --> Ax`.

#### Args:

* <b>`x`</b>: `Tensor` with compatible shape and same `dtype` as `self`.
    See class docstring for definition of compatibility.
* <b>`adjoint`</b>: Python `bool`.  If `True`, left multiply by the adjoint.
* <b>`name`</b>:  A name for this `Op.


#### Returns:

  A `Tensor` with shape `[..., M, R]` and same `dtype` as `self`.

<h3 id="assert_non_singular"><code>assert_non_singular(name='assert_non_singular')</code></h3>

Returns an `Op` that asserts this operator is non singular.

<h3 id="assert_positive_definite"><code>assert_positive_definite(name='assert_positive_definite')</code></h3>

Returns an `Op` that asserts this operator is positive definite.

Here, positive definite means the real part of all eigenvalues is positive.
We do not require the operator to be self-adjoint.

#### Args:

* <b>`name`</b>:  A name to give this `Op`.


#### Returns:

  An `Op` that asserts this operator is positive definite.

<h3 id="assert_self_adjoint"><code>assert_self_adjoint(name='assert_self_adjoint')</code></h3>

Returns an `Op` that asserts this operator is self-adjoint.

<h3 id="batch_shape_dynamic"><code>batch_shape_dynamic(name='batch_shape_dynamic')</code></h3>

Shape of batch dimensions of this operator, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb]`.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

  `int32` `Tensor`

<h3 id="determinant"><code>determinant(name='det')</code></h3>

Determinant for every batch member.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

  `Tensor` with shape `self.batch_shape` and same `dtype` as `self`.

<h3 id="domain_dimension_dynamic"><code>domain_dimension_dynamic(name='domain_dimension_dynamic')</code></h3>

Dimension (in the sense of vector spaces) of the domain of this operator.

Determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `N`.

#### Args:

* <b>`name`</b>:  A name for this `Op`.


#### Returns:

  `int32` `Tensor`

<h3 id="log_abs_determinant"><code>log_abs_determinant(name='log_abs_det')</code></h3>

Log absolute value of determinant for every batch member.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

  `Tensor` with shape `self.batch_shape` and same `dtype` as `self`.

<h3 id="range_dimension_dynamic"><code>range_dimension_dynamic(name='range_dimension_dynamic')</code></h3>

Dimension (in the sense of vector spaces) of the range of this operator.

Determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `M`.

#### Args:

* <b>`name`</b>:  A name for this `Op`.


#### Returns:

  `int32` `Tensor`

<h3 id="shape_dynamic"><code>shape_dynamic(name='shape_dynamic')</code></h3>

Shape of this `LinearOperator`, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb, M, N]`, equivalent to `tf.shape(A)`.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

  `int32` `Tensor`

<h3 id="solve"><code>solve(rhs, adjoint=False, name='solve')</code></h3>

Solve `R` (batch) systems of equations exactly: `A X = rhs`.

Examples:

```python
# Create an operator acting like a 10 x 2 x 2 matrix.
operator = LinearOperator(...)
operator.shape # = 10 x 2 x 2

# Solve one linear system (R = 1) for every member of the length 10 batch.
RHS = ... # shape 10 x 2 x 1
X = operator.solve(RHS)  # shape 10 x 2 x 1

# Solve five linear systems (R = 5) for every member of the length 10 batch.
RHS = ... # shape 10 x 2 x 5
X = operator.solve(RHS)
X[3, :, 2]  # Solution to the linear system A[3, :, :] X = RHS[3, :, 2]
```

#### Args:

* <b>`rhs`</b>: `Tensor` with same `dtype` as this operator and compatible shape.
    See class docstring for definition of compatibility.
* <b>`adjoint`</b>: Python `bool`.  If `True`, solve the system involving the adjoint
    of this `LinearOperator`.
* <b>`name`</b>:  A name scope to use for ops added by this method.


#### Returns:

  `Tensor` with shape `[...,N, R]` and same `dtype` as `rhs`.


#### Raises:

* <b>`ValueError`</b>:  If self.is_non_singular is False.

<h3 id="tensor_rank_dynamic"><code>tensor_rank_dynamic(name='tensor_rank_dynamic')</code></h3>

Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

  `int32` `Tensor`, determined at runtime.

<h3 id="to_dense"><code>to_dense(name='to_dense')</code></h3>

Return a dense (batch) matrix representing this operator.





Defined in [`tensorflow/contrib/linalg/python/ops/linear_operator_matrix.py`](https://www.tensorflow.org/code/tensorflow/contrib/linalg/python/ops/linear_operator_matrix.py).

