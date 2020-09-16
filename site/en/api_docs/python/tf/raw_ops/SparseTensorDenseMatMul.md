description: Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseTensorDenseMatMul" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseTensorDenseMatMul

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseTensorDenseMatMul`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseTensorDenseMatMul(
    a_indices, a_values, a_shape, b, adjoint_a=(False), adjoint_b=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

No validity checking is performed on the indices of A.  However, the following
input format is recommended for optimal behavior:

if adjoint_a == false:
  A should be sorted in lexicographically increasing order.  Use SparseReorder
  if you're not sure.
if adjoint_a == true:
  A should be sorted in order of increasing dimension 1 (i.e., "column major"
  order instead of "row major" order).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a_indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
2-D.  The `indices` of the `SparseTensor`, size `[nnz, 2]` Matrix.
</td>
</tr><tr>
<td>
`a_values`
</td>
<td>
A `Tensor`.
1-D.  The `values` of the `SparseTensor`, size `[nnz]` Vector.
</td>
</tr><tr>
<td>
`a_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  The `shape` of the `SparseTensor`, size `[2]` Vector.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
A `Tensor`. Must have the same type as `a_values`.
2-D.  A dense Matrix.
</td>
</tr><tr>
<td>
`adjoint_a`
</td>
<td>
An optional `bool`. Defaults to `False`.
Use the adjoint of A in the matrix multiply.  If A is complex, this
is transpose(conj(A)).  Otherwise it's transpose(A).
</td>
</tr><tr>
<td>
`adjoint_b`
</td>
<td>
An optional `bool`. Defaults to `False`.
Use the adjoint of B in the matrix multiply.  If B is complex, this
is transpose(conj(B)).  Otherwise it's transpose(B).
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
A `Tensor`. Has the same type as `a_values`.
</td>
</tr>

</table>

