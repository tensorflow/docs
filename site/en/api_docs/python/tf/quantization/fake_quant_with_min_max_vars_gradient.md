description: Compute gradients for a FakeQuantWithMinMaxVars operation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.quantization.fake_quant_with_min_max_vars_gradient" />
<meta itemprop="path" content="Stable" />
</div>

# tf.quantization.fake_quant_with_min_max_vars_gradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Compute gradients for a FakeQuantWithMinMaxVars operation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.fake_quant_with_min_max_vars_gradient`, `tf.compat.v1.quantization.fake_quant_with_min_max_vars_gradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.quantization.fake_quant_with_min_max_vars_gradient(
    gradients, inputs, min, max, num_bits=8, narrow_range=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`gradients`
</td>
<td>
A `Tensor` of type `float32`.
Backpropagated gradients above the FakeQuantWithMinMaxVars operation.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A `Tensor` of type `float32`.
Values passed as inputs to the FakeQuantWithMinMaxVars operation.
min, max: Quantization interval, scalar floats.
</td>
</tr><tr>
<td>
`min`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`max`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`num_bits`
</td>
<td>
An optional `int`. Defaults to `8`.
The bitwidth of the quantization; between 2 and 8, inclusive.
</td>
</tr><tr>
<td>
`narrow_range`
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether to quantize into 2^num_bits - 1 distinct values.
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
A tuple of `Tensor` objects (backprops_wrt_input, backprop_wrt_min, backprop_wrt_max).
</td>
</tr>
<tr>
<td>
`backprops_wrt_input`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`backprop_wrt_min`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`backprop_wrt_max`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

