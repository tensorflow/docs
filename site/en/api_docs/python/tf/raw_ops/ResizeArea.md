description: Resize images to size using area interpolation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ResizeArea" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ResizeArea

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Resize `images` to `size` using area interpolation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ResizeArea`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ResizeArea(
    images, size, align_corners=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Input images can be of different types but output images are always float.

The range of pixel values for the output image might be slightly different
from the range for the input image because of limited numerical precision.
To guarantee an output range, for example `[0.0, 1.0]`, apply
<a href="../../tf/clip_by_value.md"><code>tf.clip_by_value</code></a> to the output.

Each output pixel is computed by first transforming the pixel's footprint into
the input tensor and then averaging the pixels that intersect the footprint. An
input pixel's contribution to the average is weighted by the fraction of its
area that intersects the footprint.  This is the same as OpenCV's INTER_AREA.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
A `Tensor`. Must be one of the following types: `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `half`, `float32`, `float64`.
4-D with shape `[batch, height, width, channels]`.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The
new size for the images.
</td>
</tr><tr>
<td>
`align_corners`
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

