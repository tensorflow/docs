description: Computes the sum of elements across dimensions of a SparseTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseReduceSum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseReduceSum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the sum of elements across dimensions of a SparseTensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseReduceSum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseReduceSum(
    input_indices, input_values, input_shape, reduction_axes, keep_dims=(False),
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This Op takes a SparseTensor and is the sparse counterpart to
<a href="../../tf/math/reduce_sum.md"><code>tf.reduce_sum()</code></a>.  In particular, this Op also returns a dense `Tensor`
instead of a sparse one.

Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
`keep_dims` is true, the rank of the tensor is reduced by 1 for each entry in
`reduction_axes`. If `keep_dims` is true, the reduced dimensions are retained
with length 1.

If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
with a single element is returned.  Additionally, the axes can be negative,
which are interpreted according to the indexing rules in Python.

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
2-D.  `N x R` matrix with the indices of non-empty values in a
SparseTensor, possibly not in canonical ordering.
</td>
</tr><tr>
<td>
`input_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
1-D.  `N` non-empty values corresponding to `input_indices`.
</td>
</tr><tr>
<td>
`input_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  Shape of the input SparseTensor.
</td>
</tr><tr>
<td>
`reduction_axes`
</td>
<td>
A `Tensor` of type `int32`.
1-D.  Length-`K` vector containing the reduction axes.
</td>
</tr><tr>
<td>
`keep_dims`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, retain reduced dimensions with length 1.
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
A `Tensor`. Has the same type as `input_values`.
</td>
</tr>

</table>

