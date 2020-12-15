description: Pad image with zeros to the specified height and width.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.pad_to_bounding_box" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.pad_to_bounding_box

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L968-L1077">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Pad `image` with zeros to the specified `height` and `width`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.pad_to_bounding_box`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.pad_to_bounding_box(
    image, offset_height, offset_width, target_height, target_width
)
</code></pre>



<!-- Placeholder for "Used in" -->

Adds `offset_height` rows of zeros on top, `offset_width` columns of
zeros on the left, and then pads the image on the bottom and right
with zeros until it has dimensions `target_height`, `target_width`.

This op does nothing if `offset_*` is zero and the image already has size
`target_height` by `target_width`.

#### Usage Example:



```
>>> x = [[[1., 2., 3.],
...       [4., 5., 6.]],
...       [[7., 8., 9.],
...       [10., 11., 12.]]]
>>> padded_image = tf.image.pad_to_bounding_box(x, 1, 1, 4, 4)
>>> padded_image
<tf.Tensor: shape=(4, 4, 3), dtype=float32, numpy=
array([[[ 0.,  0.,  0.],
[ 0.,  0.,  0.],
[ 0.,  0.,  0.],
[ 0.,  0.,  0.]],
[[ 0.,  0.,  0.],
[ 1.,  2.,  3.],
[ 4.,  5.,  6.],
[ 0.,  0.,  0.]],
[[ 0.,  0.,  0.],
[ 7.,  8.,  9.],
[10., 11., 12.],
[ 0.,  0.,  0.]],
[[ 0.,  0.,  0.],
[ 0.,  0.,  0.],
[ 0.,  0.,  0.],
[ 0.,  0.,  0.]]], dtype=float32)>
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
4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
of shape `[height, width, channels]`.
</td>
</tr><tr>
<td>
`offset_height`
</td>
<td>
Number of rows of zeros to add on top.
</td>
</tr><tr>
<td>
`offset_width`
</td>
<td>
Number of columns of zeros to add on the left.
</td>
</tr><tr>
<td>
`target_height`
</td>
<td>
Height of output image.
</td>
</tr><tr>
<td>
`target_width`
</td>
<td>
Width of output image.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
If `image` was 4-D, a 4-D float Tensor of shape
`[batch, target_height, target_width, channels]`
If `image` was 3-D, a 3-D float Tensor of shape
`[target_height, target_width, channels]`
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
If the shape of `image` is incompatible with the `offset_*` or
`target_*` arguments, or either `offset_height` or `offset_width` is
negative.
</td>
</tr>
</table>

