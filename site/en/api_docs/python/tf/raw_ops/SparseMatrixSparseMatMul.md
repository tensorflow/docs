description: Sparse-matrix-multiplies two CSR matrices a and b.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseMatrixSparseMatMul" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseMatrixSparseMatMul

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Sparse-matrix-multiplies two CSR matrices `a` and `b`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseMatrixSparseMatMul`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseMatrixSparseMatMul(
    a, b, type, transpose_a=(False), transpose_b=(False), adjoint_a=(False),
    adjoint_b=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Performs a matrix multiplication of a sparse matrix `a` with a sparse matrix
`b`; returns a sparse matrix `a * b`, unless either `a` or `b` is transposed or
adjointed.

Each matrix may be transposed or adjointed (conjugated and transposed)
according to the Boolean parameters `transpose_a`, `adjoint_a`, `transpose_b`
and `adjoint_b`. At most one of `transpose_a` or `adjoint_a` may be True.
Similarly, at most one of `transpose_b` or `adjoint_b` may be True.

The inputs must have compatible shapes. That is, the inner dimension of `a`
must be equal to the outer dimension of `b`. This requirement is adjusted
according to whether either `a` or `b` is transposed or adjointed.

The `type` parameter denotes the type of the matrix elements. Both `a` and `b`
must have the same type. The supported types are: `float32`, `float64`,
`complex64` and `complex128`.

Both `a` and `b` must have the same rank. Broadcasting is not supported. If they
have rank 3, each batch of 2D CSRSparseMatrices within `a` and `b` must have the
same dense shape.

The sparse matrix product may have numeric (non-structural) zeros.

zeros.

#### Usage example:



```python
    from tensorflow.python.ops.linalg.sparse import sparse_csr_matrix_ops

    a_indices = np.array([[0, 0], [2, 3], [2, 4], [3, 0]])
    a_values = np.array([1.0, 5.0, -1.0, -2.0], np.float32)
    a_dense_shape = [4, 5]

    b_indices = np.array([[0, 0], [3, 0], [3, 1]])
    b_values = np.array([2.0, 7.0, 8.0], np.float32)
    b_dense_shape = [5, 3]

    with tf.Session() as sess:
      # Define (COO format) Sparse Tensors over Numpy arrays
      a_st = tf.SparseTensor(a_indices, a_values, a_dense_shape)
      b_st = tf.SparseTensor(b_indices, b_values, b_dense_shape)

      # Convert SparseTensors to CSR SparseMatrix
      a_sm = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
          a_st.indices, a_st.values, a_st.dense_shape)
      b_sm = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
          b_st.indices, b_st.values, b_st.dense_shape)

      # Compute the CSR SparseMatrix matrix multiplication
      c_sm = sparse_csr_matrix_ops.sparse_matrix_sparse_mat_mul(
          a=a_sm, b=b_sm, type=tf.float32)

      # Convert the CSR SparseMatrix product to a dense Tensor
      c_sm_dense = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
          c_sm, tf.float32)
      # Evaluate the dense Tensor value
      c_sm_dense_value = sess.run(c_sm_dense)
```

`c_sm_dense_value` stores the dense matrix product:

```
    [[  2.   0.   0.]
     [  0.   0.   0.]
     [ 35.  40.   0.]
     [ -4.   0.   0.]]
```

a: A `CSRSparseMatrix`.
b: A `CSRSparseMatrix` with the same type and rank as `a`.
type: The type of both `a` and `b`.
transpose_a: If True, `a` transposed before multiplication.
transpose_b: If True, `b` transposed before multiplication.
adjoint_a: If True, `a` adjointed before multiplication.
adjoint_b: If True, `b` adjointed before multiplication.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
A `Tensor` of type `variant`. A CSRSparseMatrix.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
A `Tensor` of type `variant`. A CSRSparseMatrix.
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
`transpose_a`
</td>
<td>
An optional `bool`. Defaults to `False`.
Indicates whether `a` should be transposed.
</td>
</tr><tr>
<td>
`transpose_b`
</td>
<td>
An optional `bool`. Defaults to `False`.
Indicates whether `b` should be transposed.
</td>
</tr><tr>
<td>
`adjoint_a`
</td>
<td>
An optional `bool`. Defaults to `False`.
Indicates whether `a` should be conjugate-transposed.
</td>
</tr><tr>
<td>
`adjoint_b`
</td>
<td>
An optional `bool`. Defaults to `False`.
Indicates whether `b` should be conjugate-transposed.
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

