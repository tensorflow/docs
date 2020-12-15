description: The gradient of SparseFillEmptyRows.

robots: noindex

# tf.raw_ops.SparseFillEmptyRowsGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



The gradient of SparseFillEmptyRows.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseFillEmptyRowsGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseFillEmptyRowsGrad(
    reverse_index_map, grad_values, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Takes vectors reverse_index_map, shaped `[N]`, and grad_values,
shaped `[N_full]`, where `N_full >= N` and copies data into either
`d_values` or `d_default_value`.  Here `d_values` is shaped `[N]` and
`d_default_value` is a scalar.

  d_values[j] = grad_values[reverse_index_map[j]]
  d_default_value = sum_{k : 0 .. N_full - 1} (
     grad_values[k] * 1{k not in reverse_index_map})

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`reverse_index_map`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  The reverse index map from SparseFillEmptyRows.
</td>
</tr><tr>
<td>
`grad_values`
</td>
<td>
A `Tensor`. 1-D.  The gradients from backprop.
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
A tuple of `Tensor` objects (d_values, d_default_value).
</td>
</tr>
<tr>
<td>
`d_values`
</td>
<td>
A `Tensor`. Has the same type as `grad_values`.
</td>
</tr><tr>
<td>
`d_default_value`
</td>
<td>
A `Tensor`. Has the same type as `grad_values`.
</td>
</tr>
</table>

