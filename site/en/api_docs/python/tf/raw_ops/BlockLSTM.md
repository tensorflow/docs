description: Computes the LSTM cell forward propagation for all the time steps.

robots: noindex

# tf.raw_ops.BlockLSTM

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the LSTM cell forward propagation for all the time steps.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BlockLSTM`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BlockLSTM(
    seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias=1,
    cell_clip=3, use_peephole=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is equivalent to applying LSTMBlockCell in a loop, like so:

```python
for x1 in unpack(x):
  i1, cs1, f1, o1, ci1, co1, h1 = LSTMBlock(
    x1, cs_prev, h_prev, w, wci, wcf, wco, b)
  cs_prev = cs1
  h_prev = h1
  i.append(i1)
  cs.append(cs1)
  f.append(f1)
  o.append(o1)
  ci.append(ci1)
  co.append(co1)
  h.append(h1)
return pack(i), pack(cs), pack(f), pack(o), pack(ci), pack(ch), pack(h)
```

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
`forget_bias`
</td>
<td>
An optional `float`. Defaults to `1`. The forget gate bias.
</td>
</tr><tr>
<td>
`cell_clip`
</td>
<td>
An optional `float`. Defaults to `3`.
Value to clip the 'cs' value to.
</td>
</tr><tr>
<td>
`use_peephole`
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether to use peephole weights.
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
A tuple of `Tensor` objects (i, cs, f, o, ci, co, h).
</td>
</tr>
<tr>
<td>
`i`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`cs`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`o`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`ci`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`co`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`h`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr>
</table>

