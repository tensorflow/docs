description: Function for decode_bmp, decode_gif, decode_jpeg, and decode_png.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.decode_image" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.decode_image

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L2544-L2657">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Function for `decode_bmp`, `decode_gif`, `decode_jpeg`, and `decode_png`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.image.decode_image`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.decode_image`, `tf.compat.v1.io.decode_image`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.decode_image(
    contents, channels=None, dtype=tf.dtypes.uint8, name=None,
    expand_animations=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Detects whether an image is a BMP, GIF, JPEG, or PNG, and performs the
appropriate operation to convert the input bytes `string` into a `Tensor`
of type `dtype`.

Note: `decode_gif` returns a 4-D array `[num_frames, height, width, 3]`, as
opposed to `decode_bmp`, `decode_jpeg` and `decode_png`, which return 3-D
arrays `[height, width, num_channels]`. Make sure to take this into account
when constructing your graph if you are intermixing GIF files with BMP, JPEG,
and/or PNG files. Alternately, set the `expand_animations` argument of this
function to `False`, in which case the op will return 3-dimensional tensors
and will truncate animated GIF files to the first frame.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`contents`
</td>
<td>
0-D `string`. The encoded image bytes.
</td>
</tr><tr>
<td>
`channels`
</td>
<td>
An optional `int`. Defaults to `0`. Number of color channels for
the decoded image.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The desired DType of the returned `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional)
</td>
</tr><tr>
<td>
`expand_animations`
</td>
<td>
Controls the shape of the returned op's output. If
`True`, the returned op will produce a 3-D tensor for PNG, JPEG, and BMP
files; and a 4-D tensor for all GIFs, whether animated or not. If,
`False`, the returned op will produce a 3-D tensor for all file types and
will truncate animated GIFs to the first frame.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with type `dtype` and a 3- or 4-dimensional shape, depending on
the file type and the value of the `expand_animations` parameter.
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
On incorrect number of channels.
</td>
</tr>
</table>

