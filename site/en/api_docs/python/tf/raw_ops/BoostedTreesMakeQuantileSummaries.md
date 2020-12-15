description: Makes the summary of quantiles for the batch.

robots: noindex

# tf.raw_ops.BoostedTreesMakeQuantileSummaries

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Makes the summary of quantiles for the batch.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesMakeQuantileSummaries`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesMakeQuantileSummaries(
    float_values, example_weights, epsilon, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An op that takes a list of tensors (one tensor per feature) and outputs the
quantile summaries for each tensor.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`float_values`
</td>
<td>
A list of `Tensor` objects with type `float32`.
float; List of Rank 1 Tensors each containing values for a single feature.
</td>
</tr><tr>
<td>
`example_weights`
</td>
<td>
A `Tensor` of type `float32`.
float; Rank 1 Tensor with weights per instance.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A `Tensor` of type `float32`.
float; The required maximum approximation error.
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
A list with the same length as `float_values` of `Tensor` objects with type `float32`.
</td>
</tr>

</table>

