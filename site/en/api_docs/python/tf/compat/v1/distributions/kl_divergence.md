description: Get the KL-divergence KL(distribution_a || distribution_b). (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distributions.kl_divergence" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.distributions.kl_divergence

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/kullback_leibler.py#L55-L121">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get the KL-divergence KL(distribution_a || distribution_b). (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.distributions.kl_divergence(
    distribution_a, distribution_b, allow_nan_stats=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2019-01-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of `tf.distributions`.

If there is no KL method registered specifically for `type(distribution_a)`
and `type(distribution_b)`, then the class hierarchies of these types are
searched.

If one KL method is registered between any pairs of classes in these two
parent hierarchies, it is used.

If more than one such registered method exists, the method whose registered
classes have the shortest sum MRO paths to the input types is used.

If more than one such shortest path exists, the first method
identified in the search is used (favoring a shorter MRO distance to
`type(distribution_a)`).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`distribution_a`
</td>
<td>
The first distribution.
</td>
</tr><tr>
<td>
`distribution_b`
</td>
<td>
The second distribution.
</td>
</tr><tr>
<td>
`allow_nan_stats`
</td>
<td>
Python `bool`, default `True`. When `True`,
statistics (e.g., mean, mode, variance) use the value "`NaN`" to
indicate the result is undefined. When `False`, an exception is raised
if one or more of the statistic's batch members are undefined.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` name prefixed to Ops created by this class.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Tensor with the batchwise KL-divergence between `distribution_a`
and `distribution_b`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
If no KL method is defined for distribution types
of `distribution_a` and `distribution_b`.
</td>
</tr>
</table>

