description: Splits a tensor into num_split tensors along one dimension.

robots: noindex

# tf.raw_ops.SplitV

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Splits a tensor into `num_split` tensors along one dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SplitV`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SplitV(
    value, size_splits, axis, num_split, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A `Tensor`. The tensor to split.
</td>
</tr><tr>
<td>
`size_splits`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
list containing the sizes of each output tensor along the split
dimension. Must sum to the dimension of value along split_dim.
Can contain one -1 indicating that dimension is to be inferred.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A `Tensor` of type `int32`.
0-D.  The dimension along which to split.  Must be in the range
`[-rank(value), rank(value))`.
</td>
</tr><tr>
<td>
`num_split`
</td>
<td>
An `int` that is `>= 1`.
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
A list of `num_split` `Tensor` objects with the same type as `value`.
</td>
</tr>

</table>

