description: Concatenates quantized tensors along one dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.quantization.quantized_concat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.quantization.quantized_concat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Concatenates quantized tensors along one dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.quantization.quantized_concat`, `tf.compat.v1.quantized_concat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.quantization.quantized_concat(
    concat_dim, values, input_mins, input_maxes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`concat_dim`
</td>
<td>
A `Tensor` of type `int32`.
0-D.  The dimension along which to concatenate.  Must be in the
range [0, rank(values)).
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A list of at least 2 `Tensor` objects with the same type.
The `N` Tensors to concatenate. Their ranks and types must match,
and their sizes must match in all dimensions except `concat_dim`.
</td>
</tr><tr>
<td>
`input_mins`
</td>
<td>
A list with the same length as `values` of `Tensor` objects with type `float32`.
The minimum scalar values for each of the input tensors.
</td>
</tr><tr>
<td>
`input_maxes`
</td>
<td>
A list with the same length as `values` of `Tensor` objects with type `float32`.
The maximum scalar values for each of the input tensors.
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
A tuple of `Tensor` objects (output, output_min, output_max).
</td>
</tr>
<tr>
<td>
`output`
</td>
<td>
A `Tensor`. Has the same type as `values`.
</td>
</tr><tr>
<td>
`output_min`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`output_max`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

