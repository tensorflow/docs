page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.linalg


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Operations for linear algebra.

<!-- Placeholder for "Used in" -->


## Classes

[`class LinearOperator`](../tf/linalg/LinearOperator): Base class defining a [batch of] linear operator[s].

[`class LinearOperatorAdjoint`](../tf/linalg/LinearOperatorAdjoint): `LinearOperator` representing the adjoint of another operator.

[`class LinearOperatorBlockDiag`](../tf/linalg/LinearOperatorBlockDiag): Combines one or more `LinearOperators` in to a Block Diagonal matrix.

[`class LinearOperatorCirculant`](../tf/linalg/LinearOperatorCirculant): `LinearOperator` acting like a circulant matrix.

[`class LinearOperatorCirculant2D`](../tf/linalg/LinearOperatorCirculant2D): `LinearOperator` acting like a block circulant matrix.

[`class LinearOperatorCirculant3D`](../tf/linalg/LinearOperatorCirculant3D): `LinearOperator` acting like a nested block circulant matrix.

[`class LinearOperatorComposition`](../tf/linalg/LinearOperatorComposition): Composes one or more `LinearOperators`.

[`class LinearOperatorDiag`](../tf/linalg/LinearOperatorDiag): `LinearOperator` acting like a [batch] square diagonal matrix.

[`class LinearOperatorFullMatrix`](../tf/linalg/LinearOperatorFullMatrix): `LinearOperator` that wraps a [batch] matrix.

[`class LinearOperatorHouseholder`](../tf/linalg/LinearOperatorHouseholder): `LinearOperator` acting like a [batch] of Householder transformations.

[`class LinearOperatorIdentity`](../tf/linalg/LinearOperatorIdentity): `LinearOperator` acting like a [batch] square identity matrix.

[`class LinearOperatorInversion`](../tf/linalg/LinearOperatorInversion): `LinearOperator` representing the inverse of another operator.

[`class LinearOperatorKronecker`](../tf/linalg/LinearOperatorKronecker): Kronecker product between two `LinearOperators`.

[`class LinearOperatorLowRankUpdate`](../tf/linalg/LinearOperatorLowRankUpdate): Perturb a `LinearOperator` with a rank `K` update.

[`class LinearOperatorLowerTriangular`](../tf/linalg/LinearOperatorLowerTriangular): `LinearOperator` acting like a [batch] square lower triangular matrix.

[`class LinearOperatorScaledIdentity`](../tf/linalg/LinearOperatorScaledIdentity): `LinearOperator` acting like a scaled [batch] identity matrix `A = c I`.

[`class LinearOperatorToeplitz`](../tf/linalg/LinearOperatorToeplitz): `LinearOperator` acting like a [batch] of toeplitz matrices.

[`class LinearOperatorZeros`](../tf/linalg/LinearOperatorZeros): `LinearOperator` acting like a [batch] zero matrix.

## Functions

[`adjoint(...)`](../tf/linalg/adjoint): Transposes the last two dimensions of and conjugates tensor `matrix`.

[`band_part(...)`](../tf/linalg/band_part): Copy a tensor setting everything outside a central band in each innermost matrix

[`cholesky(...)`](../tf/linalg/cholesky): Computes the Cholesky decomposition of one or more square matrices.

[`cholesky_solve(...)`](../tf/linalg/cholesky_solve): Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

[`cross(...)`](../tf/linalg/cross): Compute the pairwise cross product.

[`det(...)`](../tf/linalg/det): Computes the determinant of one or more square matrices.

[`diag(...)`](../tf/linalg/diag): Returns a batched diagonal tensor with given batched diagonal values.

[`diag_part(...)`](../tf/linalg/diag_part): Returns the batched diagonal part of a batched tensor.

[`eigh(...)`](../tf/linalg/eigh): Computes the eigen decomposition of a batch of self-adjoint matrices.

[`eigvalsh(...)`](../tf/linalg/eigvalsh): Computes the eigenvalues of one or more self-adjoint matrices.

[`einsum(...)`](../tf/einsum): A generalized contraction between tensors of arbitrary dimension.

[`expm(...)`](../tf/linalg/expm): Computes the matrix exponential of one or more square matrices.

[`eye(...)`](../tf/eye): Construct an identity matrix, or a batch of matrices.

[`global_norm(...)`](../tf/linalg/global_norm): Computes the global norm of multiple tensors.

[`inv(...)`](../tf/linalg/inv): Computes the inverse of one or more square invertible matrices or their

[`l2_normalize(...)`](../tf/math/l2_normalize): Normalizes along dimension `axis` using an L2 norm.

[`logdet(...)`](../tf/linalg/logdet): Computes log of the determinant of a hermitian positive definite matrix.

[`logm(...)`](../tf/linalg/logm): Computes the matrix logarithm of one or more square matrices:

[`lstsq(...)`](../tf/linalg/lstsq): Solves one or more linear least-squares problems.

[`lu(...)`](../tf/linalg/lu): Computes the LU decomposition of one or more square matrices.

[`matmul(...)`](../tf/linalg/matmul): Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

[`matrix_transpose(...)`](../tf/linalg/matrix_transpose): Transposes last two dimensions of tensor `a`.

[`matvec(...)`](../tf/linalg/matvec): Multiplies matrix `a` by vector `b`, producing `a` * `b`.

[`norm(...)`](../tf/norm): Computes the norm of vectors, matrices, and tensors.

[`normalize(...)`](../tf/linalg/normalize): Normalizes `tensor` along dimension `axis` using specified norm.

[`qr(...)`](../tf/linalg/qr): Computes the QR decompositions of one or more matrices.

[`set_diag(...)`](../tf/linalg/set_diag): Returns a batched matrix tensor with new batched diagonal values.

[`slogdet(...)`](../tf/linalg/slogdet): Computes the sign and the log of the absolute value of the determinant of

[`solve(...)`](../tf/linalg/solve): Solves systems of linear equations.

[`sqrtm(...)`](../tf/linalg/sqrtm): Computes the matrix square root of one or more square matrices:

[`svd(...)`](../tf/linalg/svd): Computes the singular value decompositions of one or more matrices.

[`tensor_diag(...)`](../tf/linalg/tensor_diag): Returns a diagonal tensor with a given diagonal values.

[`tensor_diag_part(...)`](../tf/linalg/tensor_diag_part): Returns the diagonal part of the tensor.

[`tensordot(...)`](../tf/tensordot): Tensor contraction of a and b along specified axes.

[`trace(...)`](../tf/linalg/trace): Compute the trace of a tensor `x`.

[`triangular_solve(...)`](../tf/linalg/triangular_solve): Solves systems of linear equations with upper or lower triangular matrices by backsubstitution.

[`tridiagonal_matmul(...)`](../tf/linalg/tridiagonal_matmul): Multiplies tridiagonal matrix by matrix.

[`tridiagonal_solve(...)`](../tf/linalg/tridiagonal_solve): Solves tridiagonal systems of equations.
