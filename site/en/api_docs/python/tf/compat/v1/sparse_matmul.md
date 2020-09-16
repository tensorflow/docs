description: Multiply matrix "a" by matrix "b".

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.sparse_matmul" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.sparse_matmul

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Multiply matrix "a" by matrix "b".

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.sparse_matmul(
    a, b, transpose_a=(False), transpose_b=(False), a_is_sparse=(False),
    b_is_sparse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The inputs must be two-dimensional matrices and the inner dimension of "a" must
match the outer dimension of "b". Both "a" and "b" must be `Tensor`s not
`SparseTensor`s.  This op is optimized for the case where at least one of "a" or
"b" is sparse, in the sense that they have a large proportion of zero values.
The breakeven for using this versus a dense matrix multiply on one platform was
30% zero values in the sparse matrix.

The gradient computation of this operation will only take advantage of sparsity
in the input gradient when that gradient comes from a Relu.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `bfloat16`.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `bfloat16`.
</td>
</tr><tr>
<td>
`transpose_a`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`transpose_b`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`a_is_sparse`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`b_is_sparse`
</td>
<td>
An optional `bool`. Defaults to `False`.
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

