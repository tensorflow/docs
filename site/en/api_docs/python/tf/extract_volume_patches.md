description: Extract patches from input and put them in the "depth" output dimension. 3D extension of extract_image_patches.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.extract_volume_patches" />
<meta itemprop="path" content="Stable" />
</div>

# tf.extract_volume_patches

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Extract `patches` from `input` and put them in the `"depth"` output dimension. 3D extension of `extract_image_patches`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.extract_volume_patches`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.extract_volume_patches(
    input, ksizes, strides, padding, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
5-D Tensor with shape `[batch, in_planes, in_rows, in_cols, depth]`.
</td>
</tr><tr>
<td>
`ksizes`
</td>
<td>
A list of `ints` that has length `>= 5`.
The size of the sliding window for each dimension of `input`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints` that has length `>= 5`.
1-D of length 5. How far the centers of two consecutive patches are in
`input`. Must be: `[1, stride_planes, stride_rows, stride_cols, 1]`.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A `string` from: `"SAME", "VALID"`.
The type of padding algorithm to use.

The size-related attributes are specified as follows:

```python
ksizes = [1, ksize_planes, ksize_rows, ksize_cols, 1]
strides = [1, stride_planes, strides_rows, strides_cols, 1]
```
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

