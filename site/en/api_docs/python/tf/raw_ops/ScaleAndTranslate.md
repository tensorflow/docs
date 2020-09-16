<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ScaleAndTranslate" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ScaleAndTranslate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>





<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ScaleAndTranslate`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ScaleAndTranslate(
    images, size, scale, translation, kernel_type='lanczos3', antialias=(True),
    name=None
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
A `Tensor`. Must be one of the following types: `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `bfloat16`, `half`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`translation`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`kernel_type`
</td>
<td>
An optional `string`. Defaults to `"lanczos3"`.
</td>
</tr><tr>
<td>
`antialias`
</td>
<td>
An optional `bool`. Defaults to `True`.
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

