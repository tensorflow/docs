page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.unicode_transcode


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/strings/unicode_transcode">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_string_ops.py`



Transcode the input text from a source encoding to a destination encoding.

### Aliases:

* <a href="/api_docs/python/tf/strings/unicode_transcode"><code>tf.compat.v1.strings.unicode_transcode</code></a>
* <a href="/api_docs/python/tf/strings/unicode_transcode"><code>tf.compat.v2.strings.unicode_transcode</code></a>


``` python
tf.strings.unicode_transcode(
    input,
    input_encoding,
    output_encoding,
    errors='replace',
    replacement_char=65533,
    replace_control_characters=False,
    name=None
)
```



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

#### Args:


* <b>`input`</b>: A `Tensor` of type `string`.
  The text to be processed. Can have any shape.
* <b>`input_encoding`</b>: A `string`.
  Text encoding of the input strings. This is any of the encodings supported
  by ICU ucnv algorithmic converters. Examples: `"UTF-16", "US ASCII", "UTF-8"`.
* <b>`output_encoding`</b>: A `string` from: `"UTF-8", "UTF-16-BE", "UTF-32-BE"`.
  The unicode encoding to use in the output. Must be one of
  `"UTF-8", "UTF-16-BE", "UTF-32-BE"`. Multi-byte encodings will be big-endian.
* <b>`errors`</b>: An optional `string` from: `"strict", "replace", "ignore"`. Defaults to `"replace"`.
  Error handling policy when there is invalid formatting found in the input.
  The value of 'strict' will cause the operation to produce a InvalidArgument
  error on any invalid input formatting. A value of 'replace' (the default) will
  cause the operation to replace any invalid formatting in the input with the
  `replacement_char` codepoint. A value of 'ignore' will cause the operation to
  skip any invalid formatting in the input and produce no corresponding output
  character.
* <b>`replacement_char`</b>: An optional `int`. Defaults to `65533`.
  The replacement character codepoint to be used in place of any invalid
  formatting in the input when `errors='replace'`. Any valid unicode codepoint may
  be used. The default value is the default unicode replacement character is
  0xFFFD or U+65533.)

  Note that for UTF-8, passing a replacement character expressible in 1 byte, such
  as ' ', will preserve string alignment to the source since invalid bytes will be
  replaced with a 1-byte replacement. For UTF-16-BE and UTF-16-LE, any 1 or 2 byte
  replacement character will preserve byte alignment to the source.
* <b>`replace_control_characters`</b>: An optional `bool`. Defaults to `False`.
  Whether to replace the C0 control characters (00-1F) with the
  `replacement_char`. Default is false.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
