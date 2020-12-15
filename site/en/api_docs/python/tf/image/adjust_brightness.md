description: Adjust the brightness of RGB or Grayscale images.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.adjust_brightness" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.adjust_brightness

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/image_ops_impl.py#L1831-L1880">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adjust the brightness of RGB or Grayscale images.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.adjust_brightness`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.adjust_brightness(
    image, delta
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a convenience method that converts RGB images to float
representation, adjusts their brightness, and then converts them back to the
original data type. If several adjustments are chained, it is advisable to
minimize the number of redundant conversions.

The value `delta` is added to all components of the tensor `image`. `image` is
converted to `float` and scaled appropriately if it is in fixed-point
representation, and `delta` is converted to the same data type. For regular
images, `delta` should be in the range `[0,1)`, as it is added to the image in
floating point representation, where pixel values are in the `[0,1)` range.

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.adjust_brightness(x, delta=0.1)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 1.1,  2.1,  3.1],
        [ 4.1,  5.1,  6.1]],
       [[ 7.1,  8.1,  9.1],
        [10.1, 11.1, 12.1]]], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`image`
</td>
<td>
RGB image or images to adjust.
</td>
</tr><tr>
<td>
`delta`
</td>
<td>
A scalar. Amount to add to the pixel values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A brightness-adjusted tensor of the same shape and type as `image`.
</td>
</tr>

</table>

