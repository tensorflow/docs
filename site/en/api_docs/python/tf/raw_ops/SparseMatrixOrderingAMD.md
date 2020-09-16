description: Computes the Approximate Minimum Degree (AMD) ordering of input.

robots: noindex

# tf.raw_ops.SparseMatrixOrderingAMD

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the Approximate Minimum Degree (AMD) ordering of `input`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseMatrixOrderingAMD`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseMatrixOrderingAMD(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the Approximate Minimum Degree (AMD) ordering for a sparse matrix.

The returned permutation may be used to permute the rows and columns of the
given sparse matrix. This typically results in permuted sparse matrix's sparse
Cholesky (or other decompositions) in having fewer zero fill-in compared to
decomposition of the original matrix.

The input sparse matrix may have rank 2 or rank 3. The output Tensor,
representing would then have rank 1 or 2 respectively, with the same batch
shape as the input.

Each component of the input sparse matrix must represent a square symmetric
matrix; only the lower triangular part of the matrix is read. The values of the
sparse matrix does not affect the returned permutation, only the sparsity
pattern of the sparse matrix is used. Hence, a single AMD ordering may be
reused for the Cholesky decompositions of sparse matrices with the same sparsity
pattern but with possibly different values.

Each batch component of the output permutation represents a permutation of `N`
elements, where the input sparse matrix components each have `N` rows. That is,
the component contains each of the integers `{0, .. N-1}` exactly once. The
`i`th element represents the row index that the `i`th row maps to.

#### Usage example:



```python
    from tensorflow.python.ops.linalg.sparse import sparse_csr_matrix_ops

    a_indices = np.array([[0, 0], [1, 1], [2, 1], [2, 2], [3, 3]])
    a_values = np.array([1.0, 2.0, 1.0, 3.0, 4.0], np.float32)
    a_dense_shape = [4, 4]

    with tf.Session() as sess:
      # Define (COO format) SparseTensor over Numpy array.
      a_st = tf.sparse.SparseTensor(a_indices, a_values, a_dense_shape)

      # Convert SparseTensors to CSR SparseMatrix.
      a_sm = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
          a_st.indices, a_st.values, a_st.dense_shape)

      # Obtain the AMD Ordering for the CSR SparseMatrix.
      ordering_amd = sparse_csr_matrix_ops.sparse_matrix_ordering_amd(sparse_matrix)

      ordering_amd_value = sess.run(ordering_amd)
```

`ordering_amd_value` stores the AMD ordering: `[1 2 3 0]`.

input: A `CSRSparseMatrix`.

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
A `Tensor` of type `int32`.
</td>
</tr>

</table>

