description: Debug NaN Value Counter Op.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.DebugNanCount" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.DebugNanCount

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Debug NaN Value Counter Op.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DebugNanCount`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DebugNanCount(
    input, device_name='', tensor_name='', debug_urls=[], gated_grpc=(False),
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Counts number of NaNs in the input tensor, for debugging.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Input tensor, non-Reference type.
</td>
</tr><tr>
<td>
`device_name`
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`tensor_name`
</td>
<td>
An optional `string`. Defaults to `""`.
Name of the input tensor.
</td>
</tr><tr>
<td>
`debug_urls`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
List of URLs to debug targets, e.g.,
file:///foo/tfdbg_dump, grpc:://localhost:11011.
</td>
</tr><tr>
<td>
`gated_grpc`
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether this op will be gated. If any of the debug_urls of this
debug node is of the grpc:// scheme, when the value of this attribute is set
to True, the data will not actually be sent via the grpc stream unless this
debug op has been enabled at the debug_url. If all of the debug_urls of this
debug node are of the grpc:// scheme and the debug op is enabled at none of
them, the output will be an empty Tensor.
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
A `Tensor` of type `int64`.
</td>
</tr>

</table>

