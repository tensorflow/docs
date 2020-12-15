description: Convert raw byte strings into tensors. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.decode_raw" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.decode_raw

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/parsing_ops.py#L887-L928">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Convert raw byte strings into tensors. (deprecated arguments)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.decode_raw`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.decode_raw(
    input_bytes=None, out_type=None, little_endian=(True), name=None, bytes=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(bytes)`. They will be removed in a future version.
Instructions for updating:
bytes is deprecated, use input_bytes instead

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_bytes`
</td>
<td>
Each element of the input Tensor is converted to an array of bytes.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
`DType` of the output. Acceptable types are `half`, `float`, `double`,
`int32`, `uint16`, `uint8`, `int16`, `int8`, `int64`.
</td>
</tr><tr>
<td>
`little_endian`
</td>
<td>
Whether the `input_bytes` data is in little-endian format. Data will be
converted into host byte order if necessary.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`bytes`
</td>
<td>
Deprecated parameter. Use `input_bytes` instead.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` object storing the decoded bytes.
</td>
</tr>

</table>

