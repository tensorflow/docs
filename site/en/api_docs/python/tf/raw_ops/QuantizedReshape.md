description: Reshapes a quantized tensor as per the Reshape op.

robots: noindex

# tf.raw_ops.QuantizedReshape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Reshapes a quantized tensor as per the Reshape op.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.QuantizedReshape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.QuantizedReshape(
    tensor, shape, input_min, input_max, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Defines the shape of the output tensor.
</td>
</tr><tr>
<td>
`input_min`
</td>
<td>
A `Tensor` of type `float32`. The minimum value of the input.
</td>
</tr><tr>
<td>
`input_max`
</td>
<td>
A `Tensor` of type `float32`. The maximum value of the input.
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
A `Tensor`. Has the same type as `tensor`.
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

