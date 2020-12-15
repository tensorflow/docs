description: Adjust the hue of one or more images.

robots: noindex

# tf.raw_ops.AdjustHue

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Adjust the hue of one or more images.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AdjustHue`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AdjustHue(
    images, delta, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`images` is a tensor of at least 3 dimensions.  The last dimension is
interpreted as channels, and must be three.

The input image is considered in the RGB colorspace. Conceptually, the RGB
colors are first mapped into HSV. A delta is then applied all the hue values,
and then remapped back to RGB colorspace.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`.
Images to adjust.  At least 3-D.
</td>
</tr><tr>
<td>
`delta`
</td>
<td>
A `Tensor` of type `float32`. A float delta to add to the hue.
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

