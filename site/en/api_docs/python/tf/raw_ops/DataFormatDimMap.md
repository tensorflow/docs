description: Returns the dimension index in the destination data format given the one in

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.DataFormatDimMap" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.DataFormatDimMap

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the dimension index in the destination data format given the one in

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DataFormatDimMap`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DataFormatDimMap(
    x, src_format='NHWC', dst_format='NCHW', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

the source data format.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A Tensor with each element as a dimension index in source data format.
Must be in the range [-4, 4).
</td>
</tr><tr>
<td>
`src_format`
</td>
<td>
An optional `string`. Defaults to `"NHWC"`.
source data format.
</td>
</tr><tr>
<td>
`dst_format`
</td>
<td>
An optional `string`. Defaults to `"NCHW"`.
destination data format.
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

