description: Applies the given transform to each of the images.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ImageProjectiveTransformV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ImageProjectiveTransformV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Applies the given transform to each of the images.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ImageProjectiveTransformV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ImageProjectiveTransformV2(
    images, transforms, output_shape, interpolation, fill_mode='CONSTANT', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If one row of `transforms` is `[a0, a1, a2, b0, b1, b2, c0, c1]`, then it maps
the *output* point `(x, y)` to a transformed *input* point
`(x', y') = ((a0 x + a1 y + a2) / k, (b0 x + b1 y + b2) / k)`, where
`k = c0 x + c1 y + 1`. If the transformed point lays outside of the input
image, the output pixel is set to 0.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
A `Tensor`. Must be one of the following types: `uint8`, `int32`, `int64`, `half`, `float32`, `float64`.
4-D with shape `[batch, height, width, channels]`.
</td>
</tr><tr>
<td>
`transforms`
</td>
<td>
A `Tensor` of type `float32`.
2-D Tensor, `[batch, 8]` or `[1, 8]` matrix, where each row corresponds to a 3 x 3
projective transformation matrix, with the last entry assumed to be 1. If there
is one row, the same transformation will be applied to all images.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A `Tensor` of type `int32`.
1-D Tensor [new_height, new_width].
</td>
</tr><tr>
<td>
`interpolation`
</td>
<td>
A `string`. Interpolation method, "NEAREST" or "BILINEAR".
</td>
</tr><tr>
<td>
`fill_mode`
</td>
<td>
An optional `string`. Defaults to `"CONSTANT"`.
Fill mode, "REFLECT", "WRAP", or "CONSTANT".
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
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `images`.
</td>
</tr>

</table>

