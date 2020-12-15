description: Calculate the sufficient statistics for the mean and variance of x.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.sufficient_statistics" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.sufficient_statistics

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_impl.py#L1151-L1223">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calculate the sufficient statistics for the mean and variance of `x`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.sufficient_statistics(
    x, axes, shift=None, keep_dims=None, name=None, keepdims=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

These sufficient statistics are computed using the one pass algorithm on
an input that's optionally shifted. See:
https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Computing_shifted_data

#### For example:


>>> t = [[1, 2, 3], [4, 5, 6]]
>>> sufficient_statistics(t, [1])
(<tf.Tensor: shape=(), dtype=int32, numpy=3>, <tf.Tensor: shape=(2,),
dtype=int32, numpy=array([ 6, 15], dtype=int32)>, <tf.Tensor: shape=(2,),
dtype=int32, numpy=array([14, 77], dtype=int32)>, None)
>>> sufficient_statistics(t, [-1])
(<tf.Tensor: shape=(), dtype=int32, numpy=3>, <tf.Tensor: shape=(2,),
dtype=int32, numpy=array([ 6, 15], dtype=int32)>, <tf.Tensor: shape=(2,),
dtype=int32, numpy=array([14, 77], dtype=int32)>, None)

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
Array of ints. Axes along which to compute mean and variance. As in
Python, the axes can also be negative numbers. A negative axis is
interpreted as counting from the end of the rank, i.e., axis +
rank(values)-th dimension.
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
`keep_dims`
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
</tr><tr>
<td>
`keepdims`
</td>
<td>
Alias for keep_dims.
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

