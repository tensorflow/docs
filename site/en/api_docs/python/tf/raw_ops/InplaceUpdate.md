description: Updates specified rows with values in v.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.InplaceUpdate" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.InplaceUpdate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Updates specified rows with values in `v`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.InplaceUpdate`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.InplaceUpdate(
    x, i, v, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

  Computes `x[i, :] = v; return x`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. A tensor of type `T`.
</td>
</tr><tr>
<td>
`i`
</td>
<td>
A `Tensor` of type `int32`.
A vector. Indices into the left-most dimension of `x`.
</td>
</tr><tr>
<td>
`v`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
A `Tensor` of type T. Same dimension sizes as x except the first dimension, which must be the same as i's size.
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
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>

