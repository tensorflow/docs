description: Performs greedy decoding on the logits given in inputs.

robots: noindex

# tf.raw_ops.CTCGreedyDecoder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Performs greedy decoding on the logits given in inputs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CTCGreedyDecoder`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CTCGreedyDecoder(
    inputs, sequence_length, merge_repeated=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A note about the attribute merge_repeated: if enabled, when
consecutive logits' maximum indices are the same, only the first of
these is emitted.  Labeling the blank '*', the sequence "A B B * B B"
becomes "A B B" if merge_repeated = True and "A B B B B" if
merge_repeated = False.

Regardless of the value of merge_repeated, if the maximum index of a given
time and batch corresponds to the blank, index `(num_classes - 1)`, no new
element is emitted.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`.
3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
</td>
</tr><tr>
<td>
`sequence_length`
</td>
<td>
A `Tensor` of type `int32`.
A vector containing sequence lengths, size `(batch_size)`.
</td>
</tr><tr>
<td>
`merge_repeated`
</td>
<td>
An optional `bool`. Defaults to `False`.
If True, merge repeated classes in output.
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
A tuple of `Tensor` objects (decoded_indices, decoded_values, decoded_shape, log_probability).
</td>
</tr>
<tr>
<td>
`decoded_indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`decoded_values`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`decoded_shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`log_probability`
</td>
<td>
A `Tensor`. Has the same type as `inputs`.
</td>
</tr>
</table>

