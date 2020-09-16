description: Split elements of input based on delimiter into a SparseTensor.

robots: noindex

# tf.raw_ops.StringSplit

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Split elements of `input` based on `delimiter` into a `SparseTensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StringSplit`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StringSplit(
    input, delimiter, skip_empty=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Let N be the size of source (typically N will be the batch size). Split each
element of `input` based on `delimiter` and return a `SparseTensor`
containing the splitted tokens. Empty tokens are ignored.

`delimiter` can be empty, or a string of split characters. If `delimiter` is an
 empty string, each element of `input` is split into individual single-byte
 character strings, including splitting of UTF-8 multibyte sequences. Otherwise
 every character of `delimiter` is a potential split point.

#### For example:

N = 2, input[0] is 'hello world' and input[1] is 'a b c', then the output
will be

indices = [0, 0;
           0, 1;
           1, 0;
           1, 1;
           1, 2]
shape = [2, 3]
values = ['hello', 'world', 'a', 'b', 'c']



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` of type `string`. 1-D. Strings to split.
</td>
</tr><tr>
<td>
`delimiter`
</td>
<td>
A `Tensor` of type `string`.
0-D. Delimiter characters (bytes), or empty string.
</td>
</tr><tr>
<td>
`skip_empty`
</td>
<td>
An optional `bool`. Defaults to `True`.
A `bool`. If `True`, skip the empty strings from the result.
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

