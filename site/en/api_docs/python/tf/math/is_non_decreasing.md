description: Returns True if x is non-decreasing.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.is_non_decreasing" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.is_non_decreasing

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/check_ops.py#L1913-L1951">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns `True` if `x` is non-decreasing.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.is_non_decreasing`, `tf.compat.v1.is_non_decreasing`, `tf.compat.v1.math.is_non_decreasing`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.is_non_decreasing(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Elements of `x` are compared in row-major order.  The tensor `[x[0],...]`
is non-decreasing if for every adjacent pair we have `x[i] <= x[i+1]`.
If `x` has less than two elements, it is trivially non-decreasing.

See also:  `is_strictly_increasing`

```
>>> x1 = tf.constant([1.0, 1.0, 3.0])
>>> tf.math.is_non_decreasing(x1)
<tf.Tensor: shape=(), dtype=bool, numpy=True>
>>> x2 = tf.constant([3.0, 1.0, 2.0])
>>> tf.math.is_non_decreasing(x2)
<tf.Tensor: shape=(), dtype=bool, numpy=False>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Numeric `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).  Defaults to "is_non_decreasing"
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Boolean `Tensor`, equal to `True` iff `x` is non-decreasing.
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
if `x` is not a numeric tensor.
</td>
</tr>
</table>

