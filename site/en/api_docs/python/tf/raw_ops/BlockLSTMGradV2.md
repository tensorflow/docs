description: Computes the LSTM cell backward propagation for the entire time sequence.

robots: noindex

# tf.raw_ops.BlockLSTMGradV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the LSTM cell backward propagation for the entire time sequence.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BlockLSTMGradV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BlockLSTMGradV2(
    seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h,
    cs_grad, h_grad, use_peephole, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This implementation is to be used in conjunction of BlockLSTMV2.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`seq_len_max`
</td>
<td>
A `Tensor` of type `int64`.
Maximum time length actually used by this input. Outputs are padded
with zeros beyond this length.
</td>
</tr><tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`.
The sequence input to the LSTM, shape (timelen, batch_size, num_inputs).
</td>
</tr><tr>
<td>
`cs_prev`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
Value of the initial cell state.
</td>
</tr><tr>
<td>
`h_prev`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
Initial output of cell (to be used for peephole).
</td>
</tr><tr>
<td>
`w`
</td>
<td>
A `Tensor`. Must have the same type as `x`. The weight matrix.
</td>
</tr><tr>
<td>
`wci`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The weight matrix for input gate peephole connection.
</td>
</tr><tr>
<td>
`wcf`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The weight matrix for forget gate peephole connection.
</td>
</tr><tr>
<td>
`wco`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The weight matrix for output gate peephole connection.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
A `Tensor`. Must have the same type as `x`. The bias vector.
</td>
</tr><tr>
<td>
`i`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The input gate over the whole time sequence.
</td>
</tr><tr>
<td>
`cs`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The cell state before the tanh over the whole time sequence.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The forget gate over the whole time sequence.
</td>
</tr><tr>
<td>
`o`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The output gate over the whole time sequence.
</td>
</tr><tr>
<td>
`ci`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The cell input over the whole time sequence.
</td>
</tr><tr>
<td>
`co`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The cell after the tanh over the whole time sequence.
</td>
</tr><tr>
<td>
`h`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The output h vector over the whole time sequence.
</td>
</tr><tr>
<td>
`cs_grad`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The current gradient of cs.
</td>
</tr><tr>
<td>
`h_grad`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The gradient of h vector.
</td>
</tr><tr>
<td>
`use_peephole`
</td>
<td>
A `bool`. Whether to use peephole weights.
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
A tuple of `Tensor` objects (x_grad, cs_prev_grad, h_prev_grad, w_grad, wci_grad, wcf_grad, wco_grad, b_grad).
</td>
</tr>
<tr>
<td>
`x_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`cs_prev_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`h_prev_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`w_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`wci_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`wcf_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`wco_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`b_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr>
</table>

