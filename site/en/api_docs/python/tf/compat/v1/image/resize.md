description: Resize images to size using the specified method.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.image.resize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.image.resize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L1258-L1339">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Resize `images` to `size` using the specified `method`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.resize_images`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.image.resize(
    images, size, method=ResizeMethodV1.BILINEAR, align_corners=(False),
    preserve_aspect_ratio=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Resized images will be distorted if their original aspect ratio is not
the same as `size`.  To avoid distortions see
<a href="../../../../tf/image/resize_with_pad.md"><code>tf.image.resize_with_pad</code></a> or <a href="../../../../tf/image/resize_with_crop_or_pad.md"><code>tf.image.resize_with_crop_or_pad</code></a>.

The `method` can be one of:

*   <b>`ResizeMethod.BILINEAR`</b>: [Bilinear interpolation.](
  https://en.wikipedia.org/wiki/Bilinear_interpolation)
*   <b>`ResizeMethod.NEAREST_NEIGHBOR`</b>: [Nearest neighbor interpolation.](
  https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)
*   <b>`ResizeMethod.BICUBIC`</b>: [Bicubic interpolation.](
  https://en.wikipedia.org/wiki/Bicubic_interpolation)
*   <b>`ResizeMethod.AREA`</b>: Area interpolation.

The return value has the same type as `images` if `method` is
`ResizeMethod.NEAREST_NEIGHBOR`. It will also have the same type as `images`
if the size of `images` can be statically determined to be the same as `size`,
because `images` is returned in this case. Otherwise, the return value has
type `float32`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
of shape `[height, width, channels]`.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The new
size for the images.
</td>
</tr><tr>
<td>
`method`
</td>
<td>
ResizeMethod.  Defaults to `ResizeMethod.BILINEAR`.
</td>
</tr><tr>
<td>
`align_corners`
</td>
<td>
bool.  If True, the centers of the 4 corner pixels of the
input and output tensors are aligned, preserving the values at the corner
pixels. Defaults to `False`.
</td>
</tr><tr>
<td>
`preserve_aspect_ratio`
</td>
<td>
Whether to preserve the aspect ratio. If this is set,
then `images` will be resized to a size that fits in `size` while
preserving the aspect ratio of the original image. Scales up the image if
`size` is bigger than the current size of the `image`. Defaults to False.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the shape of `images` is incompatible with the
shape arguments to this function
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `size` has invalid shape or type.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if an unsupported resize method is specified.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
If `images` was 4-D, a 4-D float Tensor of shape
`[batch, new_height, new_width, channels]`.
If `images` was 3-D, a 3-D float Tensor of shape
`[new_height, new_width, channels]`.
</td>
</tr>

</table>

