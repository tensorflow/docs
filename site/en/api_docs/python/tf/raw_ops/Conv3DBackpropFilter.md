description: Computes the gradients of 3-D convolution with respect to the filter.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Conv3DBackpropFilter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Conv3DBackpropFilter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the gradients of 3-D convolution with respect to the filter.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Conv3DBackpropFilter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Conv3DBackpropFilter(
    input, filter, out_backprop, strides, padding, dilations=[1, 1, 1, 1, 1],
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
Shape `[batch, depth, rows, cols, in_channels]`.
</td>
</tr><tr>
<td>
`filter`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
Shape `[depth, rows, cols, in_channels, out_channels]`.
`in_channels` must match between `input` and `filter`.
</td>
</tr><tr>
<td>
`out_backprop`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
Backprop signal of shape `[batch, out_depth, out_rows, out_cols,
out_channels]`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints` that has length `>= 5`.
1-D tensor of length 5. The stride of the sliding window for each
dimension of `input`. Must have `strides[0] = strides[4] = 1`.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A `string` from: `"SAME", "VALID"`.
The type of padding algorithm to use.
</td>
</tr><tr>
<td>
`dilations`
</td>
<td>
An optional list of `ints`. Defaults to `[1, 1, 1, 1, 1]`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

