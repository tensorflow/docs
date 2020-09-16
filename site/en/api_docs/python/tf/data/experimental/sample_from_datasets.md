description: Samples elements at random from the datasets in datasets.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.sample_from_datasets" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.sample_from_datasets

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/interleave_ops.py#L145-L226">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Samples elements at random from the datasets in `datasets`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.sample_from_datasets(
    datasets, weights=None, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`datasets`
</td>
<td>
A list of <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> objects with compatible structure.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
(Optional.) A list of `len(datasets)` floating-point values where
`weights[i]` represents the probability with which an element should be
sampled from `datasets[i]`, or a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object where each
element is such a list. Defaults to a uniform distribution across
`datasets`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
(Optional.) A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the
random seed that will be used to create the distribution. See
<a href="../../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a> for behavior.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dataset that interleaves elements from `datasets` at random, according to
`weights` if provided, otherwise with uniform probability.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the `datasets` or `weights` arguments have the wrong type.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the `weights` argument is specified and does not match the
length of the `datasets` element.
</td>
</tr>
</table>

