description: Encodes each sequence of Unicode code points in input into a string.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.unicode_encode" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.unicode_encode

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ragged/ragged_string_ops.py#L82-L175">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Encodes each sequence of Unicode code points in `input` into a string.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.strings.unicode_encode`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.unicode_encode(
    input, output_encoding, errors='replace', replacement_char=65533, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`result[i1...iN]` is the string formed by concatenating the Unicode
codepoints `input[1...iN, :]`, encoded using `output_encoding`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
An `N+1` dimensional potentially ragged integer tensor with shape
`[D1...DN, num_chars]`.
</td>
</tr><tr>
<td>
`output_encoding`
</td>
<td>
Unicode encoding that should be used to encode each
codepoint sequence.  Can be `"UTF-8"`, `"UTF-16-BE"`, or `"UTF-32-BE"`.
</td>
</tr><tr>
<td>
`errors`
</td>
<td>
Specifies the response when an invalid codepoint is encountered
(optional). One of:
* `'replace'`: Replace invalid codepoint with the
`replacement_char`. (default)
* `'ignore'`: Skip invalid codepoints.
* `'strict'`: Raise an exception for any invalid codepoint.
</td>
</tr><tr>
<td>
`replacement_char`
</td>
<td>
The replacement character codepoint to be used in place of
any invalid input when `errors='replace'`. Any valid unicode codepoint may
be used. The default value is the default unicode replacement character
which is 0xFFFD (U+65533).
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
A `N` dimensional `string` tensor with shape `[D1...DN]`.
</td>
</tr>

</table>


#### Example:

```
>>> input = tf.ragged.constant(
...     [[71, 246, 246, 100, 110, 105, 103, 104, 116], [128522]])
>>> print(unicode_encode(input, 'UTF-8'))
tf.Tensor([b'G\xc3\xb6\xc3\xb6dnight' b'\xf0\x9f\x98\x8a'],
          shape=(2,), dtype=string)
```