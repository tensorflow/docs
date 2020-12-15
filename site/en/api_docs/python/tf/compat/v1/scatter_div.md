description: Divides a variable reference by sparse updates.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.scatter_div" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.scatter_div

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/state_ops.py#L656-L705">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Divides a variable reference by sparse updates.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.scatter_div(
    ref, indices, updates, use_locking=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation computes

```python
    # Scalar indices
    ref[indices, ...] /= updates[...]

    # Vector indices (for each i)
    ref[indices[i], ...] /= updates[i, ...]

    # High rank indices (for each i, ..., j)
    ref[indices[i, ..., j], ...] /= updates[i, ..., j, ...]
```

This operation outputs `ref` after the update is done.
This makes it easier to chain operations that need to use the reset value.

Duplicate entries are handled correctly: if multiple `indices` reference
the same location, their contributions divide.

Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape =
[]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ref`
</td>
<td>
A mutable `Tensor`. Must be one of the following types: `float32`,
`float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
`qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
`uint32`, `uint64`. Should be from a `Variable` node.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`. A
tensor of indices into the first dimension of `ref`.
</td>
</tr><tr>
<td>
`updates`
</td>
<td>
A `Tensor`. Must have the same type as `ref`. A tensor of values
that `ref` is divided by.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
An optional `bool`. Defaults to `False`. If True, the operation
will be protected by a lock; otherwise the behavior is undefined, but may
exhibit less contention.
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
A mutable `Tensor`. Has the same type as `ref`.
</td>
</tr>

</table>

