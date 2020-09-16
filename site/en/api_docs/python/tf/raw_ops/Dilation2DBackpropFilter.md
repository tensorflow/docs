description: Computes the gradient of morphological 2-D dilation with respect to the filter.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Dilation2DBackpropFilter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Dilation2DBackpropFilter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the gradient of morphological 2-D dilation with respect to the filter.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Dilation2DBackpropFilter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Dilation2DBackpropFilter(
    input, filter, out_backprop, strides, rates, padding, name=None
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
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
4-D with shape `[batch, in_height, in_width, depth]`.
</td>
</tr><tr>
<td>
`filter`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
3-D with shape `[filter_height, filter_width, depth]`.
</td>
</tr><tr>
<td>
`out_backprop`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
4-D with shape `[batch, out_height, out_width, depth]`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints` that has length `>= 4`.
1-D of length 4. The stride of the sliding window for each dimension of
the input tensor. Must be: `[1, stride_height, stride_width, 1]`.
</td>
</tr><tr>
<td>
`rates`
</td>
<td>
A list of `ints` that has length `>= 4`.
1-D of length 4. The input stride for atrous morphological dilation.
Must be: `[1, rate_height, rate_width, 1]`.
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

