description: Number of unique elements along last dimension of input set.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SetSize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SetSize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Number of unique elements along last dimension of input `set`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SetSize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SetSize(
    set_indices, set_values, set_shape, validate_indices=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Input `set` is a `SparseTensor` represented by `set_indices`, `set_values`,
and `set_shape`. The last dimension contains values in a set, duplicates are
allowed but ignored.

If `validate_indices` is `True`, this op validates the order and range of `set`
indices.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`set_indices`
</td>
<td>
A `Tensor` of type `int64`.
2D `Tensor`, indices of a `SparseTensor`.
</td>
</tr><tr>
<td>
`set_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `string`.
1D `Tensor`, values of a `SparseTensor`.
</td>
</tr><tr>
<td>
`set_shape`
</td>
<td>
A `Tensor` of type `int64`.
1D `Tensor`, shape of a `SparseTensor`.
</td>
</tr><tr>
<td>
`validate_indices`
</td>
<td>
An optional `bool`. Defaults to `True`.
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
A `Tensor` of type `int32`.
</td>
</tr>

</table>

