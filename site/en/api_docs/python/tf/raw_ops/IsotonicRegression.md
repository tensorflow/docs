description: Solves a batch of isotonic regression problems.

robots: noindex

# tf.raw_ops.IsotonicRegression

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Solves a batch of isotonic regression problems.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.IsotonicRegression`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.IsotonicRegression(
    input, output_dtype=tf.dtypes.float32, name=None
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
A (batch_size, dim)-tensor holding a batch of inputs.
</td>
</tr><tr>
<td>
`output_dtype`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.half, tf.bfloat16, tf.float32, tf.float64`. Defaults to <a href="../../tf.md#float32"><code>tf.float32</code></a>.
Dtype of output.
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
A tuple of `Tensor` objects (output, segments).
</td>
</tr>
<tr>
<td>
`output`
</td>
<td>
A `Tensor` of type `output_dtype`.
</td>
</tr><tr>
<td>
`segments`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr>
</table>

