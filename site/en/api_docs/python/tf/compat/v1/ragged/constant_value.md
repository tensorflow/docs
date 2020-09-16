description: Constructs a RaggedTensorValue from a nested Python list.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.ragged.constant_value" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.ragged.constant_value

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ragged/ragged_factory_ops.py#L88-L144">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Constructs a RaggedTensorValue from a nested Python list.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.ragged.constant_value(
    pylist, dtype=None, ragged_rank=None, inner_shape=None, row_splits_dtype='int64'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: This function returns a `RaggedTensorValue`, not a `RaggedTensor`.
If you wish to construct a constant `RaggedTensor`, use
[`ragged.constant(...)`](constant.md) instead.

#### Example:



```
>>> tf.compat.v1.ragged.constant_value([[1, 2], [3], [4, 5, 6]])
tf.RaggedTensorValue(values=array([1, 2, 3, 4, 5, 6]),
                     row_splits=array([0, 2, 3, 6]))
```

All scalar values in `pylist` must have the same nesting depth `K`, and the
returned `RaggedTensorValue` will have rank `K`.  If `pylist` contains no
scalar values, then `K` is one greater than the maximum depth of empty lists
in `pylist`.  All scalar values in `pylist` must be compatible with `dtype`.

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
is not a `list` or `tuple` must be a scalar value compatible with `dtype`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
`numpy.dtype`.  The type of elements for the returned `RaggedTensor`.
If not specified, then a default is chosen based on the scalar values in
`pylist`.
</td>
</tr><tr>
<td>
`ragged_rank`
</td>
<td>
An integer specifying the ragged rank of the returned
`RaggedTensorValue`.  Must be nonnegative and less than `K`. Defaults to
`max(0, K - 1)` if `inner_shape` is not specified.  Defaults to `max(0, K
- 1 - len(inner_shape))` if `inner_shape` is specified.
</td>
</tr><tr>
<td>
`inner_shape`
</td>
<td>
A tuple of integers specifying the shape for individual inner
values in the returned `RaggedTensorValue`.  Defaults to `()` if
`ragged_rank` is not specified.  If `ragged_rank` is specified, then a
default is chosen based on the contents of `pylist`.
</td>
</tr><tr>
<td>
`row_splits_dtype`
</td>
<td>
data type for the constructed `RaggedTensorValue`'s
row_splits.  One of `numpy.int32` or `numpy.int64`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `tf.RaggedTensorValue` or `numpy.array` with rank `K` and the specified
`ragged_rank`, containing the values from `pylist`.
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

