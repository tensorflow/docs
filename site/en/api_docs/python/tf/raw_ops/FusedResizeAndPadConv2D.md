description: Performs a resize and padding as a preprocess during a convolution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.FusedResizeAndPadConv2D" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.FusedResizeAndPadConv2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Performs a resize and padding as a preprocess during a convolution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.FusedResizeAndPadConv2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.FusedResizeAndPadConv2D(
    input, size, paddings, filter, mode, strides, padding,
    resize_align_corners=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It's often possible to do spatial transformations more efficiently as part of
the packing stage of a convolution, so this op allows for an optimized
implementation where these stages are fused together. This prevents the need to
write out the intermediate results as whole tensors, reducing memory pressure,
and we can get some latency gains by merging the transformation calculations.
The data_format attribute for Conv2D isn't supported by this op, and defaults to
'NHWC' order.
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
`size`
</td>
<td>
A `Tensor` of type `int32`.
A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The
new size for the images.
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
`resize_align_corners`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, the centers of the 4 corner pixels of the input and output tensors are
aligned, preserving the values at the corner pixels. Defaults to false.
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

