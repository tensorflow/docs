description: Encode a tensor of ints into unicode strings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.UnicodeEncode" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.UnicodeEncode

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Encode a tensor of ints into unicode strings.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.UnicodeEncode`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.UnicodeEncode(
    input_values, input_splits, output_encoding, errors='replace',
    replacement_char=65533, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a vector of strings, where `output[i]` is constructed by encoding the
Unicode codepoints in `input_values[input_splits[i]:input_splits[i+1]]`
using `output_encoding`.

---

#### Example:



```
input_values = [72, 101, 108, 108, 111, 87, 111, 114, 108, 100]
input_splits = [0, 5, 10]
output_encoding = 'UTF-8'

output = ['Hello', 'World']
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_values`
</td>
<td>
A `Tensor` of type `int32`.
A 1D tensor containing the unicode codepoints that should be encoded.
</td>
</tr><tr>
<td>
`input_splits`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A 1D tensor specifying how the unicode codepoints should be split into strings.
In particular, `output[i]` is constructed by encoding the codepoints in the
slice `input_values[input_splits[i]:input_splits[i+1]]`.
</td>
</tr><tr>
<td>
`output_encoding`
</td>
<td>
A `string` from: `"UTF-8", "UTF-16-BE", "UTF-32-BE"`.
Unicode encoding of the output strings. Valid encodings are: `"UTF-8",
"UTF-16-BE", and "UTF-32-BE"`.
</td>
</tr><tr>
<td>
`errors`
</td>
<td>
An optional `string` from: `"ignore", "replace", "strict"`. Defaults to `"replace"`.
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
0xFFFD (U+65533).
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

