page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.ngrams


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/strings/ngrams">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_string_ops.py#L656-L800">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create a tensor of n-grams based on `data`.

### Aliases:

* <a href="/api_docs/python/tf/strings/ngrams"><code>tf.compat.v1.strings.ngrams</code></a>
* <a href="/api_docs/python/tf/strings/ngrams"><code>tf.compat.v2.strings.ngrams</code></a>


``` python
tf.strings.ngrams(
    data,
    ngram_width,
    separator=' ',
    pad_values=None,
    padding_width=None,
    preserve_short_sequences=False,
    name=None
)
```



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

#### Args:


* <b>`data`</b>: A Tensor or RaggedTensor containing the source data for the ngrams.
* <b>`ngram_width`</b>: The width(s) of the ngrams to create. If this is a list or
  tuple, the op will return ngrams of all specified arities in list order.
  Values must be non-Tensor integers greater than 0.
* <b>`separator`</b>: The separator string used between ngram elements. Must be a
  string constant, not a Tensor.
* <b>`pad_values`</b>: A tuple of (left_pad_value, right_pad_value), a single string,
  or None. If None, no padding will be added; if a single string, then that
  string will be used for both left and right padding. Values must be Python
  strings.
* <b>`padding_width`</b>: If set, `padding_width` pad values will be added to both
  sides of each sequence. Defaults to `ngram_width`-1. Must be greater than
  0. (Note that 1-grams are never padded, regardless of this value.)
* <b>`preserve_short_sequences`</b>: If true, then ensure that at least one ngram is
  generated for each input sequence.  In particular, if an input sequence is
  shorter than `min(ngram_width) + 2*pad_width`, then generate a single
  ngram containing the entire sequence.  If false, then no ngrams are
  generated for these short input sequences.
* <b>`name`</b>: The op name.


#### Returns:

A RaggedTensor of ngrams. If `data.shape=[D1...DN, S]`, then
`output.shape=[D1...DN, NUM_NGRAMS]`, where
`NUM_NGRAMS=S-ngram_width+1+2*padding_width`.



#### Raises:


* <b>`TypeError`</b>: if `pad_values` is set to an invalid type.
* <b>`ValueError`</b>: if `pad_values`, `padding_width`, or `ngram_width` is set to an
  invalid value.
