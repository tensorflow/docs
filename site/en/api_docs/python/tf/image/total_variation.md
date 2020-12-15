description: Calculate and return the total variation for one or more images.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.total_variation" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.total_variation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/image_ops_impl.py#L2710-L2779">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calculate and return the total variation for one or more images.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.total_variation`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.total_variation(
    images, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The total variation is the sum of the absolute differences for neighboring
pixel-values in the input images. This measures how much noise is in the
images.

This can be used as a loss-function during optimization so as to suppress
noise in images. If you have a batch of images, then you should calculate
the scalar loss-value as the sum:
`loss = tf.reduce_sum(tf.image.total_variation(images))`

This implements the anisotropic 2-D version of the formula described here:

https://en.wikipedia.org/wiki/Total_variation_denoising

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
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if images.shape is not a 3-D or 4-D vector.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The total variation of `images`.

If `images` was 4-D, return a 1-D float Tensor of shape `[batch]` with the
total variation for each image in the batch.
If `images` was 3-D, return a scalar float with the total variation for
that image.
</td>
</tr>

</table>

