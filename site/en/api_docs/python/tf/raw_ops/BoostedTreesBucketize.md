description: Bucketize each feature based on bucket boundaries.

robots: noindex

# tf.raw_ops.BoostedTreesBucketize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Bucketize each feature based on bucket boundaries.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesBucketize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesBucketize(
    float_values, bucket_boundaries, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An op that returns a list of float tensors, where each tensor represents the
bucketized values for a single feature.

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
float; List of Rank 1 Tensor each containing float values for a single feature.
</td>
</tr><tr>
<td>
`bucket_boundaries`
</td>
<td>
A list with the same length as `float_values` of `Tensor` objects with type `float32`.
float; List of Rank 1 Tensors each containing the bucket boundaries for a single
feature.
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
A list with the same length as `float_values` of `Tensor` objects with type `int32`.
</td>
</tr>

</table>

