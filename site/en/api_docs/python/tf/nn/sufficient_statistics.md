description: Calculate the sufficient statistics for the mean and variance of x.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.sufficient_statistics" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.sufficient_statistics

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_impl.py#L1226-L1253">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calculate the sufficient statistics for the mean and variance of `x`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.sufficient_statistics(
    x, axes, shift=None, keepdims=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

These sufficient statistics are computed using the one pass algorithm on
an input that's optionally shifted. See:
https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Computing_shifted_data

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
Array of ints. Axes along which to compute mean and variance.
</td>
</tr><tr>
<td>
`shift`
</td>
<td>
A `Tensor` containing the value by which to shift the data for
numerical stability, or `None` if no shift is to be performed. A shift
close to the true mean provides the most numerically stable results.
</td>
</tr><tr>
<td>
`keepdims`
</td>
<td>
produce statistics with the same dimensionality as the input.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name used to scope the operations that compute the sufficient stats.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Four `Tensor` objects of the same type as `x`:

* the count (number of elements to average over).
* the (possibly shifted) sum of the elements in the array.
* the (possibly shifted) sum of squares of the elements in the array.
* the shift by which the mean must be corrected or None if `shift` is None.
</td>
</tr>

</table>

