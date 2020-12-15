description: Generates points from the Sobol sequence.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.sobol_sample" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.sobol_sample

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L4959-L4981">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates points from the Sobol sequence.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.sobol_sample`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.sobol_sample(
    dim, num_results, skip=0, dtype=tf.dtypes.float32, name=None
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
Positive scalar `Tensor` representing each sample's dimension.
</td>
</tr><tr>
<td>
`num_results`
</td>
<td>
Positive scalar `Tensor` of dtype int32. The number of Sobol
points to return in the output.
</td>
</tr><tr>
<td>
`skip`
</td>
<td>
(Optional) Positive scalar `Tensor` of dtype int32. The number of
initial points of the Sobol sequence to skip. Default value is 0.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(Optional) The `tf.Dtype` of the sample. One of: <a href="../../tf.md#float32"><code>tf.float32</code></a> or
<a href="../../tf.md#float64"><code>tf.float64</code></a>. Defaults to <a href="../../tf.md#float32"><code>tf.float32</code></a>.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional) Python `str` name prefixed to ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` of samples from Sobol sequence with `shape` [num_results, dim].
</td>
</tr>

</table>

