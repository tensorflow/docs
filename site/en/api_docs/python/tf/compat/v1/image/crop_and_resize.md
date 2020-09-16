description: Extracts crops from the input image tensor and resizes them.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.image.crop_and_resize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.image.crop_and_resize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L4040-L4056">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Extracts crops from the input image tensor and resizes them.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.image.crop_and_resize(
    image, boxes, box_ind=None, crop_size=None, method='bilinear',
    extrapolation_value=0, name=None, box_indices=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Extracts crops from the input image tensor and resizes them using bilinear
sampling or nearest neighbor sampling (possibly with aspect ratio change) to a
common output size specified by `crop_size`. This is more general than the
`crop_to_bounding_box` op which extracts a fixed size slice from the input image
and does not allow resizing or aspect ratio change.

Returns a tensor with `crops` from the input `image` at positions defined at the
bounding box locations in `boxes`. The cropped boxes are all resized (with
bilinear or nearest neighbor interpolation) to a fixed
`size = [crop_height, crop_width]`. The result is a 4-D tensor
`[num_boxes, crop_height, crop_width, depth]`. The resizing is corner aligned.
In particular, if `boxes = [[0, 0, 1, 1]]`, the method will give identical
results to using `tf.image.resize_bilinear()` or
`tf.image.resize_nearest_neighbor()`(depends on the `method` argument) with
`align_corners=True`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
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
`[0, image_height - 1]` in image height coordinates. We do allow `y1` > `y2`, in
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
`crop_size`
</td>
<td>
A `Tensor` of type `int32`.
A 1-D tensor of 2 elements, `size = [crop_height, crop_width]`. All
cropped image patches are resized to this size. The aspect ratio of the image
content is not preserved. Both `crop_height` and `crop_width` need to be
positive.
</td>
</tr><tr>
<td>
`method`
</td>
<td>
An optional `string` from: `"bilinear", "nearest"`. Defaults to `"bilinear"`.
A string specifying the sampling method for resizing. It can be either
`"bilinear"` or `"nearest"` and default to `"bilinear"`. Currently two sampling
methods are supported: Bilinear and Nearest Neighbor.
</td>
</tr><tr>
<td>
`extrapolation_value`
</td>
<td>
An optional `float`. Defaults to `0`.
Value used for extrapolation, when applicable.
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

