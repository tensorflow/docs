description: JPEG encode input image with provided compression quality.

robots: noindex

# tf.raw_ops.EncodeJpegVariableQuality

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



JPEG encode input image with provided compression quality.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.EncodeJpegVariableQuality`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.EncodeJpegVariableQuality(
    images, quality, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`image` is a 3-D uint8 Tensor of shape `[height, width, channels]`.
`quality` is an int32 jpeg compression quality value between 0 and 100.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
A `Tensor` of type `uint8`. Images to adjust.  At least 3-D.
</td>
</tr><tr>
<td>
`quality`
</td>
<td>
A `Tensor` of type `int32`. An int quality to encode to.
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

