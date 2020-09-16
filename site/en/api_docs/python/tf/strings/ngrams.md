description: Create a tensor of n-grams based on data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.ngrams" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.ngrams

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ragged/ragged_string_ops.py#L671-L823">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Create a tensor of n-grams based on `data`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.strings.ngrams`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.ngrams(
    data, ngram_width, separator=' ', pad_values=None, padding_width=None,
    preserve_short_sequences=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Creates a tensor of n-grams based on `data`. The n-grams are created by
joining windows of `width` adjacent strings from the inner axis of `data`
using `separator`.

The input data can be padded on both the start and end of the sequence, if
desired, using the `pad_values` argument. If set, `pad_values` should contain
either a tuple of strings or a single string; the 0th element of the tuple
will be used to pad the left side of the sequence and the 1st element of the
tuple will be used to pad the right side of the sequence. The `padding_width`
arg controls how many padding values are added to each side; it defaults to
`ngram_width-1`.

If this op is configured to not have padding, or if it is configured to add
padding with `padding_width` set to less than ngram_width-1, it is possible
that a sequence, or a sequence plus padding, is smaller than the ngram
width. In that case, no ngrams will be generated for that sequence. This can
be prevented by setting `preserve_short_sequences`, which will cause the op
to always generate at least one ngram per non-empty sequence.

#### Examples:



```
>>> tf.strings.ngrams(["A", "B", "C", "D"], 2).numpy()
array([b'A B', b'B C', b'C D'], dtype=object)
>>> tf.strings.ngrams(["TF", "and", "keras"], 1).numpy()
array([b'TF', b'and', b'keras'], dtype=object)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A Tensor or RaggedTensor containing the source data for the ngrams.
</td>
</tr><tr>
<td>
`ngram_width`
</td>
<td>
The width(s) of the ngrams to create. If this is a list or
tuple, the op will return ngrams of all specified arities in list order.
Values must be non-Tensor integers greater than 0.
</td>
</tr><tr>
<td>
`separator`
</td>
<td>
The separator string used between ngram elements. Must be a
string constant, not a Tensor.
</td>
</tr><tr>
<td>
`pad_values`
</td>
<td>
A tuple of (left_pad_value, right_pad_value), a single string,
or None. If None, no padding will be added; if a single string, then that
string will be used for both left and right padding. Values must be Python
strings.
</td>
</tr><tr>
<td>
`padding_width`
</td>
<td>
If set, `padding_width` pad values will be added to both
sides of each sequence. Defaults to `ngram_width`-1. Must be greater than
0. (Note that 1-grams are never padded, regardless of this value.)
</td>
</tr><tr>
<td>
`preserve_short_sequences`
</td>
<td>
If true, then ensure that at least one ngram is
generated for each input sequence.  In particular, if an input sequence is
shorter than `min(ngram_width) + 2*pad_width`, then generate a single
ngram containing the entire sequence.  If false, then no ngrams are
generated for these short input sequences.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The op name.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A RaggedTensor of ngrams. If `data.shape=[D1...DN, S]`, then
`output.shape=[D1...DN, NUM_NGRAMS]`, where
`NUM_NGRAMS=S-ngram_width+1+2*padding_width`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if `pad_values` is set to an invalid type.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `pad_values`, `padding_width`, or `ngram_width` is set to an
invalid value.
</td>
</tr>
</table>

