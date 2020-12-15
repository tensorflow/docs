description: Transcode the input text from a source encoding to a destination encoding.

robots: noindex

# tf.raw_ops.UnicodeTranscode

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transcode the input text from a source encoding to a destination encoding.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.UnicodeTranscode`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.UnicodeTranscode(
    input, input_encoding, output_encoding, errors='replace',
    replacement_char=65533, replace_control_characters=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input is a string tensor of any shape. The output is a string tensor of
the same shape containing the transcoded strings. Output strings are always
valid unicode. If the input contains invalid encoding positions, the
`errors` attribute sets the policy for how to deal with them. If the default
error-handling policy is used, invalid formatting will be substituted in the
output by the `replacement_char`. If the errors policy is to `ignore`, any
invalid encoding positions in the input are skipped and not included in the
output. If it set to `strict` then any invalid formatting will result in an
InvalidArgument error.

This operation can be used with `output_encoding = input_encoding` to enforce
correct formatting for inputs even if they are already in the desired encoding.

If the input is prefixed by a Byte Order Mark needed to determine encoding
(e.g. if the encoding is UTF-16 and the BOM indicates big-endian), then that
BOM will be consumed and not emitted into the output. If the input encoding
is marked with an explicit endianness (e.g. UTF-16-BE), then the BOM is
interpreted as a non-breaking-space and is preserved in the output (including
always for UTF-8).

The end result is that if the input is marked as an explicit endianness the
transcoding is faithful to all codepoints in the source. If it is not marked
with an explicit endianness, the BOM is not considered part of the string itself
but as metadata, and so is not preserved in the output.

#### Examples:



```
>>> tf.strings.unicode_transcode(["Hello", "TensorFlow", "2.x"], "UTF-8", "UTF-16-BE")
<tf.Tensor: shape=(3,), dtype=string, numpy=
array([b'\x00H\x00e\x00l\x00l\x00o',
       b'\x00T\x00e\x00n\x00s\x00o\x00r\x00F\x00l\x00o\x00w',
       b'\x002\x00.\x00x'], dtype=object)>
>>> tf.strings.unicode_transcode(["A", "B", "C"], "US ASCII", "UTF-8").numpy()
array([b'A', b'B', b'C'], dtype=object)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` of type `string`.
The text to be processed. Can have any shape.
</td>
</tr><tr>
<td>
`input_encoding`
</td>
<td>
A `string`.
Text encoding of the input strings. This is any of the encodings supported
by ICU ucnv algorithmic converters. Examples: `"UTF-16", "US ASCII", "UTF-8"`.
</td>
</tr><tr>
<td>
`output_encoding`
</td>
<td>
A `string` from: `"UTF-8", "UTF-16-BE", "UTF-32-BE"`.
The unicode encoding to use in the output. Must be one of
`"UTF-8", "UTF-16-BE", "UTF-32-BE"`. Multi-byte encodings will be big-endian.
</td>
</tr><tr>
<td>
`errors`
</td>
<td>
An optional `string` from: `"strict", "replace", "ignore"`. Defaults to `"replace"`.
Error handling policy when there is invalid formatting found in the input.
The value of 'strict' will cause the operation to produce a InvalidArgument
error on any invalid input formatting. A value of 'replace' (the default) will
cause the operation to replace any invalid formatting in the input with the
`replacement_char` codepoint. A value of 'ignore' will cause the operation to
skip any invalid formatting in the input and produce no corresponding output
character.
</td>
</tr><tr>
<td>
`replacement_char`
</td>
<td>
An optional `int`. Defaults to `65533`.
The replacement character codepoint to be used in place of any invalid
formatting in the input when `errors='replace'`. Any valid unicode codepoint may
be used. The default value is the default unicode replacement character is
0xFFFD or U+65533.)

Note that for UTF-8, passing a replacement character expressible in 1 byte, such
as ' ', will preserve string alignment to the source since invalid bytes will be
replaced with a 1-byte replacement. For UTF-16-BE and UTF-16-LE, any 1 or 2 byte
replacement character will preserve byte alignment to the source.
</td>
</tr><tr>
<td>
`replace_control_characters`
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether to replace the C0 control characters (00-1F) with the
`replacement_char`. Default is false.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

