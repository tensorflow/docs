description: Applies sparse addition to input using individual values or slices

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ScatterNdNonAliasingAdd" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ScatterNdNonAliasingAdd

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Applies sparse addition to `input` using individual values or slices

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ScatterNdNonAliasingAdd`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ScatterNdNonAliasingAdd(
    input, indices, updates, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

from `updates` according to indices `indices`.  The updates are non-aliasing:
`input` is only modified in-place if no other operations will use it.
Otherwise, a copy of `input` is made.  This operation has a gradient with
respect to both `input` and `updates`.

`input` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

`indices` must be integer tensor, containing indices into `input`.
It must be shape \\([d_0, ..., d_{Q-2}, K]\\) where `0 < K <= P`.

The innermost dimension of `indices` (with length `K`) corresponds to
indices into elements (if `K = P`) or `(P-K)`-dimensional slices
(if `K < P`) along the `K`th dimension of `input`.

`updates` is `Tensor` of rank `Q-1+P-K` with shape:

$$[d_0, ..., d_{Q-2}, input.shape[K], ..., input.shape[P-1]].$$

For example, say we want to add 4 scattered elements to a rank-1 tensor to 8
elements. In Python, that addition would look like this:

    input = tf.constant([1, 2, 3, 4, 5, 6, 7, 8])
    indices = tf.constant([[4], [3], [1], [7]])
    updates = tf.constant([9, 10, 11, 12])
    output = tf.scatter_nd_non_aliasing_add(input, indices, updates)
    with tf.Session() as sess:
      print(sess.run(output))

The resulting value `output` would look like this:

    [1, 13, 3, 14, 14, 6, 7, 20]

See <a href="../../tf/scatter_nd.md"><code>tf.scatter_nd</code></a> for more details about how to make updates to slices.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `bool`.
A Tensor.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A Tensor. Must be one of the following types: `int32`, `int64`.
A tensor of indices into `input`.
</td>
</tr><tr>
<td>
`updates`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
A Tensor. Must have the same type as ref. A tensor of updated values
to add to `input`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

