description: Decodes each string in input into a sequence of Unicode code points.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.unicode_decode" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.unicode_decode

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ragged/ragged_string_ops.py#L179-L221">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Decodes each string in `input` into a sequence of Unicode code points.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.strings.unicode_decode`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.unicode_decode(
    input, input_encoding, errors='replace', replacement_char=65533,
    replace_control_characters=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`result[i1...iN, j]` is the Unicode codepoint for the `j`th character in
`input[i1...iN]`, when decoded using `input_encoding`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
An `N` dimensional potentially ragged `string` tensor with shape
`[D1...DN]`.  `N` must be statically known.
</td>
</tr><tr>
<td>
`input_encoding`
</td>
<td>
String name for the unicode encoding that should be used to
decode each string.
</td>
</tr><tr>
<td>
`errors`
</td>
<td>
Specifies the response when an input string can't be converted
using the indicated encoding. One of:
* `'strict'`: Raise an exception for any illegal substrings.
* `'replace'`: Replace illegal substrings with `replacement_char`.
* `'ignore'`: Skip illegal substrings.
</td>
</tr><tr>
<td>
`replacement_char`
</td>
<td>
The replacement codepoint to be used in place of invalid
substrings in `input` when `errors='replace'`; and in place of C0 control
characters in `input` when `replace_control_characters=True`.
</td>
</tr><tr>
<td>
`replace_control_characters`
</td>
<td>
Whether to replace the C0 control characters
`(U+0000 - U+001F)` with the `replacement_char`.
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
A `N+1` dimensional `int32` tensor with shape `[D1...DN, (num_chars)]`.
The returned tensor is a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> if `input` is a scalar, or a
<a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> otherwise.
</td>
</tr>

</table>


#### Example:

```
>>> input = [s.encode('utf8') for s in (u'G\xf6\xf6dnight', u'\U0001f60a')]
>>> tf.strings.unicode_decode(input, 'UTF-8').to_list()
[[71, 246, 246, 100, 110, 105, 103, 104, 116], [128522]]
```