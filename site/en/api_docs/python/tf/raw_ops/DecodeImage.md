description: Function for decode_bmp, decode_gif, decode_jpeg, and decode_png.

robots: noindex

# tf.raw_ops.DecodeImage

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Function for decode_bmp, decode_gif, decode_jpeg, and decode_png.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DecodeImage`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DecodeImage(
    contents, channels=0, dtype=tf.dtypes.uint8, expand_animations=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Detects whether an image is a BMP, GIF, JPEG, or PNG, and performs the
appropriate operation to convert the input bytes string into a Tensor of type
dtype.

*NOTE*: decode_gif returns a 4-D array [num_frames, height, width, 3], as
opposed to decode_bmp, decode_jpeg and decode_png, which return 3-D arrays
[height, width, num_channels]. Make sure to take this into account when
constructing your graph if you are intermixing GIF files with BMP, JPEG, and/or
PNG files. Alternately, set the expand_animations argument of this function to
False, in which case the op will return 3-dimensional tensors and will truncate
animated GIF files to the first frame.

*NOTE*: If the first frame of an animated GIF does not occupy the entire
canvas (maximum frame width x maximum frame height), then it fills the
unoccupied areas (in the first frame) with zeros (black). For frames after the
first frame that does not occupy the entire canvas, it uses the previous
frame to fill the unoccupied areas.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`contents`
</td>
<td>
A `Tensor` of type `string`. 0-D. The encoded image bytes.
</td>
</tr><tr>
<td>
`channels`
</td>
<td>
An optional `int`. Defaults to `0`.
Number of color channels for the decoded image.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.uint8, tf.uint16, tf.float32`. Defaults to <a href="../../tf.md#uint8"><code>tf.uint8</code></a>.
The desired DType of the returned Tensor.
</td>
</tr><tr>
<td>
`expand_animations`
</td>
<td>
An optional `bool`. Defaults to `True`.
Controls the output shape of the returned op. If True, the returned op will
produce a 3-D tensor for PNG, JPEG, and BMP files; and a 4-D tensor for all
GIFs, whether animated or not. If, False, the returned op will produce a 3-D
tensor for all file types and will truncate animated GIFs to the first frame.
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
A `Tensor` of type `dtype`.
</td>
</tr>

</table>

