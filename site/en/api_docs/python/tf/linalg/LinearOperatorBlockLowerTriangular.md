description: Combines LinearOperators into a blockwise lower-triangular matrix.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.LinearOperatorBlockLowerTriangular" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__matmul__"/>
<meta itemprop="property" content="add_to_tensor"/>
<meta itemprop="property" content="adjoint"/>
<meta itemprop="property" content="assert_non_singular"/>
<meta itemprop="property" content="assert_positive_definite"/>
<meta itemprop="property" content="assert_self_adjoint"/>
<meta itemprop="property" content="batch_shape_tensor"/>
<meta itemprop="property" content="cholesky"/>
<meta itemprop="property" content="cond"/>
<meta itemprop="property" content="determinant"/>
<meta itemprop="property" content="diag_part"/>
<meta itemprop="property" content="domain_dimension_tensor"/>
<meta itemprop="property" content="eigvals"/>
<meta itemprop="property" content="inverse"/>
<meta itemprop="property" content="log_abs_determinant"/>
<meta itemprop="property" content="matmul"/>
<meta itemprop="property" content="matvec"/>
<meta itemprop="property" content="range_dimension_tensor"/>
<meta itemprop="property" content="shape_tensor"/>
<meta itemprop="property" content="solve"/>
<meta itemprop="property" content="solvevec"/>
<meta itemprop="property" content="tensor_rank_tensor"/>
<meta itemprop="property" content="to_dense"/>
<meta itemprop="property" content="trace"/>
</div>

# tf.linalg.LinearOperatorBlockLowerTriangular

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py#L39-L875">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Combines `LinearOperators` into a blockwise lower-triangular matrix.

Inherits From: [`LinearOperator`](../../tf/linalg/LinearOperator.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.LinearOperatorBlockLowerTriangular`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.LinearOperatorBlockLowerTriangular(
    operators, is_non_singular=None, is_self_adjoint=None,
    is_positive_definite=None, is_square=None,
    name='LinearOperatorBlockLowerTriangular'
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operator is initialized with a nested list of linear operators, which
are combined into a new `LinearOperator` whose underlying matrix
representation is square and has each operator on or below the main diagonal,
and zero's elsewhere. Each element of the outer list is a list of
`LinearOperators` corresponding to a row-partition of the blockwise structure.
The number of `LinearOperator`s in row-partion `i` must be equal to `i`.

For example, a blockwise `3 x 3` `LinearOperatorBlockLowerTriangular` is
initialized with the list `[[op_00], [op_10, op_11], [op_20, op_21, op_22]]`,
where the `op_ij`, `i < 3, j <= i`, are `LinearOperator` instances. The
`LinearOperatorBlockLowerTriangular` behaves as the following blockwise
matrix, where `0` represents appropriately-sized [batch] matrices of zeros:

```none
[[op_00,     0,     0],
 [op_10, op_11,     0],
 [op_20, op_21, op_22]]
```

Each `op_jj` on the diagonal is required to represent a square matrix, and
hence will have shape `batch_shape_j + [M_j, M_j]`. `LinearOperator`s in row
`j` of the blockwise structure must have `range_dimension` equal to that of
`op_jj`, and `LinearOperators` in column `j` must have `domain_dimension`
equal to that of `op_jj`.

If each `op_jj` on the diagonal has shape `batch_shape_j + [M_j, M_j]`, then
the combined operator has shape `broadcast_batch_shape + [sum M_j, sum M_j]`,
where `broadcast_batch_shape` is the mutual broadcast of `batch_shape_j`,
`j = 0, 1, ..., J`, assuming the intermediate batch shapes broadcast.
Even if the combined shape is well defined, the combined operator's
methods may fail due to lack of broadcasting ability in the defining
operators' methods.

For example, to create a 4 x 4 linear operator combined of three 2 x 2
operators:
>>> operator_0 = tf.linalg.LinearOperatorFullMatrix([[1., 2.], [3., 4.]])
>>> operator_1 = tf.linalg.LinearOperatorFullMatrix([[1., 0.], [0., 1.]])
>>> operator_2 = tf.linalg.LinearOperatorLowerTriangular([[5., 6.], [7., 8]])
>>> operator = LinearOperatorBlockLowerTriangular(
...   [[operator_0], [operator_1, operator_2]])

```
>>> operator.to_dense()
<tf.Tensor: shape=(4, 4), dtype=float32, numpy=
array([[1., 2., 0., 0.],
       [3., 4., 0., 0.],
       [1., 0., 5., 0.],
       [0., 1., 7., 8.]], dtype=float32)>
```

```
>>> operator.shape
TensorShape([4, 4])
```

```
>>> operator.log_abs_determinant()
<tf.Tensor: shape=(), dtype=float32, numpy=4.3820267>
```

```
>>> x0 = [[1., 6.], [-3., 4.]]
>>> x1 = [[0., 2.], [4., 0.]]
>>> x = tf.concat([x0, x1], 0)  # Shape [2, 4] Tensor
>>> operator.matmul(x)
<tf.Tensor: shape=(4, 2), dtype=float32, numpy=
array([[-5., 14.],
       [-9., 34.],
       [ 1., 16.],
       [29., 18.]], dtype=float32)>
```

The above `matmul` is equivalent to:
>>> tf.concat([operator_0.matmul(x0),
...   operator_1.matmul(x0) + operator_2.matmul(x1)], axis=0)
<tf.Tensor: shape=(4, 2), dtype=float32, numpy=
array([[-5., 14.],
       [-9., 34.],
       [ 1., 16.],
       [29., 18.]], dtype=float32)>

#### Shape compatibility

This operator acts on [batch] matrix with compatible shape.
`x` is a batch matrix with compatible shape for `matmul` and `solve` if

```
operator.shape = [B1,...,Bb] + [M, N],  with b >= 0
x.shape =        [B1,...,Bb] + [N, R],  with R >= 0.
```

#### For example:



Create a [2, 3] batch of 4 x 4 linear operators:
>>> matrix_44 = tf.random.normal(shape=[2, 3, 4, 4])
>>> operator_44 = tf.linalg.LinearOperatorFullMatrix(matrix_44)

Create a [1, 3] batch of 5 x 4 linear operators:
>>> matrix_54 = tf.random.normal(shape=[1, 3, 5, 4])
>>> operator_54 = tf.linalg.LinearOperatorFullMatrix(matrix_54)

Create a [1, 3] batch of 5 x 5 linear operators:
>>> matrix_55 = tf.random.normal(shape=[1, 3, 5, 5])
>>> operator_55 = tf.linalg.LinearOperatorFullMatrix(matrix_55)

Combine to create a [2, 3] batch of 9 x 9 operators:
>>> operator_99 = LinearOperatorBlockLowerTriangular(
...   [[operator_44], [operator_54, operator_55]])
>>> operator_99.shape
TensorShape([2, 3, 9, 9])

Create a shape [2, 1, 9] batch of vectors and apply the operator to it.
>>> x = tf.random.normal(shape=[2, 1, 9])
>>> y = operator_99.matvec(x)
>>> y.shape
TensorShape([2, 3, 9])

Create a blockwise list of vectors and apply the operator to it. A blockwise
list is returned.
>>> x4 = tf.random.normal(shape=[2, 1, 4])
>>> x5 = tf.random.normal(shape=[2, 3, 5])
>>> y_blockwise = operator_99.matvec([x4, x5])
>>> y_blockwise[0].shape
TensorShape([2, 3, 4])
>>> y_blockwise[1].shape
TensorShape([2, 3, 5])

#### Performance

Suppose `operator` is a `LinearOperatorBlockLowerTriangular` consisting of `D`
row-partitions and `D` column-partitions, such that the total number of
operators is `N = D * (D + 1) // 2`.

* `operator.matmul` has complexity equal to the sum of the `matmul`
  complexities of the individual operators.
* `operator.solve` has complexity equal to the sum of the `solve` complexities
  of the operators on the diagonal and the `matmul` complexities of the
  operators off the diagonal.
* `operator.determinant` has complexity equal to the sum of the `determinant`
  complexities of the operators on the diagonal.

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`operators`
</td>
<td>
Iterable of iterables of `LinearOperator` objects, each with
the same `dtype`. Each element of `operators` corresponds to a row-
partition, in top-to-bottom order. The operators in each row-partition
are filled in left-to-right. For example,
`operators = [[op_0], [op_1, op_2], [op_3, op_4, op_5]]` creates a
`LinearOperatorBlockLowerTriangular` with full block structure
`[[op_0, 0, 0], [op_1, op_2, 0], [op_3, op_4, op_5]]`. The number of
operators in the `i`th row must be equal to `i`, such that each operator
falls on or below the diagonal of the blockwise structure.
`LinearOperator`s that fall on the diagonal (the last elements of each
row) must be square. The other `LinearOperator`s must have domain
dimension equal to the domain dimension of the `LinearOperator`s in the
same column-partition, and range dimension equal to the range dimension
of the `LinearOperator`s in the same row-partition.
</td>
</tr><tr>
<td>
`is_non_singular`
</td>
<td>
Expect that this operator is non-singular.
</td>
</tr><tr>
<td>
`is_self_adjoint`
</td>
<td>
Expect that this operator is equal to its hermitian
transpose.
</td>
</tr><tr>
<td>
`is_positive_definite`
</td>
<td>
Expect that this operator is positive definite,
meaning the quadratic form `x^H A x` has positive real part for all
nonzero `x`.  Note that we do not require the operator to be
self-adjoint to be positive-definite.  See:
https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
</td>
</tr><tr>
<td>
`is_square`
</td>
<td>
Expect that this operator acts like square [batch] matrices.
This will raise a `ValueError` if set to `False`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this `LinearOperator`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If all operators do not have the same `dtype`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `operators` is empty, contains an erroneous number of
elements, or contains operators with incompatible shapes.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`H`
</td>
<td>
Returns the adjoint of the current `LinearOperator`.

Given `A` representing this `LinearOperator`, return `A*`.
Note that calling `self.adjoint()` and `self.H` are equivalent.
</td>
</tr><tr>
<td>
`batch_shape`
</td>
<td>
`TensorShape` of batch dimensions of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb])`, equivalent to `A.shape[:-2]`
</td>
</tr><tr>
<td>
`domain_dimension`
</td>
<td>
Dimension (in the sense of vector spaces) of the domain of this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `N`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The `DType` of `Tensor`s handled by this `LinearOperator`.
</td>
</tr><tr>
<td>
`graph_parents`
</td>
<td>
List of graph dependencies of this `LinearOperator`. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Do not call `graph_parents`.
</td>
</tr><tr>
<td>
`is_non_singular`
</td>
<td>

</td>
</tr><tr>
<td>
`is_positive_definite`
</td>
<td>

</td>
</tr><tr>
<td>
`is_self_adjoint`
</td>
<td>

</td>
</tr><tr>
<td>
`is_square`
</td>
<td>
Return `True/False` depending on if this operator is square.
</td>
</tr><tr>
<td>
`operators`
</td>
<td>

</td>
</tr><tr>
<td>
`parameters`
</td>
<td>
Dictionary of parameters used to instantiate this `LinearOperator`.
</td>
</tr><tr>
<td>
`range_dimension`
</td>
<td>
Dimension (in the sense of vector spaces) of the range of this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `M`.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
`TensorShape` of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb, M, N])`, equivalent to `A.shape`.
</td>
</tr><tr>
<td>
`tensor_rank`
</td>
<td>
Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.
</td>
</tr>
</table>



## Methods

<h3 id="add_to_tensor"><code>add_to_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L1077-L1090">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_to_tensor(
    x, name='add_to_tensor'
)
</code></pre>

Add matrix represented by this operator to `x`.  Equivalent to `A + x`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` with same `dtype` and shape broadcastable to `self.shape`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name to give this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with broadcast shape and same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="adjoint"><code>adjoint</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L933-L948">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>adjoint(
    name='adjoint'
)
</code></pre>

Returns the adjoint of the current `LinearOperator`.

Given `A` representing this `LinearOperator`, return `A*`.
Note that calling `self.adjoint()` and `self.H` are equivalent.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`LinearOperator` which represents the adjoint of this `LinearOperator`.
</td>
</tr>

</table>



<h3 id="assert_non_singular"><code>assert_non_singular</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L541-L559">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assert_non_singular(
    name='assert_non_singular'
)
</code></pre>

Returns an `Op` that asserts this operator is non singular.

This operator is considered non-singular if

```
ConditionNumber < max{100, range_dimension, domain_dimension} * eps,
eps := np.finfo(self.dtype.as_numpy_dtype).eps
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A string name to prepend to created ops.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
the operator is singular.
</td>
</tr>

</table>



<h3 id="assert_positive_definite"><code>assert_positive_definite</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L577-L592">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assert_positive_definite(
    name='assert_positive_definite'
)
</code></pre>

Returns an `Op` that asserts this operator is positive definite.

Here, positive definite means that the quadratic form `x^H A x` has positive
real part for all nonzero `x`.  Note that we do not require the operator to
be self-adjoint to be positive definite.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name to give this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
the operator is not positive definite.
</td>
</tr>

</table>



<h3 id="assert_self_adjoint"><code>assert_self_adjoint</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L604-L618">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assert_self_adjoint(
    name='assert_self_adjoint'
)
</code></pre>

Returns an `Op` that asserts this operator is self-adjoint.

Here we check that this operator is *exactly* equal to its hermitian
transpose.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A string name to prepend to created ops.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
the operator is not self-adjoint.
</td>
</tr>

</table>



<h3 id="batch_shape_tensor"><code>batch_shape_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L355-L370">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_shape_tensor(
    name='batch_shape_tensor'
)
</code></pre>

Shape of batch dimensions of this operator, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`
</td>
</tr>

</table>



<h3 id="cholesky"><code>cholesky</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L978-L1001">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cholesky(
    name='cholesky'
)
</code></pre>

Returns a Cholesky factor as a `LinearOperator`.

Given `A` representing this `LinearOperator`, if `A` is positive definite
self-adjoint, return `L`, where `A = L L^T`, i.e. the cholesky
decomposition.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`LinearOperator` which represents the lower triangular matrix
in the Cholesky decomposition.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
When the `LinearOperator` is not hinted to be positive
definite and self adjoint.
</td>
</tr>
</table>



<h3 id="cond"><code>cond</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L1127-L1137">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cond(
    name='cond'
)
</code></pre>

Returns the condition number of this linear operator.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Shape `[B1,...,Bb]` `Tensor` of same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="determinant"><code>determinant</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L737-L754">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>determinant(
    name='det'
)
</code></pre>

Determinant for every batch member.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with shape `self.batch_shape` and same `dtype` as `self`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
If `self.is_square` is `False`.
</td>
</tr>
</table>



<h3 id="diag_part"><code>diag_part</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L1028-L1054">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>diag_part(
    name='diag_part'
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`diag_part`
</td>
<td>
A `Tensor` of same `dtype` as self.
</td>
</tr>
</table>



<h3 id="domain_dimension_tensor"><code>domain_dimension_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L440-L456">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>domain_dimension_tensor(
    name='domain_dimension_tensor'
)
</code></pre>

Dimension (in the sense of vector spaces) of the domain of this operator.

Determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `N`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`
</td>
</tr>

</table>



<h3 id="eigvals"><code>eigvals</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L1095-L1112">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>eigvals(
    name='eigvals'
)
</code></pre>

Returns the eigenvalues of this linear operator.

If the operator is marked as self-adjoint (via `is_self_adjoint`)
this computation can be more efficient.

Note: This currently only supports self-adjoint operators.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Shape `[B1,...,Bb, N]` `Tensor` of same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="inverse"><code>inverse</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L953-L976">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>inverse(
    name='inverse'
)
</code></pre>

Returns the Inverse of this `LinearOperator`.

Given `A` representing this `LinearOperator`, return a `LinearOperator`
representing `A^-1`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name scope to use for ops added by this method.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`LinearOperator` representing inverse of this matrix.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
When the `LinearOperator` is not hinted to be `non_singular`.
</td>
</tr>
</table>



<h3 id="log_abs_determinant"><code>log_abs_determinant</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L766-L783">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>log_abs_determinant(
    name='log_abs_det'
)
</code></pre>

Log absolute value of determinant for every batch member.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with shape `self.batch_shape` and same `dtype` as `self`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
If `self.is_square` is `False`.
</td>
</tr>
</table>



<h3 id="matmul"><code>matmul</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py#L394-L456">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>matmul(
    x, adjoint=(False), adjoint_arg=(False), name='matmul'
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`LinearOperator`, `Tensor` with compatible shape and same `dtype` as
`self`, or a blockwise iterable of `LinearOperator`s or `Tensor`s. See
class docstring for definition of shape compatibility.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
</td>
</tr><tr>
<td>
`adjoint_arg`
</td>
<td>
Python `bool`.  If `True`, compute `A x^H` where `x^H` is
the hermitian transpose (transposition and complex conjugation).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `LinearOperator` or `Tensor` with shape `[..., M, R]` and same `dtype`
as `self`, or if `x` is blockwise, a list of `Tensor`s with shapes that
concatenate to `[..., M, R]`.
</td>
</tr>

</table>



<h3 id="matvec"><code>matvec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py#L522-L571">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>matvec(
    x, adjoint=(False), name='matvec'
)
</code></pre>

Transform [batch] vector `x` with left multiplication:  `x --> Ax`.

```python
# Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)

X = ... # shape [..., N], batch vector

Y = operator.matvec(X)
Y.shape
==> [..., M]

Y[..., :] = sum_j A[..., :, j] X[..., j]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` with compatible shape and same `dtype` as `self`, or an
iterable of `Tensor`s. `Tensor`s are treated a [batch] vectors, meaning
for every set of leading dimensions, the last dimension defines a
vector.
See class docstring for definition of compatibility.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with shape `[..., M]` and same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="range_dimension_tensor"><code>range_dimension_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L484-L500">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>range_dimension_tensor(
    name='range_dimension_tensor'
)
</code></pre>

Dimension (in the sense of vector spaces) of the range of this operator.

Determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `M`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`
</td>
</tr>

</table>



<h3 id="shape_tensor"><code>shape_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L321-L339">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>shape_tensor(
    name='shape_tensor'
)
</code></pre>

Shape of this `LinearOperator`, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb, M, N]`, equivalent to <a href="../../tf/shape.md"><code>tf.shape(A)</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`
</td>
</tr>

</table>



<h3 id="solve"><code>solve</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py#L587-L760">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>solve(
    rhs, adjoint=(False), adjoint_arg=(False), name='solve'
)
</code></pre>

Solve (exact or approx) `R` (batch) systems of equations: `A X = rhs`.

The returned `Tensor` will be close to an exact solution if `A` is well
conditioned. Otherwise closeness will vary. See class docstring for details.

Given the blockwise `n + 1`-by-`n + 1` linear operator:

op = [[A_00     0  ...     0  ...    0],
      [A_10  A_11  ...     0  ...    0],
      ...
      [A_k0  A_k1  ...  A_kk  ...    0],
      ...
      [A_n0  A_n1  ...  A_nk  ... A_nn]]

we find `x = op.solve(y)` by observing that

`y_k = A_k0.matmul(x_0) + A_k1.matmul(x_1) + ... + A_kk.matmul(x_k)`

and therefore

`x_k = A_kk.solve(y_k -
                  A_k0.matmul(x_0) - ... - A_k(k-1).matmul(x_(k-1)))`

where `x_k` and `y_k` are the `k`th blocks obtained by decomposing `x`
and `y` along their appropriate axes.

We first solve `x_0 = A_00.solve(y_0)`. Proceeding inductively, we solve
for `x_k`, `k = 1..n`, given `x_0..x_(k-1)`.

The adjoint case is solved similarly, beginning with
`x_n = A_nn.solve(y_n, adjoint=True)` and proceeding backwards.

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`rhs`
</td>
<td>
`Tensor` with same `dtype` as this operator and compatible shape,
or a list of `Tensor`s. `Tensor`s are treated like a [batch] matrices
meaning for every set of leading dimensions, the last two dimensions
defines a matrix.
See class docstring for definition of compatibility.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
Python `bool`.  If `True`, solve the system involving the adjoint
of this `LinearOperator`:  `A^H X = rhs`.
</td>
</tr><tr>
<td>
`adjoint_arg`
</td>
<td>
Python `bool`.  If `True`, solve `A X = rhs^H` where `rhs^H`
is the hermitian transpose (transposition and complex conjugation).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name scope to use for ops added by this method.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with shape `[...,N, R]` and same `dtype` as `rhs`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
If `self.is_non_singular` or `is_square` is False.
</td>
</tr>
</table>



<h3 id="solvevec"><code>solvevec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py#L762-L822">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>solvevec(
    rhs, adjoint=(False), name='solve'
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`rhs`
</td>
<td>
`Tensor` with same `dtype` as this operator, or list of `Tensor`s
(for blockwise operators). `Tensor`s are treated as [batch] vectors,
meaning for every set of leading dimensions, the last dimension defines
a vector.  See class docstring for definition of compatibility regarding
batch dimensions.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
Python `bool`.  If `True`, solve the system involving the adjoint
of this `LinearOperator`:  `A^H X = rhs`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name scope to use for ops added by this method.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with shape `[...,N]` and same `dtype` as `rhs`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
If `self.is_non_singular` or `is_square` is False.
</td>
</tr>
</table>



<h3 id="tensor_rank_tensor"><code>tensor_rank_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L399-L413">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tensor_rank_tensor(
    name='tensor_rank_tensor'
)
</code></pre>

Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`, determined at runtime.
</td>
</tr>

</table>



<h3 id="to_dense"><code>to_dense</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L1019-L1022">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_dense(
    name='to_dense'
)
</code></pre>

Return a dense (batch) matrix representing this operator.


<h3 id="trace"><code>trace</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L1059-L1071">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>trace(
    name='trace'
)
</code></pre>

Trace of the linear operator, equal to sum of `self.diag_part()`.

If the operator is square, this is also the sum of the eigenvalues.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Shape `[B1,...,Bb]` `Tensor` of same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="__matmul__"><code>__matmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linear_operator.py#L686-L687">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__matmul__(
    other
)
</code></pre>






