

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.linalg.LinearOperatorLowRankUpdate

## Class `LinearOperatorLowRankUpdate`

Inherits From: [`LinearOperator`](../../tf/linalg/LinearOperator)

### Aliases:

* Class `tf.contrib.linalg.LinearOperatorLowRankUpdate`
* Class `tf.linalg.LinearOperatorLowRankUpdate`



Defined in [`tensorflow/python/ops/linalg/linear_operator_low_rank_update.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py).

See the guide: [Linear Algebra (contrib) > `LinearOperator`](../../../../api_guides/python/contrib.linalg#_LinearOperator_)

Perturb a `LinearOperator` with a rank `K` update.

This operator acts like a [batch] matrix `A` with shape
`[B1,...,Bb, M, N]` for some `b >= 0`.  The first `b` indices index a
batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
an `M x N` matrix.

`LinearOperatorLowRankUpdate` represents `A = L + U D V^H`, where

```
L, is a LinearOperator representing [batch] M x N matrices
U, is a [batch] M x K matrix.  Typically K << M.
D, is a [batch] K x K matrix.
V, is a [batch] N x K matrix.  Typically K << N.
V^H is the Hermitian transpose (adjoint) of V.
```

If `M = N`, determinants and solves are done using the matrix determinant
lemma and Woodbury identities, and thus require L and D to be non-singular.

Solves and determinants will be attempted unless the "is_non_singular"
property of L and D is False.

In the event that L and D are positive-definite, and U = V, solves and
determinants can be done using a Cholesky factorization.

```python
# Create a 3 x 3 diagonal linear operator.
diag_operator = LinearOperatorDiag(
    diag_update=[1., 2., 3.], is_non_singular=True, is_self_adjoint=True,
    is_positive_definite=True)

# Perturb with a rank 2 perturbation
operator = LinearOperatorLowRankUpdate(
    operator=diag_operator,
    u=[[1., 2.], [-1., 3.], [0., 0.]],
    diag_update=[11., 12.],
    v=[[1., 2.], [-1., 3.], [10., 10.]])

operator.shape
==> [3, 3]

operator.log_abs_determinant()
==> scalar Tensor

x = ... Shape [3, 4] Tensor
operator.matmul(x)
==> Shape [3, 4] Tensor
```

### Shape compatibility

This operator acts on [batch] matrix with compatible shape.
`x` is a batch matrix with compatible shape for `matmul` and `solve` if

```
operator.shape = [B1,...,Bb] + [M, N],  with b >= 0
x.shape =        [B1,...,Bb] + [N, R],  with R >= 0.
```

### Performance

Suppose `operator` is a `LinearOperatorLowRankUpdate` of shape `[M, N]`,
made from a rank `K` update of `base_operator` which performs `.matmul(x)` on
`x` having `x.shape = [N, R]` with `O(L_matmul*N*R)` complexity (and similarly
for `solve`, `determinant`.  Then, if `x.shape = [N, R]`,

* `operator.matmul(x)` is `O(L_matmul*N*R + K*N*R)`

and if `M = N`,

* `operator.solve(x)` is `O(L_matmul*N*R + N*K*R + K^2*R + K^3)`
* `operator.determinant()` is `O(L_determinant + L_solve*N*K + K^2*N + K^3)`

If instead `operator` and `x` have shape `[B1,...,Bb, M, N]` and
`[B1,...,Bb, N, R]`, every operation increases in complexity by `B1*...*Bb`.

#### Matrix property hints

This `LinearOperator` is initialized with boolean flags of the form `is_X`,
for `X = non_singular`, `self_adjoint`, `positive_definite`,
`diag_update_positive` and `square`. These have the following meaning:

* If `is_X == True`, callers should expect the operator to have the
  property `X`.  This is a promise that should be fulfilled, but is *not* a
  runtime assert.  For example, finite floating point precision may result
  in these promises being violated.
* If `is_X == False`, callers should expect the operator to not have `X`.
* If `is_X == None` (the default), callers should have no expectation either
  way.

## Properties

<h3 id="base_operator"><code>base_operator</code></h3>

If this operator is `A = L + U D V^H`, this is the `L`.

<h3 id="batch_shape"><code>batch_shape</code></h3>

`TensorShape` of batch dimensions of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb])`, equivalent to `A.get_shape()[:-2]`

#### Returns:

`TensorShape`, statically determined, may be undefined.

<h3 id="diag_operator"><code>diag_operator</code></h3>

If this operator is `A = L + U D V^H`, this is `D`.

<h3 id="diag_update"><code>diag_update</code></h3>

If this operator is `A = L + U D V^H`, this is the diagonal of `D`.

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

<h3 id="is_diag_update_positive"><code>is_diag_update_positive</code></h3>

If this operator is `A = L + U D V^H`, this hints `D > 0` elementwise.

<h3 id="is_non_singular"><code>is_non_singular</code></h3>



<h3 id="is_positive_definite"><code>is_positive_definite</code></h3>



<h3 id="is_self_adjoint"><code>is_self_adjoint</code></h3>



<h3 id="is_square"><code>is_square</code></h3>

Return `True/False` depending on if this operator is square.

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

<h3 id="u"><code>u</code></h3>

If this operator is `A = L + U D V^H`, this is the `U`.

<h3 id="v"><code>v</code></h3>

If this operator is `A = L + U D V^H`, this is the `V`.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    base_operator,
    u,
    diag_update=None,
    v=None,
    is_diag_update_positive=None,
    is_non_singular=None,
    is_self_adjoint=None,
    is_positive_definite=None,
    is_square=None,
    name='LinearOperatorLowRankUpdate'
)
```

Initialize a `LinearOperatorLowRankUpdate`.

This creates a `LinearOperator` of the form `A = L + U D V^H`, with
`L` a `LinearOperator`, `U, V` both [batch] matrices, and `D` a [batch]
diagonal matrix.

If `L` is non-singular, solves and determinants are available.
Solves/determinants both involve a solve/determinant of a `K x K` system.
In the event that L and D are self-adjoint positive-definite, and U = V,
this can be done using a Cholesky factorization.  The user should set the
`is_X` matrix property hints, which will trigger the appropriate code path.

#### Args:

* <b>`base_operator`</b>:  Shape `[B1,...,Bb, M, N]` real `float16`, `float32` or
    `float64` `LinearOperator`.  This is `L` above.
* <b>`u`</b>:  Shape `[B1,...,Bb, M, K]` `Tensor` of same `dtype` as `base_operator`.
    This is `U` above.
* <b>`diag_update`</b>:  Optional shape `[B1,...,Bb, K]` `Tensor` with same `dtype`
    as `base_operator`.  This is the diagonal of `D` above.
     Defaults to `D` being the identity operator.
* <b>`v`</b>:  Optional `Tensor` of same `dtype` as `u` and shape `[B1,...,Bb, N, K]`
     Defaults to `v = u`, in which case the perturbation is symmetric.
     If `M != N`, then `v` must be set since the perturbation is not square.
* <b>`is_diag_update_positive`</b>:  Python `bool`.
    If `True`, expect `diag_update > 0`.
* <b>`is_non_singular`</b>:  Expect that this operator is non-singular.
    Default is `None`, unless `is_positive_definite` is auto-set to be
    `True` (see below).
* <b>`is_self_adjoint`</b>:  Expect that this operator is equal to its hermitian
    transpose.  Default is `None`, unless `base_operator` is self-adjoint
    and `v = None` (meaning `u=v`), in which case this defaults to `True`.
* <b>`is_positive_definite`</b>:  Expect that this operator is positive definite.
    Default is `None`, unless `base_operator` is positive-definite
    `v = None` (meaning `u=v`), and `is_diag_update_positive`, in which case
    this defaults to `True`.
    Note that we say an operator is positive definite when the quadratic
    form `x^H A x` has positive real part for all nonzero `x`.
* <b>`is_square`</b>:  Expect that this operator acts like square [batch] matrices.
* <b>`name`</b>: A name for this `LinearOperator`.


#### Raises:

* <b>`ValueError`</b>:  If `is_X` flags are set in an inconsistent way.

<h3 id="add_to_tensor"><code>add_to_tensor</code></h3>

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

<h3 id="assert_non_singular"><code>assert_non_singular</code></h3>

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

``` python
batch_shape_tensor(name='batch_shape_tensor')
```

Shape of batch dimensions of this operator, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb]`.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

`int32` `Tensor`

<h3 id="determinant"><code>determinant</code></h3>

``` python
determinant(name='det')
```

Determinant for every batch member.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

`Tensor` with shape `self.batch_shape` and same `dtype` as `self`.


#### Raises:

* <b>`NotImplementedError`</b>:  If `self.is_square` is `False`.

<h3 id="diag_part"><code>diag_part</code></h3>

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
tf.matrix_diag_part(my_operator.to_dense())
==> [1., 2.]
```

#### Args:

* <b>`name`</b>:  A name for this `Op`.


#### Returns:

* <b>`diag_part`</b>:  A `Tensor` of same `dtype` as self.

<h3 id="domain_dimension_tensor"><code>domain_dimension_tensor</code></h3>

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

<h3 id="log_abs_determinant"><code>log_abs_determinant</code></h3>

``` python
log_abs_determinant(name='log_abs_det')
```

Log absolute value of determinant for every batch member.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

`Tensor` with shape `self.batch_shape` and same `dtype` as `self`.


#### Raises:

* <b>`NotImplementedError`</b>:  If `self.is_square` is `False`.

<h3 id="matmul"><code>matmul</code></h3>

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

* <b>`x`</b>: `Tensor` with compatible shape and same `dtype` as `self`.
    See class docstring for definition of compatibility.
* <b>`adjoint`</b>: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
* <b>`adjoint_arg`</b>:  Python `bool`.  If `True`, compute `A x^H` where `x^H` is
    the hermitian transpose (transposition and complex conjugation).
* <b>`name`</b>:  A name for this `Op.


#### Returns:

A `Tensor` with shape `[..., M, R]` and same `dtype` as `self`.

<h3 id="matvec"><code>matvec</code></h3>

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
* <b>`name`</b>:  A name for this `Op.


#### Returns:

A `Tensor` with shape `[..., M]` and same `dtype` as `self`.

<h3 id="range_dimension_tensor"><code>range_dimension_tensor</code></h3>

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

``` python
shape_tensor(name='shape_tensor')
```

Shape of this `LinearOperator`, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb, M, N]`, equivalent to `tf.shape(A)`.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

`int32` `Tensor`

<h3 id="solve"><code>solve</code></h3>

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

Examples:

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

Examples:

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

``` python
tensor_rank_tensor(name='tensor_rank_tensor')
```

Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.

#### Args:

* <b>`name`</b>:  A name for this `Op.


#### Returns:

`int32` `Tensor`, determined at runtime.

<h3 id="to_dense"><code>to_dense</code></h3>

``` python
to_dense(name='to_dense')
```

Return a dense (batch) matrix representing this operator.

<h3 id="trace"><code>trace</code></h3>

``` python
trace(name='trace')
```

Trace of the linear operator, equal to sum of `self.diag_part()`.

If the operator is square, this is also the sum of the eigenvalues.

#### Args:

* <b>`name`</b>:  A name for this `Op`.


#### Returns:

Shape `[B1,...,Bb]` `Tensor` of same `dtype` as `self`.



