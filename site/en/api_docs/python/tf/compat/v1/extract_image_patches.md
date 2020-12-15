description: Extract patches from images and put them in the "depth" output dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.extract_image_patches" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.extract_image_patches

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L5989-L6032">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Extract `patches` from `images` and put them in the "depth" output dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.extract_image_patches`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.extract_image_patches(
    images, ksizes=None, strides=None, rates=None, padding=None, name=None,
    sizes=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `complex64`, `complex128`, `bool`.
4-D Tensor with shape `[batch, in_rows, in_cols, depth]`.
</td>
</tr><tr>
<td>
`ksizes`
</td>
<td>
A list of `ints` that has length `>= 4`.
The size of the sliding window for each dimension of `images`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints` that has length `>= 4`.
How far the centers of two consecutive patches are in
the images. Must be: `[1, stride_rows, stride_cols, 1]`.
</td>
</tr><tr>
<td>
`rates`
</td>
<td>
A list of `ints` that has length `>= 4`.
Must be: `[1, rate_rows, rate_cols, 1]`. This is the
input stride, specifying how far two consecutive patch samples are in the
input. Equivalent to extracting patches with
`patch_sizes_eff = patch_sizes + (patch_sizes - 1) * (rates - 1)`, followed by
subsampling them spatially by a factor of `rates`. This is equivalent to
`rate` in dilated (a.k.a. Atrous) convolutions.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A `string` from: `"SAME", "VALID"`.
The type of padding algorithm to use.
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

