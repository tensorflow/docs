description: Extract the shape information of a JPEG-encoded image.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.extract_jpeg_shape" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.extract_jpeg_shape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Extract the shape information of a JPEG-encoded image.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.image.extract_jpeg_shape`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.extract_jpeg_shape`, `tf.compat.v1.io.extract_jpeg_shape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.extract_jpeg_shape(
    contents, output_type=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op only parses the image header, so it is much faster than DecodeJpeg.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`contents`
</td>
<td>
A `Tensor` of type `string`. 0-D. The JPEG-encoded image.
</td>
</tr><tr>
<td>
`output_type`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int32"><code>tf.int32</code></a>.
(Optional) The output type of the operation (int32 or int64).
Defaults to int32.
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
A `Tensor` of type `output_type`.
</td>
</tr>

</table>

