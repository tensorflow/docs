description: Generates points from the Sobol sequence.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SobolSample" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SobolSample

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generates points from the Sobol sequence.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SobolSample`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SobolSample(
    dim, num_results, skip, dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Creates a Sobol sequence with `num_results` samples. Each sample has dimension
`dim`. Skips the first `skip` samples.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dim`
</td>
<td>
A `Tensor` of type `int32`.
Positive scalar `Tensor` representing each sample's dimension.
</td>
</tr><tr>
<td>
`num_results`
</td>
<td>
A `Tensor` of type `int32`.
Positive scalar `Tensor` of dtype int32. The number of Sobol points to return
in the output.
</td>
</tr><tr>
<td>
`skip`
</td>
<td>
A `Tensor` of type `int32`.
Positive scalar `Tensor` of dtype int32. The number of initial points of the
Sobol sequence to skip.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.float32, tf.float64`. Defaults to <a href="../../tf.md#float32"><code>tf.float32</code></a>.
The type of the sample. One of: `float32` or `float64`.
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
A `Tensor` of type `dtype`.
</td>
</tr>

</table>

