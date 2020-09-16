description: Computes gradients of the average pooling function.

robots: noindex

# tf.raw_ops.AvgPoolGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes gradients of the average pooling function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AvgPoolGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AvgPoolGrad(
    orig_input_shape, grad, ksize, strides, padding, data_format='NHWC', name=None
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
1-D.  Shape of the original input to `avg_pool`.
</td>
</tr><tr>
<td>
`grad`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
4-D with shape `[batch, height, width, channels]`.  Gradients w.r.t.
the output of `avg_pool`.
</td>
</tr><tr>
<td>
`ksize`
</td>
<td>
A list of `ints` that has length `>= 4`.
The size of the sliding window for each dimension of the input.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints` that has length `>= 4`.
The stride of the sliding window for each dimension of the input.
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
An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`.
Specify the data format of the input and output data. With the
default format "NHWC", the data is stored in the order of:
[batch, in_height, in_width, in_channels].
Alternatively, the format could be "NCHW", the data storage order of:
[batch, in_channels, in_height, in_width].
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

