description: Computes SSIM index between img1 and img2.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.ssim" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.ssim

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L3568-L3640">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes SSIM index between img1 and img2.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.ssim`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.ssim(
    img1, img2, max_val, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function is based on the standard SSIM implementation from:
Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). Image
quality assessment: from error visibility to structural similarity. IEEE
transactions on image processing.

Note: The true SSIM is only defined on grayscale.  This function does not
perform any colorspace transform.  (If the input is already YUV, then it will
compute YUV SSIM average.)

#### Details:

- 11x11 Gaussian filter of width 1.5 is used.
- k1 = 0.01, k2 = 0.03 as in the original paper.


The image sizes must be at least 11x11 because of the filter size.

#### Example:



```python
    # Read images from file.
    im1 = tf.decode_png('path/to/im1.png')
    im2 = tf.decode_png('path/to/im2.png')
    # Compute SSIM over tf.uint8 Tensors.
    ssim1 = tf.image.ssim(im1, im2, max_val=255, filter_size=11,
                          filter_sigma=1.5, k1=0.01, k2=0.03)

    # Compute SSIM over tf.float32 Tensors.
    im1 = tf.image.convert_image_dtype(im1, tf.float32)
    im2 = tf.image.convert_image_dtype(im2, tf.float32)
    ssim2 = tf.image.ssim(im1, im2, max_val=1.0, filter_size=11,
                          filter_sigma=1.5, k1=0.01, k2=0.03)
    # ssim1 and ssim2 both have type tf.float32 and are almost equal.
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

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
Second image batch.
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
A tensor containing an SSIM value for each image in batch.  Returned SSIM
values are in range (-1, 1], when pixel values are non-negative. Returns
a tensor with shape: broadcast(img1.shape[:-3], img2.shape[:-3]).
</td>
</tr>

</table>

