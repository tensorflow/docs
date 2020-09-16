description: Operations for linear algebra.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.linalg

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Operations for linear algebra.



## Modules

[`experimental`](../tf/linalg/experimental.md) module: Public API for tf.linalg.experimental namespace.

## Classes

[`class LinearOperator`](../tf/linalg/LinearOperator.md): Base class defining a [batch of] linear operator[s].

[`class LinearOperatorAdjoint`](../tf/linalg/LinearOperatorAdjoint.md): `LinearOperator` representing the adjoint of another operator.

[`class LinearOperatorBlockDiag`](../tf/linalg/LinearOperatorBlockDiag.md): Combines one or more `LinearOperators` in to a Block Diagonal matrix.

[`class LinearOperatorBlockLowerTriangular`](../tf/linalg/LinearOperatorBlockLowerTriangular.md): Combines `LinearOperators` into a blockwise lower-triangular matrix.

[`class LinearOperatorCirculant`](../tf/linalg/LinearOperatorCirculant.md): `LinearOperator` acting like a circulant matrix.

[`class LinearOperatorCirculant2D`](../tf/linalg/LinearOperatorCirculant2D.md): `LinearOperator` acting like a block circulant matrix.

[`class LinearOperatorCirculant3D`](../tf/linalg/LinearOperatorCirculant3D.md): `LinearOperator` acting like a nested block circulant matrix.

[`class LinearOperatorComposition`](../tf/linalg/LinearOperatorComposition.md): Composes one or more `LinearOperators`.

[`class LinearOperatorDiag`](../tf/linalg/LinearOperatorDiag.md): `LinearOperator` acting like a [batch] square diagonal matrix.

[`class LinearOperatorFullMatrix`](../tf/linalg/LinearOperatorFullMatrix.md): `LinearOperator` that wraps a [batch] matrix.

[`class LinearOperatorHouseholder`](../tf/linalg/LinearOperatorHouseholder.md): `LinearOperator` acting like a [batch] of Householder transformations.

[`class LinearOperatorIdentity`](../tf/linalg/LinearOperatorIdentity.md): `LinearOperator` acting like a [batch] square identity matrix.

[`class LinearOperatorInversion`](../tf/linalg/LinearOperatorInversion.md): `LinearOperator` representing the inverse of another operator.

[`class LinearOperatorKronecker`](../tf/linalg/LinearOperatorKronecker.md): Kronecker product between two `LinearOperators`.

[`class LinearOperatorLowRankUpdate`](../tf/linalg/LinearOperatorLowRankUpdate.md): Perturb a `LinearOperator` with a rank `K` update.

[`class LinearOperatorLowerTriangular`](../tf/linalg/LinearOperatorLowerTriangular.md): `LinearOperator` acting like a [batch] square lower triangular matrix.

[`class LinearOperatorPermutation`](../tf/linalg/LinearOperatorPermutation.md): `LinearOperator` acting like a [batch] of permutation matrices.

[`class LinearOperatorScaledIdentity`](../tf/linalg/LinearOperatorScaledIdentity.md): `LinearOperator` acting like a scaled [batch] identity matrix `A = c I`.

[`class LinearOperatorToeplitz`](../tf/linalg/LinearOperatorToeplitz.md): `LinearOperator` acting like a [batch] of toeplitz matrices.

[`class LinearOperatorTridiag`](../tf/linalg/LinearOperatorTridiag.md): `LinearOperator` acting like a [batch] square tridiagonal matrix.

[`class LinearOperatorZeros`](../tf/linalg/LinearOperatorZeros.md): `LinearOperator` acting like a [batch] zero matrix.

## Functions

[`adjoint(...)`](../tf/linalg/adjoint.md): Transposes the last two dimensions of and conjugates tensor `matrix`.

[`band_part(...)`](../tf/linalg/band_part.md): Copy a tensor setting everything outside a central band in each innermost matrix to zero.

[`banded_triangular_solve(...)`](../tf/linalg/banded_triangular_solve.md): Solve triangular systems of equations with a banded solver.

[`cholesky(...)`](../tf/linalg/cholesky.md): Computes the Cholesky decomposition of one or more square matrices.

[`cholesky_solve(...)`](../tf/linalg/cholesky_solve.md): Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

[`cross(...)`](../tf/linalg/cross.md): Compute the pairwise cross product.

[`det(...)`](../tf/linalg/det.md): Computes the determinant of one or more square matrices.

[`diag(...)`](../tf/linalg/diag.md): Returns a batched diagonal tensor with given batched diagonal values.

[`diag_part(...)`](../tf/linalg/diag_part.md): Returns the batched diagonal part of a batched tensor.

[`eig(...)`](../tf/linalg/eig.md): Computes the eigen decomposition of a batch of matrices.

[`eigh(...)`](../tf/linalg/eigh.md): Computes the eigen decomposition of a batch of self-adjoint matrices.

[`eigvals(...)`](../tf/linalg/eigvals.md): Computes the eigenvalues of one or more matrices.

[`eigvalsh(...)`](../tf/linalg/eigvalsh.md): Computes the eigenvalues of one or more self-adjoint matrices.

[`einsum(...)`](../tf/einsum.md): Tensor contraction over specified indices and outer product.

[`expm(...)`](../tf/linalg/expm.md): Computes the matrix exponential of one or more square matrices.

[`eye(...)`](../tf/eye.md): Construct an identity matrix, or a batch of matrices.

[`global_norm(...)`](../tf/linalg/global_norm.md): Computes the global norm of multiple tensors.

[`inv(...)`](../tf/linalg/inv.md): Computes the inverse of one or more square invertible matrices or their

[`l2_normalize(...)`](../tf/math/l2_normalize.md): Normalizes along dimension `axis` using an L2 norm.

[`logdet(...)`](../tf/linalg/logdet.md): Computes log of the determinant of a hermitian positive definite matrix.

[`logm(...)`](../tf/linalg/logm.md): Computes the matrix logarithm of one or more square matrices:

[`lstsq(...)`](../tf/linalg/lstsq.md): Solves one or more linear least-squares problems.

[`lu(...)`](../tf/linalg/lu.md): Computes the LU decomposition of one or more square matrices.

[`lu_matrix_inverse(...)`](../tf/linalg/lu_matrix_inverse.md): Computes the inverse given the LU decomposition(s) of one or more matrices.

[`lu_reconstruct(...)`](../tf/linalg/lu_reconstruct.md): The reconstruct one or more matrices from their LU decomposition(s).

[`lu_solve(...)`](../tf/linalg/lu_solve.md): Solves systems of linear eqns `A X = RHS`, given LU factorizations.

[`matmul(...)`](../tf/linalg/matmul.md): Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

[`matrix_rank(...)`](../tf/linalg/matrix_rank.md): Compute the matrix rank of one or more matrices.

[`matrix_transpose(...)`](../tf/linalg/matrix_transpose.md): Transposes last two dimensions of tensor `a`.

[`matvec(...)`](../tf/linalg/matvec.md): Multiplies matrix `a` by vector `b`, producing `a` * `b`.

[`norm(...)`](../tf/norm.md): Computes the norm of vectors, matrices, and tensors.

[`normalize(...)`](../tf/linalg/normalize.md): Normalizes `tensor` along dimension `axis` using specified norm.

[`pinv(...)`](../tf/linalg/pinv.md): Compute the Moore-Penrose pseudo-inverse of one or more matrices.

[`qr(...)`](../tf/linalg/qr.md): Computes the QR decompositions of one or more matrices.

[`set_diag(...)`](../tf/linalg/set_diag.md): Returns a batched matrix tensor with new batched diagonal values.

[`slogdet(...)`](../tf/linalg/slogdet.md): Computes the sign and the log of the absolute value of the determinant of

[`solve(...)`](../tf/linalg/solve.md): Solves systems of linear equations.

[`sqrtm(...)`](../tf/linalg/sqrtm.md): Computes the matrix square root of one or more square matrices:

[`svd(...)`](../tf/linalg/svd.md): Computes the singular value decompositions of one or more matrices.

[`tensor_diag(...)`](../tf/linalg/tensor_diag.md): Returns a diagonal tensor with a given diagonal values.

[`tensor_diag_part(...)`](../tf/linalg/tensor_diag_part.md): Returns the diagonal part of the tensor.

[`tensordot(...)`](../tf/tensordot.md): Tensor contraction of a and b along specified axes and outer product.

[`trace(...)`](../tf/linalg/trace.md): Compute the trace of a tensor `x`.

[`triangular_solve(...)`](../tf/linalg/triangular_solve.md): Solve systems of linear equations with upper or lower triangular matrices.

[`tridiagonal_matmul(...)`](../tf/linalg/tridiagonal_matmul.md): Multiplies tridiagonal matrix by matrix.

[`tridiagonal_solve(...)`](../tf/linalg/tridiagonal_solve.md): Solves tridiagonal systems of equations.

