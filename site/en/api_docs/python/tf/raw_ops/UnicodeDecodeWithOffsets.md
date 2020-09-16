description: Decodes each string in input into a sequence of Unicode code points.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.UnicodeDecodeWithOffsets" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.UnicodeDecodeWithOffsets

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Decodes each string in `input` into a sequence of Unicode code points.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.UnicodeDecodeWithOffsets`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.UnicodeDecodeWithOffsets(
    input, input_encoding, errors='replace', replacement_char=65533,
    replace_control_characters=(False), Tsplits=tf.dtypes.int64, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The character codepoints for all strings are returned using a single vector
`char_values`, with strings expanded to characters in row-major order.
Similarly, the character start byte offsets are returned using a single vector
`char_to_byte_starts`, with strings expanded in row-major order.

The `row_splits` tensor indicates where the codepoints and start offsets for
each input string begin and end within the `char_values` and
`char_to_byte_starts` tensors.  In particular, the values for the `i`th
string (in row-major order) are stored in the slice
`[row_splits[i]:row_splits[i+1]]`. Thus:

* `char_values[row_splits[i]+j]` is the Unicode codepoint for the `j`th
  character in the `i`th string (in row-major order).
* `char_to_bytes_starts[row_splits[i]+j]` is the start byte offset for the `j`th
  character in the `i`th string (in row-major order).
* `row_splits[i+1] - row_splits[i]` is the number of characters in the `i`th
  string (in row-major order).

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
The text to be decoded. Can have any shape. Note that the output is flattened
to a vector of char values.
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
`Tsplits`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int64"><code>tf.int64</code></a>.
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
A tuple of `Tensor` objects (row_splits, char_values, char_to_byte_starts).
</td>
</tr>
<tr>
<td>
`row_splits`
</td>
<td>
A `Tensor` of type `Tsplits`.
</td>
</tr><tr>
<td>
`char_values`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`char_to_byte_starts`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

