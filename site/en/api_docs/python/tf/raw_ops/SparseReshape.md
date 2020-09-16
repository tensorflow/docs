description: Reshapes a SparseTensor to represent values in a new dense shape.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseReshape" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseReshape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Reshapes a SparseTensor to represent values in a new dense shape.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseReshape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseReshape(
    input_indices, input_shape, new_shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation has the same semantics as reshape on the represented dense
tensor.  The `input_indices` are recomputed based on the requested `new_shape`.

If one component of `new_shape` is the special value -1, the size of that
dimension is computed so that the total dense size remains constant.  At
most one component of `new_shape` can be -1.  The number of dense elements
implied by `new_shape` must be the same as the number of dense elements
originally implied by `input_shape`.

Reshaping does not affect the order of values in the SparseTensor.

If the input tensor has rank `R_in` and `N` non-empty values, and `new_shape`
has length `R_out`, then `input_indices` has shape `[N, R_in]`,
`input_shape` has length `R_in`, `output_indices` has shape `[N, R_out]`, and
`output_shape` has length `R_out`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  `N x R_in` matrix with the indices of non-empty values in a
SparseTensor.
</td>
</tr><tr>
<td>
`input_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  `R_in` vector with the input SparseTensor's dense shape.
</td>
</tr><tr>
<td>
`new_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  `R_out` vector with the requested new dense shape.
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
A tuple of `Tensor` objects (output_indices, output_shape).
</td>
</tr>
<tr>
<td>
`output_indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

