description: Returns the Peak Signal-to-Noise Ratio between a and b.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.psnr" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.psnr

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/image_ops_impl.py#L3373-L3425">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the Peak Signal-to-Noise Ratio between a and b.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.psnr`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.psnr(
    a, b, max_val, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is intended to be used on signals (or images). Produces a PSNR value for
each image in batch.

The last three dimensions of input are expected to be [height, width, depth].

#### Example:



```python
    # Read images from file.
    im1 = tf.decode_png('path/to/im1.png')
    im2 = tf.decode_png('path/to/im2.png')
    # Compute PSNR over tf.uint8 Tensors.
    psnr1 = tf.image.psnr(im1, im2, max_val=255)

    # Compute PSNR over tf.float32 Tensors.
    im1 = tf.image.convert_image_dtype(im1, tf.float32)
    im2 = tf.image.convert_image_dtype(im2, tf.float32)
    psnr2 = tf.image.psnr(im1, im2, max_val=1.0)
    # psnr1 and psnr2 both have type tf.float32 and are almost equal.
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
First set of images.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
Second set of images.
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
`name`
</td>
<td>
Namespace to embed the computation in.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The scalar PSNR between a and b. The returned tensor has type <a href="../../tf.md#float32"><code>tf.float32</code></a>
and shape [batch_size, 1].
</td>
</tr>

</table>

