description: JPEG-encode an image.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.EncodeJpeg" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.EncodeJpeg

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



JPEG-encode an image.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.EncodeJpeg`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.EncodeJpeg(
    image, format='', quality=95, progressive=(False), optimize_size=(False),
    chroma_downsampling=(True), density_unit='in', x_density=300, y_density=300,
    xmp_metadata='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`image` is a 3-D uint8 Tensor of shape `[height, width, channels]`.

The attr `format` can be used to override the color format of the encoded
output.  Values can be:

*   `''`: Use a default format based on the number of channels in the image.
*   `grayscale`: Output a grayscale JPEG image.  The `channels` dimension
    of `image` must be 1.
*   `rgb`: Output an RGB JPEG image. The `channels` dimension
    of `image` must be 3.

If `format` is not specified or is the empty string, a default format is picked
in function of the number of channels in `image`:

*   1: Output a grayscale image.
*   3: Output an RGB image.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`image`
</td>
<td>
A `Tensor` of type `uint8`.
3-D with shape `[height, width, channels]`.
</td>
</tr><tr>
<td>
`format`
</td>
<td>
An optional `string` from: `"", "grayscale", "rgb"`. Defaults to `""`.
Per pixel image format.
</td>
</tr><tr>
<td>
`quality`
</td>
<td>
An optional `int`. Defaults to `95`.
Quality of the compression from 0 to 100 (higher is better and slower).
</td>
</tr><tr>
<td>
`progressive`
</td>
<td>
An optional `bool`. Defaults to `False`.
If True, create a JPEG that loads progressively (coarse to fine).
</td>
</tr><tr>
<td>
`optimize_size`
</td>
<td>
An optional `bool`. Defaults to `False`.
If True, spend CPU/RAM to reduce size with no quality change.
</td>
</tr><tr>
<td>
`chroma_downsampling`
</td>
<td>
An optional `bool`. Defaults to `True`.
See http://en.wikipedia.org/wiki/Chroma_subsampling.
</td>
</tr><tr>
<td>
`density_unit`
</td>
<td>
An optional `string` from: `"in", "cm"`. Defaults to `"in"`.
Unit used to specify `x_density` and `y_density`:
pixels per inch (`'in'`) or centimeter (`'cm'`).
</td>
</tr><tr>
<td>
`x_density`
</td>
<td>
An optional `int`. Defaults to `300`.
Horizontal pixels per density unit.
</td>
</tr><tr>
<td>
`y_density`
</td>
<td>
An optional `int`. Defaults to `300`.
Vertical pixels per density unit.
</td>
</tr><tr>
<td>
`xmp_metadata`
</td>
<td>
An optional `string`. Defaults to `""`.
If not empty, embed this XMP metadata in the image header.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

