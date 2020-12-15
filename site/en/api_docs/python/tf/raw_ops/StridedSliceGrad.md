description: Returns the gradient of StridedSlice.

robots: noindex

# tf.raw_ops.StridedSliceGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the gradient of `StridedSlice`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StridedSliceGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StridedSliceGrad(
    shape, begin, end, strides, dy, begin_mask=0, end_mask=0, ellipsis_mask=0,
    new_axis_mask=0, shrink_axis_mask=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Since `StridedSlice` cuts out pieces of its `input` which is size
`shape`, its gradient will have the same shape (which is passed here
as `shape`). The gradient will be zero in any element that the slice
does not select.

Arguments are the same as StridedSliceGrad with the exception that
`dy` is the input gradient to be propagated and `shape` is the
shape of `StridedSlice`'s `input`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
</td>
</tr><tr>
<td>
`begin`
</td>
<td>
A `Tensor`. Must have the same type as `shape`.
</td>
</tr><tr>
<td>
`end`
</td>
<td>
A `Tensor`. Must have the same type as `shape`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A `Tensor`. Must have the same type as `shape`.
</td>
</tr><tr>
<td>
`dy`
</td>
<td>
A `Tensor`.
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
A `Tensor`. Has the same type as `dy`.
</td>
</tr>

</table>

