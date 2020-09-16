description: Computes the sparse Cholesky decomposition of input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseMatrixSparseCholesky" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseMatrixSparseCholesky

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the sparse Cholesky decomposition of `input`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseMatrixSparseCholesky`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseMatrixSparseCholesky(
    input, permutation, type, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the Sparse Cholesky decomposition of a sparse matrix, with the given
fill-in reducing permutation.

The input sparse matrix and the fill-in reducing permutation `permutation` must
have compatible shapes. If the sparse matrix has rank 3; with the batch
dimension `B`, then the `permutation` must be of rank 2; with the same batch
dimension `B`. There is no support for broadcasting.

Furthermore, each component vector of `permutation` must be of length `N`,
containing each of the integers {0, 1, ..., N - 1} exactly once, where `N` is
the number of rows of each component of the sparse matrix.

Each component of the input sparse matrix must represent a symmetric positive
definite (SPD) matrix; although only the lower triangular part of the matrix is
read. If any individual component is not SPD, then an InvalidArgument error is
thrown.

The returned sparse matrix has the same dense shape as the input sparse matrix.
For each component `A` of the input sparse matrix, the corresponding output
sparse matrix represents `L`, the lower triangular Cholesky factor satisfying
the following identity:

```
  A = L * Lt
```

where Lt denotes the transpose of L (or its conjugate transpose, if `type` is
`complex64` or `complex128`).

The `type` parameter denotes the type of the matrix elements. The supported
types are: `float32`, `float64`, `complex64` and `complex128`.

#### Usage example:



```python
    from tensorflow.python.ops.linalg.sparse import sparse_csr_matrix_ops

    a_indices = np.array([[0, 0], [1, 1], [2, 1], [2, 2], [3, 3]])
    a_values = np.array([1.0, 2.0, 1.0, 3.0, 4.0], np.float32)
    a_dense_shape = [4, 4]

    with tf.Session() as sess:
      # Define (COO format) SparseTensor over Numpy array.
      a_st = tf.SparseTensor(a_indices, a_values, a_dense_shape)

      # Convert SparseTensors to CSR SparseMatrix.
      a_sm = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
          a_st.indices, a_st.values, a_st.dense_shape)

      # Obtain the Sparse Cholesky factor using AMD Ordering for reducing zero
      # fill-in (number of structural non-zeros in the sparse Cholesky factor).
      ordering_amd = sparse_csr_matrix_ops.sparse_matrix_ordering_amd(sparse_matrix)
      cholesky_sparse_matrices = (
          sparse_csr_matrix_ops.sparse_matrix_sparse_cholesky(
              sparse_matrix, ordering_amd, type=tf.float32))

      # Convert the CSRSparseMatrix Cholesky factor to a dense Tensor
      dense_cholesky = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
          cholesky_sparse_matrices, tf.float32)

      # Evaluate the dense Tensor value.
      dense_cholesky_value = sess.run(dense_cholesky)
```

`dense_cholesky_value` stores the dense Cholesky factor:

```
    [[  1.  0.    0.    0.]
     [  0.  1.41  0.    0.]
     [  0.  0.70  1.58  0.]
     [  0.  0.    0.    2.]]
```


input: A `CSRSparseMatrix`.
permutation: A `Tensor`.
type: The type of `input`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` of type `variant`. A `CSRSparseMatrix`.
</td>
</tr><tr>
<td>
`permutation`
</td>
<td>
A `Tensor` of type `int32`.
A fill-in reducing permutation matrix.
</td>
</tr><tr>
<td>
`type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.float32, tf.float64, tf.complex64, tf.complex128`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `variant`.
</td>
</tr>

</table>

