

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.kfac.utils



Defined in [`tensorflow/contrib/kfac/python/ops/utils_lib.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/utils_lib.py).

Utility functions.

## Classes

[`class SequenceDict`](../../../tf/contrib/kfac/utils/SequenceDict): A dict convenience wrapper that allows getting/setting with sequences.

[`class SubGraph`](../../../tf/contrib/kfac/utils/SubGraph): Defines a subgraph given by all the dependencies of a given set of outputs.

## Functions

[`batch_execute(...)`](../../../tf/contrib/kfac/utils/batch_execute): Executes a subset of ops per global step.

[`column_to_tensors(...)`](../../../tf/contrib/kfac/utils/column_to_tensors): Converts a column vector back to the shape of the given template.

[`ensure_sequence(...)`](../../../tf/contrib/kfac/utils/ensure_sequence): If `obj` isn't a tuple or list, return a tuple containing `obj`.

[`fwd_gradients(...)`](../../../tf/contrib/kfac/utils/fwd_gradients): Compute forward-mode gradients.

[`generate_random_signs(...)`](../../../tf/contrib/kfac/utils/generate_random_signs): Generate a random tensor with {-1, +1} entries.

[`kronecker_product(...)`](../../../tf/contrib/kfac/utils/kronecker_product): Computes the Kronecker product two matrices.

[`layer_params_to_mat2d(...)`](../../../tf/contrib/kfac/utils/layer_params_to_mat2d): Converts a vector shaped like layer parameters to a 2D matrix.

[`mat2d_to_layer_params(...)`](../../../tf/contrib/kfac/utils/mat2d_to_layer_params): Converts a canonical 2D matrix representation back to a vector.

[`matmul_diag_sparse(...)`](../../../tf/contrib/kfac/utils/matmul_diag_sparse): Computes matmul(A, B) where A is a diagonal matrix, B is sparse.

[`matmul_sparse_dense(...)`](../../../tf/contrib/kfac/utils/matmul_sparse_dense): Computes matmul(A, B) where A is sparse, B is dense.

[`posdef_inv(...)`](../../../tf/contrib/kfac/utils/posdef_inv): Computes the inverse of tensor + damping * identity.

[`posdef_inv_cholesky(...)`](../../../tf/contrib/kfac/utils/posdef_inv_cholesky): Computes inverse(tensor + damping * identity) with Cholesky.

[`posdef_inv_matrix_inverse(...)`](../../../tf/contrib/kfac/utils/posdef_inv_matrix_inverse): Computes inverse(tensor + damping * identity) directly.

[`set_global_constants(...)`](../../../tf/contrib/kfac/utils/set_global_constants): Sets various global constants used by the classes in this module.

[`tensors_to_column(...)`](../../../tf/contrib/kfac/utils/tensors_to_column): Converts a tensor or list of tensors to a column vector.

