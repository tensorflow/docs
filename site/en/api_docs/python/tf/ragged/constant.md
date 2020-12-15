description: Constructs a constant RaggedTensor from a nested Python list.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.constant" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.constant

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ragged/ragged_factory_ops.py#L37-L87">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Constructs a constant RaggedTensor from a nested Python list.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.constant`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.constant(
    pylist, dtype=None, ragged_rank=None, inner_shape=None, name=None,
    row_splits_dtype=tf.dtypes.int64
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```
>>> tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
<tf.RaggedTensor [[1, 2], [3], [4, 5, 6]]>
```

All scalar values in `pylist` must have the same nesting depth `K`, and the
returned `RaggedTensor` will have rank `K`.  If `pylist` contains no scalar
values, then `K` is one greater than the maximum depth of empty lists in
`pylist`.  All scalar values in `pylist` must be compatible with `dtype`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`pylist`
</td>
<td>
A nested `list`, `tuple` or `np.ndarray`.  Any nested element that
is not a `list`, `tuple` or `np.ndarray` must be a scalar value
compatible with `dtype`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of elements for the returned `RaggedTensor`.  If not
specified, then a default is chosen based on the scalar values in
`pylist`.
</td>
</tr><tr>
<td>
`ragged_rank`
</td>
<td>
An integer specifying the ragged rank of the returned
`RaggedTensor`.  Must be nonnegative and less than `K`. Defaults to
`max(0, K - 1)` if `inner_shape` is not specified.  Defaults to
`max(0, K - 1 - len(inner_shape))` if `inner_shape` is specified.
</td>
</tr><tr>
<td>
`inner_shape`
</td>
<td>
A tuple of integers specifying the shape for individual inner
values in the returned `RaggedTensor`.  Defaults to `()` if `ragged_rank`
is not specified.  If `ragged_rank` is specified, then a default is chosen
based on the contents of `pylist`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr><tr>
<td>
`row_splits_dtype`
</td>
<td>
data type for the constructed `RaggedTensor`'s row_splits.
One of <a href="../../tf.md#int32"><code>tf.int32</code></a> or <a href="../../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A potentially ragged tensor with rank `K` and the specified `ragged_rank`,
containing the values from `pylist`.
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
If the scalar values in `pylist` have inconsistent nesting
depth; or if ragged_rank or inner_shape are incompatible with `pylist`.
</td>
</tr>
</table>

