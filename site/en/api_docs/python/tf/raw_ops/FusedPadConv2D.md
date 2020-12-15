description: Performs a padding as a preprocess during a convolution.

robots: noindex

# tf.raw_ops.FusedPadConv2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Performs a padding as a preprocess during a convolution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.FusedPadConv2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.FusedPadConv2D(
    input, paddings, filter, mode, strides, padding, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Similar to FusedResizeAndPadConv2d, this op allows for an optimized
implementation where the spatial padding transformation stage is fused with the
im2col lookup, but in this case without the bilinear filtering required for
resizing. Fusing the padding prevents the need to write out the intermediate
results as whole tensors, reducing memory pressure, and we can get some latency
gains by merging the transformation calculations.
The data_format attribute for Conv2D isn't supported by this op, and 'NHWC'
order is used instead.
Internally this op uses a single per-graph scratch buffer, which means that it
will block if multiple versions are being run in parallel. This is because this
operator is primarily an optimization to minimize memory usage.

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
4-D with shape `[batch, in_height, in_width, in_channels]`.
</td>
</tr><tr>
<td>
`paddings`
</td>
<td>
A `Tensor` of type `int32`.
A two-column matrix specifying the padding sizes. The number of
rows must be the same as the rank of `input`.
</td>
</tr><tr>
<td>
`filter`
</td>
<td>
A `Tensor`. Must have the same type as `input`. 4-D with shape
`[filter_height, filter_width, in_channels, out_channels]`.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
A `string` from: `"REFLECT", "SYMMETRIC"`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints`.
1-D of length 4.  The stride of the sliding window for each dimension
of `input`. Must be in the same order as the dimension specified with format.
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

