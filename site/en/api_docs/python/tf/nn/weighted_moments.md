description: Returns the frequency-weighted mean and variance of x.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.weighted_moments" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.weighted_moments

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_impl.py#L1331-L1352">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the frequency-weighted mean and variance of `x`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.weighted_moments(
    x, axes, frequency_weights, keepdims=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A tensor.
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
1-d tensor of int32 values; these are the axes along which
to compute mean and variance.
</td>
</tr><tr>
<td>
`frequency_weights`
</td>
<td>
A tensor of positive weights which can be
broadcast with x.
</td>
</tr><tr>
<td>
`keepdims`
</td>
<td>
Produce moments with the same dimensionality as the input.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name used to scope the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Two tensors: `weighted_mean` and `weighted_variance`.
</td>
</tr>

</table>

