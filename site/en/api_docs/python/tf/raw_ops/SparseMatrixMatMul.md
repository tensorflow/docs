description: Matrix-multiplies a sparse matrix with a dense matrix.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseMatrixMatMul" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseMatrixMatMul

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Matrix-multiplies a sparse matrix with a dense matrix.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseMatrixMatMul`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseMatrixMatMul(
    a, b, transpose_a=(False), transpose_b=(False), adjoint_a=(False),
    adjoint_b=(False), transpose_output=(False), conjugate_output=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a dense matrix.
For inputs A and B, where A is CSR and B is dense; this op returns a dense C;

If transpose_output is false, returns:
```
  C = A . B
```

If transpose_output is `true`, returns:
```
  C = transpose(A . B) = transpose(B) . transpose(A)
```
where the transposition is performed along the two innermost (matrix)
dimensions.

If conjugate_output is `true`, returns:
```
  C = conjugate(A . B) = conjugate(A) . conjugate(B)
```

If both conjugate_output and transpose_output are `true`, returns:
```
  C = conjugate(transpose(A . B)) = conjugate(transpose(B)) .
                                    conjugate(transpose(A))
```

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
A `Tensor`. A dense tensor.
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
`transpose_output`
</td>
<td>
An optional `bool`. Defaults to `False`.
Transposes the product of `a` and `b`.
</td>
</tr><tr>
<td>
`conjugate_output`
</td>
<td>
An optional `bool`. Defaults to `False`.
Conjugates the product of `a` and `b`.
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
A `Tensor`. Has the same type as `b`.
</td>
</tr>

</table>

