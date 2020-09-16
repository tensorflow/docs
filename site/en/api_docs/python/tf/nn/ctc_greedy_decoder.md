description: Performs greedy decoding on the logits given in input (best path).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.ctc_greedy_decoder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.ctc_greedy_decoder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ctc_ops.py#L286-L332">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Performs greedy decoding on the logits given in input (best path).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.ctc_greedy_decoder`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.ctc_greedy_decoder(
    inputs, sequence_length, merge_repeated=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: Regardless of the value of merge_repeated, if the maximum index of a
given time and batch corresponds to the blank index `(num_classes - 1)`, no
new element is emitted.

If `merge_repeated` is `True`, merge repeated classes in output.
This means that if consecutive logits' maximum indices are the same,
only the first of these is emitted.  The sequence `A B B * B * B` (where '*'
is the blank label) becomes

  * `A B B B` if `merge_repeated=True`.
  * `A B B B B` if `merge_repeated=False`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
3-D `float` `Tensor` sized `[max_time, batch_size, num_classes]`.
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
A tuple `(decoded, neg_sum_logits)` where
</td>
</tr>
<tr>
<td>
`decoded`
</td>
<td>
A single-element list. `decoded[0]`
is an `SparseTensor` containing the decoded outputs s.t.:

`decoded.indices`: Indices matrix `(total_decoded_outputs, 2)`.
The rows store: `[batch, time]`.

`decoded.values`: Values vector, size `(total_decoded_outputs)`.
The vector stores the decoded classes.

`decoded.dense_shape`: Shape vector, size `(2)`.
The shape values are: `[batch_size, max_decoded_length]`
</td>
</tr><tr>
<td>
`neg_sum_logits`
</td>
<td>
A `float` matrix `(batch_size x 1)` containing, for the
sequence found, the negative of the sum of the greatest logit at each
timeframe.
</td>
</tr>
</table>

