description: Crops an image to a specified bounding box.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.crop_to_bounding_box" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.crop_to_bounding_box

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L959-L1036">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Crops an image to a specified bounding box.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.crop_to_bounding_box`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.crop_to_bounding_box(
    image, offset_height, offset_width, target_height, target_width
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op cuts a rectangular part out of `image`. The top-left corner of the
returned image is at `offset_height, offset_width` in `image`, and its
lower-right corner is at
`offset_height + target_height, offset_width + target_width`.

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
Vertical coordinate of the top-left corner of the result in
the input.
</td>
</tr><tr>
<td>
`offset_width`
</td>
<td>
Horizontal coordinate of the top-left corner of the result in
the input.
</td>
</tr><tr>
<td>
`target_height`
</td>
<td>
Height of the result.
</td>
</tr><tr>
<td>
`target_width`
</td>
<td>
Width of the result.
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
negative, or either `target_height` or `target_width` is not positive.
</td>
</tr>
</table>

