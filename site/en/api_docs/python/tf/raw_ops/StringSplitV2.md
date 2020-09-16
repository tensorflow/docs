description: Split elements of source based on sep into a SparseTensor.

robots: noindex

# tf.raw_ops.StringSplitV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Split elements of `source` based on `sep` into a `SparseTensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StringSplitV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StringSplitV2(
    input, sep, maxsplit=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Let N be the size of source (typically N will be the batch size). Split each
element of `source` based on `sep` and return a `SparseTensor`
containing the split tokens. Empty tokens are ignored.

For example, N = 2, source[0] is 'hello world' and source[1] is 'a b c',
then the output will be
```
st.indices = [0, 0;
              0, 1;
              1, 0;
              1, 1;
              1, 2]
st.shape = [2, 3]
st.values = ['hello', 'world', 'a', 'b', 'c']
```

If `sep` is given, consecutive delimiters are not grouped together and are
deemed to delimit empty strings. For example, source of `"1<>2<><>3"` and
sep of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty
string, consecutive whitespace are regarded as a single separator, and the
result will contain no empty strings at the startor end if the string has
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
A `Tensor` of type `string`.
`1-D` string `Tensor`, the strings to split.
</td>
</tr><tr>
<td>
`sep`
</td>
<td>
A `Tensor` of type `string`.
`0-D` string `Tensor`, the delimiter character.
</td>
</tr><tr>
<td>
`maxsplit`
</td>
<td>
An optional `int`. Defaults to `-1`.
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
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple of `Tensor` objects (indices, values, shape).
</td>
</tr>
<tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

