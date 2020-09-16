description: Split elements of input based on sep.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.strings.split" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.strings.split

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ragged/ragged_string_ops.py#L597-L661">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Split elements of `input` based on `sep`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.strings.split(
    input=None, sep=None, maxsplit=-1, result_type='SparseTensor', source=None,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Let N be the size of `input` (typically N will be the batch size). Split each
element of `input` based on `sep` and return a `SparseTensor` or
`RaggedTensor` containing the split tokens. Empty tokens are ignored.

#### Examples:



```
>>> print(tf.compat.v1.strings.split(['hello world', 'a b c']))
SparseTensor(indices=tf.Tensor( [[0 0] [0 1] [1 0] [1 1] [1 2]], ...),
             values=tf.Tensor([b'hello' b'world' b'a' b'b' b'c'], ...),
             dense_shape=tf.Tensor([2 3], shape=(2,), dtype=int64))
```

```
>>> print(tf.compat.v1.strings.split(['hello world', 'a b c'],
...     result_type="RaggedTensor"))
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
`0-D` string `Tensor`, the delimiter character.
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
`result_type`
</td>
<td>
The tensor type for the result: one of `"RaggedTensor"` or
`"SparseTensor"`.
</td>
</tr><tr>
<td>
`source`
</td>
<td>
alias for "input" argument.
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
A `SparseTensor` or `RaggedTensor` of rank `N+1`, the strings split
according to the delimiter.
</td>
</tr>

</table>

