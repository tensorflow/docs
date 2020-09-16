description: Split elements of source based on delimiter. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.string_split" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.string_split

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ragged/ragged_string_ops.py#L532-L592">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Split elements of `source` based on `delimiter`. (deprecated arguments)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.string_split(
    source, sep=None, skip_empty=(True), delimiter=None, result_type='SparseTensor',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(delimiter)`. They will be removed in a future version.
Instructions for updating:
delimiter is deprecated, please use sep instead.

Let N be the size of `source` (typically N will be the batch size). Split each
element of `source` based on `delimiter` and return a `SparseTensor`
or `RaggedTensor` containing the split tokens. Empty tokens are ignored.

If `sep` is an empty string, each element of the `source` is split
into individual strings, each containing one byte. (This includes splitting
multibyte sequences of UTF-8.) If delimiter contains multiple bytes, it is
treated as a set of delimiters with each considered a potential split point.

#### Examples:



```
>>> print(tf.compat.v1.string_split(['hello world', 'a b c']))
SparseTensor(indices=tf.Tensor( [[0 0] [0 1] [1 0] [1 1] [1 2]], ...),
             values=tf.Tensor([b'hello' b'world' b'a' b'b' b'c'], ...),
             dense_shape=tf.Tensor([2 3], shape=(2,), dtype=int64))
```

```
>>> print(tf.compat.v1.string_split(['hello world', 'a b c'],
...     result_type="RaggedTensor"))
<tf.RaggedTensor [[b'hello', b'world'], [b'a', b'b', b'c']]>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`source`
</td>
<td>
`1-D` string `Tensor`, the strings to split.
</td>
</tr><tr>
<td>
`sep`
</td>
<td>
`0-D` string `Tensor`, the delimiter character, the string should
be length 0 or 1. Default is ' '.
</td>
</tr><tr>
<td>
`skip_empty`
</td>
<td>
A `bool`. If `True`, skip the empty strings from the result.
</td>
</tr><tr>
<td>
`delimiter`
</td>
<td>
deprecated alias for `sep`.
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
If delimiter is not a string.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` or `RaggedTensor` of rank `2`, the strings split according
to the delimiter.  The first column of the indices corresponds to the row
in `source` and the second column corresponds to the index of the split
component in this row.
</td>
</tr>

</table>

