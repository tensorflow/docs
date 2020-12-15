description: Computes the difference between two lists of numbers or strings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.setdiff1d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.setdiff1d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L456-L497">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the difference between two lists of numbers or strings.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.setdiff1d(
    x, y, index_dtype=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a list `x` and a list `y`, this operation returns a list `out` that
represents all values that are in `x` but not in `y`. The returned list `out`
is sorted in the same order that the numbers appear in `x` (duplicates are
preserved). This operation also returns a list `idx` that represents the
position of each `out` element in `x`. In other words:

`out[i] = x[idx[i]] for i in [0, 1, ..., len(out) - 1]`

For example, given this input:

```
x = [1, 2, 3, 4, 5, 6]
y = [1, 3, 5]
```

This operation would return:

```
out ==> [2, 4, 6]
idx ==> [1, 3, 5]
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
A `Tensor`. 1-D. Values to keep.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `Tensor`. Must have the same type as `x`. 1-D. Values to remove.
</td>
</tr><tr>
<td>
`out_idx`
</td>
<td>
An optional <a href="../../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../../tf.md#int32"><code>tf.int32</code></a>.
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
A tuple of `Tensor` objects (out, idx).
</td>
</tr>
<tr>
<td>
`out`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`idx`
</td>
<td>
A `Tensor` of type `out_idx`.
</td>
</tr>
</table>

