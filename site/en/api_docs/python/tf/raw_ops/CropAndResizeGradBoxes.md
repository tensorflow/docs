description: Computes the gradient of the crop_and_resize op wrt the input boxes tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CropAndResizeGradBoxes" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CropAndResizeGradBoxes

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the gradient of the crop_and_resize op wrt the input boxes tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CropAndResizeGradBoxes`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CropAndResizeGradBoxes(
    grads, image, boxes, box_ind, method='bilinear', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`grads`
</td>
<td>
A `Tensor` of type `float32`.
A 4-D tensor of shape `[num_boxes, crop_height, crop_width, depth]`.
</td>
</tr><tr>
<td>
`image`
</td>
<td>
A `Tensor`. Must be one of the following types: `uint8`, `uint16`, `int8`, `int16`, `int32`, `int64`, `half`, `float32`, `float64`.
A 4-D tensor of shape `[batch, image_height, image_width, depth]`.
Both `image_height` and `image_width` need to be positive.
</td>
</tr><tr>
<td>
`boxes`
</td>
<td>
A `Tensor` of type `float32`.
A 2-D tensor of shape `[num_boxes, 4]`. The `i`-th row of the tensor
specifies the coordinates of a box in the `box_ind[i]` image and is specified
in normalized coordinates `[y1, x1, y2, x2]`. A normalized coordinate value of
`y` is mapped to the image coordinate at `y * (image_height - 1)`, so as the
`[0, 1]` interval of normalized image height is mapped to
`[0, image_height - 1] in image height coordinates. We do allow y1 > y2, in
which case the sampled crop is an up-down flipped version of the original
image. The width dimension is treated similarly. Normalized coordinates
outside the `[0, 1]` range are allowed, in which case we use
`extrapolation_value` to extrapolate the input image values.
</td>
</tr><tr>
<td>
`box_ind`
</td>
<td>
A `Tensor` of type `int32`.
A 1-D tensor of shape `[num_boxes]` with int32 values in `[0, batch)`.
The value of `box_ind[i]` specifies the image that the `i`-th box refers to.
</td>
</tr><tr>
<td>
`method`
</td>
<td>
An optional `string` from: `"bilinear"`. Defaults to `"bilinear"`.
A string specifying the interpolation method. Only 'bilinear' is
supported for now.
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

