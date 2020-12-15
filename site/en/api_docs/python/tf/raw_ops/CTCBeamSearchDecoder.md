description: Performs beam search decoding on the logits given in input.

robots: noindex

# tf.raw_ops.CTCBeamSearchDecoder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Performs beam search decoding on the logits given in input.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CTCBeamSearchDecoder`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CTCBeamSearchDecoder(
    inputs, sequence_length, beam_width, top_paths, merge_repeated=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A note about the attribute merge_repeated: For the beam search decoder,
this means that if consecutive entries in a beam are the same, only
the first of these is emitted.  That is, when the top path is "A B B B B",
"A B" is returned if merge_repeated = True but "A B B B B" is
returned if merge_repeated = False.

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
A vector containing sequence lengths, size `(batch)`.
</td>
</tr><tr>
<td>
`beam_width`
</td>
<td>
An `int` that is `>= 1`.
A scalar >= 0 (beam search beam width).
</td>
</tr><tr>
<td>
`top_paths`
</td>
<td>
An `int` that is `>= 1`.
A scalar >= 0, <= beam_width (controls output size).
</td>
</tr><tr>
<td>
`merge_repeated`
</td>
<td>
An optional `bool`. Defaults to `True`.
If true, merge repeated classes in output.
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
A list of `top_paths` `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`decoded_values`
</td>
<td>
A list of `top_paths` `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`decoded_shape`
</td>
<td>
A list of `top_paths` `Tensor` objects with type `int64`.
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

