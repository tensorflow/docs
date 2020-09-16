description: Computes gradients of average pooling function.

robots: noindex

# tf.raw_ops.AvgPool3DGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes gradients of average pooling function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AvgPool3DGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AvgPool3DGrad(
    orig_input_shape, grad, ksize, strides, padding, data_format='NDHWC', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`orig_input_shape`
</td>
<td>
A `Tensor` of type `int32`.
The original input dimensions.
</td>
</tr><tr>
<td>
`grad`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
Output backprop of shape `[batch, depth, rows, cols, channels]`.
</td>
</tr><tr>
<td>
`ksize`
</td>
<td>
A list of `ints` that has length `>= 5`.
1-D tensor of length 5. The size of the window for each dimension of
the input tensor. Must have `ksize[0] = ksize[4] = 1`.
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
`data_format`
</td>
<td>
An optional `string` from: `"NDHWC", "NCDHW"`. Defaults to `"NDHWC"`.
The data format of the input and output data. With the
default format "NDHWC", the data is stored in the order of:
[batch, in_depth, in_height, in_width, in_channels].
Alternatively, the format could be "NCDHW", the data storage order is:
[batch, in_channels, in_depth, in_height, in_width].
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
A `Tensor`. Has the same type as `grad`.
</td>
</tr>

</table>

