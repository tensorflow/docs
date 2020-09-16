description: Assign value to the sliced l-value reference of ref.

robots: noindex

# tf.raw_ops.StridedSliceAssign

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Assign `value` to the sliced l-value reference of `ref`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StridedSliceAssign`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StridedSliceAssign(
    ref, begin, end, strides, value, begin_mask=0, end_mask=0, ellipsis_mask=0,
    new_axis_mask=0, shrink_axis_mask=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The values of `value` are assigned to the positions in the variable
`ref` that are selected by the slice parameters. The slice parameters
`begin`, `end`, `strides`, etc. work exactly as in `StridedSlice`.

NOTE this op currently does not support broadcasting and so `value`'s
shape must be exactly the shape produced by the slice of `ref`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ref`
</td>
<td>
A mutable `Tensor`.
</td>
</tr><tr>
<td>
`begin`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
</td>
</tr><tr>
<td>
`end`
</td>
<td>
A `Tensor`. Must have the same type as `begin`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A `Tensor`. Must have the same type as `begin`.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A `Tensor`. Must have the same type as `ref`.
</td>
</tr><tr>
<td>
`begin_mask`
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`end_mask`
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`ellipsis_mask`
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`new_axis_mask`
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`shrink_axis_mask`
</td>
<td>
An optional `int`. Defaults to `0`.
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
A mutable `Tensor`. Has the same type as `ref`.
</td>
</tr>

</table>

