description: Convert raw byte strings into tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.decode_raw" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.decode_raw

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/parsing_ops.py#L844-L884">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Convert raw byte strings into tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.decode_raw(
    input_bytes, out_type, little_endian=(True), fixed_length=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
`fixed_length`
</td>
<td>
If set, the first `fixed_length` bytes of each element will be converted.
Data will be zero-padded or truncated to the specified length.

`fixed_length` must be a multiple of the size of `out_type`.
`fixed_length` must be specified if the elements of `input_bytes` are of
variable length.
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
A `Tensor` object storing the decoded bytes.
</td>
</tr>

</table>

