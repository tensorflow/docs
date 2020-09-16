description: Applies sparse addition to individual values or slices in a Variable.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ResourceScatterNdAdd" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ResourceScatterNdAdd

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Applies sparse addition to individual values or slices in a Variable.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ResourceScatterNdAdd`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ResourceScatterNdAdd(
    ref, indices, updates, use_locking=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `ref`.
It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to
indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
dimension of `ref`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

```
[d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]]
```

For example, say we want to add 4 scattered elements to a rank-1 tensor to
8 elements. In Python, that addition would look like this:

```python
ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8], use_resource=True)
indices = tf.constant([[4], [3], [1], [7]])
updates = tf.constant([9, 10, 11, 12])
add = tf.scatter_nd_add(ref, indices, updates)
with tf.Session() as sess:
  print sess.run(add)
```

The resulting update to ref would look like this:

    [1, 13, 3, 14, 14, 6, 7, 20]

See <a href="../../tf/scatter_nd.md"><code>tf.scatter_nd</code></a> for more details about how to make updates to
slices.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ref`
</td>
<td>
A `Tensor` of type `resource`.
A resource handle. Must be from a VarHandleOp.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A Tensor. Must be one of the following types: int32, int64.
A tensor of indices into ref.
</td>
</tr><tr>
<td>
`updates`
</td>
<td>
A `Tensor`. A Tensor. Must have the same type as ref. A tensor of
values to add to ref.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
An optional `bool`. Defaults to `True`.
An optional bool. Defaults to True. If True, the assignment will
be protected by a lock; otherwise the behavior is undefined,
but may exhibit less contention.
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
The created Operation.
</td>
</tr>

</table>

