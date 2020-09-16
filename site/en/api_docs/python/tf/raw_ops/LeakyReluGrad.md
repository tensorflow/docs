description: Computes rectified linear gradients for a LeakyRelu operation.

robots: noindex

# tf.raw_ops.LeakyReluGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes rectified linear gradients for a LeakyRelu operation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.LeakyReluGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.LeakyReluGrad(
    gradients, features, alpha=0.2, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`gradients`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
The backpropagated gradients to the corresponding LeakyRelu operation.
</td>
</tr><tr>
<td>
`features`
</td>
<td>
A `Tensor`. Must have the same type as `gradients`.
The features passed as input to the corresponding LeakyRelu operation,
OR the outputs of that operation (both work equivalently).
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
An optional `float`. Defaults to `0.2`.
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
A `Tensor`. Has the same type as `gradients`.
</td>
</tr>

</table>

