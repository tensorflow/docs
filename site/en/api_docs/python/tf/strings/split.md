description: Split elements of input based on sep into a RaggedTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.split" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.split

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ragged/ragged_string_ops.py#L455-L513">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Split elements of `input` based on `sep` into a `RaggedTensor`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.split(
    input, sep=None, maxsplit=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Let N be the size of `input` (typically N will be the batch size). Split each
element of `input` based on `sep` and return a `RaggedTensor` containing the 
split tokens. Empty tokens are ignored.

#### Example:



```
>>> tf.strings.split('hello world').numpy()
 array([b'hello', b'world'], dtype=object)
>>> tf.strings.split(['hello world', 'a b c'])
<tf.RaggedTensor [[b'hello', b'world'], [b'a', b'b', b'c']]>
```

If `sep` is given, consecutive delimiters are not grouped together and are
deemed to delimit empty strings. For example, `input` of `"1<>2<><>3"` and
`sep` of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty
string, consecutive whitespace are regarded as a single separator, and the
result will contain no empty strings at the start or end if the string has
leading or trailing whitespace.

Note that the above mentioned behavior matches python's str.split.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A string `Tensor` of rank `N`, the strings to split.  If
`rank(input)` is not known statically, then it is assumed to be `1`.
</td>
</tr><tr>
<td>
`sep`
</td>
<td>
`0-D` string `Tensor`, the delimiter string.
</td>
</tr><tr>
<td>
`maxsplit`
</td>
<td>
An `int`. If `maxsplit > 0`, limit of the split of the result.
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
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If sep is not a string.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` of rank `N+1`, the strings split according to the
delimiter.
</td>
</tr>

</table>

