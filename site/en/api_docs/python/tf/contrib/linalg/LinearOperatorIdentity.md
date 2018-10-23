

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.linalg.LinearOperatorIdentity

### `class tf.contrib.linalg.LinearOperatorIdentity`



Defined in [`tensorflow/contrib/linalg/python/ops/linear_operator_identity.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/linalg/python/ops/linear_operator_identity.py).

See the guide: [Linear Algebra (contrib) > `LinearOperator`](../../../../../api_guides/python/contrib.linalg#_LinearOperator_)

`LinearOperator` acting like a [batch] square identity matrix.

This operator acts like a [batch] identity matrix `A` with shape
`[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
an `N x N` matrix.  This matrix `A` is not materialized, but for
purposes of broadcasting this shape will be relevant.

`LinearOperatorIdentity` is initialized with `num_rows`, and optionally
`batch_shape`, and `dtype` arguments.  If `batch_shape` is `None`, this
operator efficiently passes through all arguments.  If `batch_shape` is
provided, broadcasting may occur, which will require making copies.

```python
# Create a 2 x 2 identity matrix.
operator = LinearOperatorIdentity(num_rows=2, dtype=tf.float32)

operator.to_dense()
==> [[1., 0.]
     [0., 1.]]

operator.shape
==> [2, 2]

operator.log_determinant()
==> 0.

x = ... Shape [2, 4] Tensor
operator.apply(x)
==> Shape [2, 4] Tensor, same as x.

y = tf.random_normal(shape=[3, 2, 4])
# Note that y.shape is compatible with operator.shape because operator.shape
# is broadcast to [3, 2, 2].
# This broadcast does NOT require copying data, since we can infer that y
# will be passed through without changing shape.  We are always able to infer
# this if the operator has no batch_shape.
x = operator.solve(y)
==> Shape [3, 2, 4] Tensor, same as y.

# Create a 2-batch of 2x2 identity matrices
operator = LinearOperatorIdentity(num_rows=2, batch_shape=[2])
operator.to_dense()
==> [[[1., 0.]
      [0., 1.]],
     [[1., 0.]
      [0., 1.]]]

# Here, even though the operator has a batch shape, the input is the same as
# the output, so x can be passed through without a copy.  The operator is able
# to detect that no broadcast is necessary because both x and the operator
# have statically defined shape.
x = ... Shape [2, 2, 3]
operator.apply(x)
==> Shape [2, 2, 3] Tensor, same as x

# Here the operator and x have different batch_shape, and are broadcast.
# This requires a copy, since the output is different size than the input.
x = ... Shape [1, 2, 3]
operator.apply(x)
==> Shape [2, 2, 3] Tensor, equal to [x, x]
```

### Shape compatibility

This operator acts on [batch] matrix with compatible shape.
`x` is a batch matrix with compatible shape for `apply` and `solve` if

```
operator.shape = [B1,...,Bb] + [N, N],  with b >= 0
x.shape =   [C1,...,Cc] + [N, R],
and [C1,...,Cc] broadcasts with [B1,...,Bb] to [D1,...,Dd]
```

### Performance

If `batch_shape` initialization arg is `None`:

* `operator.apply(x)` is `O(1)`
* `operator.solve(x)` is `O(1)`
* `operator.determinant()` is `O(1)`

If `batch_shape` initialization arg is provided, and static checks cannot
rule out the need to broadcast:

* `operator.apply(x)` is `O(D1*...*Dd*N*R)`
* `operator.solve(x)` is `O(D1*...*Dd*N*R)`
* `operator.determinant()` is `O(B1*...*Bb)`

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



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    num_rows,
    batch_shape=None,
    dtype=None,
    is_non_singular=True,
    is_self_adjoint=True,
    is_positive_definite=True,
    assert_proper_shapes=False,
    name='LinearOperatorIdentity'
)
```

Initialize a `LinearOperatorIdentity`.

The `LinearOperatorIdentity` is initialized with arguments defining `dtype`
and shape.

This operator is able to broadcast the leading (batch) dimensions, which
sometimes requires copying data.  If `batch_shape` is `None`, the operator
can take arguments of any batch shape without copying.  See examples.

#### Args:

* <b>`num_rows`</b>:  Scalar non-negative integer `Tensor`.  Number of rows in the
    corresponding identity matrix.
* <b>`batch_shape`</b>:  Optional `1-D` integer `Tensor`.  The shape of the leading
    dimensions.  If `None`, this operator has no leading dimensions.
* <b>`dtype`</b>:  Data type of the matrix that this operator represents.
* <b>`is_non_singular`</b>:  Expect that this operator is non-singular.
* <b>`is_self_adjoint`</b>:  Expect that this operator is equal to its hermitian
    transpose.
* <b>`is_positive_definite`</b>:  Expect that this operator is positive definite.
* <b>`assert_proper_shapes`</b>:  Python `bool`.  If `False`, only perform static
    checks that initialization and method arguments have proper shape.
    If `True`, and static checks are inconclusive, add asserts to the graph.
* <b>`name`</b>: A name for this `LinearOperator`


#### Raises:

* <b>`ValueError`</b>:  If `num_rows` is determined statically to be non-scalar, or
    negative.
* <b>`ValueError`</b>:  If `batch_shape` is determined statically to not be 1-D, or
    negative.
* <b>`ValueError`</b>:  If any of the following is not `True`:
    `{is_self_adjoint, is_non_singular, is_positive_definite}`.

<h3 id="add_to_tensor"><code>add_to_tensor</code></h3>

``` python
add_to_tensor(
    mat,
    name='add_to_tensor'
)
```

Add matrix represented by this operator to `mat`.  Equiv to `I + mat`.

#### Args:

* <b>`mat`</b>:  `Tensor` with same `dtype` and shape broadcastable to `self`.
* <b>`name`</b>:  A name to give this `Op`.


#### Returns:

  A `Tensor` with broadcast shape and same `dtype` as `self`.

<h3 id="apply"><code>apply</code></h3>

``` python
apply(
    x,
    adjoint=False,
    name='apply'
)
```

Transform `x` with left multiplication:  `x --> Ax`.

#### Args:

* <b>`x`</b>: `Tensor` with compatible shape and same `dtype` as `self`.
    See class docstring for definition of compatibility.
* <b>`adjoint`</b>: Python `bool`.  If `True`, left multiply by the adjoint.
* <b>`name`</b>:  A name for this `Op.


#### Returns:

  A `Tensor` with shape `[..., M, R]` and same `dtype` as `self`.

<h3 id="assert_non_singular"><code>assert_non_singular</code></h3>

``` python
assert_non_singular(name='assert_non_singular')
```

Returns an `Op` that asserts this operator is non singular.

<h3 id="assert_positive_definite"><code>assert_positive_definite</code></h3>

``` python
assert_positive_definite(name='assert_positive_definite')
```

Returns an `Op` that asserts this operator is positive definite.

Here, positive definite means the real part of all eigenvalues is positive.
We do not require the operator to be self-adjoint.

#### Args:

* <b>`name`</b>:  A name to give this `Op`.


#### Returns:

  An `Op` that asserts this operator is positive definite.

<h3 id="assert_self_adjoint"><code>assert_self_adjoint</code></h3>

``` python
assert_self_adjoint(name='assert_self_adjoint')
```

Returns an `Op` that asserts this operator is self-adjoint.

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
    name='solve'
)
```

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



