description: Returns a RaggedTensor containing the specified sequences of numbers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.range" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.range

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ragged/ragged_math_ops.py#L41-L109">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a `RaggedTensor` containing the specified sequences of numbers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.range`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.range(
    starts, limits=None, deltas=1, dtype=None, name=None,
    row_splits_dtype=tf.dtypes.int64
)
</code></pre>



<!-- Placeholder for "Used in" -->

Each row of the returned `RaggedTensor` contains a single sequence:

```python
ragged.range(starts, limits, deltas)[i] ==
    tf.range(starts[i], limits[i], deltas[i])
```

If `start[i] < limits[i] and deltas[i] > 0`, then `output[i]` will be an
empty list.  Similarly, if `start[i] > limits[i] and deltas[i] < 0`, then
`output[i]` will be an empty list.  This behavior is consistent with the
Python `range` function, but differs from the <a href="../../tf/range.md"><code>tf.range</code></a> op, which returns
an error for these cases.

#### Examples:



```
>>> tf.ragged.range([3, 5, 2]).to_list()
[[0, 1, 2], [0, 1, 2, 3, 4], [0, 1]]
>>> tf.ragged.range([0, 5, 8], [3, 3, 12]).to_list()
[[0, 1, 2], [], [8, 9, 10, 11]]
>>> tf.ragged.range([0, 5, 8], [3, 3, 12], 2).to_list()
[[0, 2], [], [8, 10]]
```

The input tensors `starts`, `limits`, and `deltas` may be scalars or vectors.
The vector inputs must all have the same size.  Scalar inputs are broadcast
to match the size of the vector inputs.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`starts`
</td>
<td>
Vector or scalar `Tensor`.  Specifies the first entry for each range
if `limits` is not `None`; otherwise, specifies the range limits, and the
first entries default to `0`.
</td>
</tr><tr>
<td>
`limits`
</td>
<td>
Vector or scalar `Tensor`.  Specifies the exclusive upper limits for
each range.
</td>
</tr><tr>
<td>
`deltas`
</td>
<td>
Vector or scalar `Tensor`.  Specifies the increment for each range.
Defaults to `1`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the elements of the resulting tensor.  If not specified,
then a value is chosen based on the other args.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation.
</td>
</tr><tr>
<td>
`row_splits_dtype`
</td>
<td>
`dtype` for the returned `RaggedTensor`'s `row_splits`
tensor.  One of <a href="../../tf.md#int32"><code>tf.int32</code></a> or <a href="../../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` of type `dtype` with `ragged_rank=1`.
</td>
</tr>

</table>

