description: Calculate the mean and variance of based on the sufficient statistics.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.normalize_moments" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.normalize_moments

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/nn_impl.py#L1234-L1264">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calculate the mean and variance of based on the sufficient statistics.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.normalize_moments`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.normalize_moments(
    counts, mean_ss, variance_ss, shift, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`counts`
</td>
<td>
A `Tensor` containing the total count of the data (one value).
</td>
</tr><tr>
<td>
`mean_ss`
</td>
<td>
A `Tensor` containing the mean sufficient statistics: the (possibly
shifted) sum of the elements to average over.
</td>
</tr><tr>
<td>
`variance_ss`
</td>
<td>
A `Tensor` containing the variance sufficient statistics: the
(possibly shifted) squared sum of the data to compute the variance over.
</td>
</tr><tr>
<td>
`shift`
</td>
<td>
A `Tensor` containing the value by which the data is shifted for
numerical stability, or `None` if no shift was performed.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name used to scope the operations that compute the moments.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Two `Tensor` objects: `mean` and `variance`.
</td>
</tr>

</table>

