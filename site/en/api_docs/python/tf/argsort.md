description: Returns the indices of a tensor that give its sorted order along an axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.argsort" />
<meta itemprop="path" content="Stable" />
</div>

# tf.argsort

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/sort_ops.py#L69-L109">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the indices of a tensor that give its sorted order along an axis.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.argsort`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.argsort(
    values, axis=-1, direction='ASCENDING', stable=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For a 1D tensor, `tf.gather(values, tf.argsort(values))` is equivalent to
<a href="../tf/sort.md"><code>tf.sort(values)</code></a>. For higher dimensions, the output has the same shape as
`values`, but along the given axis, values represent the index of the sorted
element in that slice of the tensor at the given position.

#### Usage:



```python
import tensorflow as tf
a = [1, 10, 26.9, 2.8, 166.32, 62.3]
b = tf.argsort(a,axis=-1,direction='ASCENDING',stable=False,name=None)
c = tf.keras.backend.eval(b)
# Here, c = [0 3 1 2 5 4]
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
1-D or higher numeric `Tensor`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The axis along which to sort. The default is -1, which sorts the last
axis.
</td>
</tr><tr>
<td>
`direction`
</td>
<td>
The direction in which to sort the values (`'ASCENDING'` or
`'DESCENDING'`).
</td>
</tr><tr>
<td>
`stable`
</td>
<td>
If True, equal elements in the original tensor will not be
re-ordered in the returned order. Unstable sort is not yet implemented,
but will eventually be the default for performance reasons. If you require
a stable order, pass `stable=True` for forwards compatibility.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
An int32 `Tensor` with the same shape as `values`. The indices that would
sort each slice of the given `values` along the given `axis`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If axis is not a constant scalar, or the direction is invalid.
</td>
</tr>
</table>

