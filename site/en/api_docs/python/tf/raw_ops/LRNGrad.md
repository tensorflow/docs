description: Gradients for Local Response Normalization.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.LRNGrad" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.LRNGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Gradients for Local Response Normalization.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.LRNGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.LRNGrad(
    input_grads, input_image, output_image, depth_radius=5, bias=1, alpha=1,
    beta=0.5, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_grads`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`.
4-D with shape `[batch, height, width, channels]`.
</td>
</tr><tr>
<td>
`input_image`
</td>
<td>
A `Tensor`. Must have the same type as `input_grads`.
4-D with shape `[batch, height, width, channels]`.
</td>
</tr><tr>
<td>
`output_image`
</td>
<td>
A `Tensor`. Must have the same type as `input_grads`.
4-D with shape `[batch, height, width, channels]`.
</td>
</tr><tr>
<td>
`depth_radius`
</td>
<td>
An optional `int`. Defaults to `5`. A depth radius.
</td>
</tr><tr>
<td>
`bias`
</td>
<td>
An optional `float`. Defaults to `1`.
An offset (usually > 0 to avoid dividing by 0).
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
An optional `float`. Defaults to `1`.
A scale factor, usually positive.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
An optional `float`. Defaults to `0.5`. An exponent.
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
A `Tensor`. Has the same type as `input_grads`.
</td>
</tr>

</table>

