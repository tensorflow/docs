description: Computes the LSTM cell backward propagation for 1 timestep.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.LSTMBlockCellGrad" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.LSTMBlockCellGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the LSTM cell backward propagation for 1 timestep.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.LSTMBlockCellGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.LSTMBlockCellGrad(
    x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, cs_grad, h_grad,
    use_peephole, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This implementation is to be used in conjunction of LSTMBlockCell.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`.
The input to the LSTM cell, shape (batch_size, num_inputs).
</td>
</tr><tr>
<td>
`cs_prev`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The previous cell state.
</td>
</tr><tr>
<td>
`h_prev`
</td>
<td>
A `Tensor`. Must have the same type as `x`. The previous h state.
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
A `Tensor`. Must have the same type as `x`. The input gate.
</td>
</tr><tr>
<td>
`cs`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
The cell state before the tanh.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A `Tensor`. Must have the same type as `x`. The forget gate.
</td>
</tr><tr>
<td>
`o`
</td>
<td>
A `Tensor`. Must have the same type as `x`. The output gate.
</td>
</tr><tr>
<td>
`ci`
</td>
<td>
A `Tensor`. Must have the same type as `x`. The cell input.
</td>
</tr><tr>
<td>
`co`
</td>
<td>
A `Tensor`. Must have the same type as `x`. The cell after the tanh.
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
A `bool`. Whether the cell uses peephole connections.
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
A tuple of `Tensor` objects (cs_prev_grad, dicfo, wci_grad, wcf_grad, wco_grad).
</td>
</tr>
<tr>
<td>
`cs_prev_grad`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`dicfo`
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
</tr>
</table>

