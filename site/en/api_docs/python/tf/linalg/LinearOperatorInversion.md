page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.LinearOperatorInversion


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/LinearOperatorInversion">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator_inversion.py#L30-L198">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LinearOperatorInversion`

`LinearOperator` representing the inverse of another operator.

Inherits From: [`LinearOperator`](../../tf/linalg/LinearOperator)

### Aliases:

* Class <a href="/api_docs/python/tf/linalg/LinearOperatorInversion"><code>tf.compat.v1.linalg.LinearOperatorInversion</code></a>
* Class <a href="/api_docs/python/tf/linalg/LinearOperatorInversion"><code>tf.compat.v2.linalg.LinearOperatorInversion</code></a>


<!-- Placeholder for "Used in" -->

This operator represents the inverse of another operator.

```python
# Create a 2 x 2 linear operator.
operator = LinearOperatorFullMatrix([[1., 0.], [0., 2.]])
operator_inv = LinearOperatorInversion(operator)

operator_inv.to_dense()
==> [[1., 0.]
     [0., 0.5]]

operator_inv.shape
==> [2, 2]

operator_inv.log_abs_determinant()
==> - log(2)

x = ... Shape [2, 4] Tensor
operator_inv.matmul(x)
==> Shape [2, 4] Tensor, equal to operator.solve(x)
```

#### Performance

The performance of `LinearOperatorInversion` depends on the underlying
operators performance:  `solve` and `matmul` are swapped, and determinant is
inverted.

#### Matrix property hints

This `LinearOperator` is initialized with boolean flags of the form `is_X`,
for `X = non_singular, self_adjoint, positive_definite, square`.
These have the following meaning:

* If `is_X == True`, callers should expect the operator to have the
  property `X`.  This is a promise that should be fulfilled, but is *not* a
  runtime assert.  For example, finite floating point precision may result
  in these promises being violated.
* If `is_X == False`, callers should expect the operator to not have `X`.
* If `is_X == None` (the default), callers should have no expectation either
  way.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator_inversion.py#L76-L166">View source</a>

``` python
__init__(
    operator,
    is_non_singular=None,
    is_self_adjoint=None,
    is_positive_definite=None,
    is_square=None,
    name=None
)
```

Initialize a `LinearOperatorInversion`.

`LinearOperatorInversion` is initialized with an operator `A`.  The `solve`
and `matmul` methods are effectively swapped.  E.g.

```
A = MyLinearOperator(...)
B = LinearOperatorInversion(A)
x = [....]  # a vector

assert A.matvec(x) == B.solvevec(x)
```

#### Args:


* <b>`operator`</b>: `LinearOperator` object. If `operator.is_non_singular == False`,
  an exception is raised.  We do allow `operator.is_non_singular == None`,
  in which case this operator will have `is_non_singular == None`.
  Similarly for `is_self_adjoint` and `is_positive_definite`.
* <b>`is_non_singular`</b>:  Expect that this operator is non-singular.
* <b>`is_self_adjoint`</b>:  Expect that this operator is equal to its hermitian
  transpose.
* <b>`is_positive_definite`</b>:  Expect that this operator is positive definite,
  meaning the quadratic form `x^H A x` has positive real part for all
  nonzero `x`.  Note that we do not require the operator to be
  self-adjoint to be positive-definite.  See:
  https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
* <b>`is_square`</b>:  Expect that this operator acts like square [batch] matrices.
* <b>`name`</b>: A name for this `LinearOperator`. Default is `operator.name +
  "_inv"`.


#### Raises:


* <b>`ValueError`</b>:  If `operator.is_non_singular` is False.



## Properties

<h3 id="H"><code>H</code></h3>

Returns the adjoint of the current `LinearOperator`.

Given `A` representing this `LinearOperator`, return `A*`.
Note that calling `self.adjoint()` and `self.H` are equivalent.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`LinearOperator` which represents the adjoint of this `LinearOperator`.


<h3 id="batch_shape"><code>batch_shape</code></h3>

`TensorShape` of batch dimensions of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb])`, equivalent to `A.shape[:-2]`

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




<h3 id="is_square"><code>is_square</code></h3>

Return `True/False` depending on if this operator is square.


<h3 id="operator"><code>operator</code></h3>

The operator before inversion.


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
`TensorShape([B1,...,Bb, M, N])`, equivalent to `A.shape`.

#### Returns:

`TensorShape`, statically determined, may be undefined.


<h3 id="tensor_rank"><code>tensor_rank</code></h3>

Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

Python integer, or None if the tensor rank is undefined.




## Methods

<h3 id="add_to_tensor"><code>add_to_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L1014-L1027">View source</a>

``` python
add_to_tensor(
    x,
    name='add_to_tensor'
)
```

Add matrix represented by this operator to `x`.  Equivalent to `A + x`.


#### Args:


* <b>`x`</b>:  `Tensor` with same `dtype` and shape broadcastable to `self.shape`.
* <b>`name`</b>:  A name to give this `Op`.


#### Returns:

A `Tensor` with broadcast shape and same `dtype` as `self`.


<h3 id="adjoint"><code>adjoint</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L870-L885">View source</a>

``` python
adjoint(name='adjoint')
```

Returns the adjoint of the current `LinearOperator`.

Given `A` representing this `LinearOperator`, return `A*`.
Note that calling `self.adjoint()` and `self.H` are equivalent.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`LinearOperator` which represents the adjoint of this `LinearOperator`.


<h3 id="assert_non_singular"><code>assert_non_singular</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L485-L503">View source</a>

``` python
assert_non_singular(name='assert_non_singular')
```

Returns an `Op` that asserts this operator is non singular.

This operator is considered non-singular if

```
ConditionNumber < max{100, range_dimension, domain_dimension} * eps,
eps := np.finfo(self.dtype.as_numpy_dtype).eps
```

#### Args:


* <b>`name`</b>:  A string name to prepend to created ops.


#### Returns:

An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
  the operator is singular.


<h3 id="assert_positive_definite"><code>assert_positive_definite</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L521-L536">View source</a>

``` python
assert_positive_definite(name='assert_positive_definite')
```

Returns an `Op` that asserts this operator is positive definite.

Here, positive definite means that the quadratic form `x^H A x` has positive
real part for all nonzero `x`.  Note that we do not require the operator to
be self-adjoint to be positive definite.

#### Args:


* <b>`name`</b>:  A name to give this `Op`.


#### Returns:

An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
  the operator is not positive definite.


<h3 id="assert_self_adjoint"><code>assert_self_adjoint</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L548-L562">View source</a>

``` python
assert_self_adjoint(name='assert_self_adjoint')
```

Returns an `Op` that asserts this operator is self-adjoint.

Here we check that this operator is *exactly* equal to its hermitian
transpose.

#### Args:


* <b>`name`</b>:  A string name to prepend to created ops.


#### Returns:

An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
  the operator is not self-adjoint.


<h3 id="batch_shape_tensor"><code>batch_shape_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L319-L339">View source</a>

``` python
batch_shape_tensor(name='batch_shape_tensor')
```

Shape of batch dimensions of this operator, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb]`.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`int32` `Tensor`


<h3 id="cholesky"><code>cholesky</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L915-L938">View source</a>

``` python
cholesky(name='cholesky')
```

Returns a Cholesky factor as a `LinearOperator`.

Given `A` representing this `LinearOperator`, if `A` is positive definite
self-adjoint, return `L`, where `A = L L^T`, i.e. the cholesky
decomposition.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`LinearOperator` which represents the lower triangular matrix
in the Cholesky decomposition.



#### Raises:


* <b>`ValueError`</b>: When the `LinearOperator` is not hinted to be positive
  definite and self adjoint.

<h3 id="determinant"><code>determinant</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L678-L695">View source</a>

``` python
determinant(name='det')
```

Determinant for every batch member.


#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`Tensor` with shape `self.batch_shape` and same `dtype` as `self`.



#### Raises:


* <b>`NotImplementedError`</b>:  If `self.is_square` is `False`.

<h3 id="diag_part"><code>diag_part</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L965-L991">View source</a>

``` python
diag_part(name='diag_part')
```

Efficiently get the [batch] diagonal part of this operator.

If this operator has shape `[B1,...,Bb, M, N]`, this returns a
`Tensor` `diagonal`, of shape `[B1,...,Bb, min(M, N)]`, where
`diagonal[b1,...,bb, i] = self.to_dense()[b1,...,bb, i, i]`.

```
my_operator = LinearOperatorDiag([1., 2.])

# Efficiently get the diagonal
my_operator.diag_part()
==> [1., 2.]

# Equivalent, but inefficient method
tf.linalg.diag_part(my_operator.to_dense())
==> [1., 2.]
```

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:


* <b>`diag_part`</b>:  A `Tensor` of same `dtype` as self.

<h3 id="domain_dimension_tensor"><code>domain_dimension_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L394-L415">View source</a>

``` python
domain_dimension_tensor(name='domain_dimension_tensor')
```

Dimension (in the sense of vector spaces) of the domain of this operator.

Determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `N`.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`int32` `Tensor`


<h3 id="inverse"><code>inverse</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L890-L913">View source</a>

``` python
inverse(name='inverse')
```

Returns the Inverse of this `LinearOperator`.

Given `A` representing this `LinearOperator`, return a `LinearOperator`
representing `A^-1`.

#### Args:


* <b>`name`</b>: A name scope to use for ops added by this method.


#### Returns:

`LinearOperator` representing inverse of this matrix.



#### Raises:


* <b>`ValueError`</b>: When the `LinearOperator` is not hinted to be `non_singular`.

<h3 id="log_abs_determinant"><code>log_abs_determinant</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L707-L724">View source</a>

``` python
log_abs_determinant(name='log_abs_det')
```

Log absolute value of determinant for every batch member.


#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`Tensor` with shape `self.batch_shape` and same `dtype` as `self`.



#### Raises:


* <b>`NotImplementedError`</b>:  If `self.is_square` is `False`.

<h3 id="matmul"><code>matmul</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L575-L628">View source</a>

``` python
matmul(
    x,
    adjoint=False,
    adjoint_arg=False,
    name='matmul'
)
```

Transform [batch] matrix `x` with left multiplication:  `x --> Ax`.

```python
# Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)
operator.shape = [..., M, N]

X = ... # shape [..., N, R], batch matrix, R > 0.

Y = operator.matmul(X)
Y.shape
==> [..., M, R]

Y[..., :, r] = sum_j A[..., :, j] X[j, r]
```

#### Args:


* <b>`x`</b>: `LinearOperator` or `Tensor` with compatible shape and same `dtype` as
  `self`. See class docstring for definition of compatibility.
* <b>`adjoint`</b>: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
* <b>`adjoint_arg`</b>:  Python `bool`.  If `True`, compute `A x^H` where `x^H` is
  the hermitian transpose (transposition and complex conjugation).
* <b>`name`</b>:  A name for this `Op`.


#### Returns:

A `LinearOperator` or `Tensor` with shape `[..., M, R]` and same `dtype`
  as `self`.


<h3 id="matvec"><code>matvec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L635-L668">View source</a>

``` python
matvec(
    x,
    adjoint=False,
    name='matvec'
)
```

Transform [batch] vector `x` with left multiplication:  `x --> Ax`.

```python
# Make an operator acting like batch matric A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)

X = ... # shape [..., N], batch vector

Y = operator.matvec(X)
Y.shape
==> [..., M]

Y[..., :] = sum_j A[..., :, j] X[..., j]
```

#### Args:


* <b>`x`</b>: `Tensor` with compatible shape and same `dtype` as `self`.
  `x` is treated as a [batch] vector meaning for every set of leading
  dimensions, the last dimension defines a vector.
  See class docstring for definition of compatibility.
* <b>`adjoint`</b>: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
* <b>`name`</b>:  A name for this `Op`.


#### Returns:

A `Tensor` with shape `[..., M]` and same `dtype` as `self`.


<h3 id="range_dimension_tensor"><code>range_dimension_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L433-L454">View source</a>

``` python
range_dimension_tensor(name='range_dimension_tensor')
```

Dimension (in the sense of vector spaces) of the range of this operator.

Determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `M`.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`int32` `Tensor`


<h3 id="shape_tensor"><code>shape_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L285-L303">View source</a>

``` python
shape_tensor(name='shape_tensor')
```

Shape of this `LinearOperator`, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb, M, N]`, equivalent to <a href="../../tf/shape"><code>tf.shape(A)</code></a>.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`int32` `Tensor`


<h3 id="solve"><code>solve</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L741-L814">View source</a>

``` python
solve(
    rhs,
    adjoint=False,
    adjoint_arg=False,
    name='solve'
)
```

Solve (exact or approx) `R` (batch) systems of equations: `A X = rhs`.

The returned `Tensor` will be close to an exact solution if `A` is well
conditioned. Otherwise closeness will vary. See class docstring for details.

#### Examples:



```python
# Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)
operator.shape = [..., M, N]

# Solve R > 0 linear systems for every member of the batch.
RHS = ... # shape [..., M, R]

X = operator.solve(RHS)
# X[..., :, r] is the solution to the r'th linear system
# sum_j A[..., :, j] X[..., j, r] = RHS[..., :, r]

operator.matmul(X)
==> RHS
```

#### Args:


* <b>`rhs`</b>: `Tensor` with same `dtype` as this operator and compatible shape.
  `rhs` is treated like a [batch] matrix meaning for every set of leading
  dimensions, the last two dimensions defines a matrix.
  See class docstring for definition of compatibility.
* <b>`adjoint`</b>: Python `bool`.  If `True`, solve the system involving the adjoint
  of this `LinearOperator`:  `A^H X = rhs`.
* <b>`adjoint_arg`</b>:  Python `bool`.  If `True`, solve `A X = rhs^H` where `rhs^H`
  is the hermitian transpose (transposition and complex conjugation).
* <b>`name`</b>:  A name scope to use for ops added by this method.


#### Returns:

`Tensor` with shape `[...,N, R]` and same `dtype` as `rhs`.



#### Raises:


* <b>`NotImplementedError`</b>:  If `self.is_non_singular` or `is_square` is False.

<h3 id="solvevec"><code>solvevec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L822-L868">View source</a>

``` python
solvevec(
    rhs,
    adjoint=False,
    name='solve'
)
```

Solve single equation with best effort: `A X = rhs`.

The returned `Tensor` will be close to an exact solution if `A` is well
conditioned. Otherwise closeness will vary. See class docstring for details.

#### Examples:



```python
# Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)
operator.shape = [..., M, N]

# Solve one linear system for every member of the batch.
RHS = ... # shape [..., M]

X = operator.solvevec(RHS)
# X is the solution to the linear system
# sum_j A[..., :, j] X[..., j] = RHS[..., :]

operator.matvec(X)
==> RHS
```

#### Args:


* <b>`rhs`</b>: `Tensor` with same `dtype` as this operator.
  `rhs` is treated like a [batch] vector meaning for every set of leading
  dimensions, the last dimension defines a vector.  See class docstring
  for definition of compatibility regarding batch dimensions.
* <b>`adjoint`</b>: Python `bool`.  If `True`, solve the system involving the adjoint
  of this `LinearOperator`:  `A^H X = rhs`.
* <b>`name`</b>:  A name scope to use for ops added by this method.


#### Returns:

`Tensor` with shape `[...,N]` and same `dtype` as `rhs`.



#### Raises:


* <b>`NotImplementedError`</b>:  If `self.is_non_singular` or `is_square` is False.

<h3 id="tensor_rank_tensor"><code>tensor_rank_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L358-L376">View source</a>

``` python
tensor_rank_tensor(name='tensor_rank_tensor')
```

Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`int32` `Tensor`, determined at runtime.


<h3 id="to_dense"><code>to_dense</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L956-L959">View source</a>

``` python
to_dense(name='to_dense')
```

Return a dense (batch) matrix representing this operator.


<h3 id="trace"><code>trace</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linear_operator.py#L996-L1008">View source</a>

``` python
trace(name='trace')
```

Trace of the linear operator, equal to sum of `self.diag_part()`.

If the operator is square, this is also the sum of the eigenvalues.

#### Args:


* <b>`name`</b>:  A name for this `Op`.


#### Returns:

Shape `[B1,...,Bb]` `Tensor` of same `dtype` as `self`.
