description: Adjust hue of RGB images.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.adjust_hue" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.adjust_hue

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L2178-L2241">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adjust hue of RGB images.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.adjust_hue`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.adjust_hue(
    image, delta, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a convenience method that converts an RGB image to float
representation, converts it to HSV, adds an offset to the
hue channel, converts back to RGB and then back to the original
data type. If several adjustments are chained it is advisable to minimize
the number of redundant conversions.

`image` is an RGB image.  The image hue is adjusted by converting the
image(s) to HSV and rotating the hue channel (H) by
`delta`.  The image is then converted back to RGB.

`delta` must be in the interval `[-1, 1]`.

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.adjust_hue(x, 0.2)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 2.3999996,  1.       ,  3.       ],
        [ 5.3999996,  4.       ,  6.       ]],
      [[ 8.4      ,  7.       ,  9.       ],
        [11.4      , 10.       , 12.       ]]], dtype=float32)>
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
`delta`
</td>
<td>
float.  How much to add to the hue channel.
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



#### Usage Example:



```
>>> image = [[[1, 2, 3], [4, 5, 6]],
...          [[7, 8, 9], [10, 11, 12]],
...          [[13, 14, 15], [16, 17, 18]]]
>>> image = tf.constant(image)
>>> tf.image.adjust_hue(image, 0.2)
<tf.Tensor: shape=(3, 2, 3), dtype=int32, numpy=
array([[[ 2,  1,  3],
      [ 5,  4,  6]],
     [[ 8,  7,  9],
      [11, 10, 12]],
     [[14, 13, 15],
      [17, 16, 18]]], dtype=int32)>
```