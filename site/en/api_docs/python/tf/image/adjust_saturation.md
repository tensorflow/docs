description: Adjust saturation of RGB images.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.adjust_saturation" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.adjust_saturation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L2785-L2835">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adjust saturation of RGB images.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.adjust_saturation`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.adjust_saturation(
    image, saturation_factor, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a convenience method that converts RGB images to float
representation, converts them to HSV, adds an offset to the
saturation channel, converts back to RGB and then back to the original
data type. If several adjustments are chained it is advisable to minimize
the number of redundant conversions.

`image` is an RGB image or images.  The image saturation is adjusted by
converting the images to HSV and multiplying the saturation (S) channel by
`saturation_factor` and clipping. The images are then converted back to RGB.

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.adjust_saturation(x, 0.5)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 2. ,  2.5,  3. ],
        [ 5. ,  5.5,  6. ]],
       [[ 8. ,  8.5,  9. ],
        [11. , 11.5, 12. ]]], dtype=float32)>
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
RGB image or images. The size of the last dimension must be 3.
</td>
</tr><tr>
<td>
`saturation_factor`
</td>
<td>
float. Factor to multiply the saturation by.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Adjusted image(s), same shape and DType as `image`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`InvalidArgumentError`
</td>
<td>
input must have 3 channels
</td>
</tr>
</table>

