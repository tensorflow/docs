page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.LinearOperatorCirculant3D

## Class `LinearOperatorCirculant3D`





Defined in [`tensorflow/python/ops/linalg/linear_operator_circulant.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/linalg/linear_operator_circulant.py).

`LinearOperator` acting like a nested block circulant matrix.

This operator acts like a block circulant matrix `A` with
shape `[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
an `N x N` matrix.  This matrix `A` is not materialized, but for
purposes of broadcasting this shape will be relevant.

#### Description in terms of block circulant matrices

If `A` is nested block circulant, with block sizes `N0, N1, N2`
(`N0 * N1 * N2 = N`):
`A` has a block structure, composed of `N0 x N0` blocks, with each
block an `N1 x N1` block circulant matrix.

For example, with `W`, `X`, `Y`, `Z` each block circulant,

```
A = |W Z Y X|
    |X W Z Y|
    |Y X W Z|
    |Z Y X W|
```

Note that `A` itself will not in general be circulant.

#### Description in terms of the frequency spectrum

There is an equivalent description in terms of the [batch] spectrum `H` and
Fourier transforms.  Here we consider `A.shape = [N, N]` and ignore batch
dimensions.

If `H.shape = [N0, N1, N2]`, (`N0 * N1 * N2 = N`):
Loosely speaking, matrix multiplication is equal to the action of a
Fourier multiplier:  `A u = IDFT3[ H DFT3[u] ]`.
Precisely speaking, given `[N, R]` matrix `u`, let `DFT3[u]` be the
`[N0, N1, N2, R]` `Tensor` defined by re-shaping `u` to `[N0, N1, N2, R]` and
taking a three dimensional DFT across the first three dimensions.  Let `IDFT3`
be the inverse of `DFT3`.  Matrix multiplication may be expressed columnwise:

```(A u)_r = IDFT3[ H * (DFT3[u])_r ]```

#### Operator properties deduced from the spectrum.

* This operator is positive definite if and only if `Real{H} > 0`.

A general property of Fourier transforms is the correspondence between
Hermitian functions and real valued transforms.

Suppose `H.shape = [B1,...,Bb, N0, N1, N2]`, we say that `H` is a Hermitian
spectrum if, with `%` meaning modulus division,

```
H[..., n0 % N0, n1 % N1, n2 % N2]
  = ComplexConjugate[ H[..., (-n0) % N0, (-n1) % N1, (-n2) % N2] ].
```

* This operator corresponds to a real matrix if and only if `H` is Hermitian.
* This operator is self-adjoint if and only if `H` is real.

See e.g. "Discrete-Time Signal Processing", Oppenheim and Schafer.

### Examples

See `LinearOperatorCirculant` and `LinearOperatorCirculant2D` for examples.

#### Performance

Suppose `operator` is a `LinearOperatorCirculant` of shape `[N, N]`,
and `x.shape = [N, R]`.  Then

* `operator.matmul(x)` is `O(R*N*Log[N])`
* `operator.solve(x)` is `O(R*N*Log[N])`
* `operator.determinant()` involves a size `N` `reduce_prod`.

If instead `operator` and `x` have shape `[B1,...,Bb, N, N]` and
`[B1,...,Bb, N, R]`, every operation increases in complexity by `B1*...*Bb`.

#### Matrix property hints

This `LinearOperator` is initialized with boolean flags of the form `is_X`,
for `X = non_singular, self_adjoint, positive_definite, square`.
These have the following meaning
* If `is_X == True`, callers should expect the operator to have the
  property `X`.  This is a promise that should be fulfilled, but is *not* a
  runtime assert.  For example, finite floating point precision may result
  in these promises being violated.
* If `is_X == False`, callers should expect the operator to not have `X`.
* If `is_X == None` (the default), callers should have no expectation either
  way.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    spectrum,
    input_output_dtype=tf.dtypes.complex64,
    is_non_singular=None,
    is_self_adjoint=None,
    is_positive_definite=None,
    is_square=True,
    name='LinearOperatorCirculant3D'
)
```

Initialize an `LinearOperatorCirculant`.

This `LinearOperator` is initialized to have shape `[B1,...,Bb, N, N]`
by providing `spectrum`, a `[B1,...,Bb, N0, N1, N2]` `Tensor`
with `N0*N1*N2 = N`.

If `input_output_dtype = DTYPE`:

* Arguments to methods such as `matmul` or `solve` must be `DTYPE`.
* Values returned by all methods, such as `matmul` or `determinant` will be
  cast to `DTYPE`.

Note that if the spectrum is not Hermitian, then this operator corresponds
to a complex matrix with non-zero imaginary part.  In this case, setting
`input_output_dtype` to a real type will forcibly cast the output to be
real, resulting in incorrect results!

If on the other hand the spectrum is Hermitian, then this operator
corresponds to a real-valued matrix, and setting `input_output_dtype` to
a real type is fine.

#### Args:

* <b>`spectrum`</b>:  Shape `[B1,...,Bb, N]` `Tensor`.  Allowed dtypes are
    `float32`, `complex64`.  Type can be different than `input_output_dtype`
* <b>`input_output_dtype`</b>: `dtype` for input/output.  Must be either
    `float32` or `complex64`.
* <b>`is_non_singular`</b>:  Expect that this operator is non-singular.
* <b>`is_self_adjoint`</b>:  Expect that this operator is equal to its hermitian
    transpose.  If `spectrum` is real, this will always be true.
* <b>`is_positive_definite`</b>:  Expect that this operator is positive definite,
    meaning the real part of all eigenvalues is positive.  We do not require
    the operator to be self-adjoint to be positive-definite.  See:
    https://en.wikipedia.org/wiki/Positive-definite_matrix
        #Extension_for_non_symmetric_matrices
* <b>`is_square`</b>:  Expect that this operator acts like square [batch] matrices.
* <b>`name`</b>:  A name to prepend to all ops created by this class.



## Properties

<h3 id="batch_shape"><code>batch_shape</code></h3>

`TensorShape` of batch dimensions of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb])`, equivalent to `A.get_shape()[:-2]`

#### Returns:

`TensorShape`, statically determined, may be undefined.

<h3 id="block_depth"><code>block_depth</code></h3>

Depth of recursively defined circulant blocks defining this `Operator`.

With `A` the dense representation of this `Operator`,

`block_depth = 1` means `A` is symmetric circulant.  For example,

```
A = |w z y x|
    |x w z y|
    |y x w z|
    |z y x w|
```

`block_depth = 2` means `A` is block symmetric circulant with symemtric
circulant blocks.  For example, with `W`, `X`, `Y`, `Z` symmetric circulant,

```
A = |W Z Y X|
    |X W Z Y|
    |Y X W Z|
    |Z Y X W|
```

`block_depth = 3` means `A` is block symmetric circulant with block
symmetric circulant blocks.

#### Returns:

Python `integer`.

<h3 id="block_shape"><code>block_shape</code></h3>



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

<h3 id="spectrum"><code>spectrum</code></h3>



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

<h3 id="assert_hermitian_spectrum"><code>assert_hermitian_spectrum</code></h3>

``` python
assert_hermitian_spectrum(name='assert_hermitian_spectrum')
```

Returns an `Op` that asserts this operator has Hermitian spectrum.

This operator corresponds to a real-valued matrix if and only if its
spectrum is Hermitian.

#### Args:

* <b>`name`</b>:  A name to give this `Op`.


#### Returns:

An `Op` that asserts this operator has Hermitian spectrum.

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

* <b>`name`</b>:  A name for this `Op`.


#### Returns:

`int32` `Tensor`

<h3 id="block_shape_tensor"><code>block_shape_tensor</code></h3>

``` python
block_shape_tensor()
```

Shape of the block dimensions of `self.spectrum`.

<h3 id="cholesky"><code>cholesky</code></h3>

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

<h3 id="convolution_kernel"><code>convolution_kernel</code></h3>

``` python
convolution_kernel(name='convolution_kernel')
```

Convolution kernel corresponding to `self.spectrum`.

The `D` dimensional DFT of this kernel is the frequency domain spectrum of
this operator.

#### Args:

* <b>`name`</b>:  A name to give this `Op`.


#### Returns:

`Tensor` with `dtype` `self.dtype`.

<h3 id="determinant"><code>determinant</code></h3>

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

* <b>`name`</b>:  A name for this `Op`.


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

* <b>`name`</b>:  A name for this `Op`.


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

* <b>`name`</b>:  A name for this `Op`.


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



