description: Creates a dataset that takes a Bernoulli sample of the contents of another dataset.

robots: noindex

# tf.raw_ops.SamplingDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that takes a Bernoulli sample of the contents of another dataset.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SamplingDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SamplingDataset(
    input_dataset, rate, seed, seed2, output_types, output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

There is no transformation in the <a href="../../tf/data.md"><code>tf.data</code></a> Python API for creating this dataset.
Instead, it is created as a result of the `filter_with_random_uniform_fusion`
static optimization. Whether this optimization is performed is determined by the
`experimental_optimization.filter_with_random_uniform_fusion` option of
<a href="../../tf/data/Options.md"><code>tf.data.Options</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`
</td>
<td>
A `Tensor` of type `variant`.
</td>
</tr><tr>
<td>
`rate`
</td>
<td>
A `Tensor` of type `float32`.
A scalar representing the sample rate. Each element of `input_dataset` is
retained with this probability, independent of all other elements.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing seed of random number generator.
</td>
</tr><tr>
<td>
`seed2`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing seed2 of random number generator.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

