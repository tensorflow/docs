description: Return histogram of values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.histogram_fixed_width" />
<meta itemprop="path" content="Stable" />
</div>

# tf.histogram_fixed_width

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/histogram_ops.py#L102-L147">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return histogram of values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.histogram_fixed_width`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.histogram_fixed_width(
    values, value_range, nbins=100, dtype=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given the tensor `values`, this operation returns a rank 1 histogram counting
the number of entries in `values` that fell into every bin.  The bins are
equal width and determined by the arguments `value_range` and `nbins`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
Numeric `Tensor`.
</td>
</tr><tr>
<td>
`value_range`
</td>
<td>
Shape [2] `Tensor` of same `dtype` as `values`.
values <= value_range[0] will be mapped to hist[0],
values >= value_range[1] will be mapped to hist[-1].
</td>
</tr><tr>
<td>
`nbins`
</td>
<td>
Scalar `int32 Tensor`.  Number of histogram bins.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
dtype for returned histogram.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (defaults to 'histogram_fixed_width').
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A 1-D `Tensor` holding histogram of values.
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
If any unsupported dtype is provided.
</td>
</tr><tr>
<td>
`tf.errors.InvalidArgumentError`
</td>
<td>
If value_range does not
satisfy value_range[0] < value_range[1].
</td>
</tr>
</table>



#### Examples:



```
>>> # Bins will be:  (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
...
>>> nbins = 5
>>> value_range = [0.0, 5.0]
>>> new_values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]
>>> hist = tf.histogram_fixed_width(new_values, value_range, nbins=5)
>>> hist.numpy()
array([2, 1, 1, 0, 2], dtype=int32)
```