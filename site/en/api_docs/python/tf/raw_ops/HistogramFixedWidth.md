description: Return histogram of values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.HistogramFixedWidth" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.HistogramFixedWidth

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Return histogram of values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.HistogramFixedWidth`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.HistogramFixedWidth(
    values, value_range, nbins, dtype=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given the tensor `values`, this operation returns a rank 1 histogram counting
the number of entries in `values` that fall into every bin.  The bins are
equal width and determined by the arguments `value_range` and `nbins`.

```python
# Bins will be:  (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
nbins = 5
value_range = [0.0, 5.0]
new_values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]

with tf.get_default_session() as sess:
  hist = tf.histogram_fixed_width(new_values, value_range, nbins=5)
  variables.global_variables_initializer().run()
  sess.run(hist) => [2, 1, 1, 0, 2]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
Numeric `Tensor`.
</td>
</tr><tr>
<td>
`value_range`
</td>
<td>
A `Tensor`. Must have the same type as `values`.
Shape [2] `Tensor` of same `dtype` as `values`.
values <= value_range[0] will be mapped to hist[0],
values >= value_range[1] will be mapped to hist[-1].
</td>
</tr><tr>
<td>
`nbins`
</td>
<td>
A `Tensor` of type `int32`.
Scalar `int32 Tensor`.  Number of histogram bins.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int32"><code>tf.int32</code></a>.
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

