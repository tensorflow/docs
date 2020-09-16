description: BatchToSpace for 4-D tensors of type T.

robots: noindex

# tf.raw_ops.BatchToSpace

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



BatchToSpace for 4-D tensors of type T.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BatchToSpace`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BatchToSpace(
    input, crops, block_size, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a legacy version of the more general BatchToSpaceND.

Rearranges (permutes) data from batch into blocks of spatial data, followed by
cropping. This is the reverse transformation of SpaceToBatch. More specifically,
this op outputs a copy of the input tensor where values from the `batch`
dimension are moved in spatial blocks to the `height` and `width` dimensions,
followed by cropping along the `height` and `width` dimensions.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. 4-D tensor with shape
`[batch*block_size*block_size, height_pad/block_size, width_pad/block_size,
depth]`. Note that the batch size of the input tensor must be divisible by
`block_size * block_size`.
</td>
</tr><tr>
<td>
`crops`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
2-D tensor of non-negative integers with shape `[2, 2]`. It specifies
how many elements to crop from the intermediate result across the spatial
dimensions as follows:

crops = [[crop_top, crop_bottom], [crop_left, crop_right]]
</td>
</tr><tr>
<td>
`block_size`
</td>
<td>
An `int` that is `>= 2`.
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

