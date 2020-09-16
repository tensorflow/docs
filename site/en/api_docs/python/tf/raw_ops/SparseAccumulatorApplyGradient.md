description: Applies a sparse gradient to a given accumulator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseAccumulatorApplyGradient" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseAccumulatorApplyGradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Applies a sparse gradient to a given accumulator.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseAccumulatorApplyGradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseAccumulatorApplyGradient(
    handle, local_step, gradient_indices, gradient_values, gradient_shape,
    has_known_shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Does not add if local_step is smaller than the accumulator's
global_step.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`handle`
</td>
<td>
A `Tensor` of type mutable `string`. The handle to a accumulator.
</td>
</tr><tr>
<td>
`local_step`
</td>
<td>
A `Tensor` of type `int64`.
The local_step value at which the sparse gradient was computed.
</td>
</tr><tr>
<td>
`gradient_indices`
</td>
<td>
A `Tensor` of type `int64`.
Indices of the sparse gradient to be accumulated. Must be a
vector.
</td>
</tr><tr>
<td>
`gradient_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
Values are the non-zero slices of the gradient, and must have
the same first dimension as indices, i.e., the nnz represented by indices and
values must be consistent.
</td>
</tr><tr>
<td>
`gradient_shape`
</td>
<td>
A `Tensor` of type `int64`.
Shape of the sparse gradient to be accumulated.
</td>
</tr><tr>
<td>
`has_known_shape`
</td>
<td>
A `bool`.
Boolean indicating whether gradient_shape is unknown, in which
case the input is ignored during validation.
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
The created Operation.
</td>
</tr>

</table>

