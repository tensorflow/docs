description: Computes gradient of the FractionalAvgPool function.

robots: noindex

# tf.raw_ops.FractionalAvgPoolGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes gradient of the FractionalAvgPool function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.FractionalAvgPoolGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.FractionalAvgPoolGrad(
    orig_input_tensor_shape, out_backprop, row_pooling_sequence,
    col_pooling_sequence, overlapping=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Unlike FractionalMaxPoolGrad, we don't need to find arg_max for
FractionalAvgPoolGrad, we just need to evenly back-propagate each element of
out_backprop to those indices that form the same pooling cell. Therefore, we
just need to know the shape of original input tensor, instead of the whole
tensor.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`orig_input_tensor_shape`
</td>
<td>
A `Tensor` of type `int64`.
Original input tensor shape for `fractional_avg_pool`
</td>
</tr><tr>
<td>
`out_backprop`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `int64`.
4-D with shape `[batch, height, width, channels]`.  Gradients
w.r.t. the output of `fractional_avg_pool`.
</td>
</tr><tr>
<td>
`row_pooling_sequence`
</td>
<td>
A `Tensor` of type `int64`.
row pooling sequence, form pooling region with
col_pooling_sequence.
</td>
</tr><tr>
<td>
`col_pooling_sequence`
</td>
<td>
A `Tensor` of type `int64`.
column pooling sequence, form pooling region with
row_pooling sequence.
</td>
</tr><tr>
<td>
`overlapping`
</td>
<td>
An optional `bool`. Defaults to `False`.
When set to True, it means when pooling, the values at the boundary
of adjacent pooling cells are used by both cells. For example:

`index  0  1  2  3  4`

`value  20 5  16 3  7`

If the pooling sequence is [0, 2, 4], then 16, at index 2 will be used twice.
The result would be [41/3, 26/3] for fractional avg pooling.
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
A `Tensor`. Has the same type as `out_backprop`.
</td>
</tr>

</table>

