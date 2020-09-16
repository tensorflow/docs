description: Creates ngrams from ragged string data.

robots: noindex

# tf.raw_ops.StringNGrams

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates ngrams from ragged string data.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StringNGrams`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StringNGrams(
    data, data_splits, separator, ngram_widths, left_pad, right_pad, pad_width,
    preserve_short_sequences, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op accepts a ragged tensor with 1 ragged dimension containing only
strings and outputs a ragged tensor with 1 ragged dimension containing ngrams
of that string, joined along the innermost axis.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A `Tensor` of type `string`.
The values tensor of the ragged string tensor to make ngrams out of. Must be a
1D string tensor.
</td>
</tr><tr>
<td>
`data_splits`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
The splits tensor of the ragged string tensor to make ngrams out of.
</td>
</tr><tr>
<td>
`separator`
</td>
<td>
A `string`.
The string to append between elements of the token. Use "" for no separator.
</td>
</tr><tr>
<td>
`ngram_widths`
</td>
<td>
A list of `ints`. The sizes of the ngrams to create.
</td>
</tr><tr>
<td>
`left_pad`
</td>
<td>
A `string`.
The string to use to pad the left side of the ngram sequence. Only used if
pad_width != 0.
</td>
</tr><tr>
<td>
`right_pad`
</td>
<td>
A `string`.
The string to use to pad the right side of the ngram sequence. Only used if
pad_width != 0.
</td>
</tr><tr>
<td>
`pad_width`
</td>
<td>
An `int`.
The number of padding elements to add to each side of each
sequence. Note that padding will never be greater than 'ngram_widths'-1
regardless of this value. If `pad_width=-1`, then add `max(ngram_widths)-1`
elements.
</td>
</tr><tr>
<td>
`preserve_short_sequences`
</td>
<td>
A `bool`.
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
A tuple of `Tensor` objects (ngrams, ngrams_splits).
</td>
</tr>
<tr>
<td>
`ngrams`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`ngrams_splits`
</td>
<td>
A `Tensor`. Has the same type as `data_splits`.
</td>
</tr>
</table>

