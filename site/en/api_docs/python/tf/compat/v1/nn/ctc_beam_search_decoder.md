description: Performs beam search decoding on the logits given in input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.ctc_beam_search_decoder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.ctc_beam_search_decoder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ctc_ops.py#L338-L398">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Performs beam search decoding on the logits given in input.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.ctc_beam_search_decoder(
    inputs, sequence_length, beam_width=100, top_paths=1, merge_repeated=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

**Note** The `ctc_greedy_decoder` is a special case of the
`ctc_beam_search_decoder` with `top_paths=1` and `beam_width=1` (but
that decoder is faster for this special case).

If `merge_repeated` is `True`, merge repeated classes in the output beams.
This means that if consecutive entries in a beam are the same,
only the first of these is emitted.  That is, when the sequence is
`A B B * B * B` (where '*' is the blank label), the return value is:

  * `A B` if `merge_repeated = True`.
  * `A B B B` if `merge_repeated = False`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
3-D `float` `Tensor`, size `[max_time x batch_size x num_classes]`.
The logits.
</td>
</tr><tr>
<td>
`sequence_length`
</td>
<td>
1-D `int32` vector containing sequence lengths, having size
`[batch_size]`.
</td>
</tr><tr>
<td>
`beam_width`
</td>
<td>
An int scalar >= 0 (beam search beam width).
</td>
</tr><tr>
<td>
`top_paths`
</td>
<td>
An int scalar >= 0, <= beam_width (controls output size).
</td>
</tr><tr>
<td>
`merge_repeated`
</td>
<td>
Boolean.  Default: True.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple `(decoded, log_probabilities)` where
</td>
</tr>
<tr>
<td>
`decoded`
</td>
<td>
A list of length top_paths, where `decoded[j]`
is a `SparseTensor` containing the decoded outputs:

`decoded[j].indices`: Indices matrix `(total_decoded_outputs[j] x 2)`
The rows store: [batch, time].

`decoded[j].values`: Values vector, size `(total_decoded_outputs[j])`.
The vector stores the decoded classes for beam j.

`decoded[j].dense_shape`: Shape vector, size `(2)`.
The shape values are: `[batch_size, max_decoded_length[j]]`.
</td>
</tr><tr>
<td>
`log_probability`
</td>
<td>
A `float` matrix `(batch_size x top_paths)` containing
sequence log-probabilities.
</td>
</tr>
</table>

