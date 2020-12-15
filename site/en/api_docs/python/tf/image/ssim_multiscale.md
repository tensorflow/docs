description: Computes the MS-SSIM between img1 and img2.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.ssim_multiscale" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.ssim_multiscale

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L4180-L4305">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the MS-SSIM between img1 and img2.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.ssim_multiscale`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.ssim_multiscale(
    img1, img2, max_val, power_factors=_MSSSIM_WEIGHTS, filter_size=11,
    filter_sigma=1.5, k1=0.01, k2=0.03
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function assumes that `img1` and `img2` are image batches, i.e. the last
three dimensions are [height, width, channels].

Note: The true SSIM is only defined on grayscale.  This function does not
perform any colorspace transform.  (If the input is already YUV, then it will
compute YUV SSIM average.)

Original paper: Wang, Zhou, Eero P. Simoncelli, and Alan C. Bovik. "Multiscale
structural similarity for image quality assessment." Signals, Systems and
Computers, 2004.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`img1`
</td>
<td>
First image batch.
</td>
</tr><tr>
<td>
`img2`
</td>
<td>
Second image batch. Must have the same rank as img1.
</td>
</tr><tr>
<td>
`max_val`
</td>
<td>
The dynamic range of the images (i.e., the difference between the
maximum the and minimum allowed values).
</td>
</tr><tr>
<td>
`power_factors`
</td>
<td>
Iterable of weights for each of the scales. The number of
scales used is the length of the list. Index 0 is the unscaled
resolution's weight and each increasing scale corresponds to the image
being downsampled by 2.  Defaults to (0.0448, 0.2856, 0.3001, 0.2363,
0.1333), which are the values obtained in the original paper.
</td>
</tr><tr>
<td>
`filter_size`
</td>
<td>
Default value 11 (size of gaussian filter).
</td>
</tr><tr>
<td>
`filter_sigma`
</td>
<td>
Default value 1.5 (width of gaussian filter).
</td>
</tr><tr>
<td>
`k1`
</td>
<td>
Default value 0.01
</td>
</tr><tr>
<td>
`k2`
</td>
<td>
Default value 0.03 (SSIM is less sensitivity to K2 for lower values, so
it would be better if we took the values in the range of 0 < K2 < 0.4).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor containing an MS-SSIM value for each image in batch.  The values
are in range [0, 1].  Returns a tensor with shape:
broadcast(img1.shape[:-3], img2.shape[:-3]).
</td>
</tr>

</table>

