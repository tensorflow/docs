description: Performs [Gamma Correction](http://en.wikipedia.org/wiki/Gamma_correction).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.adjust_gamma" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.adjust_gamma

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L1902-L1963">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Performs [Gamma Correction](http://en.wikipedia.org/wiki/Gamma_correction).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.adjust_gamma`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.adjust_gamma(
    image, gamma=1, gain=1
)
</code></pre>



<!-- Placeholder for "Used in" -->

on the input image.

Also known as Power Law Transform. This function converts the
input images at first to float representation, then transforms them
pixelwise according to the equation `Out = gain * In**gamma`,
and then converts the back to the original data type.

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.adjust_gamma(x, 0.2)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[1.       , 1.1486983, 1.2457309],
        [1.319508 , 1.3797297, 1.4309691]],
       [[1.4757731, 1.5157166, 1.5518456],
        [1.5848932, 1.6153942, 1.6437519]]], dtype=float32)>
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
`gamma`
</td>
<td>
A scalar or tensor. Non-negative real number.
</td>
</tr><tr>
<td>
`gain`
</td>
<td>
A scalar or tensor. The constant multiplier.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Tensor. A Gamma-adjusted tensor of the same shape and type as `image`.
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
If gamma is negative.
</td>
</tr>
</table>



#### Notes:

For gamma greater than 1, the histogram will shift towards left and
the output image will be darker than the input image.
For gamma less than 1, the histogram will shift towards right and
the output image will be brighter than the input image.


#### References:

[Wikipedia](http://en.wikipedia.org/wiki/Gamma_correction)
